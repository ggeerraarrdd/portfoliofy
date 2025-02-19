"""
TD
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status
from fastapi.responses import FileResponse

# Local
from api.domain.schemas import PortfoliofyRequest
from api.domain.services import process_request_main










router = APIRouter()


@router.post("/main", status_code=status.HTTP_201_CREATED)
def create_output_main(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_main = post.model_dump()

    if request_output_main["request"] == 1:

        result = process_request_main(request_output_main)

        return FileResponse(f"{result}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
