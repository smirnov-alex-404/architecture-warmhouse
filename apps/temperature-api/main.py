from datetime import datetime, UTC
from random import randint

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

LOCATION_TO_ID = {
    "Living Room": "1",
	"Bedroom": "2",
	"Kitchen": "3",
}

class TemperatureResponse(BaseModel):
    sensor_id: str
    value: float
    location: str
    timestamp: datetime
    unit: str
    description: str
    unit: str = 'C'
    status: str = 'active'
    sensor_type: str = 'temp'


router = APIRouter()

@router.get(
    '/temperature'
)
def get_temperature(
    location: str = ''
) -> TemperatureResponse:
    sensor_id = LOCATION_TO_ID.get(location, '0')
    return TemperatureResponse(
        value=randint(15,40),
        timestamp=datetime.now(UTC),
        location=location,
        status='active',
        sensor_id=sensor_id,
        description='description',
        unit='C',
        sensor_type='temp',
    )


@router.get(
    '/temperature/{sensor_id}'
)
def get_temperature(
    sensor_id: str,
) -> TemperatureResponse:
    return TemperatureResponse(
        value=randint(15,40),
        timestamp=datetime.now(UTC),
        location='',
        status='active',
        sensor_id=sensor_id,
        description='description',
        unit='C',
        sensor_type='temp',
    )


app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8081,

    )
