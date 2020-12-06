from django import forms,ModelForm

class my_form(forms.Form):
    name=forms.CharField()
    about_me=forms.CharField(widget=forms.Textarea())
    active=forms.BooleanField()

# ModelForm is a regular Form which can automatically generate certain fields.
# The fields that are automatically generated depend on the content of the Meta
# class and on which fields have already been defined declaratively. Basically,
# ModelForm will only generate fields that are missing from the form, or in
# other words, fields that weren’t defined declaratively.

# example - To fill student database my taking entry from users we can make a ModelForm

class student_form(forms.ModelForm):
    # Meta is an inner class that is one of the attributes of the ModelForm class
    # that is used to specify which model will be used by the form.
    class Meta:
        model=models.student #which model to use
        fields='__all__' #which field to use
