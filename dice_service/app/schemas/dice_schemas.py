from pydantic import BaseModel


class DiceRollResponse(BaseModel):
    roll_result: int


class DiceRollModRequest(BaseModel):
    mod: int | None = 0
    roll_count: int | None = 1


class DiceRollModResponse(BaseModel):
    roll_result: int
