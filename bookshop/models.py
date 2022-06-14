from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, help_text="Inter the name of Genre")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=False)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(help_text="Enter short book description")
    amount = models.IntegerField(default=0)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True) #берет информацию ищз базы данных поэтому нужно писть str наименование класса
    genre = models.ManyToManyField(Genre, help_text='Select genres') #хранит несколько эклемпляров моделей, нужно указать моделей какого класса
    price = models.FloatField()

    def __str__(self) -> str:
        return self.title

    
    def get_url(self):
        return reverse('view', args=[str(self.id)])


    def get_url_buy(self):
        return reverse('buy', args=[str(self.id)]) 
        
#создание миграции моделей python3 manage.py makemigrations
#после нужно провести след команду(для добавления в базу данных) python3 manage.py migrate
#предварительно нужно сделать python3 manage.py superuser 


