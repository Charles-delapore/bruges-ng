# Security policy

## Supported versions

| Version | Supported |
|---|---|
| 0.5.x | yes |
| earlier | no |

## Reporting a vulnerability

Use GitHub's private vulnerability reporting on this repository
(**Security → Report a vulnerability**). Do not open a public issue for a
security problem.

Include the affected module, the command or import that triggers it, and the
expected impact. This library performs numerical calculations and does not
process untrusted files by default; the most likely issues are unsafe parsing
in user-supplied arrays or a dependency vulnerability.

## Upstream

This is a fork of `agilescientific/bruges`. Security fixes that also affect the
upstream project will be reported there as well, with attribution.

## Response

We aim to acknowledge within 7 days and to publish a patched release with a
note in `CHANGES.md`.
