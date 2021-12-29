# import django.contrib.admin.filters
import django_filters
from .models import *

# ModelnameFilter
class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['dni','enfermedad']
        
