from reportlab.pdfgen import canvas

pdf = canvas.Canvas("student.pdf")

pdf.drawString(100, 750, "Student Result")
pdf.drawString(100, 720, "Name: Ajay")
pdf.drawString(100, 690, "Marks: 80")
pdf.drawString(100, 660, "Result: Pass")

pdf.save()

print("Student PDF created")
