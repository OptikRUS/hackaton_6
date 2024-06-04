from enum import Enum


class UserRoles(str, Enum):
    CLIENT = "client"
    TRAINER = "trainer"
