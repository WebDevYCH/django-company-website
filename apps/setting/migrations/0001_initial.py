# Generated by Django 2.0.10 on 2020-01-31 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics', models.TextField(default='Statistics Code', verbose_name='Website Statistics Code ')),
            ],
            options={
                'verbose_name': 'Custom code',
                'verbose_name_plural': 'Custom code',
            },
        ),
        migrations.CreateModel(
            name='FriendLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Eastbound notebook', max_length=50, verbose_name='Site name')),
                ('link', models.CharField(default='https: //www.eastnotes.com', max_length=200, verbose_name='Website address')),
            ],
            options={
                'verbose_name': 'Links',
                'verbose_name_plural': 'Links',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DjangoEast', max_length=100, verbose_name='Site Master Name')),
                ('sub_title', models.CharField(default='DjangoEast', max_length=200, verbose_name='Site name for website')),
                ('description', models.CharField(default='DjangoEast', max_length=200, verbose_name='Site description')),
                ('keywords', models.CharField(default='DjangoEast', max_length=200, verbose_name='Keyword')),
            ],
            options={
                'verbose_name': 'SEO Set up',
                'verbose_name_plural': 'SEO Set up',
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(default=django.utils.timezone.now, verbose_name='Website time')),
                ('record_info', models.CharField(default='Record number', max_length=100, verbose_name='Record information')),
                ('development_info', models.CharField(default='Development information', max_length=100, verbose_name='Development information')),
                ('arrange_info', models.CharField(default='Deployment Information', max_length=100, verbose_name='Deployment Information')),
            ],
            options={
                'verbose_name': 'Site Information',
                'verbose_name_plural': 'Site Information',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(default='https://github.com/mxdshr/DjangoEast', verbose_name='Github address')),
                ('wei_bo', models.URLField(default='https://weibo.com/', verbose_name='Weibo address')),
                ('zhi_hu', models.URLField(default='https://www.zhihu.com/people/sylax8/', verbose_name='Know the address')),
                ('qq', models.CharField(default='783342105', max_length=20, verbose_name='QQ number')),
                ('wechat', models.CharField(default='reborn0502', max_length=50, verbose_name='WeChat')),
                ('official_wechat', models.CharField(default='Programmer Xiangdong', max_length=50, verbose_name='WeChat public account')),
            ],
            options={
                'verbose_name': 'Social account',
                'verbose_name_plural': 'Social account',
            },
        ),
    ]
