from django.test import TestCase
from .models import TestModel

class SearchableTextFieldTest(TestCase):
    def setUp(self):
        pass
        
    def test_pre_save(self):
        test_obj = TestModel(title="test", description="searchable", not_searchable_description="nosearchable")
        test_obj.save()
        self.assertEqual(test_obj.searchable_text, "test searchable")
