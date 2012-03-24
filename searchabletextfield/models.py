from django.db import models

class SearchableTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.searchable_fields = []
        if "searchable_fields" in kwargs.keys():
            self.searchable_fields = kwargs.pop("searchable_fields")
        super(SearchableTextField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        aggregated_texts = " ".join([getattr(model_instance, attname) for attname in self.searchable_fields])
        setattr(model_instance, self.attname, aggregated_texts)
        return aggregated_texts
