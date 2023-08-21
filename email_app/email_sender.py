from django.core.mail import send_mail
from .models import Event, Employee, EmailTemplate, datetime

def send_emails():
    current_date = datetime.date.today()
    events = Event.objects.filter(event_date=current_date)
    
    for event in events:
        try:
            employee = Employee.objects.get(employee_id=event.employee_id)
            template = EmailTemplate.objects.get(event_type=event.event_type)
            
            email_content = template.template.format(employee_name=employee.name, event_date=event.event_date)
            
            send_mail(
                'Event Reminder',
                email_content,
                'sender@example.com',
                [employee.email],
                fail_silently=False,
            )
            
            # Log email sending status
            event.email_sent = True
            event.save()
            
        except Employee.DoesNotExist:
            # Log error and continue
            event.email_error = 'Employee not found'
            event.save()
        except EmailTemplate.DoesNotExist:
            # Log error and continue
            event.email_error = 'Email template not found'
            event.save()
        except Exception as e:
            # Log error and retry or mark as failed attempt
            event.email_error = str(e)
            event.save()

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EmailTemplateViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'email-templates', EmailTemplateViewSet)

