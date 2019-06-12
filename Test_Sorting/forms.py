from django import forms

LENGTH_VALUES = (
    ('10', '10'),
    ('100', '100'),
    ('1000','1000'),
    ('10000','10000'),
)
KEYS = (
    ("1", 'Klucze unikalne'),
    ("0", 'Klucze mogą się powtarzać'),
)
ACTION = (
    ("test", "Pojedyńczy test"),
    ("average", "Średnie wyniki z wykonanych testów"),
)
class TestForm(forms.Form):

    list_length = forms.ChoiceField(label='Wybierz długość listy kluczy', widget=forms.RadioSelect, choices=LENGTH_VALUES)
    unique_keys = forms.ChoiceField(label='Wybierz czy klucze mają być unikalne', widget=forms.RadioSelect, choices=KEYS)
    action = forms.ChoiceField(label='Wybierz rodzaj akcji', widget=forms.RadioSelect, choices=ACTION)




