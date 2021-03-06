from django import forms
from django.forms.widgets import SelectDateWidget


class EventForm(forms.Form):
    title = forms.CharField(label='Title of event' ,max_length=255, widget= forms.TextInput({ "placeholder": "Your cool event" }))
    day = forms.DateField(label='date', widget=SelectDateWidget(empty_label="Nothing"))
    starting_time = forms.TimeField(label='start', widget=forms.TextInput({ "placeholder": "12:00" }))
    ending_time = forms.TimeField(label='end', widget=forms.TextInput({ "placeholder": "13:30"}))

    personal_notes = forms.CharField( label='notes',widget=forms.Textarea(attrs={'placeholder': 'Optional field'}), required=False )

class UploadFileFrom(forms.Form):
    file = forms.FileField(label='Import schedule')