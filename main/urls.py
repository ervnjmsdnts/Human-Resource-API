from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.employee.employee import (
    EmployeeViews, AddressViews, ContactPhoneViews, ContactEmailViews, ContactSocialLinksViews,
    EducationViews
)

router = DefaultRouter()
router.register('employee', EmployeeViews, basename='Employee')
router.register('employee-address', AddressViews, basename='Employee Address')
router.register('employee-phone', ContactPhoneViews, basename='Employee Contact Phone')
router.register('employee-email', ContactEmailViews, basename='Employee Contact Email')
router.register('employee-social-links', ContactSocialLinksViews, basename='Employee Contact Social Links')
router.register('employee-education', EducationViews, basename='Employee Education')

urlpatterns = [
    path('api/', include(router.urls), name='API Endpoints'),
    path('admin/', admin.site.urls),
]
