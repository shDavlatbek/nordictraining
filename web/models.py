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
        
