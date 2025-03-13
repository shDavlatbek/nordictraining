import os
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.conf import settings
from .models import News, Contact, TinyMCEImage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from urllib.parse import urljoin

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:4]
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')
        return context

class NewsDetailView(TemplateView):
    template_name = os.path.join('news', 'detail.html')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = get_object_or_404(News, slug=self.kwargs['slug'])
        context['news_all'] = News.objects.all().exclude(slug=self.kwargs['slug']).order_by('-created_at')[:3]
        return context

class NotFoundView(TemplateView):
    template_name = '404.html'  


@csrf_exempt
@login_required
def upload_image(request):
    """Handle image uploads from TinyMCE editor."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    uploaded_file = request.FILES['file']
    
    # Check if file is an image
    if not uploaded_file.content_type.startswith('image/'):
        return JsonResponse({'error': 'File is not an image'}, status=400)
    
    # Create a new image record
    image = TinyMCEImage(title=uploaded_file.name)
    image.image = uploaded_file
    image.save()
    
    # Get the absolute URL by combining the site URL with the media URL
    site_url = request.build_absolute_uri('/').rstrip('/')
    relative_url = image.image.url
    
    # Ensure we have an absolute URL
    if relative_url.startswith('/'):
        # Already a root-relative URL, just add the site domain
        absolute_url = f"{site_url}{relative_url}"
    else:
        # Combine with the site URL
        absolute_url = urljoin(site_url, relative_url)
    
    # Return the absolute URL to the image
    return JsonResponse({
        'location': absolute_url,  # Absolute URL for TinyMCE
        'success': True
    })