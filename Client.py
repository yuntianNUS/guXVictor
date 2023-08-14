from Server import Server


def run(server: Server):
    while True:
        curr_acc_num = int(input("Enter your account number > "))
        customer_name = server.get_cus_name_from_acc_num(curr_acc_num)
        print(f"Hello {customer_name}")
        while True:
            choice = input(
                """
                1. [S]how balance
                2. [W]ithdrawal
                3. [D]eposit
                4. [T]ransfer funds
                5. [Q]uit
                """
            ).upper()

            match choice:
                case "Q":
                    print("Bye bye lol")
                    break
                case "S":
                    print("Your balance is:", server.show_balance(curr_acc_num))
                case "W":
                    try:
                        withdraw_value = int(input("Enter amount to withdraw > "))
                        curr_bal = server.withdraw_balance(curr_acc_num, withdraw_value)
                        print("Withdrawal done. Your balance now is: ", curr_bal)
                    except Exception as e:
                        print(e)
                case "D":
                    try:
                        deposit_value = int(input("Enter amount to deposit > "))
                        curr_bal = server.deposit_balance(curr_acc_num, deposit_value)
                        print("Deposit done. Your balance now is: ", curr_bal)
                    except Exception as e:
                        print(e)
                case "T":
                    try:
                        to_acc_num = int(
                            input(
                                "Enter the account number you'd like to transfer funds to > "
                            )
                        )
                        value = int(
                            input("Enter the amount you would like to transfer > ")
                        )
                        curr_bal = server.transfer_funds(
                            curr_acc_num, to_acc_num, value
                        )
                        print("Your current balance is: ", curr_bal)
                    except Exception as e:
                        print(e)


def main():
    server = Server()
    run(server)
    return


if __name__ == "__main__":
    main()
