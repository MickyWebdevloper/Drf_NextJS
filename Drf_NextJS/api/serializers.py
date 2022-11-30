from .models import Posts

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)


class PostSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='apis:detail',
        lookup_field='slug'
    )

    author = SerializerMethodField()

    class Meta:
        model = Posts
        fields = ['url', 'title', 'content', 'author', 'slug', 'date_created']

    def get_author(self, obj):
        return obj.author.email
