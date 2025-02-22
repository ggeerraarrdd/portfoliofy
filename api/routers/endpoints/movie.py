"""
FastAPI router for handling OUTPUT_MOVIE requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status
from fastapi.responses import FileResponse

# Local
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_movie










router = APIRouter()


@router.post('/movie', status_code=status.HTTP_201_CREATED)
def handle_request_movie(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_MOVIE.

    Request Body:
        post (PortfoliofyRequest): Request containing URL and output parameters
            - Validated via Pydantic PortfoliofyRequest model
            - See schemas.py for detailed field specifications

    Returns:
        Response (201):
            - content: Video data in MP4 format
            - media_type: video/mp4
        Response (204):
            - Empty response if request is invalid or screenshot height exceeds maximum

    Notes:
        - Delegates processing to process_request_movie()
        - Only processes requests where request is True
        - Ignores format parameter and always returns MP4
    """
    request_output_movie = post.model_dump()

    if request_output_movie['request'] == 1:

        result = process_request_movie(request_output_movie)

        if result == 0:
            Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return FileResponse(f'{result}', media_type='movie/mp4')

    return Response(status_code=status.HTTP_204_NO_CONTENT)
