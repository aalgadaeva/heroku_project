from django.db import models

class Photos(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to='', verbose_name='Картинка')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
