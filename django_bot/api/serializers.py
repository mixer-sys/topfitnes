from rest_framework import serializers


from base.models import (Sleep, WorkoutSession, Nutrients,
                         Category, TrainingVideo)



class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ['id', 'title_exercise',
                  'count_approaches', 'count_repetitions', 'user_id']


class NutrientsSerializer(serializers.ModelSerializer):
    """Сериализатор Питательных веществ."""
    class Meta:
        model = Nutrients
        fields = (
            'id', 'chat', 'calories', 'protein', 'fats',
            'carbohydrates', 'date_record'
        )


class SleepDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = (
            'id', 'user', 'time_down'
            )


class SleepUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = (
            'id', 'user', 'time_up'
            )
        
        
class TrainingVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingVideo
        fields = [
            'pk',
            'title',
            'description',
            'duration',
            'file_path',
            'category',
            'difficulty'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']



class DifficultySerializer(serializers.Serializer):
    key = serializers.CharField()
    name = serializers.CharField()
