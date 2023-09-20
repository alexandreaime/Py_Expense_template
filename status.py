from PyInquirer import prompt
import csv

def read_users_from_csv(filename):
    users = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                users.append(row[0])
    return users

def read_expenses_from_csv(filename):
    expenses = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            expenses.append(row)
    return expenses

def calculate_status(users, expenses):
    status = {user: 0.0 for user in users}
    total_expenses = {user: 0.0 for user in users}

    for expense in expenses:
        # Idk why it is not working...
        spender = expense['spender']
        amount = float(expense['amount'])
        total_expenses[spender] += amount

    for expense in expenses:
        spender = expense['spender']
        payback = expense['payback']

        if spender in payback:
            num_involved = len(payback)
            amount_per_person = float(expense['amount']) / num_involved

            for person in payback:
                if person != spender:
                    status[spender] -= amount_per_person
                    status[person] += amount_per_person

    return status

def print_status():
    users = read_users_from_csv('users.csv')
    expenses = read_expenses_from_csv('expense_report.csv')
    status = calculate_status(users, expenses)

    print("Status Report:")
    for user, balance in status.items():
        if balance > 0:
            print(f"{user} owes {balance:.2f}€")
        elif balance < 0:
            print(f"{user} is owed {-balance:.2f}€")
        else:
            print(f"{user} owes nothing")