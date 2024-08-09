# Notion Take-Home Assessment

**Walkthrough Video:** https://drive.google.com/file/d/1rvl-7s5ly8tjAqurhUadzyS-23OoDVrd/preview
**Notion Database:** https://www.notion.so/9d917d9de1a34184be855d679baf7420?v=30191fed75fb4a33b5c59fd8a3a89e7a&pvs=4

## General Overview
The program is meant to run once and complete one of 3 operations:
1. Send an email with a given sender, recipient, and content.
2. Return all of the mail sent to a given user.
3. Return all mails whose content contains a given string.
The video shows this in action. The database starts with 2 emails addressed to user `Sudar` (operation 1). Using command 1, I send 2 emails to Kathir, from users Sudar and Ashwin. I then check Kathir's inbox (operation 2) to verify that 2 results show up and they are the emails I just sent before. Finally, I use operation 3 to term search for "hey", yielding the 2 emails that were originally there, and also search the term "what's" for good measure.

## Run Program
1. After Python is installed, navigate to root and install dependencies with `pip install -r requirements.txt`
2. Now in root, we simply run `python3 app.py` to begin the CLI app.

## Additions:
I made 2 main additions past the base requirements in the 3 hours I allocated to this.
- **Time stamp:** Adding a timestamp was as simple as adding a `Created Time` type column which is automatically populated for every row (without any additions by me) in Notion itself. After this, I just called that property on each row to populate my Mail objects.
- **Custom addition - message content search:** In addition to the specified 2 options, I added a 3rd option which looks through all of the mail in the database to see which ones have a given string in their contents. The result is returned in an identical fashion to the read mail for user command (2).

## Referred to:
- https://github.com/ramnes/notion-sdk-py
- https://developers.notion.com/docs/working-with-databases
- https://developers.notion.com/reference/post-database-query
- https://developers.notion.com/reference/property-value-object
- https://developers.notion.com/reference/patch-page
- TUI Reversi project from intro CS class in college to refresh how user input works (private repo)

## Improvements
- If I had more time to work on this, I would definitely write robust tests to verify performance. This would involve having a TEST_TABLE env variable so that I could persist objects and verify search/inbox behavior in a different table in Notion without worrying about creating dirty pages in the prod table.
- Additionally, implementing more advanced filters for mail would be a cool endeavor. After reading up on the documentation for filters, I noticed a lot of cool things like boolean trees, which could be used for compound searches (e.g. time range plus text content plus ignore users). This is a bit much for implementing without a GUI though! 

## Implementation Choices
- Among other things, I went with the choice of having a Mail class. This made it easy to create objects after reading rows, and simply return objects to the caller in the 'frontend' CLI. By creating a string method for the class, it was as easy as just printing objects in the frontend after making a call, which greatly reduces code complexity.
- I also decided against using an infinite loop for > 1 operation because it seemed more intuitive for users to run the program to complete an operation, and repeat if needed (rather than killing the program when done or having the overhead of needing to listen for a quit command in the text interface).
- Obviously, for security and good practice, I hid tokens and called them safely through the virtual environment. 

## Some banger songs I was listening to while working:
- https://www.youtube.com/watch?v=hOHKltAiKXQ
- https://www.youtube.com/watch?v=ylssgHLVZaE
- https://www.youtube.com/watch?v=RLnA25dVzrQ
- https://www.youtube.com/watch?v=AIKS-4JfoQg
