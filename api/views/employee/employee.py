from rest_framework import viewsets
from rest_framework.response import Response

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

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.active_status = False
        item.save()

        return Response(data='not active')

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

class AddressViews(viewsets.ModelViewSet):
    serializer_class = AddressSerializers
    queryset = Address.objects.all()

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.active_status = False
        item.save()

        return Response(data='not active')

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

class ContactPhoneViews(viewsets.ModelViewSet):
    serializer_class = ContactPhoneSerializers
    queryset = ContactPhone.objects.all()

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.active_status = False
        item.save()

        return Response(data='not active')

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

class ContactEmailViews(viewsets.ModelViewSet):
    serializer_class = ContactEmailSerializers
    queryset = ContactEmail.objects.all()

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.active_status = False
        item.save()

        return Response(data='not active')

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

class ContactSocialLinksViews(viewsets.ModelViewSet):
    serializer_class = ContactSocialLinksSerializer
    queryset = ContactSocialLinks.objects.all()

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.active_status = False
        item.save()

        return Response(data='not active')

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

class EducationViews(viewsets.ModelViewSet):
    serializer_class = EducationSerializers
    queryset = Education.objects.all()

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.active_status = False
        item.save()

        return Response(data='not active')

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)