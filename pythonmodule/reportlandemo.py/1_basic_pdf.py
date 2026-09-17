from reportlab.pdfgen import canvas

pdf = canvas.Canvas("hello.pdf")
pdf.drawString(100, 750, "Hello ReportLab")
pdf.save()

print("PDF created successfully")
