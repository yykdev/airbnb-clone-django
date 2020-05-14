from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            User.objects.get(username=email)

            return email
        except User.DoesNotExist:
            raise forms.ValidationError("해당하는 유저가 존재하지 않습니다")

    def clean_password(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                return email
            else:
                raise forms.ValidationError("비밀번호가 유효하지 않습니다.")
        except User.DoesNotExist:
            raise forms.ValidationError("해당하는 유저가 존재하지 않습니다")
