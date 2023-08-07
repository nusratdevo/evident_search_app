from rest_framework import serializers
from .models import CustomUser, SortedInput

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        email = serializers.CharField(max_length=255)
        password = serializers.CharField(min_length=8, write_only=True)
        name = serializers.CharField(max_length=255)
        username = serializers.CharField(max_length=255)
        image=serializers.ImageField()
        model = CustomUser
        fields = ['email','name','username' ,'password', 'image']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    #    def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = User.objects.create(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user
        #   def create(self, validated_data):
        #     password = validated_data.pop('password')
        #     user = super().create(validated_data)
        #     user.set_password( make_password(validated_data['password']))
        #     user.save()
        #     return user
        
class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = CustomUser
    fields = ['email', 'password']
    
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['email','name','username', 'image', 'updated_at']

class SortedInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = SortedInput
        fields = '__all__'

class SortedSerializer(serializers.ModelSerializer):

    class Meta:
        model = SortedInput
        fields = ['input_values', 'timestamp', 'search_value']
