# arXiv Dataset Overview

## Introduction

**arXiv** is a free, open pipeline on Kaggle to a machine-readable dataset containing 1.7 million scholarly articles. This document serves as an in-depth guide to the dataset, offering insights into its structure, contents, and usability.

## Dataset Description

### About arXiv

- **Origin**: Founded by Paul Ginsparg in 1991.
- **Maintenance**: Operated by Cornell University.
- **Scope**: Covers a wide range of STEM fields, including physics, computer science, mathematics, and more.
- **Purpose**: Facilitates efficient extraction of insights from scholarly articles.

### Dataset Features

- **Content**: Titles, authors, categories, abstracts, full-text PDFs, etc.
- **Applications**: Suitable for machine learning techniques, trend analysis, paper recommendation, category prediction, and more.
- **Accessibility**: Available via Google Cloud Storage buckets.
- **Update Frequency**: Weekly updates.
- **Size**: Metadata file in JSON format, original dataset over 1.1TB.

## Metadata

### Fields Description

- `id`: Unique ArXiv ID for each paper.
- `submitter`: The individual who submitted the paper.
- `authors`: List of authors of the paper.
- `title`: Title of the paper.
- `comments`: Additional information like number of pages and figures.
- `journal-ref`: Journal publication details.
- `doi`: Digital Object Identifier.
- `abstract`: Summary of the paper.
- `categories`: ArXiv system categories/tags.
- `versions`: History of paper versions.
- `update_date`: Date of the latest update.
- `authors_parsed`: Structured author names.

### Accessing Papers

- Abstracts and details: `https://arxiv.org/abs/{id}`
- PDF downloads: `https://arxiv.org/pdf/{id}`

### Bulk Access

- Google Cloud Storage: `gs://arxiv-dataset`
- Download commands using `gsutil`.

## Licensing and Acknowledgements

- **License**: Creative Commons CC0 1.0 Universal Public Domain Dedication for metadata.
- **Acknowledgements**: Thanks to ArXiv team and Matt Bierbaum for the `arxiv-public-datasets` tool.

## Usability and Engagement

- **Usability Score**: 8.75.
- **Public Domain License**: CC0.
- **Expected Update Frequency**: Monthly.
- **Community Engagement**: Active discussions and high download rates.

## Data Snapshot

### Sample Entry

```json
{
  "id": "0704.0001",
  "submitter": "Pavel Nadolsky",
  "authors": "C. Balázs, E. L. Berger, P. M. Nadolsky, C.-P. Yuan",
  "title": "Calculation of prompt diphoton production cross sections at Tevatron and LHC energies",
  ...
}
```