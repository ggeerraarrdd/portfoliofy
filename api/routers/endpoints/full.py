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

    Request Body:
        post (PortfoliofyRequest): Request containing URL and output parameters
            - Validated via Pydantic PortfoliofyRequest model
            - See schemas.py for detailed field specifications

    Returns:
        Response (201):
            - content: Image data in requested format
            - media_type: Corresponding MIME type
        Response (204):
            - Empty response if request is invalid or format is movie/mp4 or application/pdf

    Notes:
        - Delegates processing to process_request_full()
        - Only processes requests where request is True and format not movie/mp4 or application/pdf
    """
    request_output_full = post.model_dump()

    mime_type = get_mime(request_output_full['format'])

    if request_output_full['request'] == 1:

        if mime_type not in ['movie/mp4', 'application/pdf']:

            result = process_request_full(request_output_full)

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
