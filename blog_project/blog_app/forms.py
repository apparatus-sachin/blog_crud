from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
	class Meta:
		model=Blog
		fields="__all__"

		widgets={
		'title':forms.TextInput(attrs={'class':'form-control'}),
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'date':forms.DateTimeInput(attrs={'class':'form-control','id':'datetimepicker'}),
		'blog':forms.TextInput(attrs={'class':'form-control'})
		}
