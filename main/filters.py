# import django.contrib.admin.filters
import django_filters
from .models import *

# ModelnameFilter
class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['bed_num']
        #fields = '__all__'
        #exclude = ['phone_num', 'address','doctors_notes']
        
