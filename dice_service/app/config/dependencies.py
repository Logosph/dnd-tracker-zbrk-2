from dice_service.app.services.dice_service import DiceService
from app.schemas.dice_schemas import DiceRoll

def get_dice_service() -> DiceService:
    return DiceService()
