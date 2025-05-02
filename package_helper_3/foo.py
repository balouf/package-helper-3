def foo() -> str:
    """
    Summary line.

    Extended description of function.

    Returns
    -------
    :class:`str`
        Description of return value

    Examples
    --------

    >>> foo()
    'foo'
    """

    return "foo"


def fibo(n):
    """

    Parameters
    ----------
    n: :class:`int`
        The sequence number

    Returns
    -------
    :class:`int`

    Examples
    --------

    >>> fibo(3)
    2
    >>> fibo(30)
    832040
    """
    return 1 if n < 3 else fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":  # pragma: no cover
    print(foo())
