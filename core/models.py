from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Owner(models.Model):
    name = models.CharField(max_length=225)
    nick_name = models.CharField(max_length=40)
    about = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='owner/')
    portfolio_link = models.URLField()
    designation = models.CharField(max_length=300)
    location = models.CharField(max_length=225)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=225)
    # media links 
    fav_icon = models.ImageField(upload_to='favicon/')
    hero_bg_color = models.CharField(max_length=225, default='gray')
    github = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()
    # Headings and sub-headings
    service_heading = models.CharField(max_length=255, default="Services")
    service_sub_heading = models.CharField(max_length=255, default='Our latest Services')
    skill_heading = models.CharField(max_length=255, default="Skills")
    skill_sub_heading = models.CharField(max_length=255, default="My skills")
    testimonial_heading = models.CharField(max_length=255, default="Testimonials")
    testimonial_sub_heading = models.CharField(max_length=255, default="Client Response")
    blog_heading = models.CharField(max_length=255, default="Blogs")
    blog_sub_heading = models.CharField(max_length=255, default="Featured Blog")
    contact_heading = models.CharField(max_length=255, default="Contacts")
    contact_sub_heading = models.CharField(max_length=255, default="feel free to contact!!")
    call_to_action = models.CharField(max_length=300, default="Let's have a one to one session with me.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WidgetItem(models.Model):
    number = models.IntegerField()
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.label
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='service_category')
    tags = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='service/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug based on the title
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1

        while Services.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{counter}"
            counter += 1

        self.slug = unique_slug
        super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Images(models.Model):
    logo_file = models.ImageField(upload_to='logo/')
    hero_file = models.ImageField(upload_to='hero/')
    about_file = models.ImageField(upload_to='about/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureService(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=50)  # icon, e.g., 'ti-crown'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=225)
    quote = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='testimonials_images/', blank=True, null=True)
    designation = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HomeContact(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    