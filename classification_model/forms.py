from django.forms import ModelForm
from . models import PredictMark

class MyForm(ModelForm):
	class Meta:
		model=PredictMark
		fields = '__all__'