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
    with open('transactions.txt') as w:
        amounts = w.readlines()
        float_amounts = []
        for i in amounts:
            float_amounts.append(float(i))
        print('Your balance is ${:,.2f}'.format(sum(float_amounts)))

# ----------------------------------
def withdraw_balance():
#    some code to build the dictionary
#     like this   transaction = {'transaction': 'deposit', 'category': 'open account', 'amount':25.00 }
    valid_input = False
    deduct_amount = 0
    while valid_input == False:
        deduct_input = input('Debit- Please input the amount to deduct : (or Q to quit)  ')
        if deduct_input.lower() == 'q':
            break
        else:
            try:
                deduct_amount = float(deduct_input)
                if deduct_amount > 0:
                    deduct_amount = 0 - deduct_amount
                transaction = {'transaction': 'withdraw', 'category': 'need to fill in', 'amount': deduct_amount }
                append_dict(transaction)
                valid_input = True
            except:
                print('Invalid input')

    return deduct_amount
# ------------------------------------
def deposit_balance():
#    some code to build the dictionary
#     like this   transaction = {'transaction': 'deposit', 'category': 'open account', 'amount':25.00 }
    valid_input = False
    credit_amount = 0
    while valid_input == False:
        deduct_input = input('Deposit- Please input the amount to credit : (or Q to quit)  ')
        if deduct_input.lower() == 'q':
            break
        else:
            try:
                credit_amount = float(deduct_input)
                if credit_amount < 0:
                    credit_amount = abs(credit_amount)
                transaction = {'transaction': 'deposit', 'category': 'need to fill in', 'amount': credit_amount }
                append_dict(transaction)
                valid_input = True
            except:
                print('Invalid input')

    return credit_amount    
    
    
    
    
    transaction = {'transaction': 'deposit', 'category': 'need to fill in', 'amount': 25.00 }




    append_dict(transaction)
    current_balance = 25
    return current_balance
# -------------------------------------
print("-----  Welcome to your terminal checkbook! -----")
user_choice = 0
while user_choice != 4:  
    print('1) View current balance')
    print('2) Record a debit (withdraw)')
    print('3) Record a credit (deposit)')
    print('4) Exit  (Q)')
    user_choice = input('What would you like to do? Please choose 1-4: ')
    if user_choice.isdigit() == True:
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
            break 
    else:
        if user_choice.lower() == 'q':
            user_choice = 4
        else:  
            print('I did not undestand your choice. Please try again') 
            user_choice = 0
            
print('terminal checkbook closed')
