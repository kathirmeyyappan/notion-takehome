from mail_ops import *
from mail import *

def run_cli(option):
    
    # send mail
    if option == WRITE:
        print("\n--- NEW MESSAGE ---")
        # prompt mail info from user
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        message = input("Message: ")
        
        # persist log to database and alert user
        print("\nSending...")
        send_mail(sender, recipient, message)
        print("Sent!\n")
    
    # read mail inbox for user
    elif option == READ:
        print("\n--- INBOX ---")
        # prompt info from user
        user = input("User: ")
        
        # fetch relevant mails
        inbox = read_mail(user)
        
        # parse result into client message and print query result
        print(f"{user}'s Inbox ({len(inbox)}):\n")
        for i, mail in enumerate(inbox):
            print(f"[{i + 1}].")
            print(mail)
    
    # search for mail with string contained
    elif option == SEARCH:
        print("\n--- MAIL SEARCH ---")
        text = input("Contains: ")
        
        # fetch relevant mails
        mails = search_mail(text)
        
        # parse result into client message and print query result
        print(f"Search Results ({len(mails)}):\n")
        for i, mail in enumerate(mails):
            print(f"[{i + 1}].")
            print(mail)

if __name__ == "__main__":
    
    # intro
    print("\nWelcome! Please select an option to continue.")
    print("(1) Send mail to a user")
    print("(2) Read mail for a user")
    print("(3) Search for mail that contains text")
    
    # get operation
    option = input()
    while option not in ('1', '2', '3'):
        print("Please enter '1' '2', or '3'.")
        option = input()
    
    run_cli(int(option))
    
    # end message
    print("Thank you! Run again to do another operation.\n")