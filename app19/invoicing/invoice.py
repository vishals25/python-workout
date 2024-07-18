from fileinput import filename
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os



def generate(invoices_path,pdfs_path,product_id,product_name,amount_purchased,price_per_unit,total_price,company_name):
    """
        Generate and save invoice PDFs.

        This function generates invoice PDFs for the given product details and saves them to the specified paths.

        Args:
            :param invoices_path (str): The directory path where the generated invoice files will be saved.
            :param pdfs_path (str): The directory path where the generated PDF files will be saved.
            :param product_id (int or str): The unique identifier for the product.
            :param product_name (str): The name of the product.
            :param amount_purchased (int or float): The quantity of the product purchased.
            :param price_per_unit (float): The price per unit of the product.
            :param total_price (float): The total price for the purchased quantity of the product.
            :param company_name (str): The name of the company generating the invoice.

        Returns:
            None
        """

    filepaths = glob.glob(f"{invoices_path}/*.xlsx")
    for path in filepaths:

        pdf = FPDF("l",unit="mm",format="A4")
        pdf.add_page()

        total_prices=0.00
        filename=Path(path).stem

        invoiceno,idate=filename.split("-")

        pdf.set_font(family="Times",style="B",size=16)
        pdf.cell(w=0,h=14,txt=f'Invoice No : {invoiceno}',ln=1) #type:ignore
        pdf.cell(w=0,h=14,txt=f'Date            : {idate}',ln=1) #type:ignore
        pdf.ln(10)

        df=pd.read_excel(path,sheet_name="Sheet 1")

        columns=list(df.columns)
        columns=[item.replace("_"," ").title() for item in columns]


        pdf.set_font(family="Times",style="B",size=14)
        pdf.cell(w=30,h=8,txt=str(columns[0]),border=1)#type:ignore
        pdf.cell(w=70,h=8,txt=str(columns[1]),border=1)#type:ignore
        pdf.cell(w=60,h=8,txt=str(columns[2]),border=1)#type:ignore
        pdf.cell(w=60,h=8,txt=str(columns[3]),border=1)#type:ignore
        pdf.cell(w=50,h=8,txt=str(columns[4]),border=1,ln=1)#type:ignore

        for index,row in df.iterrows():
            pdf.set_font(family="Times",style="I",size=10)
            pdf.set_text_color(80,80,80)
            pdf.cell(w=30,h=8,txt=str(row[product_id]),border=1)#type:ignore
            pdf.cell(w=70,h=8,txt=str(row[product_name]),border=1)#type:ignore
            pdf.cell(w=60,h=8,txt=str(row[amount_purchased]),border=1,align="R")#type:ignore
            pdf.cell(w=60,h=8,txt=str(row[price_per_unit]),border=1,align="R")#type:ignore
            pdf.cell(w=50,h=8,txt=str(row[total_price]),border=1,align="R",ln=1)#type:ignore
            total_prices+=row[total_price]

        pdf.set_font(family="Times",size=12)

        pdf.cell(w=220,h=8,txt="Total Purchase Price",border=1,align="R")#type:ignore
        pdf.cell(w=50,h=8,txt=str(total_price),border=1,align="R",ln=1)#type:ignore

        pdf.ln(10)

        pdf.set_font(family="Times",style="B",size=14)
        pdf.set_fill_color(0,0,0)
        pdf.cell(w=0,h=8,txt=company_name,align="C",ln=1)#type:ignore



        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f'{pdfs_path}/{filename}.pdf')