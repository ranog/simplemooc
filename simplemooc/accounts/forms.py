from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        
        # vai retorna um booleano para verificar se o e-mail é unico.
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Já existe usuário com este E-mail')

        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditAccountForm(forms.ModelForm):
    
    def clean_email(self):
        email = self.cleaned_data['email']
        
        queryset = User.objects.filter(
            email=email).exclude(pk=self.instance.pk)
        # vai retorna um booleano para verificar se o e-mail é unico.
        if queryset.exists():
            raise forms.ValidationError(
                'Já existe usuário com este E-mail')

        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
