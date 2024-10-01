# game/forms.py
from django import forms

class PasswordGameForm(forms.Form):
    player_name = forms.CharField(max_length=100, label="Enter your name")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter a password")
