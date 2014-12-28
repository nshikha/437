from django import forms

from app.models import *

#by model validation already assumes uniqueness of username / email??
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length = 200, label = "Confirm Password",
                                widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(max_length = 200, label="Email", required=True)

    class Meta:
        model = User
		#required by default
        fields = ['username', 'email', 'password', 'password2']
		#labels can be set here
        widgets = {
            'password': forms.PasswordInput(),
        }

    #None is returned if nothing is in the text field
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
		# Confirms that the two password fields match
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and (password != password2):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=200, label="Change Name", required=False)
    password = forms.CharField(max_length = 200, label="Old Password", required=False,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length = 200, label="", required=False,
                                widget=forms.PasswordInput())
    new_password = forms.CharField(max_length = 200, label = "New Password", required=False,
                                widget=forms.PasswordInput())
    image = forms.ImageField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if (username and User.objects.filter(username__exact=username)):
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean(self):
        cleaned_data = super(EditProfileForm, self).clean()
        password = cleaned_data.get('password')   
        password2 = cleaned_data.get('password2')
        new_password = cleaned_data.get('new_password')
        print password, password2, new_password
        if (password or password2):
            if (password != password2):
                raise forms.ValidationError("Passwords do not match.")
            if (not new_password):
                raise forms.ValidationError("Enter new password.")
        return cleaned_data






















