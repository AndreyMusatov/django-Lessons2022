# Generated by Django 4.1.5 on 2023-01-07 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание курса')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Стоимость')),
                ('cover', models.CharField(default='no_image.svg', max_length=125, verbose_name='Картинка')),
                ('description_as_markdown', models.BooleanField(default=False, verbose_name='Разметка в формате Html')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('preamble', models.CharField(max_length=1024, verbose_name='Вступление')),
                ('body', models.TextField(verbose_name='Содержание')),
                ('body_as_markdown', models.BooleanField(default=False, verbose_name='Разметка в формате Html')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(verbose_name='Номер урока')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_as_markdown', models.BooleanField(default=False, verbose_name='Разметка в формате Html')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='courseTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('Courses', models.ManyToManyField(to='mainapp.course')),
            ],
            options={
                'verbose_name': 'курс к учителю',
                'verbose_name_plural': 'курсы к учетелям',
            },
        ),
    ]
