from random import choice

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from django.http import HttpResponseNotFound

from users.models import User
from .utils import (
    calorie_calculation, toFixed, calculation_n_days_ago
)

from .serializers import (SleepDownSerializer,
                          NutrientsSerializer,
                          WorkoutSessionSerializer,
                          CategorySerializer,
                          TrainingVideoSerializer,
                          CategorySerializer,
                          DifficultySerializer)

from base.models import (
    WorkoutSession, Nutrients, Sleep, Category, TrainingVideo
)

from base.configurations import (
    INDICATORS_MEN, INDICATORS_WOMEN, RANGE_TRAINING_DAYS,
    USER_ACTIVITY, OUTPUT_AFTER_COMMA, BAD_SLEEP, GOOD_SLEEP,
    VERY_GOOD_SLEEP, SEC, DIFFICULTY_CHOICES
)


class SleepDownViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepDownSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class SleepUpViewSet(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = ...


class NutrientsViewSet(viewsets.ModelViewSet):
    """Показатели калорий и БЖУ который внёс пользователь."""
    queryset = Nutrients.objects.all()
    serializer_class = NutrientsSerializer


class СalorieСalculationView(APIView):
    """Вычисление Нормы калорий."""
    def get(self, request, pk):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        indicaors = INDICATORS_WOMEN
        if user.sex:
            indicaors = INDICATORS_MEN
        training_capture_day = calculation_n_days_ago(RANGE_TRAINING_DAYS)
        user_activity = WorkoutSession.objects.filter(
            user_id=user.id,
            date__gte=training_capture_day
        ).count()
        if not user_activity:
            result = 'Пользователь не тренировался.'
        else:
            for value in USER_ACTIVITY.values():
                if user_activity in value['training']:
                    user_activity *= value['activity']
            result = calorie_calculation(
                user.weight,
                user.height,
                user.age,
                indicaors,
                user_activity,
                user.target
            )
            result = toFixed(result, OUTPUT_AFTER_COMMA)
        return Response(
            {'result': result}, status=status.HTTP_200_OK
        )


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer


class WorkoutSessionView(APIView):
    #  permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        if not request.data:
            return Response({"error": "No data provided"},
                            status=status.HTTP_400_BAD_REQUEST)
        workoutsession = get_object_or_404(WorkoutSession, pk=pk)
        serializer = WorkoutSessionSerializer(workoutsession,
                                              data=request.data,
                                              partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def delete(self, request, pk):
        workoutsession = get_object_or_404(WorkoutSession, pk=pk)
        workoutsession.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrainingVideoView(APIView):
    def get(self, *args, **kwargs):
        all_videos = TrainingVideo.objects.filter(
            category=self.kwargs.get('category_id'),
            difficulty=self.kwargs.get('difficulty')
        )
        if not all_videos:
             return HttpResponseNotFound()
        random_video = choice(all_videos)
        serialzed_videos = TrainingVideoSerializer(random_video, many=False)
        return Response(serialzed_videos.data)


class CategoryView(APIView):
    def get(self, *args, **kwargs):
        all_categories = Category.objects.all()
        serialzed_category = CategorySerializer(all_categories, many=True)
        return Response(serialzed_category.data)


class DifficultyView(APIView):
    """Уровни сложности."""
    def get(self, *args, **kwargs):
        # Построение словаря из DIFFICULTY_CHOICES для дальнейшей сериализации
        difficulty_data = [
            {'key': key, 'name': name} for (key, name) in DIFFICULTY_CHOICES
        ]
        serialized_difficulty = DifficultySerializer(difficulty_data, many=True)
        return Response(serialized_difficulty.data)
