from django import forms
from .models import PageData

class EditForm(forms.ModelForm):
    class Meta:
        model = PageData  # 사용할 모델
        fields = ['content']
        widgets = {'content' : forms.Textarea(attrs={'row' : 10 , 'class' : 'editor', 'spellcheck' : 'false'})}
        
class CreateForm(forms.ModelForm):
    class Meta:
        model = PageData
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-subject', 'placeholder' : '새 문서 제목', 'spellcheck' : 'false'}),
            'content': forms.Textarea(attrs={'class': 'form-content', 'rows': 10, 'placeholder' : '새 문서 내용', 'spellcheck' : 'false'}),
        }