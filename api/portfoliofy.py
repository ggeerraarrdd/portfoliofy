"""
TD
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
