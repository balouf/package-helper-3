from cookiecutter.utils import simple_filter


@simple_filter
def split_last(value):
    """
    Parameters
    ----------
    value: :class:`str`
        Firstname Lastname

    Returns
    -------
    :class:`dict`
        First and last name in a dict.

    Examples
    --------

    >>> split_last('Fabien Paul Cédric Sébastien Mathieu')
    {'left': 'Fabien Paul Cédric Sébastien', 'right': 'Mathieu'}
    """
    left, sep, right = value.rpartition(' ')
    return {'left': left, 'right': right}
