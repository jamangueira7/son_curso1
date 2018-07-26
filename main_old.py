from olds import operations, ultils
from olds import generate_bank
from olds.file_old import load_bank_data
from olds.bank_account_variables import money_slips,accounts_list

def main():
    load_bank_data()
    print(money_slips)
    print(accounts_list)
    ultils.header()
    account_auth = operations.auth_account()

    if account_auth:
        ultils.clear()
        ultils.header()
        option_typed = operations.get_menu_options_typed(account_auth)
        operations.do_operation(option_typed, account_auth)
    else:
        print('Conta inválida')

#generate_bank.main()
while True:
     main()

