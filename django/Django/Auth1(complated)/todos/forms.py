#forms.py

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

	# 필드를 정의하는 부분
    content=forms.CharField(
    
        widget=forms.Textarea(
            attrs={
                    'class':'work',
                    'placeholder':'할일을 등록해 주세요',
                    'rows': 4, 'cols': 15
                }
            )
        )
        
	# Meta 클래스 작성하는 부분
    class Meta:
        model = Todo
        fields = '__all__'