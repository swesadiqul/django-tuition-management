from cProfile import label
from django import forms
from .models import Contact, Post, PostFile
from .fields import ListTextWidget

# create forms
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=101, label='Full name')
#     phone = forms.CharField(max_length=14, label='Your phone')
#     content = forms.CharField(max_length=500, label='Your Details')


class ContactForm(forms.ModelForm):
    # if we use only Form class
    # name = forms.CharField(max_length=100, label='Full name', help_text='type your full name.', widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Full name'}))
    # phone = forms.CharField(max_length=100, label='Mobile number', help_text='enter your mobile number.', widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Mobile number'}))
    # content = forms.CharField(max_length=100, label='Description', help_text='please send your message.', widget=forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'Message..'}))
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'content']

        # if the form is ModelForm
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Full name'}),
            'phone': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Mobile number'}),
            'content': forms.Textarea(attrs={'class':'form-control mb-3', 'placeholder':'Message...', 'rows':6}),
        }
        labels = {
            'name': 'Full name',
            'phone': 'Mobile number',
            'content': 'Description',
        }
        # help_texts = {
        #     'name': 'type your full name.',
        #     'phone': 'enter your phone number',
        #     'content': 'please send your message.'
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['name'].label = 'My name'
    #     self.fields['name'].initial = 'My name '
    #     self.fields['phone'].initial = '+880'
    #     self.fields['content'].initial = 'My problem is '

    def clean_name(self):
        value = self.cleaned_data.get('name')
        name_of_wrd = value.split(' ')
        if len(name_of_wrd) > 3:
            self.add_error('name', 'Name can have maximum of 3 words.')
        else:
            return value

class ContactFormTwo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','id', 'created_at','slug','likes','views']

        widgets = {
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        _district_set = kwargs.pop('district_set', None)
        super(PostForm,self).__init__(*args, **kwargs)
        self.fields['district'].widget = ListTextWidget(data_list= _district_set, name='district-set')

class FileModelForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ['image']