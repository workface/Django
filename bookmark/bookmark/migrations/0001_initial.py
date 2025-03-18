# Generated by Django 5.1.7 on 2025-03-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('url', models.URLField(verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
            ],
            options={
                'verbose_name': '북마크',
                'verbose_name_plural': '북마크 목록',
            },
        ),
    ]


# makemigrations => migration.py 파일을 만듬
# 실제 DB에는 영향 x => 실제 DB에 넣기 위한 정의를 하는 파일 생성

# migrate => migrations/ 폴더 안에 있는 migraion 파일들을 실제 DB에 적용함

# makemigrations => Git의 commit => github에 적용 x => DB에 적용 x, 적용할 파일 생성
# migrate => Git의 push => github에 적용 O => DB에 적용 O, 로컬애 있는 커밋 기록 => DB 적용O => migrations 파일들을 가지고 적용