from django.db import models
from .forms import LENGTH_VALUES
# Create your models here.

class TestInstance(models.Model):

    list_length = models.IntegerField(choices=LENGTH_VALUES)
    unique_keys = models.BooleanField(default=True)
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
        return "list.length: {}; keys.unique: {}".format(str(self.list_length), str(self.unique_keys))


class AverageTimes(models.Model):

    test = models.ForeignKey(TestInstance, on_delete=models.CASCADE)
    test_number = models.IntegerField(default=0)
    avg_bubble = models.FloatField(default=0)
    avg_select = models.FloatField(default=0)
    avg_merge = models.FloatField(default=0)
    avg_heap = models.FloatField(default=0)
    avg_quick = models.FloatField(default=0)

    def update_data(self):
        self.avg_bubble = (self.avg_bubble * self.test_number + self.test.bubble)/(self.test_number + 1)
        self.avg_select = (self.avg_select * self.test_number + self.test.select)/(self.test_number + 1)
        self.avg_merge = (self.avg_merge * self.test_number + self.test.merge)/(self.test_number + 1)
        self.avg_heap = (self.avg_heap * self.test_number + self.test.heap)/(self.test_number + 1)
        self.avg_quick = (self.avg_quick * self.test_number + self.test.quick)/(self.test_number + 1)
        self.test_number += 1

    def get_data(self):

        data = {}
        data['bubble'] = self.avg_bubble
        data['select'] = self.avg_select
        data['merge'] = self.avg_merge
        data['heap'] = self.avg_heap
        data['quick'] = self.avg_quick

        return data

    def __str__(self):
        return "Avg_test_type: {}".format(str(self.test))


