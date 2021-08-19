import pandas as pds
import numpy as npy
import matplotlib as mplt
import openpyxl as opyxl

file = 'database.xlsx'
database = pds.read_excel(io=file, sheet_name="Dados-Questão1")

variavel = (database.head(9), database.tail(0))
print(variavel)
