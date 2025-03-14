# Import json from stored_data.json and process the orders

from process_data.process_orders import process_order_form, print_order_receipts
from stored_data.data import companies
from process_data.tests import validate_orders
from utils import import_all_modules_from_directory, run_company_specific_functions

def process_and_print_orders():
    import_all_modules_from_directory('company_files')

    # Process the newest order form and store the data
    orders = process_order_form(companies)

    # Apply any company specific transformations
    run_company_specific_functions(orders=orders)

    validate_orders(orders)

    # Return a list of order items
    print_order_receipts(companies, orders)

# Run it all
if __name__ == '__main__':
    process_and_print_orders()



