"""
FastAPI router for handling OUTPUT_MAIN requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_main










router = APIRouter()


@router.post('/main', status_code=status.HTTP_201_CREATED)
def handle_request_main(post: PortfoliofyRequest) -> Response:
    """
    Handles requests for OUTPUT_MAIN. Delegates processing to 
    process_request_main().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_main = post.model_dump()

    if request_output_main["request"] == 1:

        result = process_request_main(request_output_main)

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
