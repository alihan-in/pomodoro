import faker

from pydantic import BaseModel, Field, model_validator


class TaskSchema(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int

    class Config:
        from_attributes = True

    @model_validator(mode="after")
    def check_name_or_pomodoro_count_is_not_none(self):
        if self.name is None and self.pomodoro_count is not None:
            self.name = faker.Faker().name()
            return self

        elif self.name is None and self.pomodoro_count is None:
            raise ValueError("name or pomodoro count must be provided")
        return self
