<<<<<<< HEAD
# # setup user input loop
# # ----------  write a dummy file to start off with
# import json

# #    create a dummy file
# trans = {"transaction": "deposit", "category": "initial", "amount": 550.50}
# json.dump(trans, open("Codeup_checkbook.txt",'w'))
# trans = {"transaction": "deposit", "category": "paycheck", "amount": 2200.99}
# json.dump(trans, open("Codeup_checkbook.txt",'a'))
# trans = {"transaction": "deposit", "category": "tax refund", "amount": 1.00}
# json.dump(trans, open("Codeup_checkbook.txt",'a'))
# trans = {"transaction": "deposit", "category": "sold bike", "amount": 8000.00}
# json.dump(trans, open("Codeup_checkbook.txt",'a'))
# trans = {"transaction": "withdrawl", "category": "rent", "amount": 500.00}
# json.dump(trans, open("Codeup_checkbook.txt",'a'))
# trans = {"transaction": "withdrawl", "category": "utilities", "amount": 150.80}
# json.dump(trans, open("Codeup_checkbook.txt",'a'))
# trans = {"transaction": "withdrawl", "category": "groceries", "amount": 682.15}
# json.dump(trans, open("Codeup_checkbook.txt",'a'))

=======
# setup user input loop
# ----------  write a dummy file to start off with
import json
filename = "Codeup_checkbook.txt"
checkbook_lst = [
    {
        'transaction': 'append test2',
        'category': 'giraffe',
        'amount': 150.34
    },
]
with open(filename, 'a', encoding='utf-8') as file:
    for item in checkbook_lst:
        x = json.dumps(item, indent=4)
        file.write(x + '\n')
#  now read it back
with open(filename, "r") as read_file:
    transactions = json.load(read_file)
    for x in transactions:
         transamount = transactions['amount']
         action = transaction['category']
         print(transamount, action)
>>>>>>> 3f61a3cba6928c093ab1da410dfb909e91df6529




# ---------------------------------
def get_balance():
    with open('transactions.txt') as w:
        amounts = w.readlines()
        float_amounts = []
        for i in amounts:
            float_amounts.append(float(i))
        print('Your balance is ${:,.2f}'.format(sum(float_amounts)))

# ----------------------------------
def withdraw_balance():
    amount = float(input('What amount would you like to withdraw? '))
    with open('transactions.txt', 'a') as w:
        w.write('{}\n'.format(amount * -1))

# ------------------------------------
def deposit_balance():
    amount = float(input('What amount would you like to deposit? '))
    with open('transactions.txt', 'a') as w:
        w.write('{}\n'.format(amount))

# -------------------------------------
print("-----  Welcome to your terminal checkbook! -----")
user_choice = 0
while user_choice != 4:  
    print('1) View current balance')
    print('2) Record a debit (withdraw)')
    print('3) Record a credit (deposit)')
    print('4) Exit')
    user_choice = input('What would you like to do? Please choose 1-4: ')
    if user_choice.isdigit() == True:
        print('isdigit')
        if int(user_choice) == 1:
            current_balance = get_balance()
            user_choice = 0
        elif int(user_choice) == 2:
            current_balance = withdraw_balance()
            user_choice = 0
        elif int(user_choice) == 3:
            current_balance = deposit_balance()
            user_choice = 0
        elif int(user_choice) == 4:
            print('user choice = 4')
            break    
        else:
            print('I did not undestand your choice. Please try again') 
            user_choice = 0

print('terminal checkbook closed')
# -------------------------------------
#    create a book dictionary

checkbook = [
    {
        'transaction': 'withdraw',
        'category': 'entertainment',
        'amount': 0
    },
    {
        'transaction': 'deposit',
        'category': 'paycheck',
        'amount': 0
    },
    {
        'transaction': 'inquiry',
        'category': '',
        'amount': 0
    },
]



# genre_to_show = input('Enter a genre: ')
# for book in books:
#    if genre_to_show not in book['genre']:
#        continue
 
#    print('---------------')        
#    print('- title: %s' % book['title'])    
#    print('- author: %s' % book['author'])
#    print('- genre: %s' % book['genre'])
