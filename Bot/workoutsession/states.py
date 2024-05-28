from aiogram.fsm.state import State, StatesGroup


class WorkoutSessionForm(StatesGroup):
    done = State()
    count_approaches = State()
    count_repetitions = State()
