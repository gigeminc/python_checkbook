# initial read of checkbook file
import json
import datetime as d
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
    all_transactions = []
    for i in data:
        all_transactions.append(i['amount'])
    return sum(all_transactions)
    

# ----------------------------------
def withdraw_balance():
#    some code to build the dictionary
#     like this   transaction = {'transaction': 'deposit', 'category': 'open account', 'amount':25.00 }
    c = input('Category for withdraw? ')
    print('\n')
    a = (int(input('Amount to debit? ')) * -1)
    print('\n')
    transaction = {}
    transaction['transaction'] = 'withdraw'
    transaction['category'] = c
    transaction['amount'] = a
    transaction['date'] = str(d.date.today())
    transaction['time'] = str(d.datetime.now().time())
    # transaction = {'transaction': 'withdraw', 'category': 'need to fill in', 'amount': -25.00 }
    append_dict(transaction)
    return print('Your current balance is now ${:,.2f}'.format(get_balance()))

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
                c = input('Category for withdraw? ')
                transaction = {}
                transaction['transaction'] = 'withdraw'
                transaction['category'] = c
                transaction['date'] = str(d.date.today())
                transaction['time'] = str(d.datetime.now().time())
                transaction['amount'] = deduct_amount
                # transaction = {'transaction': 'withdraw', 'category': 'need to fill in', 'amount': deduct_amount }
                append_dict(transaction)
                valid_input = True
            except:
                print('Invalid input')

    return deduct_amount

# ------------------------------------
def deposit_balance():
#    some code to build the dictionary
#     like this   transaction = {'transaction': 'deposit', 'category': 'open account', 'amount':25.00 }
    c = input('Category for deposit? ')
    print('\n')
    a = int(input('Amount to credit? '))
    print('\n')
    transaction = {}
    transaction['transaction'] = 'deposit'
    transaction['category'] = c
    transaction['amount'] = a
    transaction['date'] = str(d.date.today())
    transaction['time'] = str(d.datetime.now().time())
    # transaction = {'transaction': 'withdraw', 'category': 'need to fill in', 'amount': -25.00 }
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
                c = input('Category for deposit? ')
                transaction = {}
                transaction['transaction'] = 'deposit'
                transaction['category'] = c
                transaction['amount'] = credit_amount
                transaction['date'] = str(d.date.today())
                transaction['time'] = str(d.datetime.now().time())
                transaction = {'transaction': 'deposit', 'category': 'need to fill in', 'amount': credit_amount }
                append_dict(transaction)
                valid_input = True
            except:
                print('Invalid input')

    return credit_amount    
    
    
    
    
    # transaction = {'transaction': 'deposit', 'category': 'need to fill in', 'amount': 25.00 }

    append_dict(transaction)
    return print('Your current balance is now ${:,.2f}'.format(get_balance()))

# -------------------------------------
def transaction_history():
    for transaction in data:
        print(transaction)
    

# -------------------------------------
def category_transactions():
    defined_category = input('What category would you like to filter by? ')
    print('\n')
    n = 0
    amount_total = 0
    for i in data:
        if i['category'] == defined_category:
            print(i)
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
def day_search():
    defined_day = input('What day would you like to see transactions for? (Enter in format YYYY-MM-DD)')
    print('\n')
    n = 0
    amount_total = 0
    for i in data:
        if i['date'] == defined_day:
            print(i)
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
print("-----  Welcome to your terminal checkbook! -----")
user_choice = 0
while user_choice != 4:  
    print('\n')
    print('1) View current balance')
    print('2) Record a debit (withdraw)')
    print('3) Record a credit (deposit)')
<<<<<<< HEAD
    print('4) View transaction history')
    print('5) View transactions from a category')
    print('6) View transactions on a certain day')
    print('7) Exit')
    print('\n')
    user_choice = input('What would you like to do? Please choose 1-7: ')
    print('\n')
    if user_choice.isdigit() == True:
        #
        print('\n')
        if int(user_choice) == 1:
            print('Your current balance is ${:,.2f}.'.format(get_balance()))
            user_choice = 0
        elif int(user_choice) == 2:
            withdraw_balance()
            user_choice = 0
        elif int(user_choice) == 3:
            deposit_balance()
            user_choice = 0
        elif int(user_choice) == 4:
            transaction_history()
            user_choice = 0
        elif int(user_choice) == 5:
            category_transactions()
            user_choice = 0
        elif int(user_choice) == 6:
            day_search()
            user_choice = 0
        elif int(user_choice) == 7:
            print('user choice = 7')
            print('\n')
            break    
        else:
            print('I did not understand your choice. Please try again') 
            print('\n')
            user_choice = 0
    else:
        if user_choice.lower() == 'q':
            user_choice = 7
        else:
            print('I did not understand your choice. Please try again') 
            print('\n')
            user_choice = 0
            
print('terminal checkbook closed')
