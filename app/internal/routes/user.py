from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.internal import services
from app.pkg import models

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/",
    response_model=models.User,
    status_code=status.HTTP_201_CREATED,
    summary="Create user.",
)
@inject
async def create_user(
    cmd: models.CreateUserCommand,
    user_service: services.User = Depends(Provide[services.Services.user]),
):
    return await user_service.create_user(cmd=cmd)


@router.get(
    "/",
    response_model=List[models.User],
    status_code=status.HTTP_200_OK,
    summary="Get all users.",
)
@inject
async def read_all_users(
    user_service: services.User = Depends(Provide[services.Services.user]),
):
    return await user_service.read_all_users()


@router.get(
    "/{user_id:int}",
    response_model=models.User,
    status_code=status.HTTP_200_OK,
    summary="Read specific user.",
)
@inject
async def read_user(
    user_id: int = models.UserFields.id,
    user_service: services.User = Depends(Provide[services.Services.user]),
):
    return await user_service.read_specific_user_by_id(
        query=models.ReadUserByIdQuery(id=user_id),
    )


@router.delete(
    "/{user_id:int}",
    response_model=models.User,
    status_code=status.HTTP_200_OK,
    summary="Delete specific user.",
)
@inject
async def delete_user(
    user_id: int = models.UserFields.id,
    user_service: services.User = Depends(Provide[services.Services.user]),
):
    return await user_service.delete_specific_user(
        cmd=models.DeleteUserSpecificCommand(id=user_id),
    )
