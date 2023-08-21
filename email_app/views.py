from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Event, EmailTemplate, Employee
from .serializers import EventSerializer, EmailTemplateSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer


def home(request):
    return render(request, 'home.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})

def emp_detail(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return render(request, 'emp_detail.html', {'employee': employee})
