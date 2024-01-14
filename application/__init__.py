from datetime import datetime

def print_current_date():
    current_date = datetime.today()
    formatted_date = current_date.strftime('%Y-%m-%d')
    print(f"Текущая дата: {formatted_date}")

print_current_date()

