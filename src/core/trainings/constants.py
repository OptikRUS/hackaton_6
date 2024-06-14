from enum import Enum


class TrainingType(str, Enum):
    STRENGTH = "strength"
    TRAINER = "cardio"
    FUNCTIONAL = "functional"
    DANCE = "dance"
    YOGA = "yoga"
    PILATES = "pilates"


class IntensityType(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
