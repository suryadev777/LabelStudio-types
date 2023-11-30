from typing import List
from pydantic import BaseModel

class ImageAttributes(BaseModel):
    original_width: int
    original_height: int
    image_rotation: int

class BrushValue(BaseModel):
    format: str
    rle: List[int]
    brushlabels: List[str]

class BrushResult(ImageAttributes):
    value: BrushValue

class RectangleLabelValue(BaseModel):
    x: float
    y: float
    width: int
    height: int
    rectanglelabels: List[str]

class RectangleLabelResult(ImageAttributes):
    value: RectangleLabelValue

class PolygonLabelValue(BaseModel):
    points: List[Tuple[float, float]]
    polygonlabels: List[str]

class PolygonLabelResult(ImageAttributes):
    value: PolygonLabelValue

class KeypointLabelValue(BaseModel):
    x: float
    y: float
    width: int
    keypointlabels: List[str]

class KeypointLabelResult(ImageAttributes):
    value: KeypointLabelValue

class EllipseLabelValue(BaseModel):
    x: float
    y: float
    radiusX: int
    radiusY: int
    ellipselabels: List[str]

class EllipseLabelResult(ImageAttributes):
    value: EllipseLabelValue