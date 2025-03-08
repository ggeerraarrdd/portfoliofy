"""
TD
"""

# import pytest
from api.core.utils import get_mime









def test_get_mime_pdf():
    """
    TD
    """
    assert get_mime('PDF') == 'application/pdf'
    assert get_mime('pdf') == 'application/pdf'

def test_get_mime_mp4():
    """
    TD
    """
    assert get_mime('MP4') == 'video/mp4'
    assert get_mime('mp4') == 'video/mp4'

def test_get_mime_svg():
    """
    TD
    """
    assert get_mime('SVG') == 'image/svg+xml'
    assert get_mime('svg') == 'image/svg+xml'

def test_get_mime_image():
    """
    TD
    """
    assert get_mime('png') == 'image/png'
    assert get_mime('jpg') == 'image/jpg'
    assert get_mime('gif') == 'image/gif'
