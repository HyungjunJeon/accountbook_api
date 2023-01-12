from django.db import models
from django.conf import settings

class Accounts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='author') # 작성자
    amount = models.BigIntegerField() # 가계부 금액은 정수이며 입력할 수 있는 범위를 고려하여 BigInteger로 설정
    memo = models.TextField() # 메모는 Text로 설정

    class Meta:
        db_table = 'accounts' # 테이블 명은 accounts로 설정
        ordering = ['-id'] # 최신 순으로 정렬
