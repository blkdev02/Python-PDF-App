from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(0,20,250,20)

    # create the lines 
    for y in range(20, 298, 10):
        pdf.line(0, y, 250, y)

    #set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180,100,190)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180,100,190)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

            # create the lines 
        for y in range(20, 298, 10):
            pdf.line(0, y, 250, y)
    
pdf.output("output.pdf")