from rest_framework import serializers
class SchooleSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    number=serializers.IntegerField()
    adress=serializers.CharField()
    info=serializers.JSONField()
class ClassSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
class PersonSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    fname=serializers.CharField()
    date_of_birth=serializers.DateField()
    address=serializers.CharField()
class ParentsSerializer(PersonSerializer):
    id=serializers.IntegerField()
    user_name=serializers.CharField()
    password=serializers.CharField()
class StudentSerializer(PersonSerializer):
    id=serializers.IntegerField()
    school=SchooleSerializer()
    clasS=ClassSerializer()
    parents=ParentsSerializer()
    user_name=serializers.CharField()
    password=serializers.CharField()
    activite=serializers.BooleanField()
    phone=serializers.CharField()