from fpdf import FPDF

class Photo():

    def __init__(self, name):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 45)
        pdf.cell(0, 60, 'CS50 Shirtificate', align='C')
        pdf.image('shirtificate.png', x=0, y=70)
        pdf.set_font('Arial', 'B', 30)
        pdf.set_text_color(255, 255, 255)
        pdf.set_xy(0, 140)
        pdf.cell(0, 10, f'{name} took CS50', align='C')
        pdf.output('shirtificate.pdf')

name = 'Adriano'
pdf = Photo(name)
