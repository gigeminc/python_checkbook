# initial read of checkbook file
import json
filename = "Codeup_checkbook.json"
# read the entire current checkbook file into a dictionary
data = json.load(open(filename))
# -----------------------------------------
def append_dict(transaction):
    data.append(transaction)
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, sort_keys = True, indent = 4)
# ---------------------------------
def get_balance():
    current_balance = 1.4
    print('calling get_balance')
    return current_balance
# ----------------------------------
def withdraw_balance():
#    some code to build the dictionary
#     like this   transaction = {'transaction': 'deposit', 'category': 'open account', 'amount':25.00 }
    transaction = {'transaction': 'withdraw', 'category': 'need to fill in', 'amount': -25.00 }
    append_dict(transaction)
    current_balance = 25
    return current_balance
# ------------------------------------
def deposit_balance():
#    some code to build the dictionary
#     like this   transaction = {'transaction': 'deposit', 'category': 'open account', 'amount':25.00 }
    transaction = {'transaction': 'deposit', 'category': 'need to fill in', 'amount': 25.00 }
    append_dict(transaction)
    current_balance = 25
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
