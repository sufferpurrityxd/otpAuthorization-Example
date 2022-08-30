from django.core import validators
phonenumber_regex = validators.RegexValidator(
    regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
    message='Неверный формат телефона, используйте: "+79009009090"'

)
