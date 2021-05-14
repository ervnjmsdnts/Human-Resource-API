from django.db import models
import datetime, uuid

class Employee(models.Model):
    def uuid_pk():
        date_today = datetime.date.today()
        date = datetime.datetime.strftime(date_today, "%Y%m%d")
        uuid_char = uuid.uuid4()
        uuid_pk = date+str(uuid_char)[:5]
        return uuid_pk
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        ('DIVORCED', 'DIVORCED'),
        ('WIDOWED', 'WIDOWED'),
    ]

    emp_number = models.CharField(max_length=100, default=uuid_pk, primary_key=True, editable=False)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    socials_security_number = models.CharField(max_length=10)
    tin_number = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    active_status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateField(auto_now_add=True, null=True, blank=True)

class Address(models.Model):
    emp_number = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    street_address_1 = models.CharField(max_length=100)
    street_address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    active_status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateField(auto_now_add=True, null=True, blank=True)

class ContactPhone(models.Model):
    emp_number = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=100)
    active_status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateField(auto_now_add=True, null=True, blank=True)

class ContactEmail(models.Model):
    emp_number = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    email_address = models.EmailField(max_length=255)
    email_type = models.CharField(max_length=100)

class ContactSocialLinks(models.Model):
    emp_number = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    social_link = models.CharField(max_length=100)
    link_type = models.CharField(max_length=100)
    active_status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateField(auto_now_add=True, null=True, blank=True)

class Education(models.Model):
    emp_number = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    school_name = models.CharField(max_length=100)
    school_city = models.CharField(max_length=100)
    school_state = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    active_status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateField(auto_now_add=True, null=True, blank=True)






