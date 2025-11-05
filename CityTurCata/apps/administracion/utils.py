# apps/administracion/utils.py
import csv
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# --- GENERADOR DE CSV ---
def generar_csv(filename, cabecera, datos):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)
    if cabecera:
        writer.writerow(cabecera)
    for fila in datos:
        writer.writerow(fila)
    return response

# --- GENERADOR DE EXCEL ---
def generar_excel(filename, cabecera, datos):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = filename.replace('_', ' ').title()
    
    if cabecera:
        ws.append(cabecera)
    for fila in datos:
        ws.append(fila)

    wb.save(response)
    return response

# --- GENERADOR DE PDF ---
def generar_pdf(filename, titulo, cabecera, datos):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    
    # (Aquí puedes agregar un título al PDF si quieres)
    
    tabla_data = [cabecera] + datos
    t = Table(tabla_data)
    
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    t.setStyle(style)
    
    elements.append(t)
    doc.build(elements)
    
    return response