from django import forms
from django.forms import widgets
from multiselectfield import MultiSelectFormField
from django_select2.forms import Select2MultipleWidget
from .models import ApplicantUserProfile

year=[tuple([x,x]) for x in range(1980,2020)]
class UserProfileForm(forms.ModelForm):
    skill_info = forms.MultipleChoiceField(choices=ApplicantUserProfile.SKILLS,required=False)
    class Meta:
        model = ApplicantUserProfile
        fields = ("first_name","last_name",
        "resume_link","linkedin", "summary",
        "referee_name", "referee_email","referee_designation", "referee_organisation",
        "referee_relationship","referee_phone","designation",
        "company_name","company_start_date","company_doc",
        "company_end_date",
        "company_loaction",
        "company_description",
        "skill_info",
        "profile_pic",
        "job_profile",
        "marital_status","blood_group",
        "certifications","dob","degree","institute_name","branch","cgpa","ins_start_date","ins_end_date","edu_description"
        )
    pass

class UserProfileUpdationForm(forms.ModelForm):
    skill_info = forms.MultipleChoiceField(choices=ApplicantUserProfile.SKILLS,required=False)
    class Meta:
        model = ApplicantUserProfile
        fields = ("first_name","last_name",
        "resume_link","linkedin", "summary",
        "referee_name", "referee_email","referee_designation", "referee_organisation",
        "referee_relationship","referee_phone","designation",
        "company_name","company_start_date",
        "company_end_date",
        "company_loaction",
        "company_description","location","company_doc",
        "skill_info",
        "profile_pic",
        "job_profile",
        "marital_status","blood_group",
        "certifications","dob","degree","institute_name","branch","cgpa","ins_start_date","ins_end_date","edu_description"
        )
        widgets= {
            'summary':forms.Textarea(attrs={'class':'desc','cols':76,'rows':2}),
            'edu_description':forms.Textarea(attrs={'class':'desc', 'cols':76,'rows':2}),
            'company_description':forms.Textarea(attrs={'class':'desc','cols':77,'rows':2}),
            
        }
    pass

class PicForm(forms.ModelForm):

    class Meta:
        model = ApplicantUserProfile
        fields = ("profile_pic",)
    pass

class ResumeForm(forms.ModelForm):

    class Meta:
        model = ApplicantUserProfile
        fields = ("profile_resume",)
    pass

class InputForm(forms.Form):

    fullname = forms.CharField(max_length = 200)
    mail = forms.EmailField()
    contact = forms.IntegerField()
