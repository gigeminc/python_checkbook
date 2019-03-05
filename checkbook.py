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
def overwrite_dict(x):
    with open(filename, 'w') as json_file:
        json.dump(x, json_file, sort_keys = True, indent = 4)

# ---------------------------------
def get_balance():
    all_transactions = []
    for i in data:
        all_transactions.append(i['amount'])
    return sum(all_transactions)
    

# ----------------------------------
def withdraw_balance():
    filename = "Codeup_checkbook.json"
    valid_input = False
    deduct_amount = 0
    while valid_input == False:
        deduct_input = input('Debit- Please input the amount to deduct : (or Q to quit)  ')
        if deduct_input.lower() == 'q':
            break
        else:
            try:
                # sets data to global scope so that it can be modified within the function
                global data
                deduct_amount = float(deduct_input)
                if deduct_amount > 0:
                    deduct_amount = 0 - deduct_amount
                c = input('Category for withdraw? ')
                desc = input('Input a description for this transaction or press Enter to skip: ')
                if desc == '':
                    desc = ' '
                transaction = {}
                transaction['transaction'] = 'withdraw'
                transaction['category'] = c
                transaction['date'] = str(d.date.today())
                transaction['time'] = str(d.datetime.now().time())
                transaction['amount'] = deduct_amount
                transaction['description'] = desc
                append_dict(transaction)
                data_with_new_transaction = json.load(open(filename))
                data_with_new_transaction[data_with_new_transaction.index(transaction)]['transaction_id'] = data_with_new_transaction.index(transaction)
                overwrite_dict(data_with_new_transaction)
                data = data_with_new_transaction
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
                global data
                credit_amount = float(deduct_input)
                if credit_amount < 0:
                    credit_amount = abs(credit_amount)
                c = input('Category for deposit? ')
                desc = input('Input a description for this transaction or press Enter to skip: ')
                if desc == '':
                    desc = ' '
                # creates an empty dictionary to be filled
                transaction = {}
                transaction['transaction'] = 'deposit'
                transaction['category'] = c
                transaction['amount'] = credit_amount
                transaction['date'] = str(d.date.today())
                transaction['time'] = str(d.datetime.now().time())
                transaction['description'] = desc
                append_dict(transaction)
                # creates a variable to store the json file that we just modified with the current transaction
                data_with_new_transaction = json.load(open(filename))
                # adds id number to current transaction based on index of transaction in list
                data_with_new_transaction[data_with_new_transaction.index(transaction)]['transaction_id'] = data_with_new_transaction.index(transaction)
                # overwrites the previous json file so that current transaction now has an id
                overwrite_dict(data_with_new_transaction)
                # overwrites global data variable so that it is updated to contain current transaction with id number
                data = data_with_new_transaction
                valid_input = True
                print('Your current balance is now ${:,.2f}'.format(get_balance()))
            except:
                print('Invalid input')
    return credit_amount    

# -------------------------------------
def transaction_history():
    n = 0
    amount_total = 0
    temp_list = []
    print(' id |    Date    |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('----|------------|-----------------|----------------|------------|-------------|----------------------------------')
    for i in data:
        print('{:^4}| {:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['transaction_id'], i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
        n += 1
        amount_total = amount_total + i['amount']
        temp_list.append(i)
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))
    

# -------------------------------------
def category_search():
    defined_category = input('What category would you like to filter by? ')
    print('\n')
    n = 0
    amount_total = 0
    print(' id |    Date    |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('----|------------|-----------------|----------------|------------|-------------|----------------------------------')
    for i in data:
        if i['category'].lower() == defined_category.lower():
            print('{:^4}| {:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['transaction_id'], i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
def day_search():
    defined_day = input('What day would you like to see transactions for? (Enter in format YYYY-MM-DD) ')
    print('\n')
    n = 0
    amount_total = 0
    print(' id |    Date    |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('----|------------|-----------------|----------------|------------|-------------|----------------------------------')
    for i in data:
        if i['date'] == defined_day:
            print('{:^4}| {:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['transaction_id'], i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
def desc_search():
    keywords = input('Please type the keywords to search for separated by a space: ')
    keyword_list = keywords.lower().split(' ')
    n = 0
    amount_total = 0
    print(' id |    Date    |      Time       |   Transaction  |   Amount   |  Category   |            Description ')
    print('----|------------|-----------------|----------------|------------|-------------|----------------------------------')
    for i in data:
        desc_list = i['description'].lower().split(' ')
        if set(keyword_list).issubset(desc_list):
            print('{:^4}| {:^5} | {:^5} | {:^14} | {:^10} | {:^10}  |   {:^20}'.format(i['transaction_id'], i['date'], i['time'], i['transaction'], i['amount'], i['category'], i['description']))
            n += 1
            amount_total = amount_total + i['amount']
    print('There are a total of {} transaction(s) totaling an amount of ${:,.2f}'.format(n, amount_total))

# -------------------------------------
def modify_transaction():
    global data
    print('\n')
    transaction_number = int(input('Choose the transaction id of the transaction you would like to modify: '))
    print('What information would you like to modify? ')
    print('1) Amount')
    print('2) Category')
    print('3) Description')
    info_number = int(input('Please choose 1 - 3: '))
    info_key = ''
    if info_number == 1:
        info_key = 'amount'
        new_info = float(input('Enter the correct information for {}: '.format(info_key)))
        if data[transaction_number]['transaction'] == 'withdraw':
            if new_info > 0:
                    new_info = 0 - new_info
    if info_number == 2:
        info_key = 'category'
        new_info = input('Enter the correct information for {}: '.format(info_key))
    if info_number == 3:
        info_key = 'description'
        new_info = input('Enter the correct information for {}: '.format(info_key))
    data[transaction_number][info_key] = new_info
    overwrite_dict(data)



# -------------------------------------
def modify_menu():
    print('You have chosen to modify a transaction.')
    print('First, choose an option below: ')
    user_choice = 0
    while user_choice != 4:  
        print('\n')
        print('1) View all transactions:')
        print('2) Search for a transaction by date:')
        print('3) Search for a transaction by category')
        print('4) Search for a transaction by description')
        print('5) Exit to main menu')
        print('\n')
        user_choice = input('What would you like to do? Please choose 1-5 (Q to quit): ')
        print('\n')
        if user_choice.isdigit() == True:
            print('\n')
            if int(user_choice) == 1:
                transaction_history()
                modify_transaction()
                user_choice = 0
            elif int(user_choice) == 2:
                day_search()
                modify_transaction()
                user_choice = 0
            elif int(user_choice) == 3:
                category_search()
                modify_transaction()
                user_choice = 0
            elif int(user_choice) == 4:
                desc_search()
                modify_transaction()
                user_choice = 0
            elif int(user_choice) == 5:
                print('user choice = 5')
                print('\n')
                break    
            else:
                print('I did not understand your choice. Please try again') 
                print('\n')
                user_choice = 0
        else:
            if user_choice.lower() == 'q':
                user_choice = 4
            else:
                print('I did not understand your choice. Please try again') 
                print('\n')
                user_choice = 0
    



        
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
    print('6) View transactions on a certain date')
    print('7) Search transactions by keywords')
    print('8) Modify a transaction')
    print('9) Exit')
    print('\n')
    user_choice = input('What would you like to do? Please choose 1-9 (q to quit): ')
    print('\n')
    if user_choice.isdigit() == True:
        #
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
            category_search()
            user_choice = 0
        elif int(user_choice) == 6:
            day_search()
            user_choice = 0
        elif int(user_choice) == 7:
            desc_search()
            user_choice = 0
        elif int(user_choice) == 8:
            modify_menu()
            user_choice = 0
        elif int(user_choice) == 9:
            print('user choice = 9')
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
