from django import forms
from django.forms.widgets import CheckboxSelectMultiple, Select, TextInput

class LinkForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)

        initial =  kwargs.get('initial', {})
        s_choices = initial.get('share_choices', None)
        c_choices = initial.get('calendar_choices', None)

        self.fields['share_choices'].choices = s_choices
        self.fields['calendar_choices'].choices = c_choices

    #Drop down
    calendar_choices = forms.ChoiceField(widget=Select)
    #Check boxes
    share_choices = forms.MultipleChoiceField(widget=CheckboxSelectMultiple)
    #Text entry for interpreting variables
    format_text = forms.CharField(widget=TextInput)
