from django.contrib import admin
from mainapp.models import News, Course, Lesson, courseTeacher

# admin.site.register(News)
admin.site.register(Course)


# admin.site.register(Lesson)


# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # list_per_page = 10
    search_fields = ('title', 'preamble', 'body')
    list_display = ('title', 'preamble', 'body')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'description', 'deleted')
    ordering = ('-num', '-title',)
    actions = ('mark_as_delete',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = ' Пометить удаленным '
