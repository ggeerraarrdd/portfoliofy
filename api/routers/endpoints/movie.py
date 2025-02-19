"""
TD
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status
from fastapi.responses import FileResponse

# Local
from api.domain.schemas import PortfoliofyRequest
from api.domain.services import process_request_movie










router = APIRouter()


@router.post("/movie", status_code=status.HTTP_201_CREATED)
def create_output_movie(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_movie = post.model_dump()

    if request_output_movie["request"] == 1:

        result = process_request_movie(request_output_movie)

        if result == 0:
            Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return FileResponse(f"{result}")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
