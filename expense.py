from PyInquirer import prompt
import csv

def read_users_from_csv(filename):
    users = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                users.append({"name": row[0], "value": row[0]})
    return users

user_choices = read_users_from_csv('users.csv')

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "Spender",
        "choices": user_choices,
    },
    {
        "type": "checkbox",
        "name": "payback",
        "message": "People involved in the expense: ",
        "choices": user_choices,
    }
]

def new_expense(*args):
    while True:
        infos = prompt(expense_questions)
        
        try:
            amount = float(infos['amount'])
        except ValueError:
            print("Integer expected for your amout !")
            continue
        
        break
    # Writing the informations to an external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        expensewriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        expensewriter.writerow(infos.values())
    print("Expense Added !")
    return True
