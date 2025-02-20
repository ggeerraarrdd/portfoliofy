"""
FastAPI router for handling individual device OUTPUT_SCREENSHOTS requests.
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation
from api.domain.services import process_request_screenshots










router = APIRouter()


@router.post('/screenshots/desktop', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_desktop(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_SCREENSHOTS/desktop. 
    
    Delegates processing to process_request_screenshots().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots['request'] == 1:

        result = process_request_screenshots(request_output_screenshots, 'desktop')

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/laptop', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_laptop(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_SCREENSHOTS/laptop. 
    
    Delegates processing to process_request_screenshots().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots['request'] == 1:

        result = process_request_screenshots(request_output_screenshots, 'laptop')

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/tablet', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_tablet(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_SCREENSHOTS/tablet. 
    
    Delegates processing to process_request_screenshots().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots['request'] == 1:

        result = process_request_screenshots(request_output_screenshots, 'tablet')

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/smartphone', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_smarphone(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_SCREENSHOTS/smartphone. 
    
    Delegates processing to process_request_screenshots().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots['request'] == 1:

        result = process_request_screenshots(request_output_screenshots, 'smartphone')

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/screenshots/full', status_code=status.HTTP_201_CREATED)
def handle_request_screenshots_full(post: PortfoliofyRequest) -> Response:
    """
    Handle requests for OUTPUT_SCREENSHOTS/full. 
    
    Delegates processing to process_request_screenshots().

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.

    Returns:
        Response: PNG image response if request is valid, 
            NO_CONTENT response otherwise
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots['request'] == 1:

        result = process_request_screenshots(request_output_screenshots, 'full')

        return Response(content=result, media_type='image/png')

    return Response(status_code=status.HTTP_204_NO_CONTENT)
