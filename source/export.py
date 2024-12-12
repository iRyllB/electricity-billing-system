import pandas as pd
from ui_validation import print_message

def export_payment_history(customer):
    if not hasattr(customer, 'bills') or not customer.bills:
        print_message("No payment history to export.")
        return

    # Create a DataFrame from payment history
    data = [{
        "Units Consumed": bill.units,
        "Bill Amount": bill.bill_amount,
        "Final Amount Paid": bill.bill_amount,  # Assuming there's no separate final_amount
        "Payment Date": bill.payment_date,
        "Due Date": bill.due_date,
        "Next Due Date": bill.next_due_date
    } for bill in customer.bills]

    df = pd.DataFrame(data)

    # Save to a CSV file
    filename = f"{customer.username}_payment_history.csv"
    df.to_csv(filename, index=False)
    print_message(f"Payment history exported successfully! File: {filename}")

    # Display the DataFrame on the screen
    print("\n--- Payment History ---")
    print(df.to_string(index=False))
