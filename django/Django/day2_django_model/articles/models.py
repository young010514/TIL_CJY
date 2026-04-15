from django.db import models

# Create your models here.
class Article(models.Model):  # 반드시 models.Model 상속 받을 것!
    # 그 외 데이터 타입들 정의하기
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

