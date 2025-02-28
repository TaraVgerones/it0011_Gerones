date_input = input('Enter the Date (MM/DD/YYYY): ')
month, day, year = date_input.split('/')

month_names = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

month_index = int(month) - 1
month_name = month_names[month_index] if 0 <= month_index < 12 else 'Invalid month'

if month_name != 'Invalid month':
    date_output = f'{month_name} {int(day)}, {year}'
    print(f'Date Output: {date_output}')
else:
    print('Invalid date format. Please enter a valid date in mm/dd/yyyy format.')
