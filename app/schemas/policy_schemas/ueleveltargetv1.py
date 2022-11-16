from pydantic import BaseModel, Field


class PlmnID(BaseModel):
    mcc: str
    mnc: str


class SliceID(BaseModel):
    plmnId: PlmnID
    sd: str
    sst: int


class GroupID(BaseModel):
    spId: int
    rfspIndex: int


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
    groupId: GroupID
    sliceId: SliceID
    ueId: str
    qosId: QosID


class ReliabilityType(BaseModel):
    packetSize: float
    successProbility: float
    userPlaneLatency: float


class UeLevelObjectives(BaseModel):
    dlPacketDelay: float
    dlReliability: ReliabilityType
    dlRlcSduPacketLossRate: float
    dlThroughput: float
    ulPacketDelay: float
    ulPdcpSduPacketLossRate: float
    ulReliability: ReliabilityType
    ulThroughput: float


class API(BaseModel):
    scope: Scope
    ueLevelObjectives: UeLevelObjectives


def marshalAPI(api: API):
    json_data = api.json(by_alias=True, exclude_none=True)
    return json_data
