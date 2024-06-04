from src.config.settings import settings

DATABASE_SETTINGS = {
    "connections": {"default": settings.DATABASE.URL.get_secret_value()},
    "apps": {
        "models": {
            "models": [
                "src.core.users.models",
                "src.core.trainings.models",
                "src.core.chats.models",
                "src.core.media.models",
            ],
        },
    },
}
