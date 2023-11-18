from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    # add any additional fields you need
    class usuario_login:
        model = User
        fields = ('username', 'password1')

class LoginForm(AuthenticationForm):
    class usuario_login:
        model = User
        fields = ('username', 'password1') 
