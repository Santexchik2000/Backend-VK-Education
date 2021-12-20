from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from db.models import Contract

@registry.register_document
class ContractDocument(Document):

    class Index:
        name = 'contract'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = Contract
        fields = [
            'id',
            'contract_price',
            'creation_date',
            'closing_date',
        ]
      