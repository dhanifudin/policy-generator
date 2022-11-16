from typing import List
from pydantic import BaseModel


class PlmnID(BaseModel):
    mcc: str
    mnc: str


class SliceID(BaseModel):
    plmnId: PlmnID
    sd: str
    sst: int


class TaI(BaseModel):
    plmnId: PlmnID
    tac: str


class CID(BaseModel):
    ncI: int
    ecI: int


class CellID(BaseModel):
    cId: CID
    plmnId: PlmnID


class SliceSlaResources(BaseModel):
    cellIdList: List[CellID]
    taIList: List[TaI]


class SliceSlaObjectives(BaseModel):
    guaDlThptPerSlice: float
    guaUlThptPerSlice: float
    maxDlThptPerSlice: float
    maxDlThptPerUe: float
    maxNumberOfPdusessons: float
    maxNumberOfUes: float
    maxUlThptPerSlice: float
    maxUlThptPerUe: float


class Scope(BaseModel):
    sliceId: SliceID


class API(BaseModel):
    scope: Scope
    sliceSlaObjectives: SliceSlaObjectives
    sliceSlaResources: SliceSlaResources


def marshalAPI(api: API):
    json_data = api.json(by_alias=True, exclude_none=True)
    return json_data
