"""
FastAPI router for handling individual device OUTPUT_SCREENSHOTS requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.core.utils import get_mime
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_screenshots










router = APIRouter()


@router.post('/screenshots/desktop', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_desktop(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for plain, viewport-specific screenshots at desktop resolution (2160x1360)

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
        - Delegates processing to process_request_screenshots()
        - Only processes requests where request is True and format not movie/mp4
    """
    request_output_screenshots = post.model_dump()

    mime_type = get_mime(request_output_screenshots['format'])

    if request_output_screenshots['request'] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_screenshots(request_output_screenshots, 'desktop')

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/laptop', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_laptop(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for plain, viewport-specific screenshots at laptop resolution (1440x900)

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
        - Delegates processing to process_request_screenshots()
        - Only processes requests where request is True and format not movie/mp4
    """
    request_output_screenshots = post.model_dump()

    mime_type = get_mime(request_output_screenshots['format'])

    if request_output_screenshots['request'] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_screenshots(request_output_screenshots, 'laptop')

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/tablet', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_tablet(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for plain, viewport-specific screenshots at tablet resolution (768x1024)

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
        - Delegates processing to process_request_screenshots()
        - Only processes requests where request is True and format not movie/mp4
    """
    request_output_screenshots = post.model_dump()

    mime_type = get_mime(request_output_screenshots['format'])

    if request_output_screenshots['request'] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_screenshots(request_output_screenshots, 'tablet')

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/smartphone', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_smarphone(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for plain, viewport-specific screenshots at smartphone resolution (230x490)

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
        - Delegates processing to process_request_screenshots()
        - Only processes requests where request is True and format not movie/mp4
    """
    request_output_screenshots = post.model_dump()

    mime_type = get_mime(request_output_screenshots['format'])

    if request_output_screenshots['request'] == 1:

        if mime_type not in ['movie/mp4']:

            result = process_request_screenshots(request_output_screenshots, 'smartphone')

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/full', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_full(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for plain, full-page screenshot.

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
        - Delegates processing to process_request_screenshots()
        - Only processes requests where request is True and format not movie/mp4 or application/pdf
    """
    request_output_screenshots = post.model_dump()

    mime_type = get_mime(request_output_screenshots['format'])

    if request_output_screenshots['request'] == 1:

        if mime_type not in ['movie/mp4', 'application/pdf']:

            result = process_request_screenshots(request_output_screenshots, 'full')

            return Response(content=result, media_type=mime_type)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
