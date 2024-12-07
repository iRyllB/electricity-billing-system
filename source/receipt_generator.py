from datetime import datetime
from reportlab.pdfgen import canvas
import os
import webbrowser

def generate_receipt_pdf(customer, units, total_bill, payment_date, tax_rate, due_date, next_due_date):
    tax_amount = total_bill * (tax_rate / 100)
    total_with_tax = total_bill + tax_amount
    
    receipt_width = 300  # 3 inches wide
    receipt_height = 600  # 6 inches tall
    
    pdf_filename = f"receipt_{customer.account_no}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=(receipt_width, receipt_height))
    
    # LOGO
    try:
        logo_path = "logo.png"
        c.drawImage(logo_path, 45, 450, width=200, height=150, preserveAspectRatio=True, mask='auto')
    except Exception as e:
        print(f"Error inserting logo: {e}")
    
    c.line(50, 460, 250, 460)  # Line below the logo
    
    # Receipt Details Header
    c.setFont("Courier-Bold", 10)
    c.drawString(50, 440, f"Receipt Number: {datetime.now().strftime('%Y%m%d_%H%M%S')}")
    
    c.setFont("Courier-Bold", 10)
    c.drawString(50, 420, "Customer Details:")
    
    # Customer Info
    c.setFont("Courier", 8)
    c.drawString(50, 400, f"Account Number: {customer.account_no}")
    c.drawString(50, 380, f"Name: {customer.first_name} {customer.last_name}")
    
    c.setFont("Courier-Bold", 10)
    c.drawString(50, 350, "Bill Details:")
    
    # Bill Info
    c.setFont("Courier", 8)
    c.drawString(50, 330, f"Units Consumed: {units} kWh")
    c.drawString(50, 310, f"VAT ({tax_rate}%): {tax_amount:.2f} PHP")
    c.drawString(50, 290, f"Total (with tax): {total_with_tax:.2f} PHP")
    c.drawString(50, 270, f"Payment Date: {payment_date}")
    c.drawString(50, 250, f"Due Date: {due_date}")
    c.drawString(50, 230, f"Next Due Date: {next_due_date}")
    
    c.line(50, 220, 250, 220)  # Line before footer
    
    # Footer
    c.setFont("Courier-Oblique", 7)
    c.drawString(50, 200, "Thank you for using USTP OmniCharge!")
    c.drawString(50, 180, "Please keep this receipt for your records.")
    
    c.save()

    print(f"Receipt saved as {pdf_filename}")
    
    # Automatically open the PDF
    if os.name == 'nt':  # For Windows
        webbrowser.open(f'file:///{os.path.abspath(pdf_filename)}')
    else:  # For macOS/Linux
        webbrowser.open(f'file://{os.path.abspath(pdf_filename)}')
