from rest_framework import serializers
from qdpc_core_models.models.user import User
from qdpc_core_models.models.role import Role
from qdpc_core_models.models.division import Division
from qdpc_core_models.models.center import Center
from qdpc_core_models.models.user_type import UserType


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'name']


class CenterSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(read_only=True)  # This will include UserType details
    user_type_id = serializers.PrimaryKeyRelatedField(queryset=UserType.objects.all(), source='user_type', write_only=True)

    class Meta:
        model = Center
        fields = ['id', 'name', 'user_type', 'user_type_id']

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        center = Center.objects.create(user_type=user_type, **validated_data) # test data
        return center


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class UserSignupSerializer(serializers.ModelSerializer):
    centre = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    divisions = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    role = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'status', 'desired_salutation', 'user_id', 'first_name', 
            'last_name', 'email', 'centre', 'divisions', 'phone_number', 'role_id', 
            'usertype', 'role', 'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        centres = validated_data.pop('centre')
        divisions = validated_data.pop('divisions')
        roles = validated_data.pop('role')

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        instance.centre.set(centres)
        instance.divisions.set(divisions)
        instance.role.set(roles)

        return instance
