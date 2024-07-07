# PDF Generator 

This README provides instructions and details about the PDF Generator Script that reads topics from a CSV file and generates a structured PDF document with those topics.

> The final generated is stored in `output.pdf`

## Overview

This Python script uses the `fpdf` library to create a PDF document based on the data provided in a CSV file. Each topic from the CSV file is added to the PDF, formatted with lines and text as specified.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- `fpdf`
- `pandas`

You can install these using pip:

```sh
pip install fpdf pandas
```

## Input

The script reads from a CSV file named `topics.csv`. The CSV file should have the following structure:

|Order| Topic   | Pages |
|---|---------|-------|
|1| Topic 1 | 2     |
|2| Topic 2 | 3     |
|...| ...     | ...   |


- **order**: The order of topics in Pdf.
- **Topic**: The title of the topic to be included in the PDF.
- **Pages**: The number of pages to be allocated for each topic.


## Dependencies

- `fpdf`
- `pandas`