from fastapi import APIRouter, Depends, HTTPException
from fastapi import status

from config.logger import logger

from dto.personal_data import CheckPersonalDataDTO, CreatePersonalDataDTO, UpdatePersonalDataDTO, \
    CheckPersonalDataResponse, ResponseUpdatePersonalDataDTO, ResponseCreatePersonalDataDTO
from service.crud.personal_data import get_personal_data, create_personal_data, update_personal_data


personal_data_router = APIRouter()


@personal_data_router.get(
    "/check_data",
    description="This endpoint checks for the presence of the transmitted "
                "Russian phone number and, if found, returns the address",
    responses={status.HTTP_404_NOT_FOUND: {"description": ""}},
)
async def check_data(
        personal_data: CheckPersonalDataDTO = Depends(),
) -> CheckPersonalDataResponse:
    result = await get_personal_data(personal_data.phone)
    logger.debug("Endpoint [GET] check_data: [%s, %s]", personal_data.phone, result)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no information for this phone number."
        )

    return CheckPersonalDataResponse(address=result)


@personal_data_router.post(
    "/write_data",
    responses={status.HTTP_201_CREATED: {"description": "Personal data created"}},
    description="This endpoint allows you to create a Russian phone number to address mapping record."
)
async def write_data(
        personal_data: CreatePersonalDataDTO,
) -> ResponseCreatePersonalDataDTO:
    result = await create_personal_data(
        phone_number=personal_data.phone_number,
        address=personal_data.address,
    )
    logger.debug("Endpoint [POST] write_data: [%s, %s]", (personal_data.phone_number, personal_data.address), result)

    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return ResponseCreatePersonalDataDTO.model_validate(personal_data)


@personal_data_router.put(
    "/write_data",
    responses={status.HTTP_200_OK: {"description": "Personal data updated"}},
    description="This endpoint allows you to change the Russian phone number and address mapping record.",
)
async def write_data(
        personal_data: UpdatePersonalDataDTO,
) -> ResponseUpdatePersonalDataDTO:
    result = await update_personal_data(
        phone_number=personal_data.phone_number,
        address=personal_data.address,
    )
    logger.debug("Endpoint [PUT] write_data: [%s, %s]", (personal_data.phone_number, personal_data.address), result)

    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return ResponseUpdatePersonalDataDTO.model_validate(personal_data)
