from rest_framework import viewsets

from api.models.employee.models import (
    Employee, Address, ContactPhone, ContactEmail, ContactSocialLinks, Education
)

from api.serializers.employee.employee_serializer import (
    EmployeeSerializers, AddressSerializers, ContactPhoneSerializers, ContactEmailSerializers,
    ContactSocialLinksSerializer, EducationSerializers
)

class EmployeeViews(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()

class AddressViews(viewsets.ModelViewSet):
    serializer_class = AddressSerializers
    queryset = Address.objects.all()

class ContactPhoneViews(viewsets.ModelViewSet):
    serializer_class = ContactPhoneSerializers
    queryset = ContactPhone.objects.all()

class ContactEmailViews(viewsets.ModelViewSet):
    serializer_class = ContactEmailSerializers
    queryset = ContactEmail.objects.all()

class ContactSocialLinksViews(viewsets.ModelViewSet):
    serializer_class = ContactSocialLinksSerializer
    queryset = ContactSocialLinks.objects.all()

class EducationViews(viewsets.ModelViewSet):
    serializer_class = EducationSerializers
    queryset = Education.objects.all()