import os
from olds import bank_account_variables

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)


def open_file_bank(mode):
    return open(BASE_PATH + '/_file_bank.dat',mode)

#20=5;50=5;100=5;
def write_money_slips(file):
    for money_bill,value in bank_account_variables.money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')

def write_bank_accounts(file):
    for account,account_data in bank_account_variables.accounts_list.items():
        file.writelines((
            account, ':',
            account_data['name'],';',
            account_data['password'],';',
            str(account_data['value']),';',
            str(account_data['admin']),';',
            '\n'
        ))
def read_money_slips(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        money_bill_value = line[0:semicolon_pos]
        set_money_bill_value(money_bill_value)
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos+1:len(line)]

def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=')
    money_bill = money_bill_value[0:equal_pos]
    count = len(money_bill_value)
    value = money_bill_value[equal_pos+1:count]
    bank_account_variables.money_slips[money_bill] = int(value)

def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extratc_bank_account(account_line)

def extratc_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';')
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        if semicolon_pos + 1 == len(account_line):
            break
        else:
            acctoun_line = account_line[semicolon_pos+1:len(account_line)]
    add_bank_account(account_data)
def add_bank_account(account_data):
    bank_account_variables.accounts_list[account_data[0]] = {
        'name':account_data[1],
        'password':account_data[2],
        'value':float(account_data[3]),
        'admin': bool(account_data[4]),
    }
def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()
    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()

def save_money_slips():
    file = open_file_bank('r')
    lines = file.readline()
    file.close()
    file = open_file_bank('w')
    lines[0] = ""

    for money_bill,value in bank_account_variables.money_slips.items():
        lines[0] += money_bill + '=' + str(value) + ';'
    lines[0] += '\n'
    file.writelines(lines)
    file.close()