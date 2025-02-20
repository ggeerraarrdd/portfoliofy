"""
TD
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.domain.schemas import PortfoliofyRequest
from api.domain.services import process_request_full










router = APIRouter()


@router.post("/full", status_code=status.HTTP_201_CREATED)
def create_output_full(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_full = post.model_dump()

    if request_output_full["request"] == 1:

        result = process_request_full(request_output_full)

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
