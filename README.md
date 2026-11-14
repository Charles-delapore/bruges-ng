# bruges-ng

> **Fork note.** This is `bruges-ng`, a maintained fork of
> [`agilescientific/bruges`](https://github.com/Charles-delapore/bruges-ng)
> v0.5.4 (upstream inactive since 2023-12-19). The import name stays
> `bruges`; only the distribution name changed (`bruges` on PyPI is
> taken by the unmaintained 0.5.4). License stays **Apache-2.0**; the
> original copyright, `LICENSE.txt` and author attribution are
> unchanged. What this fork changes is recorded in `REFACTORING.md`
> and `CHANGES.md`.

# bruges is a

![Bruges](http://agile.geosci.ai/bruges.png)

In other words, it's just a load of functions that implement important equations in (mostly seismic) geophysics, from Aki-Richards to Zoeppritz.

[![Run tests](https://github.com/Charles-delapore/bruges-ng/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Charles-delapore/bruges-ng/actions/workflows/run-tests.yml)
[![Build docs](https://github.com/Charles-delapore/bruges-ng/actions/workflows/build-docs.yml/badge.svg)](https://github.com/Charles-delapore/bruges-ng/actions/workflows/build-docs.yml)
[![PyPI version](https://img.shields.io/pypi/v/bruges-ng.svg)](https://pypi.python.org/pypi/bruges-ng/)
[![PyPI versions](https://img.shields.io/pypi/pyversions/bruges-ng.svg)](https://pypi.org/project/bruges-ng//)
[![PyPI license](https://img.shields.io/pypi/l/bruges-ng.svg)](https://pypi.org/project/bruges-ng/)


## Quick start

Install with:

```shell
pip install bruges-ng
```

Make a trapezoidal wavelet like:

```python
import bruges as bg
w, t = bg.filters.ormsby(duration=0.256, dt=0.002, f=[5, 10, 40, 80])
```

This produces two arrays: amplitude `w` and time `t`.


## Links

- [Documentation](https://code.agilescientific.com/bruges)
- [Issue Tracker](https://github.com/Charles-delapore/bruges-ng/issues/)
- [PyPi](http://pypi.python.org/pypi/bruges-ng/)
- [Agile's website](http://www.agilescientific.com)

![Bruges rooves](https://www.dropbox.com/s/tzvi22ujq6rozdb/bruges_long_rooves.png?raw=1)
