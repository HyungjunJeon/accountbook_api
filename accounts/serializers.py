from rest_framework import serializers
from .models import Accounts
from users.serializers import UserInfoSerializer

class AccountsSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True) # 유저 정보 가져오기

    class Meta:
        model = Accounts
        fields = '__all__'