from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"Your name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        userwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        userwriter.writerow(infos.values())
    print("User Added !")
    return