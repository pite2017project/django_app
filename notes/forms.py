from django import forms
from models import NoteFileImage, NoteFileText, NoteFilePdf

class NoteImageForm(forms.ModelForm):
    class Meta:
        model = NoteFileImage
        fields = ('name', 'author', 'subject', 'lecture_number',
                'lecture_title', 'content')

class NoteTextForm(forms.ModelForm):
    class Meta:
        model = NoteFileText
        fields = ('name', 'author', 'subject', 'lecture_number',
                'lecture_title', 'content')

class NotePdfForm(forms.ModelForm):
    class Meta:
        model = NoteFilePdf
        fields = ('name', 'author', 'subject', 'lecture_number',
                'lecture_title', 'content')

