import re

class Validation:

    @staticmethod
    def text_validation(to_validate_text)->bool:
        text_characters=re.compile('^[A-Za-z0-9äüöß\-()&#.: ]+$', re.IGNORECASE)
        if text_characters.match(to_validate_text):
            return True
        else:
            return False

    @staticmethod
    def date_validation(to_validate_date)->bool:
        date_characters=re.compile('^\d{2}\.\d{2}\.\d{4}$', re.IGNORECASE)
        if date_characters.match(to_validate_date):
            return True
        else:
            return False

    @staticmethod
    def price_validation(to_validate_price)->bool:
        price_characters=re.compile('^\d+(\.\d{1,2})$', re.IGNORECASE)
        if price_characters.match(str(to_validate_price)):
            return True
        else:
            return False  

    @staticmethod
    def room_validation(to_validate_room)->bool:
        room_characters=re.compile('^\d+$', re.IGNORECASE)
        if room_characters.match(str(to_validate_room)):
            return True
        else:
            return False   
                  