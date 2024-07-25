from django import forms
from.models import Admission
class DateInput(forms.DateInput):
   input_type='date'

class AdmissionForm(forms.ModelForm):
   class Meta:
      model=Admission
      fields='__all__'
      widgets={
         'admission_date':DateInput()
      }
