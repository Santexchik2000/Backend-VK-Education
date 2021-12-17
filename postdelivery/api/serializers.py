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
    
    def validate(self,attrs):

        
        if len(attrs['first_name']) < 1 and len(attrs['first_name']) > 35:
            raise serializers.ValidationError(
                "Поле фамилия не должно содержать больше 35 символов")
        
        if len(attrs['last_name']) < 1 and len(attrs['last_name']) > 35:
            raise serializers.ValidationError(
                "Поле имя не должно содержать больше 35 символов")

        if len(attrs['telefon']) != 12:
            raise serializers.ValidationError(
                "Номер пользователя должен содержать ровно 12 букв,включая префикс +")
        if not all([i in "+1234567890" for i in attrs['telefon']]):
            raise serializers.ValidationError(
                "Номер пользователя не должен содержать символы алфавита, только цифры и префикс +")
        return attrs

        

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
    # creation_date = serializers.DateTimeField()
    # closing_date = serializers.DateTimeField()
    class Meta:
        model = Contract
        fields = ('id', 'client', 'recipient', 'route', 'manager','driver', 'loader')

    
