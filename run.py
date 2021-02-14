import sys
from users import User
from credentials import Credential

def main():
    home = True
             
    head = ' ***********************************************************************************************'
    while home:
        print(head)
        print('|\t\t\t\t\t\t\t\t\t\t\t\t| \n|\t\t\t\tHi.Welcome\tto\tthe\tPassword-Locker\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|\n|\t\t\t***Have all your credentials from one point.***\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|\n|\tSelect a number to proceed...\t\t\t\t\t\t\t\t|\n|1. Create a password\t\t\t\t\t\t\t\t\t\t|\n|2. Login with an existing\t\t\t\t\t\t\t\t\t\t|\n|3. Exit Password-Locker\t\t\t\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|')
        print(head)

        option = input()
        if option == '1':
            signup = False
            while not signup:
                print('--------------------------------------------------------')
                print('|\t\t\t\t\t\t\t|\n|\tHi! the system says- "Happy you are running me".\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter  Your first name\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                print('--------------------------------------------------------')
                first_name = input()
                if first_name == '1':
                    signup = not signup
                else: 
                    print('--------------------------------------------------------')
                    print('|\t\t\t\t\t\t\t|\n|\tHi! the system says- "Happy you are running me"\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter Your last name\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                    print('--------------------------------------------------------')
                    last_name = input()
                    if last_name == '1':
                        signup = not signup
                    else:
                        print('--------------------------------------------------------')
                        print('|\t\t\t\t\t\t\t|\n|\tHi! the system says- "Happy you are running me"\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter your email\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                        print('--------------------------------------------------------')
                        email = input()
                        if email == '1':
                            signup = not signup
                        else:
                            print('--------------------------------------------------------')
                            print('|\t\t\t\t\t\t\t|\n|\tHi! the system says- "Happy you are running me"\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter a password\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                            print('--------------------------------------------------------')
                            password = input()
                            if password == '1':
                                signup = not signup
                            else:
                                user_created = User(first_name, last_name, email, password)
                                if user_created.create_account():
                                    print('--------------------------------------------------------')
                                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t Hello! User created successfully!\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                                    print('--------------------------------------------------------')
                                    status = input()
                                    if status == '1':
                                        signup = not signup
                                    else:
                                        signup = not signup
                                else:
                                    print('--------------------------------------------------------')
                                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tThe process was violated.Kindly repeat.\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tPress Enter\t\t\t\t|')
                                    print('--------------------------------------------------------')
                                    status = input()
                                    if status == '1':
                                        signup = not signup
                                    else:
                                        signup = not signup

        if option =='2':
            login = False
            while not login:
                print('--------------------------------------------------------')
                print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter your email\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                print('--------------------------------------------------------')
                email = input()
                if email == '1':
                    login = not login
                else:
                    print('--------------------------------------------------------')
                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter your password\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                    print('--------------------------------------------------------')
                    password = input()
                    if password == '1':
                        login = not login
                    else:
                        account_status = User.check_account_exist(email, password)
                        if account_status:
                            print('--------------------------------------------------------')
                            print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tYou are now logged in \t\t\t\t|\n|\t\t\t\t\t\t\t|\n|1. View Password Accounts\t\t\t\t|\n|2. Create a new Password Account\t\t\t\t|\n|3. Delete an existing Account\t\t\t\t|\n\t\t\t\t\t\t\t|')
                            print('--------------------------------------------------------')
                            perform = input()
                            if perform == '1':
                                all_acounts = Credential.display_accounts(email)
                                print('--------------------------------------------------------')
                                print('|\t\t\t\t\t\t\t|\n|\tHolla!!!! See your accounts now.\t\t\t|')
                                if len(all_acounts) > 0:
                                    count = 1
                                    for account in all_acounts:
                                        print(f'\t\t\t\t\t\t\t|\n|{count} {account["account"]}\t{account["password"]}')
                                        count +=1
                                else:
                                    print('|\t\t\t\t\t\t\t|\n|\t!!!!!!!!!!!!!!!!!!!!\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Sorry! You do not have any accounts set up.\t\t|')
                                print('|\t\t\t\t\t\t\t|\n|\tEnter\t\t\t\t\t\t|')
                                print('--------------------------------------------------------')
                                input()
                                login = not login
                            elif perform == '2':
                                print('--------------------------------------------------------')
                                print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Which  account is this? i.e Instagram/Twitter ...\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t\t|')
                                print('--------------------------------------------------------')
                                account = input()
                                account_exists = Credential.check_an_account_exist(email, account)
                                if len(account) > 0 and not account_exists :
                                    print('--------------------------------------------------------')
                                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tYou are now logged in\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|1. Get a system generated password\t\t\t\t|\n|2. Generate your own password\t\t\t\t|\n|\t\t\t\t\t\t\t|')
                                    print('--------------------------------------------------------')
                                    selected_account = input()
                                    if selected_account == '1':
                                        generated_password = Credential.randomizer()
                                        user_created_account = Credential(email, account, generated_password)
                                                
                                        if user_created_account.create_credential():
                                            print('--------------------------------------------------------')
                                            print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Account created successfully.\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t\t|')
                                            print('--------------------------------------------------------')
                                            input()
                                        else:
                                            print('--------------------------------------------------------')
                                            print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Sorry! Please try again.\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t|')
                                            print('--------------------------------------------------------')
                                        
                                        login = not login
                                    else:
                                        print('--------------------------------------------------------')
                                        print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Enter a password to use.(At least more than 8 characters long) \t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t\t|')
                                        print('--------------------------------------------------------')
                                        account_password = input()
                                        ok_create = True
                                        while ok_create:
                                            if len(account_password) > 8:
                                                user_created_account = Credential(email, account, account_password)
                                                
                                                if user_created_account.create_credential():
                                                    print('--------------------------------------------------------')
                                                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Account created successfully.\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t\t|')
                                                    print('--------------------------------------------------------')
                                                    input()
                                                else:
                                                    print('--------------------------------------------------------')
                                                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Something wrong happened. Please try again.\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t|')
                                                    print('--------------------------------------------------------')
                                                
                                                ok_create = not ok_create
                                                login = not login
                                            else:
                                                print('--------------------------------------------------------')
                                                print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Password too short try again.\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t|')
                                                print('--------------------------------------------------------')
                                                ok_create = not ok_create    
                                else:
                                    print('--------------------------------------------------------')
                                    print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Sorry. Account already exist.\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t\t\t|')
                                    print('--------------------------------------------------------')
                                    input()  
                                    login = not login      
                            elif perform == '3':
                                all_acounts = Credential.display_accounts(email)
                                print('--------------------------------------------------------')
                                print('|\t\t\t\t\t\t\t|\n|\tSelect the account to delete.\t\t\t|')
                                if len(all_acounts) > 0:
                                    count = 1
                                    for account in all_acounts:
                                        print(f'\t\t\t\t\t\t\t|\n|{count} {account["account"]}\t{account["password"]}')
                                        count +=1     
                                    to_delete = int(input())      
                                    account_to_delete = all_acounts[to_delete - 1]
                                    print(account_to_delete)   
                                    print(account_to_delete['account'])
                                    is_deleted = Credential.delete_account(account_to_delete['email'], account_to_delete['account'])  
                                    if is_deleted:
                                        print('--------------------------------------------------------')
                                        print('|\t\t\t\t\t\t\t|\n|\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Account deleted successfully\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                                        print('--------------------------------------------------------')
                                        input()
                                    else:
                                        print('--------------------------------------------------------')
                                        print('|\t\t\t\t\t\t\t|\n|\!!!!!!!!!!!!!!!!!!!!!!!!!!t\t\t|\n|\t\t\t\t\t\t\t|\n|Sorry Something wrong happened!\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                                        print('--------------------------------------------------------')
                            else:
                                login = not login
                        else:
                            print('--------------------------------------------------------')
                            print('|\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|Account does not exist. Please Sign Up\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                            print('--------------------------------------------------------')
                            error = input()
                            login = not login

        elif option == '3':
            home = not home


if __name__ == '__main__':
    main()