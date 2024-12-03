from datetime import datetime, timedelta
from reportlab.pdfgen import canvas
import os
import webbrowser

def generate_receipt_pdf(customer, units, total_bill, payment_date, tax_rate, due_date, next_due_date):
    tax_amount = total_bill * (tax_rate / 100)
    total_with_tax = total_bill + tax_amount
    
    receipt_width = 300  # 3 inches wide
    receipt_height = 700  # 7 inches tall
    
    pdf_filename = f"receipt_{customer.account_no}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=(receipt_width, receipt_height))
    
    c.setFont("Courier", 10) 
    
    c.setFont("Courier-Bold", 14)
    c.drawString(80, 670, "USTP OmniCharge")
    
    c.line(50, 660, 250, 660)
    
    c.setFont("Courier", 8)
    c.drawString(50, 640, f"Receipt Number: {datetime.now().strftime('%Y%m%d_%H%M%S')}")
    
    c.setFont("Courier-Bold", 10)
    c.drawString(50, 620, "Customer Details:")
    
    c.setFont("Courier", 8)
    c.drawString(50, 600, f"Account Number: {customer.account_no}")
    c.drawString(50, 580, f"Name: {customer.name}")
    c.drawString(50, 560, f"Phone: {customer.phone_no}")
    c.drawString(50, 540, f"Address: {customer.address}")
    
    c.setFont("Courier-Bold", 10)
    c.drawString(50, 510, "Bill Details:")
    
    c.setFont("Courier", 8)
    c.drawString(50, 490, f"Units Consumed: {units} kWh")
    c.drawString(50, 450, f"VAT ({tax_rate}%): {tax_amount:.2f} PHP")
    c.drawString(50, 430, f"Total: {total_with_tax:.2f} PHP")
    
    c.drawString(50, 410, f"Payment Date: {payment_date}")
    c.drawString(50, 390, f"Due Date: {due_date}")
    c.drawString(50, 370, f"Next Due Date: {next_due_date}")
    
    c.line(50, 400, 250, 400)
    
    c.setFont("Courier-Oblique", 7)
    c.drawString(50, 380, "Thank you for using USTP OmniCharge!")
    c.drawString(50, 360, "Please keep this receipt for your records.")
    
    c.save()

    print(f"Receipt saved as {pdf_filename}")
    
    if os.name == 'nt':  # For Windows
        webbrowser.open(f'file:///{os.path.abspath(pdf_filename)}')
    else:  # For macOS/Linux
        webbrowser.open(f'file://{os.path.abspath(pdf_filename)}')
