"""
TD
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status
from fastapi.responses import FileResponse

# Local
from api.domain.schemas import PortfoliofyRequest
from api.domain.services import process_request_browser










router = APIRouter()


@router.post("/browser", status_code=status.HTTP_201_CREATED)
def create_output_browser(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_browser = post.model_dump()

    if request_output_browser["request"] == 1:

        result = process_request_browser(request_output_browser)

        return FileResponse(f"{result}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
