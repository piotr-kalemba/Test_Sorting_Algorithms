from django.db import models
from .forms import LENGTH_VALUES, ALGORITHMS
from django.contrib.auth.models import User

# Create your models here.

class AllAlgorithmsTest(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_length = models.IntegerField(choices=LENGTH_VALUES)
    unique_keys = models.BooleanField(default=True)
    test_date = models.DateTimeField(auto_now=True)
    bubble = models.FloatField(default=0)
    select = models.FloatField(default=0)
    merge = models.FloatField(default=0)
    heap = models.FloatField(default=0)
    quick = models.FloatField(default=0)

    def set_data(self, data):
        self.bubble = data['bubble']
        self.select = data['select']
        self.merge = data['merge']
        self.heap = data['heap']
        self.quick = data['quick']

    def __str__(self):
        if self.unique_keys == True:
            return "Wszystkie algorytmy: rozmiar tablicy (elementy unikalne): {}; data testu: {}."\
                .format(str(self.list_length),str(self.test_date.replace(microsecond=0))[:-6])
        else:
            return "Wszystkie algorytmy: rozmiar tablicy: {}; data testu: {}." \
                .format(str(self.list_length), str(self.test_date.replace(microsecond=0))[:-6])


class AlgorithmTest(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    algorithm = models.CharField(max_length=20, choices=ALGORITHMS)
    unique_keys = models.BooleanField(default=True)
    test_date = models.DateTimeField(auto_now=True)
    time_10 = models.FloatField(default=0)
    time_100 = models.FloatField(default=0)
    time_1000 = models.FloatField(default=0)
    time_10000 = models.FloatField(default=0)


    def set_data(self, data):
        self.time_10 = data['10']
        self.time_100 = data['100']
        self.time_1000 = data['1000']
        self.time_10000 = data['10000']

    def __str__(self):
        if self.unique_keys == True:
            return "Algorytm: {}; elementy unikalne; data testu: {}.".\
                format(self.algorithm, str(self.test_date.replace(microsecond=0))[:-6])
        else:
            return  "Algorytm: {}; data testu: {}.".\
                format(self.algorithm, str(self.test_date.replace(microsecond=0))[:-6])

