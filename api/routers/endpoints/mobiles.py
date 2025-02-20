"""
TD
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.domain.schemas import PortfoliofyRequest
from api.domain.services import process_request_mobiles










router = APIRouter()


@router.post("/mobiles", status_code=status.HTTP_201_CREATED)
def create_output_mobiles(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_mobiles = post.model_dump()

    if request_output_mobiles["request"] == 1:

        result = process_request_mobiles(request_output_mobiles)

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
