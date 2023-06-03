from fastapi import (
    status,
    Query,
    HTTPException,
    APIRouter,
)

from schemas import items as schemas


car_query = Query('base', min_length=3)
router = APIRouter()


@router.get("/{name}/{age}/")
async def index(name: str, age: int, page: int = 1):
    return {
        'name': name,
        'age': age,
        'page': page,
    }


@router.post(
    '/item/',
    response_model=schemas.ItemOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_item(item: schemas.Item, car: str = car_query):
    if item.name == 'admin':
        raise HTTPException(400, "This name is not a valid item name.")
    return dict(item) | {'car': car}
