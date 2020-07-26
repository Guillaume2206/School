from django.forms.models import ModelForm
from .models import Student, Presence

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