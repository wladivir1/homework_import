from datetime import datetime, date
from config import token
from aplication.salary import calculate_salary
from aplication.db.people import get_employees

def main():
    calculate = calculate_salary()
    employees = get_employees()
    print( f'переменная с которой потом можно будет работать: {token}')
    print(f'имя: {employees} запралта: {calculate}$ текущая дата: {datetime.now().date()}')

if __name__ == '__main__':
    # calculate_salary()
    # get_employees()
    main()