from fastapi import FastAPI, Response, status, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel, HttpUrl, constr, conint, Field
from starlette.requests import Request
from app.output_main import process_request_main
from app.output_browser import process_request_browser
from app.output_mobiles import process_request_mobiles
from app.output_full import process_request_full
from app.output_movie import process_request_movie
from app.output_screenshots import process_request_screenshots


app = FastAPI()


class Request(BaseModel):
    request: bool = Field(False, description='Request flag')
    remote_url: HttpUrl = Field(
        "https://ggeerraarrdd.github.io/", description="Valid and accessible URL")
    wait: conint(gt=0, lt=101) = Field(
        2, description="Wait time for screenshot")
    format: str = Field("png", pattern="^(png)$", description="Output file format")
    doc_pad_h: conint(gt=0, lt=1001) = Field(
        300, description="Padding value for horizontal dimension")
    doc_pad_v: conint(gt=0, lt=1001) = Field(
        200, description="Padding value for vertical dimension")
    doc_fill_color: constr(
        pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#ffffff", description="RGB hexadecimal value")
    base_stroke_color: constr(
        pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#23445d", description="RGB hexadecimal value")
    base_fill_color: constr(
        pattern=r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") = Field("#bac8d3", description="RGB hexadecimal value")


@app.post("/main", status_code=status.HTTP_201_CREATED)
def create_output_main(post: Request):

    request_output_main = post.model_dump()

    if request_output_main["request"] == 1:

        result = process_request_main(request_output_main)

        return FileResponse(f"{result}")

    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/browser", status_code=status.HTTP_201_CREATED)
def create_output_browser(post: Request):

    request_output_browser = post.model_dump()

    if request_output_browser["request"] == 1:

        result = process_request_browser(request_output_browser)

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/mobiles", status_code=status.HTTP_201_CREATED)
def create_output_mobiles(post: Request):

    request_output_mobiles = post.model_dump()

    if request_output_mobiles["request"] == 1:

        result = process_request_mobiles(request_output_mobiles)

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/full", status_code=status.HTTP_201_CREATED)
def create_output_full(post: Request):

    request_output_full = post.model_dump()

    if request_output_full["request"] == 1:

        result = process_request_full(request_output_full)

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/movie", status_code=status.HTTP_201_CREATED)
def create_output_movie(post: Request):

    request_output_movie = post.model_dump()

    if request_output_movie["request"] == 1:

        result = process_request_movie(request_output_movie)

        if result == 0:
            Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            return FileResponse(f"{result}")
        
    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/screenshots/desktop", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_desktop(post: Request):

    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "desktop")

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.post("/screenshots/laptop", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_laptop(post: Request):

    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "laptop")

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.post("/screenshots/tablet", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_tablet(post: Request):

    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "tablet")

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.post("/screenshots/smartphone", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_smarphone(post: Request):

    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "smartphone")

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.post("/screenshots/full", status_code=status.HTTP_201_CREATED)
def create_output_screenshots_full(post: Request):

    request_output_screenshots = post.model_dump()

    if request_output_screenshots["request"] == 1:

        result = process_request_screenshots(request_output_screenshots, "full")

        return FileResponse(f"{result}")

    else:

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
