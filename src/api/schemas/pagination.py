from src.api.schemas.base_schemas import ApiModel


class PaginationInput(ApiModel):
    page: int | None = 1
    size: int | None = 10

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size
