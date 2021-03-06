from django.db import models

# Create your models here.
import mongoengine


class SearchModel(mongoengine.Document):
    search_text = mongoengine.StringField(max_length=500)

    def __str__(self):
        return self.search_text


class TriplesModel(mongoengine.Document):
    triples_id = mongoengine.StringField(max_length=500)
    item_name = mongoengine.StringField(max_length=500)
    attr = mongoengine.StringField(max_length=500)
    value = mongoengine.StringField(max_length=500)
