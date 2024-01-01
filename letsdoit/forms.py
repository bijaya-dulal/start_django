from django import forms



class usersForm(forms.Form):
    num1 = forms.CharField(label="college",widget=forms.TextInput(attrs={'class':"input-field"}),)
    num2 = forms.CharField(label="school",widget=forms.TextInput(attrs={'class':"input-field"}))


