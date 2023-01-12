from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Accounts
from accounts.serializers import AccountsSerializer

# 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 로그인 한 유저만 가능
@authentication_classes([JWTAuthentication]) # JWT 토큰 확인
def account_create(request):
    serializer = AccountsSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)

# 리스트 확인
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def account_list(request):
    account_list = Accounts.objects.all()
    paginator = PageNumberPagination()

    page_size = request.GET.get('size')
    if not page_size == None:
        paginator.page_size = page_size

    result = paginator.paginate_queryset(account_list, request)
    serializers= AccountsSerializer(result, many=True)
    return paginator.get_paginated_response(serializers.data)

# 세부 내역 확인
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def account_detail(request, pk):
    account = get_object_or_404(Accounts, pk=pk)
    serializer = AccountsSerializer(account)

    return Response(serializer.data, status=status.HTTP_200_OK)

# 수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def account_update(request, pk):
    account = get_object_or_404(Accounts, pk=pk)
    serializer = AccountsSerializer(instance=account, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK)

# 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def account_delete(request, pk):
    account = get_object_or_404(Accounts, pk)
    account.delete()
    return Response(status=status.HTTP_200_OK)