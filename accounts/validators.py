from django.core.exceptions import ValidationError

class ContainsLetterValidator:

    def validate(self, password,user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('The password must contain at least a letter',code='password_no_letter')

    
    def get_help_text(self):
        return "Your password must contain at least an uppercase or lowercase letter."


class ContainsDigitValidator:

    def validate(self, password,user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError('The password must contain at least a digit',code='password_no_digit')

    
    def get_help_text(self):
        return "Your password must contain at least a digit."