from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from tuition.models import Subject, Class_in, District
from multiselectfield import MultiSelectField

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CATEGORY = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    BLOOD_GROUP = (
        ('A+','A+'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)
    nationality = models.CharField(max_length=30)
    religion = models.CharField(max_length=50)
    biodata = models.TextField(max_length=200)
    profession = models.CharField(max_length=50, choices=CATEGORY, null=True)
    image = models.ImageField(default='default.jpg', upload_to='session/images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class TuitionProfile(models.Model):
    STATUS = (
        ('Available','Available'),
        ('Busy','Busy'),
    )
    Choice_Style = (
        ('Group_Tuition', 'Group Tuition'),
        ('Private_Tuition', 'Private Tuition'),
    )
    Choice_Place = (
        ('Class_Rooms', 'Class Rooms'),
        ('Coaching_Center', 'Coaching Center'),
        ('Home_Visit', 'Home Visit'),
        ('My_Place', 'My Place'),
    )
    Choice_Approach = (
        ('Online_Help', 'Online Help'),
        ('Mobile_Help', 'Mobile Help'),
        ('Provide_Hand_Notes', 'Provide Hand_Notes'),
        ('Video_Tutorials', 'Video_Tutorials'),
    )
    Choice_Medium = (
        ('Bangla_Medium','Bangla Medium'),
        ('English_Medium','English Medium'),
        ('Arabic_Medium','Arabic Medium'),
        ('Hindi_Medium','Hindi Medium'),
        ('Sports_Section','Sport Section'),
        ('Singing_Section','Singing Section'),
        ('Dance_Section','Dance Section'),
        ('Extra Curricular Activities','Extra Curricular Activities'),
        ('Language Learning','Language Learning'),
        ('Computer Learning','Computer Learning'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tuitionprofile')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='district')
    style = MultiSelectField(choices=Choice_Style, max_choices=3, max_length=100)
    place = MultiSelectField(choices=Choice_Place, max_choices=3, max_length=100)
    approach = MultiSelectField(choices=Choice_Approach, max_choices=3, max_length=100)
    medium = MultiSelectField(choices=Choice_Medium, max_choices=3, max_length=100)
    subject = models.ManyToManyField(Subject, related_name='subjects')
    class_in = models.ManyToManyField(Class_in, related_name='classes')
    salary = models.CharField(max_length=100)
    days_per_week = models.CharField(max_length=100)
    education = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.user.username



