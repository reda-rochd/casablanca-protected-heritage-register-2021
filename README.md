# Casablanca protected-heritage register (December 2021): 109 source rows

## Quick visual overview

![Counts of Casablanca register rows by source year](casablanca-register-counts-by-source-year-v2.svg)

Counts follow the source year and source-category labels. This is a row count from the December 2021 register, not a count of unique places or current legal status.

## Files

- [Search the 109 source rows](https://reda-rochd.github.io/casablanca-protected-heritage-register-2021/) — filter the published names, year and source category, and inspect each record's official references.
- [Download the CSV](data/casablanca-protected-heritage-register-2021-casablanca-109.csv) — 109 Casablanca rows extracted from the source register. Arabic source values are preserved.
- [Year-count chart](casablanca-register-counts-by-source-year-v2.svg) — a source-labeled visualization of the register row counts.
- [Reproducible extractor](src/build_casablanca_heritage_csv.py) — requires Python 3, BeautifulSoup 4, and LibreOffice (`soffice`).
- Download the original Word document from the official source resource before reproducing; this repository does not mirror the source document.

## Provenance and scope

Prepared by Reda Rochd, who works with [MarocTours](https://maroctours.ru/), a commercial Casablanca tour operator. This is an independent open-data reuse, not an MJCC publication or endorsement; the dataset does not promote a tour. The author has no claim to heritage-law expertise.

- Publisher: Morocco's Ministry of Youth, Culture and Communication (MJCC).
- Dataset: « المواقع الأثرية و المباني التاريخية بجهة الدار البيضاء سطات » (archaeological sites and historic buildings in Casablanca-Settat).
- Source portal: <https://data.gov.ma/data/fr/dataset/3ae1adac-b0d4-4cdf-9e11-34c482534945>
- Source resource: <https://data.gov.ma/data/fr/dataset/3ae1adac-b0d4-4cdf-9e11-34c482534945/resource/913f28ef-3b82-48e7-b459-ccd1283c6e62>
- Reference date: December 2021, as stated in the register. This is not a current-status inventory.
- The portal lists the dataset under the Open Data Commons Open Database License (ODbL). This adapted extract, its row-count visualization, and the machine-readable JSON copy retain that attribution and are released under ODbL as well. The extractor and search-page code are licensed under MIT below; the extracted data remains under ODbL. See <https://opendatacommons.org/licenses/odbl/1-0/>.
- For a citable version, use [release v1.1.1](https://github.com/reda-rochd/casablanca-protected-heritage-register-2021/releases/tag/v1.1.1) and cite the official Ministry/portal source as well. GitHub's **Cite this repository** panel reads the included `CITATION.cff`; it does not provide a DOI.

## Extraction and validation

The source is a Word document. The script converts it to HTML using LibreOffice so merged cells can be reconstructed, then extracts the first six tables, which contain the Casablanca entries in a consistent six-column structure. It preserves merged source values and keeps zero-based source table/row indexes for auditability. Summary rows and repeated headers are excluded.

The 109 output rows reconcile exactly with the source's own Casablanca totals: 2 rows marked `الترتيب` and 107 marked `التقييد`. No names or legal-category labels are translated or normalized. The categories' legal effects have not been independently interpreted.

## CSV field dictionary

| Field | Meaning |
|---|---|
| `official_gazette_reference_ar` | Official Gazette reference, transcribed in Arabic as printed in the source. |
| `protection_decision_reference_ar` | Ministerial or administrative decision reference, transcribed in Arabic as printed in the source. |
| `protection_category_ar` | Original Arabic category label (`الترتيب` or `التقييد`); legal effects are not interpreted here. |
| `protected_site_name_as_published_ar` | Name/description of the entry exactly as published in Arabic, including mixed-script text where present. |
| `decision_year_as_published` | Year value from the source table; not independently verified as a legal effective date. |
| `province_as_published_ar` | Province/administrative place value from the source table, in Arabic. |
| `source_table_index` | Zero-based table number in the source Word document after conversion for extraction. |
| `source_row_index` | Zero-based row index within that source table; supports checking the extraction against the document. |

## Counts by year as shown in the source

These are counts of extracted rows by the source column `السنة` (rendered in the CSV as `decision_year_as_published`). They are not independently verified dates of legal effect.

| Year in source | `الترتيب` rows | `التقييد` rows | Total rows |
|---:|---:|---:|---:|
| 1942 | 1 | 0 | 1 |
| 1951 | 1 | 0 | 1 |
| 2000 | 0 | 1 | 1 |
| 2003 | 0 | 24 | 24 |
| 2004 | 0 | 17 | 17 |
| 2005 | 0 | 4 | 4 |
| 2006 | 0 | 2 | 2 |
| 2011 | 0 | 3 | 3 |
| 2012 | 0 | 5 | 5 |
| 2013 | 0 | 5 | 5 |
| 2014 | 0 | 20 | 20 |
| 2015 | 0 | 5 | 5 |
| 2018 | 0 | 21 | 21 |
| **Total** | **2** | **107** | **109** |

## Limitations

This extract contains the source's names, protection-category labels, references, and years. It contains no coordinates, access information, condition survey, architectural classification, or confirmation that any place can be visited. Do not treat an entry as a unique tourist attraction or as proof of current legal status. Consult the cited decisions and current official sources for legal or access questions.

## Extractor code license (MIT)

This license applies only to `src/build_casablanca_heritage_csv.py`, `index.html`, and their associated code documentation. It does not change the ODbL terms for the extracted dataset or the chart.

Copyright (c) 2026 Reda Rochd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
