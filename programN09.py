import pandas as pd

clients = {'first_name': ['Oralie', 'Imojean', 'Michele', 'Ailbert', 'Stevy'],
           'last_name': ['Fidgeon', 'Benet', 'Woodlands', 'Risdale', 'MacGorman'],
           'age': [30, 21, 29, 22, 24]}
clients = pd.DataFrame(clients, columns = ['first_name', 'last_name', 'age'])
print("Mi primer dataframe:")
print(clients)
print("\n")
invoices = {'invoice_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'cliend_id': [3, 2, 7, 2, 7, 3, 1, 4, 2, 3, 6, 2],
            'amount': [77.91, 24.36, 74.65, 19.75, 27.46, 17.13, 45.77, 81.7, 14.41, 52.69, 32.03, 12.78]}
invoices = pd.DataFrame(invoices, columns = ['invoice_id', 'cliend_id', 'amount'])
print("Mi segundo dataframe:")
print(invoices)
print("\n")
print("Ahora toca concatenar los dataframe 1 y 2:")
new_clients = pd.DataFrame({'first_name' : 
