"""
FastAPI router for handling OUTPUT_MAIN requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.core.utils import get_mime
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_main










router = APIRouter()


@router.post('/main', status_code=status.HTTP_201_CREATED)
def handle_request_main(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_MAIN. 
    
    Delegates processing to process_request_main().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: Image response in requested format if request is valid,
            NO_CONTENT response otherwise
    """
    request_output_main = post.model_dump()

    mime_type = get_mime(request_output_main['format'])

    if request_output_main["request"] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_main(request_output_main)

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
