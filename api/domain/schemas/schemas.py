"""
Pydantic model for validating and processing Portfoliofy screenshot requests.
"""

from pydantic import BaseModel, HttpUrl, constr, conint, Field










class PortfoliofyRequest(BaseModel):
    """
    This model defines the structure and validation rules for screenshot request parameters,
    including URL, timing, formatting, and styling options. It uses Pydantic's Field class
    for detailed validation and documentation.

    Attributes:
        request (bool): Flag to indicate if this is a request. Defaults to False.
        remote_url (HttpUrl): Valid URL to capture. Must be accessible.
            Default: "https://ggeerraarrdd.github.io/"
        wait (int): Seconds to wait for page load before capture. Range: 1-100.
            Default: 2
        format (str): Output image format. Supports png, jpeg, bmp, tiff, mp4.
            Default: "png"
        doc_pad_h (int): Horizontal padding in pixels. Range: 1-1000.
            Default: 300
        doc_pad_v (int): Vertical padding in pixels. Range: 1-1000.
            Default: 200
        doc_fill_color (str): Document background color in hex format (#RGB or #RRGGBB).
            Default: "#ffffff"
        base_stroke_color (str): Base stroke color in hex format (#RGB or #RRGGBB).
            Default: "#23445d"
        base_fill_color (str): Base fill color in hex format (#RGB or #RRGGBB).
            Default: "#bac8d3"

    Example:
        ```python
        request = PortfoliofyRequest(
            request=True,
            remote_url="https://example.com",
            wait=5,
            format="png",
            doc_pad_h=400,
            doc_pad_v=200,
            doc_fill_color="#ffffff",
            base_stroke_color="#23445d",
            base_fill_color="#bac8d3"
        )
        ```
    """
    request: bool = Field(False, description='Request flag')
    remote_url: HttpUrl = Field("https://ggeerraarrdd.github.io/", description="Valid and accessible URL")
    wait: conint(gt=0, lt=101) = Field(2, description="Wait time for screenshot") # type: ignore[reportInvalidTypeForm]
    format: str = Field("png", pattern="^(png|jpe?g|bmp|tiff|pdf|mp4)$", description="Output file format")
    doc_pad_h: conint(gt=0, lt=1001) = Field(300, description="Padding value for horizontal dimension") # type: ignore[reportInvalidTypeForm]
    doc_pad_v: conint(gt=0, lt=1001) = Field(200, description="Padding value for vertical dimension") # type: ignore[reportInvalidTypeForm]
    doc_fill_color: constr(pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#ffffff", description="RGB hexadecimal value") # type: ignore[reportInvalidTypeForm]
    base_stroke_color: constr(pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#23445d", description="RGB hexadecimal value") # type: ignore[reportInvalidTypeForm]
    base_fill_color: constr(pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#bac8d3", description="RGB hexadecimal value") # type: ignore[reportInvalidTypeForm]
