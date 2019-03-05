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
                desc = input('Input a description for this transaction or press Enter to skip: ')
                if desc == '':
                    desc = None
                transaction = {}
                transaction['transaction'] = 'withdraw'
                transaction['category'] = c
                transaction['date'] = str(d.date.today())
                transaction['time'] = str(d.datetime.now().time())
                transaction['amount'] = deduct_amount
                transaction['description'] = desc
                append_dict(transaction)
                valid_input = True
            except:
                print('Invalid input')

    return deduct_amount

# ------------------------------------
def deposit_balance():
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
                desc = input('Input a description for this transaction or press Enter to skip: ')
                if desc == '':
                    desc = ' '
                transaction = {}
                transaction['transaction'] = 'deposit'
                transaction['category'] = c
                transaction['amount'] = credit_amount
                transaction['date'] = str(d.date.today())
                transaction['time'] = str(d.datetime.now().time())
                transaction['description'] = desc
                append_dict(transaction)
                valid_input = True
                print('Your current balance is now ${:,.2f}'.format(get_balance()))
            except:
                print('Invalid input')
    return credit_amount    

# -------------------------------------
def transaction_history():
    print('    Date   |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('-----------|-----------------|----------------|------------|-------------|-----------------------------------')
    for i in data:
        print('{:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
    

# -------------------------------------
def category_transactions():
    defined_category = input('What category would you like to filter by? ')
    print('\n')
    n = 0
    amount_total = 0
    print('    Date   |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('-----------|-----------------|----------------|------------|-------------|----------------------------------')
    for i in data:
        if i['category'].lower() == defined_category.lower():
            print('{:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
def day_search():
    defined_day = input('What day would you like to see transactions for? (Enter in format YYYY-MM-DD) ')
    print('\n')
    n = 0
    amount_total = 0
    print('    Date   |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('-----------|-----------------|----------------|------------|-------------|--------------------------------')
    for i in data:
        if i['date'] == defined_day:
            print('{:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
def desc_search():
    keywords = input('Please type the keywords to search by separated for a space: ')
    keyword_list = keywords.lower().split(' ')
    print('    Date   |      Time       |   Transaction  |   Amount   |  Category')
    print('-----------|-----------------|----------------|------------|-----------')
    for i in data:
        desc_list = i['description'].lower().split(' ')
        if set(keyword_list).issubset(desc_list):
            print('{:^5} | {:^5} | {:^14} | {:^10} | {:^9}'.format(i['date'], i['time'], i['transaction'], i['amount'], i['category']))

        
# -------------------------------------
print("-----  Welcome to your terminal checkbook! -----")
user_choice = 0
while user_choice != 4:  
    print('\n')
    print('1) View current balance')
    print('2) Record a debit (withdraw)')
    print('3) Record a credit (deposit)')
    print('4) View transaction history')
    print('5) View transactions from a category')
    print('6) View transactions on a certain day')
    print('7) Search transactions by keywords')
    print('8) Exit')
    print('\n')
    user_choice = input('What would you like to do? Please choose 1-8: ')
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
            desc_search()
            user_choice = 0
        elif int(user_choice) == 8:
            print('user choice = 8')
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
