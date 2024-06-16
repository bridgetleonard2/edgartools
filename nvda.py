import edgar as e

e.set_identity("Bridget Leonard leonardbridget01@gmail.com")

nvda_10k = e.Company("NVDA").get_filings(form="10-K").latest(1)

# Calling .obj() on filing automatically downloads and parses data files into
# data object
tenk = nvda_10k.obj()
print(tenk)

# Can also extract financial statements from 10-k and 10-q
financials = tenk.financials
print(financials.balance_sheet)

# Use to_dataframe method to get as pd df
balance_sheet_df = financials.balance_sheet.to_dataframe()
