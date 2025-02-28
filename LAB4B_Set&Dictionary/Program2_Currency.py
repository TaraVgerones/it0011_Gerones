file = open('currency.csv', 'r')
column_names = file.readline().strip() #read the first line of the CSV
exchange_rates = {line.strip().split(',')[0]: float(line.strip().split(',')[2]) for line in file}

print('-' * 60)
amount_usd = float(input("How much dollar do you have?  "))
print('-' * 60)
target_currency = input("What currency do you want to have? ").strip().upper()
print('-' * 60)

# Convert currency
converted_amount = exchange_rates.get(target_currency, None)
if converted_amount is not None:
    print(f"Dollar: {amount_usd} USD")
    print(f"{target_currency}: {amount_usd * converted_amount:.2f}")
    print('-' * 60)
else:
    print('-' * 60)
    print("Currency not found.")
    print('-' * 60)
