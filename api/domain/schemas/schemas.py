"""
TD
"""

from pydantic import BaseModel, HttpUrl, constr, conint, Field










class PortfoliofyRequest(BaseModel):
    """
    TD
    """
    request: bool = Field(False, description='Request flag')
    remote_url: HttpUrl = Field("https://ggeerraarrdd.github.io/", description="Valid and accessible URL")
    wait: conint(gt=0, lt=101) = Field(2, description="Wait time for screenshot") # type: ignore[reportInvalidTypeForm]
    format: str = Field("png", pattern="^(png)$", description="Output file format")
    doc_pad_h: conint(gt=0, lt=1001) = Field(300, description="Padding value for horizontal dimension") # type: ignore[reportInvalidTypeForm]
    doc_pad_v: conint(gt=0, lt=1001) = Field(200, description="Padding value for vertical dimension") # type: ignore[reportInvalidTypeForm]
    doc_fill_color: constr(pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#ffffff", description="RGB hexadecimal value") # type: ignore[reportInvalidTypeForm]
    base_stroke_color: constr(pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#23445d", description="RGB hexadecimal value") # type: ignore[reportInvalidTypeForm]
    base_fill_color: constr(pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#bac8d3", description="RGB hexadecimal value") # type: ignore[reportInvalidTypeForm]
