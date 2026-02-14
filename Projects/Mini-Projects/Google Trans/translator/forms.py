from django import forms

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('te', 'Telugu'),
    ('hi', 'Hindi'),
    ('ja', 'Japanese'),
    ('zh-CN', 'Chinese'),
    ('ur', 'Urdu'),
]

class TranslationForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter text to translate...',
            'rows': 5,
        }),
        label=''
    )
    target_language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial='hi'
    )
