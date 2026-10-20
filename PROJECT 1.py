pin = 1235
mpesa_number = "254721254883"
mpesa_name = "John Njuguna"
ACC_BAL = 5000
def mpesa_money_transfer_calculator(recipient_number, transfered_amount, user_pin, recipient_name, user_num):
    if user_pin != pin or not isinstance((user_pin),int) or user_pin <1000 or user_pin >9999:
       return "Your input does not match! Try Again"
    elif transfered_amount > ACC_BAL:
         return "Failed,insufficient Balance"
    elif user_num != mpesa_number or not isinstance(recipient_number,str) or len(recipient_number)!= 12:
         return "Failed,invalid mpesa number"
    elif transfered_amount <= 0:
         return "Failed,invalid transfer amount"
    else:
        return f"success, {transfered_amount} sent to {recipient_name} from {mpesa_name}. Your new balance is {ACC_BAL- transfered_amount}"

   
print("===WELCOME TO MPESA MONEY TRANSFER===")

recipient_number = input("Enter the receipient mpesa number:")
transfered_amount = int(input("Enter amount you want to transfer:"))
user_pin = int(input("Enter your pin:"))
recipient_name = input("Enter the receipient name:")
user_num = str(input("Enter your mpesa number:"))

outcome = mpesa_money_transfer_calculator(recipient_number, transfered_amount, user_pin, recipient_name, user_num)


print(outcome)


