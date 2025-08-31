def get_amount():
  while True:
    try:
      amount = float(input('Enter the amount: '))
      if amount <= 0:
        raise ValueError()
      return amount
    except ValueError:
      print('Invalid amount')

def get_currency(label):
  currencies = ('USD', 'EUR', 'CAD','INR')
  while True:
    currency = input(f'{label} currency (USD/EUR/CAD/INR): ').upper()
    if currency not in currencies:
      print('Invalid currency')
    else:
      return currency


def convert(amount, source_currency, target_currency):
  exchange_rates = {
    'USD': { 'EUR': 0.85, 'CAD': 1.25,'INR': 88.15 },
    'EUR': { 'USD': 1.18, 'CAD': 1.47, 'INR': 102.98 },
    'CAD': { 'USD': 0.80, 'EUR': 0.68, 'INR': 64.17 },
    'INR': { 'USD': 0.011, 'EUR': 0.0097, 'CAD': 0.016 }
  }

  if source_currency == target_currency:
    return amount
  
  return amount * exchange_rates[source_currency][target_currency]

def main():
  amount = get_amount()
  source_currency = get_currency('Source')
  target_currency = get_currency('Target')
  converted_amount = convert(amount, source_currency, target_currency)
  print(f'{amount} {source_currency} is equal to {converted_amount:.2f}')


if __name__ == "__main__":
  main()