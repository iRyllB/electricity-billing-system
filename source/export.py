import pandas as pd
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
import os
import platform
from ui_validation import print_message

def export_payment_history(customer):
    if not hasattr(customer, 'bills') or not customer.bills:
        print_message("No payment history to export.")
        return

    # Prepare the data to be exported
    data = [{
        "Units Consumed": bill.units,
        "Bill Amount": round(bill.bill_amount, 2),
        "Final Amount Paid": round(bill.bill_amount, 3),  
        "Payment Date": bill.payment_date,
        "Due Date": bill.due_date,
        "Next Due Date": bill.next_due_date
    } for bill in customer.bills]

    df = pd.DataFrame(data)

    csv_filename = f"{customer.username}_payment_history.csv"
    df.to_csv(csv_filename, index=False)

    # Change page size to landscape
    pdf_filename = f"{customer.username}_payment_history.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=landscape(letter))
    width, height = landscape(letter)
    c.setFont("Helvetica", 10)

    # Title
    c.drawString(200, height - 40, f"Payment History for {customer.username}")

    # Table headers
    x_start = 50
    y_start = height - 80
    row_height = 18  # Reduced row height
    column_widths = [120, 120, 130, 100, 100, 120]  # Adjust column widths
    headers = df.columns.tolist()

    # Draw headers
    for i, header in enumerate(headers):
        c.drawString(x_start + sum(column_widths[:i]), y_start, header)

    y_position = y_start - row_height
    # Draw table content
    for _, row in df.iterrows():
        for i, value in enumerate(row):
            c.drawString(x_start + sum(column_widths[:i]), y_position, str(value))
        y_position -= row_height

    # Add link to the CSV file
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0, 0, 1)  
    c.drawString(50, y_position - 20, "Click here to download the CSV file:")
    csv_file_link = os.path.abspath(csv_filename)
    c.linkURL(csv_file_link, (50, y_position - 30, width - 50, y_position - 20), relative=1)

    c.save()

    print_message(f"Payment history exported successfully! PDF File: {pdf_filename}")
    print("\n--- Payment History ---")
    print(df.to_string(index=False))

    if platform.system() == "Windows":  
        os.system(f"start {pdf_filename}")
    else: 
        os.system(f"xdg-open {pdf_filename}")
