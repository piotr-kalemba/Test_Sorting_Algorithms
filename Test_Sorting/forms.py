from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_new_username(username):

    if User.objects.filter(username=username):
        raise ValidationError('Nazwa użytkownika jest już zajęta')

LENGTH_VALUES = (
    ('10', '10'),
    ('100', '100'),
    ('1000','1000'),
    ('10000','10000'),
)
KEYS = (
    ("1", 'Elementy unikalne'),
    ("0", 'Elementy mogą się powtarzać'),
)
ACTION = (
    ("test", "Pojedyńczy test"),
    ("average", "Średnie wyniki z wykonanych testów"),
)
ALGORITHMS = (
    ('bubble', 'bubble sort'),
    ('select', 'select sort'),
    ('merge', 'merge sort'),
    ('heap', 'heap sort'),
    ('quick', 'quick sort'),

)
class AllAlgorithmsForm(forms.Form):

    list_length = forms.ChoiceField(label='Wybierz długość tablicy', widget=forms.RadioSelect, choices=LENGTH_VALUES)
    unique_keys = forms.ChoiceField(label='Wybierz czy elementy mają być unikalne', widget=forms.RadioSelect, choices=KEYS)
    action = forms.ChoiceField(label='Wybierz rodzaj akcji', widget=forms.RadioSelect, choices=ACTION)

class SingleAlgorithmForm(forms.Form):

    algorithm = forms.ChoiceField(label='Wybierz algorytm sortowania', widget=forms.RadioSelect, choices=ALGORITHMS)
    unique_keys = forms.ChoiceField(label='Wybierz czy elementy mają być unikalne', widget=forms.RadioSelect,
                                    choices=KEYS)

class UserLoginForm(forms.Form):

    username = forms.CharField(label='Nazwa użytkownika', required=True)
    password = forms.CharField(label='Hasło', required=True, widget=forms.PasswordInput)

class UserCreateForm(forms.Form):

    username = forms.CharField(label='Nazwa użytkownika', required=True, validators=[validate_new_username])
    password1 = forms.CharField(label='Hasło', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Hasło (ponownie)', required=True, widget=forms.PasswordInput)






