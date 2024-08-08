# user operation constants
WRITE = 1
READ = 2
SEARCH = 3

# class for one row in database, i.e. one mail
# we have a string method here for printing mails in our TUI
class Mail:
    
    def __init__(self, sender="UNKNOWN", recipient="UNKNOWN", message="UNKNOWN", time="UNKNOWN") -> None:
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.time = time
    
    def __str__(self) -> str:
        res = f"From: {self.sender}\n" + \
              f"To: {self.recipient}\n" + \
              f"@ {self.time}\n" + \
              f"Content: {self.message}\n"
        return res