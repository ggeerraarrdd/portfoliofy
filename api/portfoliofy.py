"""
FastAPI application for the Portfoliofy API.

This is the main application module that initializes the FastAPI app
and includes all router endpoints. Portfoliofy generates portfolio-ready
styled screenshots across multiple device viewports.

Available endpoints:
- /main: Handles OUTPUT_MAIN requests
- /browser: Handles OUTPUT_BROWSER requests
- /mobiles: Handles OUTPUT_MOBILES requests
- /full: Handles OUTPUT_FULL requests
- /movie: Handles OUTPUT_MOVIE requests
- /screenshots: Handles OUTPUT_SCREENSHOTS requests

The API accepts URLs and styling parameters.

See README.md for API documentation.
"""

# Third-Party Libraries
from fastapi import FastAPI

# Local
from api.routers import router_main
from api.routers import router_browser
from api.routers import router_mobiles
from api.routers import router_full
from api.routers import router_movie
from api.routers import router_screenshots










app = FastAPI()


app.include_router(router_main)
app.include_router(router_browser)
app.include_router(router_mobiles)
app.include_router(router_full)
app.include_router(router_movie)
app.include_router(router_screenshots)
