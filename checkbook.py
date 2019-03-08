# setup user input loop
# ----------  write a dummy file to start off with
import json

#    create a dummy file
# trans = {"transaction": "deposit", "category": "initial", "amount": 550.50}
json.dump(trans, open("Codeup_checkbook.txt",'w'))
trans = {"transaction": "deposit", "category": "paycheck", "amount": 2200.99}
json.dump(trans, open("Codeup_checkbook.txt",'a'))
trans = {"transaction": "deposit", "category": "tax refund", "amount": 1.00}
json.dump(trans, open("Codeup_checkbook.txt",'a'))
trans = {"transaction": "deposit", "category": "sold bike", "amount": 8000.00}
json.dump(trans, open("Codeup_checkbook.txt",'a'))
trans = {"transaction": "withdrawl", "category": "rent", "amount": 500.00}
json.dump(trans, open("Codeup_checkbook.txt",'a'))
trans = {"transaction": "withdrawl", "category": "utilities", "amount": 150.80}
json.dump(trans, open("Codeup_checkbook.txt",'a'))
trans = {"transaction": "withdrawl", "category": "groceries", "amount": 682.15}
json.dump(trans, open("Codeup_checkbook.txt",'a'))





# ---------------------------------
def get_balance():
    current_balance = 1.4
    print('calling get_balance')
    return current_balance
# ----------------------------------
def withdraw_balance():
    current_balance = 1.4
    print('calling withdraw_balance')
    return current_balance
# ------------------------------------
def deposit_balance():
    current_balance = 1.4
    print('calling deposit_balance')
    return current_balance

# -------------------------------------
print("-----  Welcome to your terminal checkbook! -----")
user_choice = 0
while user_choice != 4:  
    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) exit')
    user_choice = input('What would youlike to do? Please choose 1-4')
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
        'category': 'entertainment'
        'amount': 0,
    },
    {
        'transaction': 'deposit',
        'category': 'paycheck'
        'amount': 0,
    },
    {
        'transaction': 'inquiry',
        'category': ''
        'amount': 0,
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
