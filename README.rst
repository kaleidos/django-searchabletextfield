Django Searchable Text Field
============================

A Django field for aggregate text fields in one to easy fulltext searches.

Example model fields
--------------------

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

Example using relations
-----------------------

::

  >>> from django.db import models
  >>> from searchabletextfield.models import SearchableTextField
  >>> class Article(models.Model):
  >>>     title = models.CharField(max_length=100)
  >>>     description = models.TextField()
  >>>     no_idx_description = models.TextField()
  >>>     searchable_text = SearchableTextField(searchable_fields=['title','description','comments__text']
  >>> class Comment(models.Model):
  >>>     article = models.ForeignKey(Article, related_name='comments')
  >>>     text = models.CharField(max_length=200)
  >>> article = Article(title='title', description='description', no_idx_description='no idx description')
  >>> article.save()
  >>> comment = Comment(article=article, text="example1").save()
  >>> comment = Comment(article=article, text="example2").save()
  >>> article.searchabe_text
  'title description'
  >>> article.save()
  >>> article.searchabe_text
  'title description example1 example2'
