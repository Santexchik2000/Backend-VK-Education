from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from user.documents import UserDocument


class UserDocumentSerializer(DocumentSerializer):

    class Meta:
        document = UserDocument
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'telefon',
            'role'
        )