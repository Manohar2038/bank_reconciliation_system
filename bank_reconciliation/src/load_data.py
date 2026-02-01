from data_loader import load_internal_transactions, load_bank_transactions

load_internal_transactions("../internal_transactions.csv")
load_bank_transactions("../bank_transactions.csv")

print("Data loaded successfully")
