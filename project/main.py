"""Provide a FastAPI application."""

from fastapi import FastAPI, HTTPException
from logger import get_logger

logger = get_logger(__name__)

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    logger.debug("DEBUG log")
    logger.info("INFO log")
    logger.warning("WARNING log")

    return {"message": "Hello World"}


@app.get("/error")
async def error() -> None:
    """Error endpoint."""
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        logger.exception("EXCEPTION log")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        ) from e
