from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    preamble = models.CharField(max_length=1024, verbose_name="Вступление")

    body = models.TextField(verbose_name="Содержание")
    body_as_markdown = models.BooleanField(default=False, verbose_name="Разметка в формате Html")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан", editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено", editable=False)
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name='новость'
        verbose_name_plural='новости'

    def delete(self, *args,**kwargs):
        self.deleted = True
        self.save()





class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)





class Course(models.Model):
    name = models.CharField(max_length=256, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)
    
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Стоимость", default=0)
    cover = models.CharField(max_length=125, default="no_image.svg", verbose_name="Картинка")

    description_as_markdown = models.BooleanField(verbose_name="Разметка в формате Html", default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан", editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено", editable=False)

    deleted = models.BooleanField(default=False, verbose_name="Удалено")
    
    def __str__(self):
        return f"{self.pk} {self.name}"

    class Meta:
        verbose_name='курс'
        verbose_name_plural='курсы'    
    
    def delete(self, *args,**kwargs):
        self.deleted = True
        self.save()




class Lesson(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name="Курс")

    num = models.PositiveIntegerField(verbose_name="Номер урока")
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")


    description_as_markdown = models.BooleanField(verbose_name="Разметка в формате Html", default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан", editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено", editable=False)
    deleted = models.BooleanField(default=False, verbose_name="Удалено")
    
    
    def __str__(self):
        return f"{self.course.name} {self.num} {self.title}"
    
    
    def delete(self, *args,**kwargs):
        self.deleted = True
        self.save()


    class Meta:
        verbose_name='Урок'
        verbose_name_plural='Уроки' 

class courseTeacher(models.Model):
    Courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан", editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено", editable=False)
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    def delete(self, *args,**kwargs):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name='курс к учителю'
        verbose_name_plural='курсы к учетелям'