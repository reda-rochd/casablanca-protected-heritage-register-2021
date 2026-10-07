#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Reda Rochd
"""Extract the Casablanca entries from the official Dec 2021 heritage-register DOC.

Requires LibreOffice/soffice and BeautifulSoup 4. The source DOC is converted to
HTML solely to preserve its table cell rowspan/colspan structure. Arabic labels
and names are kept as published; no location, legal status, or visitor access is inferred.
"""
from __future__ import annotations
import csv
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from bs4 import BeautifulSoup

SOURCE_URL = "https://data.gov.ma/data/fr/dataset/3ae1adac-b0d4-4cdf-9e11-34c482534945"
HEADERS = [
    "official_gazette_reference_ar",
    "protection_decision_reference_ar",
    "protection_category_ar",
    "protected_site_name_as_published_ar",
    "decision_year_as_published",
    "province_as_published_ar",
    "source_table_index",
    "source_row_index",
]


def expanded_rows(table):
    occupied = {}
    for row_index, tr in enumerate(table.find_all("tr")):
        row, col = [], 0
        for cell in tr.find_all(["td", "th"], recursive=False):
            while (row_index, col) in occupied:
                row.append(occupied[(row_index, col)])
                col += 1
            value = " ".join(cell.get_text(" ", strip=True).split())
            rowspan = int(cell.get("rowspan", 1))
            colspan = int(cell.get("colspan", 1))
            row.extend([value] + [""] * (colspan - 1))
            if rowspan > 1:
                for future_row in range(row_index + 1, row_index + rowspan):
                    for future_col in range(col, col + colspan):
                        occupied[(future_row, future_col)] = value if future_col == col else ""
            col += colspan
        while (row_index, col) in occupied:
            row.append(occupied[(row_index, col)])
            col += 1
        yield row_index, row


def extract(source: Path):
    with tempfile.TemporaryDirectory(prefix="heritage-register-") as tmp:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "html", "--outdir", tmp, str(source)],
            check=True, capture_output=True, text=True,
        )
        html = Path(tmp) / f"{source.stem}.html"
        soup = BeautifulSoup(html.read_text(encoding="utf-8"), "html.parser")
    rows, counts = [], Counter()
    for table_index, table in enumerate(soup.find_all("table")[:6]):
        for row_index, raw in expanded_rows(table):
            row = (raw + [""] * 6)[:6]
            gazette, decision, category, site, year, province = row
            if "الجريدة الرسمية" in row or "مجموع" in gazette:
                continue
            if not site or not category or "الدار البيضاء" not in province:
                continue
            counts[category] += 1
            rows.append([
                gazette, decision, category, site, year, province,
                str(table_index), str(row_index),
            ])
    expected = {"الترتيب": 2, "التقييد": 107}
    if dict(counts) != expected or len(rows) != 109:
        raise SystemExit(f"Validation failed: counts={dict(counts)}, rows={len(rows)}; expected {expected}")
    return rows, counts


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: build_casablanca_heritage_csv.py SOURCE.doc OUTPUT.csv")
    source, output = map(Path, sys.argv[1:])
    rows, counts = extract(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(HEADERS)
        writer.writerows(rows)
    print(f"Wrote {len(rows)} entries; category counts: {dict(counts)}; output: {output}")

if __name__ == "__main__":
    main()
