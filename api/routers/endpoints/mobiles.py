"""
FastAPI router for handling OUTPUT_MOBILES requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.core.utils import get_mime
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_mobiles










router = APIRouter()


@router.post('/mobiles', status_code=status.HTTP_201_CREATED)
def handle_request_mobiles(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_MOBILES.

    Request Body:
        post (PortfoliofyRequest): Request containing URL and output parameters
            - Validated via Pydantic PortfoliofyRequest model
            - See schemas.py for detailed field specifications

    Returns:
        Response (201):
            - content: Image data in requested format
            - media_type: Corresponding MIME type
        Response (204):
            - Empty response if request is invalid or format is movie/mp4

    Notes:
        - Delegates processing to process_request_mobiles()
        - Only processes requests where request is True and format not movie/mp4
    """
    request_output_mobiles = post.model_dump()

    mime_type = get_mime(request_output_mobiles['format'])

    if request_output_mobiles['request'] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_mobiles(request_output_mobiles)

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
