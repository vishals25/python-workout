from fpdf import FPDF
import pandas as pd

df=pd.read_csv("topics.csv")

pdf = FPDF("p",unit="mm",format="A4")

pdf.set_auto_page_break(auto=False,margin=0)

for index,row in df.iterrows():

    pages=row["Pages"]
    pdf.add_page()

    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)

    pdf.cell(w=0,h=24,txt=row['Topic'],ln=1) #type:ignore

    y=28
    for i in range(0,26):
        pdf.line(10,y,200,y)
        y+=10

    pdf.ln(y-42)

    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=8,txt=row['Topic'],align="R") #type:ignore

    for i in range(1,pages):

        pdf.add_page()
        
        y=18

        for i in range(0,27):
            pdf.line(10,y,200,y)
            y+=10

        pdf.ln(y-18)
        pdf.set_font(family="Times",style="I",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=8,txt=row['Topic'],align="R") #type:ignore

pdf.output("output.pdf")