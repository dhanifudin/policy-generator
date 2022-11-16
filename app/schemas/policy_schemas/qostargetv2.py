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


class GroupID(BaseModel):
    spId: int
    rfspIndex: int


class CID(BaseModel):
    ncI: int
    ecI: int


class CellID(BaseModel):
    cId: CID
    plmnId: PlmnID


class Scope(BaseModel):
    cellId: CellID
    groupId: GroupID
    qosId: QosID
    ueId: str
    sliceId: SliceID


class QosObjectives(BaseModel):
    gfbr: float
    mfbr: float
    pdb: float
    priorityLevel: float


class API(BaseModel):
    qosObjectives: QosObjectives
    scope: Scope


def marshalAPI(api: API):
    json_data = api.json(by_alias=True, exclude_none=True)
    return json_data
