"""
FastAPI router for handling OUTPUT_MOVIE requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status
from fastapi.responses import FileResponse

# Local
from api.core.utils import get_mime
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_movie










router = APIRouter()


@router.post('/movie', status_code=status.HTTP_201_CREATED)
def handle_request_movie(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_MOVIE. 
    
    Delegates processing to process_request_movie().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: MP4 video response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_movie = post.model_dump()

    mime_type = get_mime(request_output_movie['format'])

    if request_output_movie['request'] == 1:

        if mime_type in ['movie/mp4']:

            result = process_request_movie(request_output_movie)

            if result == 0:
                Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                return FileResponse(f'{result}', media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
