from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from user.models import UserProfile

@registry.register_document
class UserDocument(Document):

    class Index:
        name = 'user'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = UserProfile
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'telefon',
            'role'
        ]
      