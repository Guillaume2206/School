from django.forms.models import ModelForm
from django import forms
from .models import Student, Presence, CallOfRoll
from django.utils import timezone, dateformat

class StudentForm(ModelForm):

  class Meta:
    # Ref du model
    model = Student

    # list des champs à éditer
    fields = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )

class PresenceForm(ModelForm):

  class Meta:
    # Ref du model
    model = Presence

    # list des champs à éditer
    fields = (
      "reason",
      "isMissing",
      "date",
      "student"
    )

class CallOfRollForm(ModelForm):

    class Meta:
        model = CallOfRoll
        exclude = ['']
        fields = (
        "date",
        "dayhalf"
        )
        
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'value':dateformat.format(timezone.now(), 'Y-m-d')}),
        }

    def __init__(self, cursus_id,*args, **kwargs):
        super(CallOfRollForm, self).__init__(*args, **kwargs)
        students = Student.objects.filter(cursus=cursus_id)
        for q in students:
            self.fields[str(q.id)] = forms.BooleanField(
              initial=True,
              required=False,
              label=q.first_name + " " + q.last_name
              )