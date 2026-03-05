"""Tests for main.py."""

import pytest
from fastapi import HTTPException
from pytest_mock import MockerFixture

from main import error, root

INTERNAL_SERVER_ERROR_STATUS_CODE = 500


@pytest.mark.asyncio
async def test_root(mocker: MockerFixture) -> None:
    """Test the root function returns correct message."""
    mocker.patch("main.logger")
    result = await root()
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_error_raises_http_exception(mocker: MockerFixture) -> None:
    """Test the error function raises HTTPException."""
    mocker.patch("main.logger")
    with pytest.raises(HTTPException) as exc_info:
        await error()
    assert exc_info.value.status_code == INTERNAL_SERVER_ERROR_STATUS_CODE
    assert exc_info.value.detail == "Internal Server Error"
