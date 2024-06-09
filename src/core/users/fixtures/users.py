from random import choice

from faker import Faker

from src.common.auth.constants import UserRoles
from src.core.users.constants import GenderType
from src.core.users.models import User
from src.core.users.utils.password import generate_password_hash

make_mock = Faker("ru_RU")


def gen_persons(count: int) -> list:
    return [
        choice(  # noqa: S311
            [
                (
                    (
                        make_mock.middle_name_male(),
                        make_mock.last_name_male(),
                        make_mock.middle_name_male(),
                    ),
                    GenderType.MALE.value,
                ),
                (
                    (
                        make_mock.first_name_female(),
                        make_mock.last_name_female(),
                        make_mock.middle_name_female(),
                    ),
                    GenderType.FEMALE.value,
                ),
            ]
        )
        for _ in range(count)
    ]


async def create_users(persons: list, role: str) -> None:
    await User.filter(role=role).delete()
    for person in persons:
        full_name = person[0]
        gender = person[1]
        name, surname, patronymic = full_name
        await User.update_or_create(
            email=make_mock.email(),
            password=generate_password_hash(make_mock.password()),
            phone="",
            name=name,
            surname=surname,
            patronymic=patronymic,
            gender=gender,
            role=role,
            age=make_mock.pyint(min_value=18, max_value=50),
            weight=make_mock.pyfloat(min_value=40, max_value=120, right_digits=1),
            height=make_mock.pyfloat(min_value=160, max_value=180, right_digits=1),
            rate=make_mock.pyfloat(min_value=3, max_value=5, right_digits=1),
            description=make_mock.text(),
        )


async def fill_clients(count: int) -> None:
    role = UserRoles.CLIENT.value
    persons = gen_persons(count=count)
    await create_users(persons=persons, role=role)
    await User.create(
        email="client@example.com",
        password=generate_password_hash("password123"),
        role=role,
        phone="",
        name="Клиент",
        surname="Клинтов",
        patronymic="Клиентович",
        gender=GenderType.MALE.value,
        age=20,
        weight=90.0,
        height=175.0,
        rate=5.0,
        description="Люблю спорт",
    )


async def fill_trainers(count: int) -> None:
    role = UserRoles.TRAINER.value
    persons = gen_persons(count=count)
    await create_users(persons=persons, role=role)
    await User.create(
        email="trainer@example.com",
        password=generate_password_hash("password123"),
        role=role,
        phone="",
        name="Тренер",
        surname="Тренеров",
        patronymic="Тренерович",
        gender=GenderType.MALE.value,
        age=30,
        weight=95.0,
        height=180.0,
        rate=5.0,
        description="Люблю тренировать людей",
    )
