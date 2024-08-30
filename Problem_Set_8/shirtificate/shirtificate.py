from fpdf import FPDF

def main():
    inp = input("name: ")
    name =  inp + " took CS50"
    pdf = FPDF(orientation="Portrait", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 55)
    pdf.cell(50, 75, "CS50 Shirtificate")
    pdf.image("shirtificate.png", 40, 70, 125)
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(220, 50, 50)
    pdf.cell(40, 200, name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()