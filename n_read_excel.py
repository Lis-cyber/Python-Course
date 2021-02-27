import pandas as pd

# Print name sheets
# file = pd.ExcelFile("/Users/Usuario/Desktop/sales.xlsx")
file = pd.ExcelFile("/Users/Usuario/Desktop/Python-Course/sales.xlsx")
print(file.sheet_names) # ['sales', 'customers']

# Print data sheet
sheet = file.parse("sales")
print(sheet)
print(type(sheet)) # <class 'pandas.core.frame.DataFrame'>

# Print Data Column
print(sheet.Date)
# Sum column values
print(sheet.Amount.sum())
# Locate a single row of data
print(sheet.loc[0])
print(sheet.loc[0, "Amount"])

# Found all de data by index
sheet.set_index("Customer", inplace=True)
print(sheet.loc["MMC Inc."])
sheet = sheet.reset_index()

# Found the data by series
print(sheet.loc[sheet["Invoice"] == 99])
print(sheet.loc[sheet["Amount"] > 1800])
print(sheet.loc[sheet["Amount"].idxmax()])
print(sheet.loc[sheet["Amount"].idxmax()]["Customer"])
print(sheet.loc[sheet["Amount"] > 1800]["Customer"].unique())


for customer in sheet.loc[sheet["Amount"] > 1800]["Customer"].unique():
  print(customer)


