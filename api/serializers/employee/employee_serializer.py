from rest_framework import serializers

from api.models.employee.models import (
    Employee, Address, ContactPhone, ContactEmail, ContactSocialLinks, Education
)

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
    
class ContactPhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactPhone
        fields = '__all__'

class ContactEmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = '__all__'

class ContactSocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSocialLinks
        fields = '__all__'
    
class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'