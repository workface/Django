#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free', '자유'),
        ('travel', '여행'),
        ('cat', '고양이'),
        ('dog', '강아지'),
    )

    category = models.CharField('카테고리', max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # models.CASCADE => 같이 삭제
    # models.PROTECT => 삭제 불가능 (유저가 삭제하려고 할 때 블로그가 있으면 유저 삭제가 불가능)
    # models.SET_NULL => null값을 넣음 => 유저삭제시 블로그의 author가 null이됨


    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'
# 제못
# 본문
# 작성자
# 작성일자
# 수정일자
# 카테고리

# 썸네일 이미지
# 태그

