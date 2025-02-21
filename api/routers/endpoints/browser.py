"""
FastAPI router for handling OUTPUT_BROWSER requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.core.utils import get_mime
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_browser










router = APIRouter()


@router.post('/browser', status_code=status.HTTP_201_CREATED)
def handle_request_browser(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_BROWSER. 
    
    Delegates processing to process_request_browser().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: Image data in requested format if request is valid,
            NO_CONTENT response otherwise
    """
    request_output_browser = post.model_dump()

    mime_type = get_mime(request_output_browser['format'])

    if request_output_browser['request'] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_browser(request_output_browser)

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
