from src.core.trainings.models import TrainingType


async def fill_training_types() -> None:
    training_types = [
        {
            "title": "Силовая",
            "description": "Силовые тренировки – это один из самых эффективных способов увеличить "
                           "мышечную массу и силу. Силовые тренировки могут включать в себя "
                           "упражнения с гантелями, штангами, каблуками и другими снарядами. Эти "
                           "упражнения направлены на развитие силы и мышечной массы, а также на "
                           "укрепление костей.",
        },
        {
            "title": "Кардио",
            "description": "Кардио-тренировки – это упражнения, которые улучшают "
                           "кардиоваскулярную систему и увеличивают выносливость. "
                           "Кардио-упражнения могут включать в себя бег, езду на велосипеде, "
                           "скакалку и другие упражнения, которые увеличивают пульс и заставляют "
                           "сердце работать более интенсивно.",
        },
        {
            "title": "Функциональная",
            "description": "Функциональные тренировки – это упражнения, которые имитируют "
                           "движения, которые мы делаем в повседневной жизни. Такие тренировки "
                           "направлены на улучшение баланса, координации, гибкости и силы. "
                           "Примерами функциональных тренировок могут быть упражнения с TRX или "
                           "бодибаром.",
        },
        {
            "title": "Танцевальная",
            "description": "Танцевальные тренировки – это отличный способ улучшить координацию и "
                           "выносливость. Танцевальные тренировки могут включать в себя различные "
                           "стили танца, такие как зумба, belly dance и многие другие.",
        },
        {
            "title": "Йога",
            "description": "Йога – это упражнения, которые направлены на улучшение гибкости, "
                           "силы и баланса. Йога также помогает снять стресс и улучшить "
                           "настроение. Йога может включать в себя различные асаны и дыхательные "
                           "упражнения.",
        },
        {
            "title": "Пилатес",
            "description": "Пилатес – это упражнения, которые направлены на улучшение гибкости, "
                           "силы и баланса. Пилатес также помогает улучшить осанку и снять "
                           "напряжение в мышцах. Пилатес может включать в себя упражнения как на "
                           "специальном студийном оборудовании, так и на мяче, резиновых кольцах "
                           "и других специальных приспособлениях.",
        },
    ]
    for training_type in training_types:
        await TrainingType.update_or_create(**training_type)
