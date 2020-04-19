
class Constant:

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean'),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KRW, 'KRW'),
    )
