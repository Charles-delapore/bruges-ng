# bruges-ng

**A maintained fork of [bruges](https://github.com/agilescientific/bruges): a
library of geophysical equations, from Aki–Richards to Zoeppritz.**

[![Run tests](https://github.com/Charles-delapore/bruges-ng/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Charles-delapore/bruges-ng/actions/workflows/run-tests.yml)

> **Fork note.** `bruges-ng` is based on `agilescientific/bruges` v0.5.4
> (`905fe4f`, 2023-12-19). The import name stays `bruges`; only the
> distribution name changed, because `bruges` on PyPI is taken by the
> unmaintained 0.5.4. License stays **Apache-2.0**; the original copyright,
> `LICENSE.txt` and `AUTHORS.md` are unchanged. Changes are recorded in
> [REFACTORING.md](REFACTORING.md) and [CHANGES.md](CHANGES.md).

## Install

Not yet on PyPI; install from the repository:

```shell
pip install "bruges-ng @ git+https://github.com/Charles-delapore/bruges-ng.git"
```

Requires Python 3.9+ and NumPy 1.20+; CI covers NumPy 1.26 and 2.x.

## Quick start

Make a trapezoidal wavelet:

```python
import bruges as bg

w, t = bg.filters.ormsby(duration=0.256, dt=0.002, f=[5, 10, 40, 80])
```

`w` is amplitude and `t` is time.

## Links

- [Upstream documentation](https://code.agilescientific.com/bruges)
- [Issue tracker](https://github.com/Charles-delapore/bruges-ng/issues)
- [Original project](https://github.com/agilescientific/bruges)

