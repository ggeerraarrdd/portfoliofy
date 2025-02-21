"""
FastAPI router for handling OUTPUT_FULL requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.core.utils import get_mime
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_full










router = APIRouter()


@router.post('/full', status_code=status.HTTP_201_CREATED)
def handle_request_full(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_FULL. 
    
    Delegates processing to process_request_full().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-pvalidated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: Image data in requested format if request is valid,
            NO_CONTENT response otherwise
    """
    request_output_full = post.model_dump()

    mime_type = get_mime(request_output_full['format'])

    if request_output_full['request'] == 1:

        if mime_type not in ['movie/mp4', 'application/pdf']:

            result = process_request_full(request_output_full)

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
