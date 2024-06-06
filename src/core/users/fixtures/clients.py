from random import choice

from faker import Faker

from src.common.auth.constants import UserRoles
from src.core.users.constants import GenderType
from src.core.users.models import User
from src.core.users.utils.password import generate_password_hash


def gen_persons(count: int) -> list:
    make_mock = Faker("ru_RU")
    return [
        choice(  # noqa: S311
            [
                (make_mock.name_male(), GenderType.MALE.value),
                (make_mock.name_female(), GenderType.FEMALE.value),
            ]
        )
        for _ in range(count)
    ]


async def fill_clients(count: int) -> None:
    await User.filter(role=UserRoles.CLIENT.value).delete()
    make_mock = Faker("ru_RU")
    persons = gen_persons(count=count)
    for person in persons:
        full_name = person[0]
        gender = person[1]
        surname, name, patronymic, *_ = full_name.split()
        await User.update_or_create(
            email=make_mock.email(),
            password=generate_password_hash(make_mock.password()),
            phone="",
            name=name,
            surname=surname,
            patronymic=patronymic,
            gender=gender,
            role=UserRoles.CLIENT.value,
            age=make_mock.pyint(min_value=18, max_value=50),
            weight=make_mock.pyfloat(min_value=40, max_value=120, right_digits=1),
            height=make_mock.pyfloat(min_value=160, max_value=180, right_digits=1),
            rate=make_mock.pyfloat(min_value=3, max_value=5, right_digits=1),
            description=make_mock.text(),
        )


async def fill_trainers(count: int) -> None:
    await User.filter(role=UserRoles.TRAINER.value).delete()
    make_mock = Faker("ru_RU")
    persons = gen_persons(count=count)
    for person in persons:
        full_name = person[0]
        gender = person[1]
        surname, name, patronymic, *_ = full_name.split()
        await User.update_or_create(
            email=make_mock.email(),
            password=generate_password_hash(make_mock.password()),
            phone="",
            name=name,
            surname=surname,
            patronymic=patronymic,
            gender=gender,
            role=UserRoles.TRAINER.value,
            age=make_mock.pyint(min_value=18, max_value=50),
            weight=make_mock.pyfloat(min_value=40, max_value=120, right_digits=1),
            height=make_mock.pyfloat(min_value=160, max_value=180, right_digits=1),
            rate=make_mock.pyfloat(min_value=3, max_value=5, right_digits=1),
            description=make_mock.text(),
        )
