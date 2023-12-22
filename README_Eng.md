**Section №1 "Description"**

PhoneBook is a phone directory with a graphical interface on Easygui.
This application is developed in Python language, which allows the user to add, delete, edit, and search for entries in the phone directory, which is stored in a database.

**Attention! **

Due to technical difficulties - on the second week of development, Easygui stopped working, and it has not been possible to restore it yet. The project is being tested on a classmate's working machine. The project will be completed by the end of assignment №10 (Certification work) and presented in the release version. I apologize for the inconvenience.

**Section №2 "Installation"**

To run this application, you need to:

Install Python 3.11 or higher.
Download and install a compatible interpreter (recommended: VS, VS Code, or PyCharm).
Execute the following commands in the command line:
> git clone https://github.com/rbnhd6984/PhoneBook.git
> 
> pip install easygui
> 
> cd phonebook

Or download the file from the link: https://github.com/Grosere/phytonHometask.git, and run it on your PC.
You may need to choose the default program for this; in that case, select the previously installed VS, VS Code, or PyCharm.

**Section №3 "How to Use the Program"
**
Launch the application (execute the phone.py file).
After launching the application, you will see a menu with the available actions:
> Add new contacts (def contact_add)
> 
> Search for contacts (def contact_search)
> 
> Edit contact (def contact_edit)
> 
> Delete contact (def contact_delete)
> 
> View the entire directory (def contact_show)

A contact should contain:
> Name - a required input field, up to 16 characters, either Cyrillic or Latin.
> 
> Last name - an optional input field, up to 16 characters.
> 
> Phone number - a required input field, up to 14 digits, with a check for entering only digits.
> 
> Comment - an optional input field, up to 265 characters.

**Section №4 "Function Description"**

**The function def contact_add should:**

> Create a new id for the contact.
> 
> Request input for "Name".
> 
> Check if the "Name" field is filled. If the field is not filled correctly, display the error message "Field is filled incorrectly" and repeat the Name input request.
> 
> Request input for "Surname".
> 
> Request input for "Phone".
> 
> Check the "Phone" field - must contain no more than 14 digits and only digits are allowed. If the field is not filled correctly, display the error message "Field is filled incorrectly" and repeat the Phone input request.
> 
> Request input for "Comment".
> 
> Display the message: ("Name" & "Surname" & "Phone" - successfully saved).
> 
> Check if the specified phone number exists in the SQL database.
> 
> If such phone number exists, ask: "A contact with this number already exists. Add the contact again?"
> 
> Display 2 buttons "Yes" and "No".
> 
> If "Yes" is selected, create a contact by adding "(Second)" to the "Name".
> 
> If "No" is selected, return to the main menu.
> 
> If the contact is saved, return to the main menu.

**The function def contact_search should:**

> Request "Who are we looking for?"
> 
> Check for matches in "Name", "Surname", "Phone".
> 
> If multiple contacts are found, display the entire list of contacts on the screen, assigning them ordinal numbers.
> 
> Ask the user "Which contact do you choose?" and display a field for inputting the ordinal number.
> 
> After selecting the ordinal number, request "What do you want to do with the contact?" and display buttons "Edit", "Delete", "Return to Main Menu".
> 
> If "Edit" is selected, go to the function def contact_edit.
> 
> If "Delete" is selected, go to the function def contact_delete.
> 
> If "Return to Main Menu" is selected, return to the main menu.

**The function def contact_edit should:**

> Request "Which field do you want to edit?"
> 
> Display buttons "Name", "Surname", "Phone", "Comment".
> 
> If "Name" is selected, overwrite the "Name" field, with mandatory checks, as in the function def contact_add.
> 
> If "Surname" is selected, overwrite the "Surname" field.
> 
> If "Phone" is selected, overwrite the "Phone" field of the contact, with mandatory checks, as in the function def contact_add.
> 
> If "Comment" is selected, overwrite the "Comment" field.
> 
> Display the prompt "Finish editing Y / N?"
> 
> Display buttons "Finish" or "Continue".
> 
> If the user selects "Continue", execute the function def contact_edit again.
> 
> If the user selects "Finish", exit to the main menu.

**The function def contact_delete should:**

> Delete the contact record.
> 
> Modify and rearrange the id of other contacts.
> 
> Return to the main menu.

**The function def contact_show should:**

Display the entire list in tabular form by columns:
> ID
> 
> "Name"
> 
> "Surname"
> 
> "Phone"
> 
> "Comment"
> 
> Display a button "Return to Main Menu" which returns to the main menu.

**Section №5 "License"**

This project is distributed as is, the developers are not responsible for data entered by the user.

Authors
GeekBrains Student
> Sergey Kozmenko

During consultation:
> Igor Martyshevsky

Project Manager:
> Timur Islamgulov
