# Generated by Django 3.1.5 on 2021-01-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0008_delete_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자')),
                ('useremail', models.EmailField(max_length=128, verbose_name='이메일')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='가입일시')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='수정일시')),
            ],
            options={
                'verbose_name': '오픈튜토리얼스 사용자',
                'verbose_name_plural': 'o2 사용자',
                'db_table': 'o2_users',
            },
        ),
    ]
