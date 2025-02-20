"""
FastAPI router for handling OUTPUT_BROWSER requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_browser










router = APIRouter()


@router.post('/browser', status_code=status.HTTP_201_CREATED)
def handle_request_browser(post: PortfoliofyRequest) -> Response:
    """
    Handles requests for OUTPUT_BROWSER. Delegates processing to 
    process_request_browser().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_browser = post.model_dump()

    if request_output_browser['request'] == 1:

        result = process_request_browser(request_output_browser)

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)
