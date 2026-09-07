# Program validators

def validate_menu_choice(choice, valid_choices):
    return choice.strip() in valid_choices

# Read/Unread

BOOK_STATUS = {
    "Y" : "Read",
    "N" : "Unread"
}