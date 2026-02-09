from django.db import models
from django.db.models import SET_NULL
# Create your models here.
class Readers(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    enrollment_date=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    def __str__(self):
        return f'Name : {self.name}, Email : {self.email}, Enrollment_Date: {self.enrollment_date}, Image: {self.image}'

class Books(models.Model):
    title=models.CharField(max_length=60)
    author=models.CharField(max_length=60)
    genre=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    stock=models.IntegerField()
    assignment=models.ForeignKey(Readers, on_delete=SET_NULL, null=True, blank=True, related_name='books')

    def __str__(self):
        assigned_reader = self.assignment.name if self.assignment else "Unassigned"
        return (f'Title: {self.title}, Author: {self.author}, '
                f'Genre: {self.genre}, Price: {self.price}, '
                f'Stock: {self.stock}, Assigned Reader: {assigned_reader}')
