from django.db import models

class SearchableTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.searchable_fields = []
        if "searchable_fields" in kwargs.keys():
            self.searchable_fields = kwargs.pop("searchable_fields")
        super(SearchableTextField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        values = []
        for field in self.searchable_fields:
            value = self.__searchable_related_field_resolver(model_instance, field.split("__"))
            values.append(value)
        aggregated_texts = " ".join(values)
        setattr(model_instance, self.attname, aggregated_texts)
        return aggregated_texts

    def __searchable_related_field_resolver(self, obj, path):
        next_obj_level = getattr(obj, path[0])
        if len(path) <= 1:
            return next_obj_level
        else:
            if isinstance(next_obj_level, models.Manager):
                values = []
                for item in next_obj_level.all():
                    values.append(self.__searchable_related_field_resolver(item, path[1:]))
                return " ".join(values)
            else:
                return self.__searchable_related_field_resolver(next_obj_level, path[1:])

