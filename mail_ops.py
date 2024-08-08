import os
from notion_client import Client
from dotenv import load_dotenv
from mail import Mail

load_dotenv()
notion = Client(auth=os.environ["NOTION_TOKEN"])
DB_ID = os.environ["DB_ID"]

# send email with given params and persist to database
def send_mail(sender, recipient, message):
    
    try:
        response = notion.pages.create(
            parent={"database_id": DB_ID},
            properties={
                "Message": {
                    "title": [
                        {
                            "text": {
                                "content": message
                            }
                        }
                    ]
                },
                "Sender": {
                    "rich_text": [
                        {
                            "text": {
                                "content": sender
                            }
                        }
                    ]
                },
                "Recipient": {
                    "rich_text": [
                        {
                            "text": {
                                "content": recipient
                            }
                        }
                    ]
                }
            }
        )
    
    except Exception as e:
        print(f"An error occurred: {e}")
        quit()
        
# retrieve all emails from database with given recipient
# returns list of Mail objects to caller
def read_mail(user):
    
    try:
        # search for rows with given recipient
        response = notion.databases.query(
            database_id=DB_ID,
            **{
                "filter": {
                    "property": "Recipient",
                    "rich_text": {
                        "equals": user
                    }
                }
            }
        )
                
        # initialize return object
        inbox = []
        for item in response['results']:
            row = item['properties']
            # get sender and message to add to return object
            msg = row['Message']['title'][0]['plain_text']
            sender = row['Sender']['rich_text'][0]['plain_text']
            time = row['Created time']['created_time']
            # add main to return object
            mail = Mail(sender=sender, recipient=user, message=msg, time=time)
            inbox.append(mail)
        return inbox
    
    except Exception as e:
        print(f"An error occurred: {e}")
        quit()

# retrieve all emails from database whose message content contains the search text
def search_mail(search_text):
    
    try:
        # search for rows with given recipient
        response = notion.databases.query(
            database_id=DB_ID,
            **{
                "filter": {
                    "property": "Message",
                    "rich_text": {
                        "contains": search_text
                    }
                }
            }
        )
                
        # initialize return object
        mails = []
        for item in response['results']:
            row = item['properties']
            # get mail to add to return object
            msg = row['Message']['title'][0]['plain_text']
            sender = row['Sender']['rich_text'][0]['plain_text']
            recipient = row['Recipient']['rich_text'][0]['plain_text']
            time = row['Created time']['created_time']
            # add mail to return object
            mail = Mail(sender=sender, recipient=recipient, message=msg, time=time)
            mails.append(mail)
        return mails
    
    except Exception as e:
        print(f"An error occurred: {e}")
        quit()