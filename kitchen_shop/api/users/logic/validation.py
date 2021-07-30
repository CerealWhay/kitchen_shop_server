from django.contrib.auth import get_user_model

from kitchen_shop.api.exceptions import ValidationError

User = get_user_model()


class UserDataValidator:
    """Валидатор пользовательских данных."""

    WRONG_PASSWORD_CONFIRMATION = 'Password mismatch.'
    USERNAME_EXISTS = 'Username already exists.'
    EMAIL_EXISTS = 'User with this E-mail already exists.'

    @classmethod
    def compare_passwords(
        cls, password: str, password_confirmation: str
    ) -> None:
        """Сравнение паролей."""
        if not password == password_confirmation:
            raise ValidationError(cls.WRONG_PASSWORD_CONFIRMATION, 'password')

    @classmethod
    def validate_username(cls, username: str) -> None:
        """Проверка на уникальность имени пользователя."""
        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            raise ValidationError(cls.USERNAME_EXISTS, 'username')

    @classmethod
    def validate_email(cls, email: str) -> None:
        """Проверка на уникальность почнового ящика."""
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError(cls.EMAIL_EXISTS, 'email')
