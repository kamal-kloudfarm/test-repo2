"""Environment utilities."""

import os
from typing import (
    Any,
    ParamSpec,
    TypeVar,
    cast,
    overload,
)

T = TypeVar("T", bound=Any)
P = ParamSpec("P")
R = TypeVar("R")
MISSING = cast(Any, object())


@overload
def getenv(name: str) -> str: ...


@overload
def getenv(name: str, default: T) -> str | T: ...


def getenv(name: str, default: str | T = MISSING) -> str | T:
    """Get environment variable or return default value."""
    try:
        return os.environ[name]
    except KeyError:
        if default is MISSING:
            raise RuntimeError(
                f"Environment variable {name!r} is not set."
            ) from None
        return default


@overload
def getlistenv(name: str) -> list[str]: ...


@overload
def getlistenv(name: str, sep: str) -> list[str]: ...


@overload
def getlistenv(name: str, sep: str, default: T) -> list[str] | T: ...


def getlistenv(
    name: str, sep=",", default: list[str] | T = MISSING
) -> list[str] | T:  # type: ignore[assignment]
    """Get environment variable or return default value."""
    try:
        return os.environ[name].split(sep)
    except KeyError:
        if default is MISSING:
            raise RuntimeError(
                f"Environment variable {name!r} is not set."
            ) from None
        return default


@overload
def getintenv(name: str) -> int: ...


@overload
def getintenv(name: str, default: T) -> int | T: ...


def getintenv(name: str, default: int | T = MISSING) -> int | T:
    """Get environment variable or return default value."""
    try:
        return int(os.environ[name])
    except KeyError:
        if default is MISSING:
            raise RuntimeError(
                f"Environment variable {name!r} is not set."
            ) from None
        return default


@overload
def getfloatenv(name: str) -> float: ...


@overload
def getfloatenv(name: str, default: T) -> float | T: ...


def getfloatenv(name: str, default: float | T = MISSING) -> float | T:
    """Get environment variable or return default value."""
    try:
        return float(os.environ[name])
    except KeyError:
        if default is MISSING:
            raise RuntimeError(
                f"Environment variable {name!r} is not set."
            ) from None
        return default


@overload
def getboolenv(name: str) -> bool: ...


@overload
def getboolenv(name: str, default: T) -> bool | T: ...


def getboolenv(name: str, default: bool | T = MISSING) -> bool | T:
    """Get environment variable or return default value."""
    try:
        return os.environ[name].lower() in ["true", "1", "yes"]
    except KeyError:
        if default is MISSING:
            raise RuntimeError(
                f"Environment variable {name!r} is not set."
            ) from None
        return default


def setenv(name: str, value: Any) -> None:
    """Set an environment variable."""
    os.environ[name] = str(value)


def setlistenv(name: str, value: list[Any]) -> None:
    """Set a list environment variable."""
    os.environ[name] = ",".join(map(str, value))


def getenvs(prefix: str) -> dict[str, str]:
    """Get all environment variables with a prefix."""
    return {
        name: value
        for name, value in os.environ.items()
        if name.startswith(prefix)
    }
