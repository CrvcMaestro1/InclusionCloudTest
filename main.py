from question_2 import WindowsDialog
from question_3 import even_numbers_first_way, even_numbers_second_way
from question_4 import result_one, result_two
from question_5 import InvoiceManager

print("---------------------------------------# Test question 1 and 2 #---------------------------------")
# Classmethod
WindowsDialog.show_default_message()
# Instance method
windowsDialog = WindowsDialog(10, 20, False, True, 5.5, 10.5)
windowsDialog.render()

print("---------------------------------------# Test question 3 #---------------------------------------")
# First way
print(even_numbers_first_way)
# Second way
print(even_numbers_second_way)

print("---------------------------------------# Test question 4 #---------------------------------------")
# First case
print(f"Case 1: {result_one}")
# Second case
print(f"Case 2: {result_two}")

print("---------------------------------------# Test question 5 #---------------------------------------")
invoice_manager = InvoiceManager("fixtures.json")
# Payee ID
print(f"Payee ID: {invoice_manager.get_payee_id()}")
# Invoices that contain the text "583"
print(f"Invoices that contain the text '583': {invoice_manager.filter_invoices_by_text('583')}")
# Change any date/time fields to text in the format "%Y-%m-%dT%H:%M:%S"
new_filename = invoice_manager.change_dateformat("receivedDateTime")
print(f"Change datetime field to text format: filename written {new_filename}")
# Write the json document back out to a new file
print(f"Write the json document back out to a new file: {new_filename}")
