from django.contrib import admin

from .models import (
    Nutrients,
    Category,
)


@admin.register(Nutrients)
class NutrientsPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'chat',
        'protein',
        'fats',
        'carbohydrates',
        'calories',
        'date_record',
    )


"""@admin.register(TrainingVideo)
class TrainingVideoPanel(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'duration',
        'file_path',
        'category',
        'difficulty',
    )
    search_fields = ('title',
                     'description',
                     'duration',
                     'file_path',
                     'category',
                     'difficulty',
                     )
    list_filter = ('category', 'difficulty')"""


@admin.register(Category)
class CategoryPanel(admin.ModelAdmin):
    list_display = (
        'name',
    )
