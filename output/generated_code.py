```python
#!/usr/bin/env python3
"""
Utility for calculating the factorial of a non‑negative integer.

The module provides a single public function :func:`factorial` that validates
its input and returns the exact factorial value using an iterative algorithm.
A small command‑line interface is also included for quick manual testing.

Example
-------
>>> factorial(5)
120
>>> factorial(0)
1
"""

from __future__ import annotations

import argparse
import sys
from typing import List

__all__: List[str] = ["factorial"]


def factorial(n: int) -> int:
    """
    Return the factorial of a non‑negative integer ``n``.

    Parameters
    ----------
    n: int
        The number whose factorial is to be computed. Must be an integer
        greater than or equal to zero.

    Returns
    -------
    int
        ``n!`` – the product of all positive integers up to ``n``.
        For ``n == 0`` the result is ``1`` by definition.

    Raises
    ------
    TypeError
        If ``n`` is not an instance of :class:`int` (booleans are rejected).
    ValueError
        If ``n`` is negative.
    """
    # Reject booleans explicitly because ``bool`` is a subclass of ``int``.
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(
            f"factorial() only accepts integer values, got {type(n).__name__}"
        )
    if n < 0:
        raise ValueError("factorial() not defined for negative integers")

    # Fast path for the two smallest inputs.
    if n <= 1:
        return 1

    result: int = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _non_negative_int(value: str) -> int:
    """`argparse` type that converts *value* to ``int`` and ensures it is non‑negative."""
    iv = int(value)
    if iv < 0:
        raise argparse.ArgumentTypeError("value must be non‑negative")
    return iv


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command‑line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate the factorial of a non‑negative integer."
    )
    parser.add_argument(
        "number",
        type=_non_negative_int,
        help="non‑negative integer whose factorial will be computed",
    )
    return parser.parse_args(argv)


def _main() -> None:
    """Entry point for the command‑line interface."""
    try:
        args = _parse_args()
        result = factorial(args.number)
    except (TypeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    else:
        print(result)


if __name__ == "__main__":
    _main()
```