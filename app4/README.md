# Invoice Generator

This project processes multiple Excel files containing invoice data from excel files and generates corresponding PDF invoices.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `pandas`
  - `fpdf`
  - `glob`
  - `pathlib`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/invoice-generator.git
   cd app4
   ```

2. Install required Python packages:

   ```bash
   pip install pandas fpdf
   ```

## Directory Structure

```sh

app4/
│
├── invoices/ # Directory containing Excel files
│ ├── invoice1.xlsx
│ └── invoice2.xlsx
├── pdf/ # Directory where generated PDF invoices will be saved
├── main.py

```

## Usage

1. Place your Excel invoice files in the `invoices` directory. Ensure the files follow the naming convention `invoiceno-date.xlsx`.

2. Run the script:

   ```bash
   python main.py
   ```

3. The script will:
   - Read each Excel file in the `invoices` directory.
   - Process the invoice data and generate a PDF for each invoice.
   - Save the generated PDF files in the `pdf` directory.

---

Happy Coding!
