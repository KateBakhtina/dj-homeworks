from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

from advertisements.models import Advertisement, Favorite_advertisements


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username')


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True,)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at')

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        if self.context["request"].method == 'POST':
            creator = self.context["request"].user.id
            advertisement_open = Advertisement.objects.\
                filter(creator_id=creator).\
                filter(status='OPEN')
            if len(advertisement_open) >= 10:
                raise ValidationError('Количество открытых объявлений превышает 10')
        return data


class FavoriteSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Favorite_advertisements
        fields = ("user", "advertisement")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["advertisement"] = self.context["view"]
        return super().create(validated_data)


class UserAdvertisements(serializers.ModelSerializer):
    my_advertisements = AdvertisementSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("username", "my_advertisements")





