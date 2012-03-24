from django.db import models
from ..models import SearchableTextField

class TestModel(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    not_searchable_description = models.TextField()
    searchable_text = SearchableTextField(searchable_fields=['title', 'description'])

class Test2Model(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    not_searchable_description = models.TextField()
    searchable_text = SearchableTextField(searchable_fields=['title', 'description', 'related__other_text'])

class Test2RelatedModel(models.Model):
    test = models.ForeignKey(Test2Model, related_name="related")
    other_text = models.TextField()
