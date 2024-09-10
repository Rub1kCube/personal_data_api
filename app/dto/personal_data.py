from pydantic import BaseModel, ConfigDict, field_validator, Field

import re


class PhoneNumber(BaseModel):
    phone_number: str = Field(default_factory=str, max_length=13)

    @field_validator("phone_number", mode="before")
    @classmethod
    def validate_phone_number(cls, value: str):
        regex = re.compile(r"^(8|\+7)[0-9]{10}$")
        if regex.search(value):
            return value if not value.startswith("+7") else value.replace("+7", "8")
        raise ValueError("Incorrect phone number")


class Address(BaseModel):
    address: str


class CheckPersonalDataDTO(PhoneNumber):
    model_config = ConfigDict(frozen=True)


class ResponseUpdatePersonalDataDTO(Address):
    model_config = ConfigDict(from_attributes=True)


class ResponseCreatePersonalDataDTO(PhoneNumber, Address):
    model_config = ConfigDict(from_attributes=True)


class CheckPersonalDataResponse(Address):
    ...


class CreatePersonalDataDTO(PhoneNumber, Address):
    ...


class UpdatePersonalDataDTO(PhoneNumber, Address):
    ...
