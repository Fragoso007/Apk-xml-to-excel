import xmltodict
import os
import pandas as pd

def take_info(file_name, values):
    #print(f'took the informations {file_name}')
    with open(f'invoices/{file_name}', 'rb') as file_xml:
        dic_file = xmltodict.parse(file_xml)

        
       
        if 'NFe' in dic_file:
             infos_inv = dic_file['NFe']['infNFe']
        else:
            infos_inv = dic_file['nfeProc']['NFe']['infNFe']
        invoice_number = infos_inv['@Id']
        invoice_issuer = infos_inv['emit']['xNome']
        client_name = infos_inv['dest']['xNome']
        address = infos_inv['dest']['enderDest']
        if 'vol' in infos_inv['transp']:
            gross_weight = infos_inv['transp']['vol']['pesoB']
        else:
            gross_weight = 'uninformed'

        values.append([invoice_number, invoice_issuer, client_name,address, gross_weight])
        

files_list = os.listdir('invoices')

columns = ['invoice_number', 'invoice_issuer', 'client_name', 'address', 'gross_weight']

values = []


for file in files_list:
    take_info(file, values)

tables = pd.DataFrame(columns=columns, data=values)
print(tables)
tables.to_excel('Invoices.xlsx', index=False)