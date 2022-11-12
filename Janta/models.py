from django.db import models
import uuid
import datetime
from django.core.validators import MaxValueValidator
from django.conf import settings
from Department.models import Department , Department_user


Severity_CHOICES = (
    ('0','0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

Status_CHOICES = (
    ('1','Submitted'),
    ('2', 'Verified'),
    ('3', 'Assigned'),
    ('4', 'Processing'),
    ('5', 'Resolved'),
)

# Create your models here.
class Complaint(models.Model):
    Uuid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    # User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # User information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 , default = "default@email.com")
    phone = models.CharField(max_length=10)
    adhaar_number = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])

    # Complaint information
    public = models.BooleanField(default = False)
    # Created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    severity = models.CharField(max_length=1, choices=Severity_CHOICES, default='0')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Department_user, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='complaint/proofs',blank=True)
    location = models.CharField(max_length=100)
    send_to_email = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=Status_CHOICES, default='1')
    last_updated = models.DateTimeField(auto_now=True)

    status_com_1 = models.CharField(max_length=1000 , default = "Complaint Submitted")
    status_com_2 = models.CharField(max_length=1000 , default = "Complaint Verified")
    status_com_3 = models.CharField(max_length=1000 , default = "Complaint Assigned")
    status_com_4 = models.CharField(max_length=1000 , default = "Complaint Processing")
    status_com_5 = models.CharField(max_length=1000 ,  default = "Complaint Resolved")



    def __str__(self):
        return self.title + "           Comaplaint No : " + str(self.Uuid)

