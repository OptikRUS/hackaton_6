from random import choice

from faker import Faker

from src.common.auth.constants import UserRoles
from src.core.users.constants import GenderType
from src.core.users.models import User
from src.core.users.utils.password import generate_password_hash

make_mock = Faker("ru_RU")

CLIENT_MALE_URLS = [
    "https://icieducation.co.uk/blog/wp-content/uploads/2021/12/Fitness-1.jpg",
    "https://educatefitness.co.uk/wp-content/uploads/2023/05/Client-Consultation-Techniques-A-Comprehensive-Guide-for-Fitness-Professionals.jpg",
    "https://media.gettyimages.com/id/1411440889/photo/coach-planning-sports-training-with-his-client.jpg?s=612x612&w=gi&k=20&c=72e7Ef4CzSNIiH3jSwboiUnW7vqF56mi1jjx3-p1nBo=",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHbY9C5y19FG9bogKSSwHhNW27CwudTpeTvg&s",
    "https://www.mypthub.net/wp-content/uploads/my-pt-hub-blog-photos-1920-x-1080-px-1-1-1024x576.png",
]

CLIENT_FEMALE_URLS = [
    "https://img.freepik.com/premium-photo/picture-personal-fitness-trainer-female-client-gym-posing-front-camera-healthy-life-fitness-concept_116317-21224.jpg",
    "https://img.freepik.com/premium-photo/trainer-client-discussing-her-progress-gym-exercise-personal-fitness-instructor_116317-2698.jpg",
    "https://www.constantcontact.com/blog/wp-content/uploads/2021/01/Blog-header-1-14.jpg",
    "https://t4.ftcdn.net/jpg/01/71/18/77/360_F_171187710_fXMH2FGiy9rbC7EGoFXXbmETqtRpFgul.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgPLjf_lK6bceNKXTWDmYf1_50gfUBXwP20EqoST8kLw0O1jz7I43PA8b97XkCW9Px41Q&usqp=CAU",
]

TRAINER_MALE_URLS = [
    "https://www.shutterstock.com/image-photo/personal-trainer-arms-crossed-gym-260nw-493318507.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGJFNNuX1dfV3xTzOEo1tfY5nS2oXw4__9Ym8ohGx3zxlEcdMOs2gTQmvvFWc4ge85ZkQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxFZVO_fg5sLJA_jgDzIz_3JzlshPXktSpVWFKDPJY0tuDCaHbDy2Q1BgpRepcCp0rV7c&usqp=CAU",
    "https://media.gettyimages.com/id/1072395722/photo/fitness-trainer-at-gym.jpg?s=612x612&w=gi&k=20&c=E0xrov7O0JaS1T3i2d5_HX6BdWNECBTeQqHjkYEgVlk=",
    "https://media.istockphoto.com/id/1345133813/photo/portrait-of-young-fitness-instructor-in-gym.jpg?s=612x612&w=is&k=20&c=96nDISVtrVpw5OojTwqgg8tHDBPMBQ9NK0n8wK9mJtM=",
]

TRAINER_FEMALE_URLS = [
    "https://www.shutterstock.com/image-photo/portrait-female-personal-trainer-holding-260nw-2249557387.jpg",
    "https://img.freepik.com/premium-photo/young-female-fitness-personal-trainer-with-notepad-standing-gym-with-thumb-up_146671-31563.jpg",
    "https://slidesbase.com/wp-content/uploads/2023/07/02-portrait-of-female-personal-gym-trainer-stock-photo_slidesbase-1.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQk7zisFvseK1Ti4GapBmUzipr4-u24zd_kRUPC0u6PK0-zPbwJX4Xc3ly6QKxiWI1gnSk&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3zIj6X7HnFqwnZpCnINM_o6rwPY87aArhDFX_IzmMsQV15obwEV8cmqCMhXbhP90oiEA&usqp=CAU",
    "https://educatefitness.co.uk/wp-content/uploads/2023/05/Conducting-a-Fitness-Consultation-Step-by-Step-Guide.jpg",
]


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
        ava_path = ""
        if role == UserRoles.TRAINER.value and gender == GenderType.MALE.value:
            ava_path = choice(TRAINER_MALE_URLS)
        if role == UserRoles.CLIENT.value and gender == GenderType.MALE.value:
            ava_path = choice(CLIENT_MALE_URLS)
        if role == UserRoles.TRAINER.value and gender == GenderType.FEMALE.value:
            ava_path = choice(TRAINER_FEMALE_URLS)
        if role == UserRoles.CLIENT.value and gender == GenderType.FEMALE.value:
            ava_path = choice(CLIENT_FEMALE_URLS)
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
            avatar_path=ava_path,
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
        avatar_path=choice(CLIENT_MALE_URLS),
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
        avatar_path=choice(TRAINER_MALE_URLS),
    )
