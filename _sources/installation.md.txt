```{highlight} shell
```

# Installation


## Stable release

To install Package Helper 3 on your Python distribution, you can run this command in your terminal:

```console
$ pip install package-helper-3
```

If you don't have [pip] installed, this [Python installation guide] can guide
you through the process.


However, if you have `uv` installed (highly recommended), it is best to install PH3 as a UV tool:

(install)=
```console
$ uv tool install package-helper-3
```

This is the preferred method to install Package Helper 3, as it will not tie PH3 to your Python installation.


## From sources

The sources for Package Helper 3 can be downloaded from the [Github repo].

You can either clone the public repository:

```console
$ git clone git://github.com/balouf/package-helper-3
```

Or download the [tarball]:

```console
$ curl -OJL https://github.com/balouf/package-helper-3/tarball/main
```

Once you have a copy of the source, you can install it with:

```console
$ pip install .
```

[pip]: https://pip.pypa.io
[Python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/
[Github repo]: https://github.com/balouf/package-helper-3
[tarball]: https://github.com/balouf/package-helper-3/tarball/main
