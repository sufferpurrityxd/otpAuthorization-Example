from customUser.models import User
from customUser.validators import phonenumber_regex
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    phonenumber = serializers.CharField(
        validators=[phonenumber_regex]
    )

    class Meta:
        model = User
        fields = ('phonenumber',)

    def create(self, validated_data):
        try:
            user = User.objects.get(phonenumber=validated_data['phonenumber'])
        except Exception:
            user = User.objects.create_user(phonenumber=validated_data['phonenumber'])

        user.set_password(validated_data['code'])
        user.save()
        return user
