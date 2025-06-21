from fastapi import APIRouter, Response, status
from fixtures import categories as fixture_categories
from schema.category import Category

router = APIRouter(prefix="/category", tags=["categories"])

@router.get(
    "/all",
    response_model=list[Category],
    status_code=status.HTTP_200_OK)
async def get_categories():
    return fixture_categories

@router.post(
    "/",
    response_model=Category,
    status_code=status.HTTP_201_CREATED)
async def create_category(category: Category):
    fixture_categories.append(category)
    return category

@router.patch(
    "/{category_id}",
    response_model=Category)
async def patch_category(category_id: int, name: str):
    for category in fixture_categories:
        if category["id"] == category_id:
            category["name"] = name
            return category

@router.delete("/{category_id}", status_code=status.HTTP_200_OK)
async def delete_category(category_id: int, response: Response):
    for index, category in enumerate(fixture_categories):
        if category["id"] == category_id:
            del fixture_categories[index]
            return {"message": f"Category {category_id} was deleted"}

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Object is not found"}
