from olds import bank_account_variables
from olds.file_old import save_money_slips
import getpass

def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '10' and bank_account_variables.accounts_list[account_auth]['admin']:
        insert_money_slips()
    elif option_typed == '2':
        withdraw()

def show_balance(account_auth):
    print('Seu saldo é %s' % bank_account_variables.accounts_list[account_auth]['value'])

def insert_money_slips():
    amount_typed = input('Digite a quantidade de células: ')
    money_bill_typed = input('Digite a célula a ser incluída: ')
    bank_account_variables.money_slips[money_bill_typed] += int(amount_typed)
    print(bank_account_variables.money_slips)

def withdraw():
    value_typed = input('Digite o valor a ser sacado: ')

    money_slips_user = {}
    value_int = int(value_typed)
    money_list = [20,50,100]
    for money in money_list:
        if value_int // money > 0 and value_int // money <= bank_account_variables.money_slips[str(money)]:
            money_slips_user[str(money)] = value_int// money
            value_int = value_int - value_int // money * money
    if value_int != 0:
        print('O caixa não tem cédulas disponíveis para esse valor')
    else:
        for money_bill in money_slips_user:
            bank_account_variables.money_slips[money_bill] -= money_slips_user[money_bill]
        save_money_slips()
        print('Pegue as notas: ')
        print(money_slips_user)

def auth_account():
    account_typed = input("Digite sua conta:")
    password_typed = getpass.getpass("Digite sua senha:")

    if account_typed in bank_account_variables.accounts_list and password_typed == bank_account_variables.accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False

def get_menu_options_typed(account_auth):
    print("1 - Saldo")
    print("2 - Saque")
    if bank_account_variables.accounts_list[account_auth]['admin']:
        print("10 - Incluir cédula")
    return input("Escolha uma das opções acima:")


