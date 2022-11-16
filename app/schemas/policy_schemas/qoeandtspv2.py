# generated by datamodel-codegen:
#   filename:  policy_schema_qoe_and_tsp.json
#   timestamp: 2022-11-16T03:56:32+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field, conint, constr


class QoeObjectives(BaseModel):
    class Config:
        extra = Extra.forbid

    qoeScore: Optional[float] = None
    initialBuffering: Optional[float] = None
    reBuffFreq: Optional[float] = None
    stallRatio: Optional[float] = None


class UeId(BaseModel):
    __root__: constr(regex=r"^[A-Fa-f0-9]{16}$")


class QosIdItem(BaseModel):
    class Config:
        extra = Extra.forbid

    field_5qI: conint(ge=1, le=256) = Field(..., alias="5qI")


class QosIdItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    qcI: conint(ge=1, le=256)


class QosId(BaseModel):
    __root__: Union[QosIdItem, QosIdItem1]


class NcI(BaseModel):
    __root__: conint(ge=0, le=68719476735)


class EcI(BaseModel):
    __root__: conint(ge=0, le=268435455)


class PlmnId(BaseModel):
    class Config:
        extra = Extra.forbid

    mcc: constr(regex=r"^[0-9]{3}$")
    mnc: constr(regex=r"^[0-9]{2,3}$")


class PreferenceType(Enum):
    SHALL = "SHALL"
    PREFER = "PREFER"
    AVOID = "AVOID"
    FORBID = "FORBID"


class SliceId(BaseModel):
    class Config:
        extra = Extra.forbid

    sst: conint(ge=0, le=255)
    sd: Optional[constr(regex=r"^[A-Fa-f0-9]{6}$")] = None
    plmnId: PlmnId


class CIdItem(BaseModel):
    class Config:
        extra = Extra.forbid

    ncI: NcI


class CIdItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    ecI: EcI


class CId(BaseModel):
    __root__: Union[CIdItem, CIdItem1]


class CellId(BaseModel):
    class Config:
        extra = Extra.forbid

    plmnId: PlmnId
    cId: CId


class CellIdList(BaseModel):
    __root__: List[CellId]


class TspResource(BaseModel):
    class Config:
        extra = Extra.forbid

    cellIdList: CellIdList
    preference: PreferenceType
    primary: Optional[bool] = None


class ScopeItem(BaseModel):
    class Config:
        extra = Extra.forbid

    ueId: UeId
    sliceId: SliceId
    qosId: Optional[QosId] = None
    cellId: Optional[CellId] = None


class ScopeItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    ueId: UeId
    qosId: QosId
    cellId: Optional[CellId] = None


class ScopeItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    sliceId: SliceId
    qosId: Optional[QosId] = None
    cellId: Optional[CellId] = None


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    scope: Union[ScopeItem, ScopeItem1, ScopeItem2]
    qoeObjectives: QoeObjectives
    tspResources: List[TspResource] = Field(..., min_items=1)
