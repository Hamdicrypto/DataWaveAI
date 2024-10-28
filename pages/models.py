from django.db import models

# Create your models here.



class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name_arabic = models.CharField(max_length=100, blank=True )
    last_name_arabic = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    designation_arabic = models.CharField(max_length=100, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.designation_arabic:  # Set default value as designation only if designation_arabic is empty
            self.designation_arabic =  self.designation
        if not self.first_name_arabic:  # Set default value as first_name only if first_name_arabic is empty
            self.first_name_arabic =  self.first_name    
        if not self.last_name_arabic:  # Set default value as last_name only if last_name_arabic is empty
            self.last_name_arabic =  self.last_name    
            
        super().save(*args, **kwargs)
        
    photo = models.ImageField(upload_to='photos/%Y/%M/%D/')
    facebook = models.URLField(max_length=255)
    xlink = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    instgram = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
    

    
    
    
