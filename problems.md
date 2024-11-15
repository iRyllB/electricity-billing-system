1. Customer ID Generation
Change: Customer ID should be randomly generated.
Update: During account creation, generate a random Customer ID and store it in the database.
Database Update: Add a column for customer_id in the log_in table to store this value.

2. Update Customer Details View
Change: Include customer name and random-generated customer ID in the details.
View: Ensure the customer_id, cust_name, and address are displayed when viewing customer details.

3. Optional Message for Rating
Change: Add an optional message field for user feedback during rating.
Database Update: Add a column for rating_message to store the optional message (can be added to the log_in table or a separate table).
Function Update: Allow users to leave an optional message with their rating.

4. Update Customer Number
Change: The phone number should not be asked during billing but should be collected during account creation.
Function Update: Collect the phone number during account creation and store it in the log_in table.

5. Update Account Functionality
Change: Add an option in the dashboard to update account details.
Ability to update phone number.
Ability to update address.
Functionality: Allow users to modify their phone number and address in the log_in and consumer_details tables.

6. Create Account Updates
Change: Add address input during account creation.
Database Update: Add address column to the log_in and consumer_details tables.
Function Update: Ensure the address is saved and displayed in the user details.

7. Database Updates to Match New Code
Changes Required:
Add a customer_id column to the log_in table (if not already done).
Add phone_no, address columns to log_in and consumer_details tables.
Optionally, create a separate table for storing feedback (rating_message).
Database Update Summary
Add customer_id (randomly generated) to log_in and consumer_details tables.
Add phone_no and address columns to both log_in and consumer_details tables.
Add rating_message column to store feedback from users in the log_in table.
Dashboard Menu Updates
You will need to update the dashboard menu options:

Add an option to update customer details (phone number, address).
Allow users to modify phone number and address through a separate function.
Ensure the details shown on the dashboard reflect any updates made.
