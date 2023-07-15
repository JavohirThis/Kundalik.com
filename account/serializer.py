from rest_framework import serializers
from .models import TeacherModel,StudentModel, ParentsModel

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsModel
        fields = '__all__'