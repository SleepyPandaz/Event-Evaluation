from django import forms

class AddEventForm(forms.Form):
    add_events = forms.CharField(label='EventForm', max_length=100)