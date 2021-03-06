from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from core.models import (
    User, Project, Dataset, Attribute, Analysis, Parameter, Argument
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (  'id','username','password','first_name',
                    'last_name','email','is_superuser','is_active'
        )
        extra_kwargs = {'password': {'write_only': True}}


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('__all__')


class DatasetSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = ('id','name','file','creation_status','attributes')


class ParameterSerializer(serializers.ModelSerializer):
    parameter_type = serializers.SlugRelatedField(
        read_only=True, slug_field='description'
    )

    class Meta:
        model = Parameter
        fields = ('name','parameter_type','default_value')


class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'


class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')


class ProjectAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('id','analysis_type','analysis_status')


class ProjectGetSerializer(serializers.ModelSerializer):
    users = ProjectUserSerializer(many=True, read_only=True)
    owner = ProjectUserSerializer(read_only=True)
    analysis = ProjectAnalysisSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'description', 'location', 'people_editing', 
            'visibility', 'datasets', 'users', 'owner', 'created', 'modified', 
            'analysis'
        )


class ProjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
