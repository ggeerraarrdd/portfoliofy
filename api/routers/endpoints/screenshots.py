"""
TD
"""

# Third-Party Libraries
from fastapi import APIRouter, Response, status

# Local
from api.domain.schemas import PortfoliofyRequest
from api.domain.services import process_request_screenshots










router = APIRouter()


@router.post("/screenshots/desktop", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_desktop(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "desktop")

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/screenshots/laptop", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_laptop(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "laptop")

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/screenshots/tablet", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_tablet(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "tablet")

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/screenshots/smartphone", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_smarphone(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "smartphone")

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/screenshots/full", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_full(post: PortfoliofyRequest):
    """
    TD
    """
    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "full")

        return Response(content=result, media_type="image/png")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
