import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.conf import settings
from .models import News, Contact

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'
    def post(self, request):
        Contact.objects.create(
            full_name=request.POST.get('full_name'),
            sex=request.POST.get('sex'),
            age=request.POST.get('age'),
            phone_number=request.POST.get('phone_number'),
            status='new',
            email=request.POST.get('email'),
            page=request.POST.get('page'),
        )
        return JsonResponse({'status': 'success'})
    
class AboutView(TemplateView):
    template_name = 'about.html'

class AboutUniversityView(TemplateView):
    template_name = os.path.join('university', 'index.html')

class StaffView(TemplateView):
    template_name = 'staff.html'

class PartnersView(TemplateView):
    template_name = 'partners.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class TeacherTrainingView(TemplateView):
    template_name = 'teacher-training.html'

class ProgramDetailsView(TemplateView):
    template_name = 'program-details.html'


class NewsView(TemplateView):
    template_name = os.path.join('news', 'index.html')

class NewsDetailView(TemplateView):
    template_name = os.path.join('news', 'detail.html')

class NotFoundView(TemplateView):
    template_name = '404.html'  


