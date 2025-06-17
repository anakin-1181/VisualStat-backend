from pydantic import BaseModel, Field
from typing import Literal, Union

# Validate user input before generating plots

class UniformParams(BaseModel):
    distribution: Literal["uniform"]
    size: int = Field(default=10000, gt=0, le=100000)
    show_mean: bool = True
    show_sd: bool = True
    
    low: float = 0
    high: float = 1
    
class BinomialParams(BaseModel):
    distribution: Literal["binomial"]
    size: int = Field(default=10000, gt=0, le=100000)
    show_mean: bool = True
    
    n: int = Field(default=10, gt=0)
    p: float = Field(default=0.5, ge=0,le=1)

Plotparams = Union[UniformParams, BinomialParams]