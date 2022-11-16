from pydantic import BaseModel, Field


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
    sliceId: SliceID
    ueId: str


class QoeObjectives(BaseModel):
    initialBuffering: float
    qoeScore: float
    reBuffFreq: float
    stallRatio: float


class API(BaseModel):
    qoeObjectives: QoeObjectives
    scope: Scope


def marshalAPI(api: API):
    json_data = api.json(by_alias=True, exclude_none=True)
    return json_data
