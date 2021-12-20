from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from db.documents import ContractDocument


class ContractDocumentSerializer(DocumentSerializer):

    class Meta:
        document = ContractDocument
        fields = (
            'id',
            'contract_price',
            'creation_date',
            'closing_date',
        )