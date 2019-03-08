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
