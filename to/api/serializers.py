from rest_framework.serializers import ModelSerializer
from to.models import Todo
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class Todoserializer(TaggitSerializer, ModelSerializer):
    tag = TagListSerializerField()

    class Meta:
        model = Todo
        #fields = '__all__'
        fields = ['id', 'title', 'description',
                  'tag', 'status', 'due_date', 'created']
