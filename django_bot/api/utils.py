from datetime import datetime, timedelta, timezone

# from django.utils import timezone

from base.configurations import (
    PERCENTAGE_WEIGHT_ADDITION,
    PERCENTAGE_WEIGHT_LOSS,
    TrainingMode,
)


def toFixed(numObj: float, digits: int = 0) -> str:
    """Ограничиваем вывод для FLOAT."""
    return f"{numObj:.{digits}f}"


def percentage_weight(coficent: float, percent: int) -> float:
    """Вычисляет процент от веса."""
    return (coficent / 100)*percent


def calculation_n_days_ago(number_days: int) -> datetime:
    """Расчитываем день с которого начинает диапазон поиска тренировок."""
    return datetime.now(tz=timezone.utc) - timedelta(days=number_days)


def calorie_calculation(
        weight: float,
        height: float,
        age: int,
        human_indicators: dict,
        activity_coefficient: dict,
        training_mode: str,
) -> float:
    """Расчёт норма калорий для (мужчин, женщин)."""
    result = (human_indicators[0] +
              (human_indicators[1] * weight) +
              (human_indicators[2] * height) -
              (human_indicators[3] * age))
    result *= activity_coefficient
    if training_mode == TrainingMode.WEIGHT_GAIN.value:
        result += percentage_weight(result, PERCENTAGE_WEIGHT_ADDITION)
    if training_mode == TrainingMode.RESET.value:
        result -= percentage_weight(result, PERCENTAGE_WEIGHT_LOSS)
    return result
