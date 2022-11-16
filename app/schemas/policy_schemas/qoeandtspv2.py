from enum import Enum
from pydantic import BaseModel, Field
from typing import List


class PreferenceType(str, Enum):
    AVOID = "AVOID"
    FORBID = "FORBID"
    PREFER = "PREFER"
    SHALL = "SHALL"


class PlmnID(BaseModel):
    mcc: str
    mnc: str


class SliceID(BaseModel):
    plmnId: PlmnID
    sd: str
    sst: int


class QosID(BaseModel):
    the5qI: int = Field(alias="5qi")
    qcI: int


class CID(BaseModel):
    ncI: int
    ecI: int


class CellID(BaseModel):
    cId: CID
    plmnId: PlmnID


class Scope(BaseModel):
    cellId: CellID
    qosId: QosID
    ueId: str
    sliceId: SliceID


class QoeObjectives(BaseModel):
    initialBuffering: float
    qoeScore: float
    reBuffFreq: float
    stallRatio: float


class TSPResource(BaseModel):
    cellIdList: List[CellID]
    preference: PreferenceType
    primary: bool


class API(BaseModel):
    qoeObjectives: QoeObjectives
    scope: Scope
    tspResources: List[TSPResource]


def marshalAPI(api: API):
    json_data = api.json(by_alias=True, exclude_none=True)
    return json_data
