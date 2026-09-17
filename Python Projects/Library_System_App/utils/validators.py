# Program validators

import datetime

def validate_menu_choice(choice, valid_choices):
    return choice.strip() in valid_choices

# Book detail validators
def validate_non_empty(value):
    return value.strip() != ""

def validate_release_date(release_date):
    if release_date.strip() == "":
        return True
    
    try:
        datetime.datetime.strptime(release_date, "%Y-%m-%d")
        return True
    
    except ValueError:
        return False

def validate_rating(rating):
    if rating.strip() == "":
        return True
    
    try:
        rating_value = float(rating)
        return 0 <= rating_value <= 5
    
    except ValueError:
        return False

# Read/Unread

BOOK_STATUS = {
    "Y" : "Read",
    "N" : "Unread"
}