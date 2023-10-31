from fastapi import APIRouter,Body,status, HTTPException
from contracts.car import CarInDB, UpdateCarInDB, CarModel
from fastapi.encoders import jsonable_encoder
from db import db
from fastapi.responses import JSONResponse
from typing import Optional, List
from bson import ObjectId

router = APIRouter()
