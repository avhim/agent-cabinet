from rest_framework import serializers
from .models import Agency
from useraccount.serializers import UserDetailSerializer


class AgencyDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True, many=False)

    class Meta:
        model = Agency
        fields = ('__all__')