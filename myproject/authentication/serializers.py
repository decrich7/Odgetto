
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'username')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            username=validated_data['username']

        )
        return user



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'full_name', 'profile_photo', 'interests', 'stats', 'bio', 'registration_date', 'email']



    # full_name = models.CharField(max_length=255)
    # profile_photo = models.URLField(max_length=255)
    # interests = models.TextField()
    # stats = models.TextField()
    # bio = models.TextField()
    # registration_date = models.DateTimeField(auto_now_add=True)
    # email = models.EmailField(unique=True)
