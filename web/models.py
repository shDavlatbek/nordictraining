import os
import uuid
from django.db import models
from tinymce import models as tinymce_models

GENDER = [
    ('male', 'Erkak'),
    ('female', 'Ayol'),
]

STATUS = [
    ('new', 'Yangi'),
    ('read', 'O\'qilgan'),
    ('replied', 'Javob berilgan'),
]

# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    content = tinymce_models.HTMLField(verbose_name='Kontent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='O\'zgartirilgan vaqti')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
    

class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='F.I.O')
    sex = models.CharField(max_length=255, blank=True, null=True, verbose_name='Jinsi')
    age = models.IntegerField(blank=True, null=True, verbose_name='Yoshi')
    phone_number = models.CharField(max_length=255, verbose_name='Telefon raqami')
    email = models.EmailField(verbose_name='Email')
    status = models.CharField(max_length=255, choices=STATUS, default='new', verbose_name='Status')
    page = models.CharField(max_length=255, verbose_name='Murojaat-sahifasi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='O\'zgartirilgan vaqti')

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Murojaat'
        verbose_name_plural = 'Murojaatlar'
        
        

def get_image_path(instance, filename):
    """Generate a unique path for uploaded images."""
    ext = filename.split('.')[-1]
    # Create a unique filename with uuid
    filename = f"{uuid.uuid4().hex}.{ext}"
    # Return the upload path
    return os.path.join('uploads', 'tinymce', filename)



class TinyMCEImage(models.Model):
    """Model to store images uploaded through TinyMCE."""
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=get_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title or f"Image {self.id}"
    
    def save(self, *args, **kwargs):
        # If no title is provided, use the original filename
        if not self.title and self.image:
            self.title = os.path.basename(self.image.name)
        super().save(*args, **kwargs)