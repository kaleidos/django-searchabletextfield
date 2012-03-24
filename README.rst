Django Searchable Text Field
============================

A Django field for aggregate text fields in one to easy fulltext searches.

Example
-------

::

  >>> from django.db import models
  >>> from searchabletextfield.models import SearchableTextField
  >>> class Article(models.Model):
  >>>     title = models.CharField(max_length=100)
  >>>     description = models.TextField()
  >>>     no_idx_description = models.TextField()
  >>>     searchable_text = SearchableTextField(searchable_fields=['title','description']
  >>> article = Article(title='title', description='description', no_idx_description='no idx description')
  >>> article.save()
  >>> article.searchabe_text
  'title description'
