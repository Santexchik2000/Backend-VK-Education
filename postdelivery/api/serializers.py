from rest_framework import serializers
from db.models import Contract, Recipient, AdressSender, AdressRecipient, Route
from user.models import UserProfile


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields =('id','fname','lname','telefon')

class AdressSenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdressSender
        fields = ('id','city','street','house','flat')

class AdressRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdressRecipient
        fields = ('id','city','street','house','flat')

class RouteSerializer(serializers.ModelSerializer):
    adress_Sender = AdressSenderSerializer(read_only=True)
    adress_Recipient = AdressRecipientSerializer(read_only=True)

    class Meta:
        model = Route
        fields =('adress_Sender','adress_Recipient')


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields =(
        'id','username','email','first_name',
        'last_name','telefon','role'
        )


class ContractSerializer(serializers.ModelSerializer):
    client = UserProfileSerializer(read_only=True)
    recipient = RecipientSerializer(read_only=True)
    route = RouteSerializer(read_only=True)
    manager = UserProfileSerializer(read_only=True)
    driver = UserProfileSerializer(read_only=True)
    loader = UserProfileSerializer(many=True,read_only=True)
    class Meta:
        model = Contract
        fields = (
        'id','client','recipient','route',
        'manager','driver', 'creation_date',
        'closing_date', 'contract_price',
        'count_loader','comment','loader')

    
