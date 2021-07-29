from typing import Any
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from multiselectfield import MultiSelectField
from Profcess_Dev.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL
from django.core.exceptions import ValidationError

# from accounts import profcess

# Create your models here.



class ApplicantUserProfile(models.Model):
    def validate(value):  # <-changed this
        filesize = value.size

        if filesize > 14000:
            raise ValidationError("Your file is too big. The maximum file size that can be uploaded is 13KB")
        else:
            return value  # <-to this

    def validate1(value):  # <-changed this
        filesize = value.size

        if filesize > 14000:
            raise ValidationError("Your file is too big. The maximum file size that can be uploaded is 13KB")
        else:
            return value  # <-to this

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "Applicant"},
        related_name="applicantuserprofile",
        null=True,)
    
    first_name = models.CharField(blank=True, max_length=140)
    last_name = models.CharField(blank=True, max_length=140)
    # pheadline = models.CharField(blank=True, max_length=140)
    # current_position = models.CharField(blank=True, max_length=140)
    # education = models.CharField(blank=True, max_length=140)
    # country_region = models.CharField(blank=True, max_length=140)
    location = models.CharField(blank=True, max_length=140)
    industry = models.CharField(blank=True, max_length=140)
    # contact_information = models.CharField(blank=True, max_length=140)
    description = models.CharField(blank=True, max_length=25)
    # school_name = models.CharField(blank=True, max_length=140)
    # school_degree = models.CharField(blank=True, max_length=140)
    # field_of_study = models.CharField(blank=True, max_length=140)
    # location_of_school = models.CharField(blank=True, max_length=140)
    # start_school = models.CharField(blank=True, max_length=140)
    # end_school = models.CharField(blank=True, max_length=140)
    # experience_title = models.CharField(blank=True, max_length=140)
    # company_name = models.CharField(blank=True, max_length=140)
    # company_city = models.CharField(blank=True, max_length=140)
    # company_state = models.CharField(blank=True, max_length=140)
    # start_company = models.CharField(blank=True, max_length=140)
    # end_company = models.CharField(blank=True, max_length=140)
    # area_of_expertise = models.CharField(blank=True, max_length=140)
    # project_name = models.CharField(blank=True, max_length=140)
    # start_project = models.CharField(blank=True, max_length=140)
    # end_project = models.CharField(blank=True, max_length=140)
    # project_creator = models.CharField(blank=True, max_length=140)
    # associated_with = models.CharField(blank=True, max_length=140)
    # project_url = models.CharField(blank=True, max_length=140)
    # project_description = models.CharField(blank=True, max_length=140)
    # accomplishment_title = models.CharField(blank=True, max_length=140)
    # accomplishment_associated_with = models.CharField(blank=True, max_length=140)
    # issuer = models.CharField(blank=True, max_length=140)
    # issue_date = models.CharField(blank=True, max_length=140)
    # accomplishment_description = models.CharField(blank=True, max_length=140)
    #SKILLS = []

    #file1 = open('static/skill/all_skills.txt', 'r', encoding="utf-8")
    #Lines = file1.readlines()

    #for line in Lines:
     #   SKILLS += [(str(line[:-1]), str(line[:-1]))]

    SKILLS = [
         ('A/B Testing', 'A/B Testing'),
         ('Abap', 'Abap'),
         ('Accounting', 'Accounting'),
         ('Active Listening', 'Active Listening'),
         ('Ada', 'Ada'),
         ('Adaptability', 'Adaptability'),
         ('Agile', 'Agile'),
         ('Agile Development', 'Agile Development'),
         ('Answering Phones', 'Answering Phones'),
         ('Artificial Intelligence', 'Artificial Intelligence'),
         ('Ballerina', 'Ballerina'),
         ('BASIC Alice', 'BASIC Alice'),
         ('Billing', 'Billing'),
         ('Blood Pressure Monitoring', 'Blood Pressure Monitoring'),
         ('Budgeting', 'Budgeting'),
         ('C', 'C'),
         ('C#', 'C#'),
         ('C++', 'C++'),
         ('CAD', 'CAD'),
         ('Calendar Management', 'Calendar Management'),
         ('Cashier Skills', 'Cashier Skills'),
         ('Clojure Elixir', 'Clojure Elixir'),
         ('Cloud Management', 'Cloud Management'),
         ('CMS Tools', 'CMS Tools'),
         ('Cobol', 'Cobol'),
         ('COBOL', 'COBOL'),
         ('Coding Java Script', 'Coding Java Script'),
         ('Collaboration', 'Collaboration'),
         ('Communication', 'Communication'),
         ('Computer Skills', 'Computer Skills'),
         ('Conflict Resolution', 'Conflict Resolution'),
         ('Contract Negotiation', 'Contract Negotiation'),
         ('CPC', 'CPC'),
         ('Creativity', 'Creativity'),
         ('Critical Thinking', 'Critical Thinking'),
         (
         'CRM Software (Salesforce, Hubspot, Zoho, Freshsales)', 'CRM Software (Salesforce, Hubspot, Zoho, Freshsales)'),
         ('CRO', 'CRO'),
         ('CSS', 'CSS'),
         ('Customer Needs Analysis', 'Customer Needs Analysis'),
         ('Customer Service', 'Customer Service'),
         ('Dart', 'Dart'),
         ('Data Entry', 'Data Entry'),
         ('Data Structures', 'Data Structures'),
         ('Data Visualization', 'Data Visualization'),
         ('Debugging', 'Debugging'),
         ('Decision Making', 'Decision Making'),
         ('Design', 'Design'),
         ('Digital marketing', 'Digital marketing'),
         ('Eiffel', 'Eiffel'),
         ('Electronic Heart Record (EHR)', 'Electronic Heart Record (EHR)'),
         ('Electronic Medical Record (EMR)', 'Electronic Medical Record (EMR)'),
         ('Elm', 'Elm'),
         ('Email Automation', 'Email Automation'),
         ('Email Marketing', 'Email Marketing'),
         ('Empathy', 'Empathy'),
         ('Erlang', 'Erlang'),
         ('Feature Definition', 'Feature Definition'),
         ('Financial Modelling', 'Financial Modelling'),
         ('Forecasting', 'Forecasting'),
         ('FORTRAN', 'FORTRAN'),
         ('Front-End & Back-End Development', 'Front-End & Back-End Development'),
         ('Glucose Checks', 'Glucose Checks'),
         ('Go (Golang)', 'Go (Golang)'),
         ('Graphic Design Skills', 'Graphic Design Skills'),
         ('Groovy Perl', 'Groovy Perl'),
         ('Haskell Delphi', 'Haskell Delphi'),
         ('Hygiene Assistance', 'Hygiene Assistance'),
         ('HTML', 'HTML'),
         ('Ideation Leadership', 'Ideation Leadership'),
         ('Increasing Customer Lifetime Value (CLV)', 'Increasing Customer Lifetime Value (CLV)'),
         ('Interpersonal Communication', 'Interpersonal Communication'),
         ('Java', 'Java'),
         ('JavaScript', 'JavaScript'),
         ('Julia', 'Julia'),
         ('Kotlin', 'Kotlin'),
         ('Lead Prospecting', 'Lead Prospecting'),
         ('Lead Qualification', 'Lead Qualification'),
         ('Leadership', 'Leadership'),
         ('Lean Manufacturing', 'Lean Manufacturing'),
         ('LISP', 'LISP'),
         ('Lua', 'Lua'),
         ('Machine Learning', 'Machine Learning'),
         ('Management', 'Management'),
         ('Managing Cross-Functional Teams', 'Managing Cross-Functional Teams'),
         ('MATLAB', 'MATLAB'),
         ('Medicine Administration', 'Medicine Administration'),
         ('Meditech', 'Meditech'),
         ('Meeting Facilitation', 'Meeting Facilitation'),
         ('MS Office', 'MS Office'),
         ('Negotiation', 'Negotiation'),
         ('NIH Stroke Scale Patient Assessment', 'NIH Stroke Scale Patient Assessment'),
         ('Objective-C', 'Objective-C'),
         ('Office Equipment', 'Office Equipment'),
         ('Open Source Experience', 'Open Source Experience'),
         ('Organization', 'Organization'),
         ('Pascal', 'Pascal'),
         ('Patient Assessment', 'Patient Assessment'),
         ('Patient Care', 'Patient Care'),
         ('Patient Education', 'Patient Education'),
         ('Performance Tracking', 'Performance Tracking'),
         ('Phlebotomy', 'Phlebotomy'),
         ('Photography and Branding', 'Photography and Branding'),
         ('PHP', 'PHP'),
         ('POS Skills', 'POS Skills'),
         ('PowerShell', 'PowerShell'),
         ('PPC', 'PPC'),
         ('Print Design', 'Print Design'),
         ('Problem Solving', 'Problem Solving'),
         ('Product Knowledge', 'Product Knowledge'),
         ('Profit and Loss', 'Profit and Loss'),
         ('Project Launch', 'Project Launch'),
         ('Project Lifecycle Management', 'Project Lifecycle Management'),
         ('Prolog', 'Prolog'),
         ('Prototyping', 'Prototyping'),
         ('Public relations', 'Public relations'),
         ('Public Speaking', 'Public Speaking'),
         ('Python', 'Python'),
         ('QuickBooks', 'QuickBooks'),
         ('R', 'R'),
         ('Rebol', 'Rebol'),
         ('Recording Patient Medical History', 'Recording Patient Medical History'),
         ('Record-Keeping', 'Record-Keeping'),
         ('Reducing Customer Acquisition Cost (CAC)', 'Reducing Customer Acquisition Cost (CAC)'),
         ('Referral Marketing', 'Referral Marketing'),
         ('Rehabilitation Therapy', 'Rehabilitation Therapy'),
         ('Ruby', 'Ruby'),
         ('Rust', 'Rust'),
         ('Sales Funnel Management', 'Sales Funnel Management'),
         ('Salesforce', 'Salesforce'),
         ('Scala', 'Scala'),
         ('Scheduling', 'Scheduling'),
         ('Scope Management', 'Scope Management'),
         ('Scratch', 'Scratch'),
         ('Scrum', 'Scrum'),
         ('Security', 'Security'),
         ('Self Motivation', 'Self Motivation'),
         ('SEO/SEM', 'SEO/SEM'),
         ('Shipping', 'Shipping'),
         ('Simula', 'Simula'),
         ('Smalltalk', 'Smalltalk'),
         ('Social Media Marketing and Paid Social Media Advertising',
          'Social Media Marketing and Paid Social Media Advertising'),
         ('SolidWorks', 'SolidWorks'),
         ('Speakeasy', 'Speakeasy'),
         ('SQL', 'SQL'),
         ('STEM Skills', 'STEM Skills'),
         ('Swift', 'Swift'),
         ('Taking Vital Signs', 'Taking Vital Signs'),
         ('Teamwork', 'Teamwork'),
         ('Technical Report Writing', 'Technical Report Writing'),
         ('Testing', 'Testing'),
         ('Troubleshooting', 'Troubleshooting'),
         ('TypeScript', 'TypeScript'),
         ('Typography', 'Typography'),
         ('Urgent and Emergency Care', 'Urgent and Emergency Care'),
         ('Use of X-Ray, MRI, CAT Scans', 'Use of X-Ray, MRI, CAT Scans'),
         ('UX/UI', 'UX/UI'),
         ('VBA', 'VBA'),
         ('Visual Basic', 'Visual Basic'),
         ('Web Development', 'Web Development'),
         ('Welcoming Visitors', 'Welcoming Visitors'),
         ('Workflow Development', 'Workflow Development'),
         ('Wound Dressing and Care', 'Wound Dressing and Care'),
         ('Marketing', 'Marketing'),
         ('Field Sales', 'Field Sales'),
         ('Sales', 'Sales'),
     ]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    # ---old code----- dont delete even if commented
    gender = models.CharField(blank=True,default='',choices=GENDER,max_length=20)
    mailid = models.CharField(blank=True, max_length=140)
    skill_info = MultiSelectField(blank=True,default='',choices=SKILLS,max_length=540)
    profile_pic = models.ImageField(default='person.png',null = True, blank = True, upload_to='profile_pic')
    profile_resume = models.FileField(upload_to='resumes/',default='blank_resume.docx',null = True, blank = True)
    job_for_which_shortlisted=models.CharField(blank=True,default='',max_length=20)
    experience=models.CharField('Experience in years',blank=True,default='',max_length=40)
    company=models.CharField('Company',blank=True,default='',max_length=40)
    designation=models.CharField('Designation',blank=True,default='',max_length=40)
    current_ctc=models.CharField('Current CTC',blank=True, max_length=140, null=True)
    expected_ctc=models.CharField('Expected CTC',blank=True, max_length=140, null=True)
    notice_period=models.CharField('Notice Period',blank=True,default='',max_length=40)
    resume_link=models.CharField('Resume Link',blank=True,default='',max_length=40)
    linkedin=models.CharField('LinkedIn',blank=True,default='',max_length=40)
    
    

    # -------Kuldeep---additions--------


    # -----choices-------
    PRIMARY_PROFILE_CHOICES = [
        ('Business Development', 'Business Development'),
        ('Graphic Design', 'Graphic Design'),
        ('Social Media Marketing', 'Social Media Marketing'),
        ('Web Development', 'Web Development'),
        ('Content Writing', 'Content Writing'),
        ('Marketing', 'Marketing'),
        ('Operations', 'Operations'),
        ('App Development', 'App Development'),
        ('Human Resource(HR)', 'Human Resource(HR)'),
        ('Public Relations', 'Public Relations'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Research & Development', 'Research & Development'),
        ('Creative Designing', 'Creative Designing'),
        ('Law Legal', 'Law Legal'),
        ('Design', 'Design'),
        ('Software Development','Software Development'),
        ('Others', 'Others'),
    ]
    CITY_CHOICES = [
        ('Agra', 'Agra'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Ajmer', 'Ajmer'),
        ('Aligarh', 'Aligarh'),
        ('Allahabad', 'Allahabad'),
        ('Ambala', 'Ambala'),
        ('Amritsar', 'Amritsar'),
        ('Bangalore', 'Bangalore'),
        ('Bareilly', 'Bareilly'),
        ('Bharatpur', 'Bharatpur'),
        ('Bhilwara', 'Bhilwara'),
        ('Bhojpur', 'Bhojpur'),
        ('Bhopal', 'Bhopal'),
        ('Chandigarh', 'Chandigarh'),
        ('Chennai', 'Chennai'),
        ('Chhatarpur', 'Chhatarpur'),
        ('Chitrakoot', 'Chitrakoot'),
        ('Churu', 'Churu'),
        ('Coimbatore', 'Coimbatore'),
        ('Daman', 'Daman'),
        ('Darbhanga', 'Darbhanga'),
        ('Darjeeling', 'Darjeeling'),
        ('Dehradun', 'Dehradun'),
        ('Dholpur', 'Dholpur'),
        ('Diu', 'Diu'),
        ('Delhi', 'Delhi'),
        ('Sikkim', 'Sikkim'),
        ('Faridabad', 'Faridabad'),
        ('Fatehabad', 'Fatehabad'),
        ('Fatehpur', 'Fatehpur'),
        ('Firozabad', 'Firozabad'),
        ('Gandhinagar', 'Gandhinagar'),
        ('Ganganagar', 'Ganganagar'),
        ('Garhwa', 'Garhwa'),
        ('Gaya', 'Gaya'),
        ('Gautam Buddh Nagar', 'Gautam Buddh Nagar'),
        ('Ghaziabad', 'Ghaziabad'),
        ('Ghazipur', 'Ghazipur'),
        ('Gurgaon', 'Gurgaon'),
        ('Gwalior', 'Gwalior'),
        ('Hamirpur', 'Hamirpur'),
        ('Haridwar', 'Haridwar'),
        ('Hissar', 'Hissar'),
        ('Hooghly', 'Hooghly'),
        ('Hyderabad', 'Hyderabad'),
        ('Indore', 'Indore'),
        ('Jaipur', 'Jaipur'),
        ('Jaisalmer', 'Jaisalmer'),
        ('Jalandhar', 'Jalandhar'),
        ('Jammu', 'Jammu'),
        ('Jhansi', 'Jhansi'),
        ('Jodhpur', 'Jodhpur'),
        ('Kanchipuram', 'Kanchipuram'),
        ('Kanpur', 'Kanpur'),
        ('Kanyakumari', 'Kanyakumari'),
        ('Kargil ', 'Kargil'),
        ('Kohima', 'Kohima'),
        ('Kolhapur', 'Kolhapur'),
        ('Kolkata', 'Kolkata'),
        ('Kota', 'Kota'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Kurnool', 'Kurnool'),
        ('Kurukshetra', 'Kurukshetra'),
        ('Kutch', 'Kutch'),
        ('Lalitpur', 'Lalitpur'),
        ('Leh', 'Leh'),
        ('Lucknow', 'Lucknow'),
        ('Ludhiana', 'Ludhiana'),
        ('Madurai', 'Madurai'),
        ('Mainpuri', 'Mainpuri'),
        ('Mathura', 'Mathura'),
        ('Meerut', 'Meerut'),
        ('Mumbai ', 'Mumbai'),
        ('Muzaffarnagar', 'Muzaffarnagar'),
        ('Mysore', 'Mysore'),
        ('Nagpur', 'Nagpur'),
        ('Nainital', 'Nainital'),
        ('Nashik ', 'Nashik'),
        ('Nanital', 'Nanital'),
        ('Pali', 'Pali'),
        ('Panipat', 'Panipat'),
        ('Patna', 'Patna'),
        ('Pithoragarh', 'Pithoragarh'),
        ('Pondicherry', 'Pondicherry'),
        ('Pune', 'Pune'),
        ('Raigarh', 'Raigarh'),
        ('Raipur', 'Raipur'),
        ('Rajkot', 'Rajkot'),
        ('Ramgarh ', 'Ramgarh'),
        ('Ranchi', 'Ranchi'),
        ('Rohta', 'Rohta'),
        ('Sambalpur', 'Sambalpur'),
        ('Shimla', 'Shimla'),
        ('Sikar', 'Sikar'),
        ('Solapur', 'Solapur'),
        ('Sonipat', 'Sonipat'),
        ('Srinagar', 'Srinagar'),
        ('Surat', 'Surat'),
        ('Thane', 'Thane'),
        ('Thrissur', 'Thrissur'),
        ('Tiruchirappalli', 'Tiruchirappalli'),
        ('Tonk', 'Tonk'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Udaipur', 'Udaipur'),
        ('Udupi', 'Udupi'),
        ('Ujjain', 'Ujjain'),
        ('Uttarkashi', 'Uttarkashi'),
        ('Vadodara', 'Vadodara'),
        ('Varanasi', 'Varanasi'),
        ('Vellore', 'Vellore'),
        ('Visakhapatnam', 'Visakhapatnam'),
    ]
    DEGREE = [
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('B.Sc', 'B.Sc'),
        ('B.Com', 'B.Com'),
        ('B.A', 'B.A'),
    ]
    MARITAL_STATUS = [
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried')
    ]




    # ----model fields------
    summary = models.TextField(blank=True, max_length=540)

    job_profile=models.CharField('Job Profile',blank=True,default='',max_length=40,choices=PRIMARY_PROFILE_CHOICES)  



    # Experience details
    designation=models.CharField(blank=True,default='',max_length=40)
    company_name=models.CharField(blank=True,default='',max_length=100)
    company_start_date = models.CharField(blank =True, max_length=20)
    company_end_date = models.CharField(blank=True, max_length=20)
    company_loaction = models.CharField(blank=True, max_length=100)
    company_description = models.TextField(blank=True, max_length=540)
    company_doc = models.FileField(blank=True, upload_to="company_docs",null=True)
    already_working_here = models.BooleanField(default=False)

    # Reference details
    referee_name =models.CharField(blank=True, max_length=140)
    referee_email = models.CharField(blank = True, max_length=100)
    referee_designation = models.CharField(blank = True, max_length=100)
    referee_organisation = models.CharField(blank = True, max_length = 100)
    referee_relationship = models.CharField(blank = True, max_length=30)
    referee_phone = models.CharField(blank=True, max_length=20)


    # Other Prsonal details
    
    marital_status = models.CharField(max_length=20, blank=True,choices=MARITAL_STATUS)

    blood_group = models.CharField(blank = True, max_length=5)

    certifications = models.CharField(blank=True, max_length=500)
    
    dob = models.CharField(blank=True, max_length=140)


    # Education Details

    degree = models.CharField(blank = True, default="",choices=DEGREE, max_length=30)

    institute_name = models.CharField(max_length=200, default="", blank = True)
    branch = models.CharField(blank = True, max_length=100)
    cgpa = models.CharField(max_length=5, blank = True)
    ins_start_date = models.CharField(blank = True, max_length=20)
    ins_end_date = models.CharField(blank=True, max_length=20)
    edu_description = models.TextField(blank=True, max_length=500)
    certifications = models.FileField(blank=True, upload_to="certificates",null=True)

    def _str_(self):
        return self.name
