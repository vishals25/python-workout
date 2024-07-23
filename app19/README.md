# Invoice Generator Package

This package generates invoice PDFs from Excel files containing product details. It reads the data from Excel files, processes it, and generates a PDF invoice for each file.

## Features

- **Generate Invoices**: Automatically generate PDF invoices from Excel files.
- **Customizable**: Easily specify product details and company information.
- **Directory Support**: Supports batch processing of all Excel files in a specified directory.

## Requirements

- Python 3.x
- pandas
- fpdf
- openpyxl

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/invoice-generator.git
    cd invoice-generator
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Function: `generate`

The `generate` function generates invoice PDFs for the given product details and saves them to the specified paths.

#### Parameters

- `invoices_path` (str): The directory path where the Excel invoice files are located.
- `pdfs_path` (str): The directory path where the generated PDF files will be saved.
- `product_id` (int or str): The unique identifier for the product.
- `product_name` (str): The name of the product.
- `amount_purchased` (int or float): The quantity of the product purchased.
- `price_per_unit` (float): The price per unit of the product.
- `total_price` (float): The total price for the purchased quantity of the product.
- `company_name` (str): The name of the company generating the invoice.

#### Example

```python
from invoice_generator import generate

invoices_path = "path/to/excel/files"
pdfs_path = "path/to/save/pdf/files"
product_id = "Product ID"
product_name = "Product Name"
amount_purchased = "Amount Purchased"
price_per_unit = "Price Per Unit"
total_price = "Total Price"
company_name = "Your Company Name"

generate(invoices_path, pdfs_path, product_id, product_name, amount_purchased, price_per_unit, total_price, company_name)
```

## How It Works

1. **Read Excel Files**: The function reads all Excel files in the specified `invoices_path` directory.
2. **Generate PDF**: For each Excel file, it generates a PDF invoice with the provided product and company details.
3. **Save PDF**: The generated PDF invoices are saved in the specified `pdfs_path` directory.
