#This project introduces the core functionality of a simple invoice payment application, where users can log in, select an invoice type, input usage amounts, and complete the payment process using their credit card details.


ahmet_page = {
    "name": "Ahmet",
    "surname": "Yılmaz",
    "ID": "12345678901",
    "birth_date": "1990-05-15",
    "password": "ahmet1234"
}
mehmet_page = {
    "name": "Mehmet",
    "surname": "Kaya",
    "ID": "23456789012",
    "birth_date": "1985-07-22",
    "password": "mehmet5678"
}
elif_page = {
    "name": "Elif",
    "surname": "Demir",
    "ID": "34567890123",
    "birth_date": "1993-11-30",
    "password": "elif91011"
}

users = [ahmet_page, mehmet_page, elif_page]

def login(ID: str, password: str) -> dict:
    ID = ID.strip()
    password = password.strip()
    for user in users:
        if user['ID'] == ID and user['password'] == password:
            return user
    return {}

def pay_invoice(invoice_type: str, contract_number: str, usage_amount: int):
    if invoice_type.lower() == 'electricity':
        amount = usage_amount * 0.18  #as vat
        print(f'Electricity bill for contract {contract_number}, need to pay: {amount} TL')
        return amount
    elif invoice_type.lower() == 'water':
        amount = usage_amount * 0.05
        print(f'Water bill for contract {contract_number}, need to pay: {amount} TL')
        return amount
    elif invoice_type.lower() == 'gas':
        amount = usage_amount * 0.20
        print(f'Gas bill for contract {contract_number}, need to pay: {amount} TL')
        return amount
    else:
        print('Invalid invoice type!')
        return 0


def get_credit_card_details():
    card_number = input('Enter your credit card number (16 digits): ').strip()
    expiration_date = input('Enter the expiration date (MM/YY): ').strip()
    ccv = input('Enter the CCV code (3 digits): ').strip()

    if len(card_number) == 16 and len(expiration_date) == 5 and len(ccv) == 3:
        print('Credit card information successfully received.')
        return True
    else:
        print('Invalid credit card information. Please try again.')
        return False

def main():
    while True:
        ID = input('ID: ').strip()
        password = input('Password: ').strip()

        login_user = login(ID, password)
        if login_user:
            print(f'Welcome {login_user['name']}, please choose the invoice you want to pay: Electricity / Water / Gas')
            invoice_type = input('Invoice type: ').strip()
            contract_number = input('Contract number: ').strip()
            usage_amount = int(input('Usage amount: ').strip())

            amount = pay_invoice(invoice_type, contract_number, usage_amount)

            if amount > 0:
                if get_credit_card_details():
                    print(f'Payment successful for {amount} TL. Thank you for your payment!')
                    break
                else:
                    print('Payment could not be processed. Please try again.')
                    break
        else:
            print('Invalid login, please try again.')

if __name__ == "__main__":
    main()

