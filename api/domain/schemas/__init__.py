"""
Pydantic model for validating and processing Portfoliofy screenshot requests.
"""

from .schemas import PortfoliofyRequest


# Define what should be available when using "from .schemas import *"
__all__ = ['PortfoliofyRequest']
