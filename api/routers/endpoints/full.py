"""
FastAPI router for handling OUTPUT_FULL requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
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
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_full = post.model_dump()

    if request_output_full['request'] == 1:

        result = process_request_full(request_output_full)

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)
