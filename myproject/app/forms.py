from .models import user
from django.forms import ModelForm

class adduser(ModelForm):
	class Meta:
		model=user
		fields=['name','password']
	