from django.test import TestCase
from .models import TestModel, Test2Model, Test2RelatedModel

class SearchableTextFieldTest(TestCase):
    def setUp(self):
        pass
        
    def test_pre_save(self):
        test_obj = TestModel(title="test", description="searchable", not_searchable_description="nosearchable")
        test_obj.save()
        self.assertEqual(test_obj.searchable_text, "test searchable")

    def test_related_pre_save(self):
        # Not objects on the related query
        test_obj = Test2Model(title="test", description="searchable", not_searchable_description="nosearchable")
        test_obj.save()
        self.assertEqual(test_obj.searchable_text, "test searchable ")

        # One object on related query
        test_obj2 = Test2Model(title="test", description="searchable", not_searchable_description="nosearchable")
        test_obj2.save()
        Test2RelatedModel(test=test_obj2, other_text="other_text").save()
        test_obj2.save()
        self.assertEqual(test_obj2.searchable_text, "test searchable other_text")

        # Many object on related query
        test_obj2 = Test2Model(title="test", description="searchable", not_searchable_description="nosearchable")
        test_obj2.save()
        Test2RelatedModel(test=test_obj2, other_text="other_text1").save()
        Test2RelatedModel(test=test_obj2, other_text="other_text2").save()
        test_obj2.save()
        self.assertEqual(test_obj2.searchable_text, "test searchable other_text1 other_text2")
