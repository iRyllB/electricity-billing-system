from datetime import datetime, timedelta
from reportlab.pdfgen import canvas
import os
import webbrowser

def generate_receipt_pdf(customer, units, total_bill, payment_date, tax_rate, due_date, next_due_date):
    generation_charge = 11.42
    transmission_charge = 0.8786
    sysloss_charge = 1.045
    distribution_charge = 0.4613
    supply_charge = 0.5376
    metering_charge = 0.3205
    rp_tax_provision = 0.0105
    franchi_tax_cur = 0.0022
    business_tax_cur = 0.0085
    
    tax_amount = total_bill * (tax_rate / 100)
    total_with_tax = total_bill + tax_amount
    
    # PDF dimensions
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
    
    c.line(50, 460, 250, 460) 
    
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
    
    #Bill Details
    c.setFont("Courier", 8)
    c.drawString(50, 330, f"Units Consumed: {units} kWh")
    c.drawString(50, 310, f"Generation Charge: {generation_charge:.2f} PHP")
    c.drawString(50, 290, f"Transmission Charge: {transmission_charge:.4f} PHP")
    c.drawString(50, 270, f"SysLoss Charge: {sysloss_charge:.3f} PHP")
    c.drawString(50, 250, f"Distribution Charge: {distribution_charge:.4f} PHP")
    c.drawString(50, 230, f"Supply Charge: {supply_charge:.4f} PHP")
    c.drawString(50, 210, f"Metering Charge: {metering_charge:.4f} PHP")
    c.drawString(50, 190, f"RP Tax Provision: {rp_tax_provision:.4f} PHP")
    c.drawString(50, 170, f"Franchise Tax Cur: {franchi_tax_cur:.4f} PHP")
    c.drawString(50, 150, f"Business Tax Cur: {business_tax_cur:.4f} PHP")
    
    c.setFont("Courier-Bold", 10)
    c.setFillColorRGB(1, 0, 0) 
    c.drawString(50, 130, f"VAT ({tax_rate}%): {tax_amount:.2f} PHP")
    c.setFont("Courier-Bold", 12)
    c.drawString(50, 110, f"NET TOTAL: {total_with_tax:.2f} PHP")
    
    c.setFont("Courier-Bold", 10)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(50, 90, f"Payment Date: {payment_date}")
    c.drawString(50, 70, f"Due Date: {due_date}")
    c.drawString(50, 50, f"Next Due Date: {next_due_date}")
    
    c.line(50, 40, 250, 40)
    
    c.setFont("Courier-Oblique", 7)
    c.drawString(50, 20, "Thank you for using USTP OmniCharge!")
    c.drawString(50, 10, "Please keep this receipt for your records.")
    c.save()

    print(f"Receipt saved as {pdf_filename}")
    
    # Automatically open the PDF
    if os.name == 'nt':  # For Windows
        webbrowser.open(f'file:///{os.path.abspath(pdf_filename)}')
    else:  # For MAC/Linux
        webbrowser.open(f'file://{os.path.abspath(pdf_filename)}')
