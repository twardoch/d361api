# Changelog

All notable changes to `d361api` are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
git tags (`vX.Y.Z`) via `hatch-vcs`.

## [2.2.8] - 2026-07-05

### Fixed
- Test suite is green again after the package moved its API operation classes
  into the nested `d361api.d361api` subpackage. The ten `test_*_api.py` modules
  imported the old flat paths (`d361api.articles_api`); they now import the
  nested modules.
- `test_models.py` imported model classes from the API subpackage instead of the
  top-level package; it now imports them from `d361api`.
- `test_configuration.py` asserted a `timeout` and `user_agent` attribute on
  `Configuration`. Neither exists on the generated class: request timeout is a
  per-call argument, and `user_agent` lives on `ApiClient`. Both tests now check
  the real surface.

### Added
- `asyncio_mode = "auto"` and `pytest-asyncio` so the async integration tests
  actually run instead of erroring on collection.
- `docs/assets/icon.png` project icon.
- `CHANGELOG.md`, `TODO.md`, `PLAN.md`.

### Changed
- `ruff format` applied across the tree; `ruff check` is clean. The generated
  `d361api/` package is excluded from linting (machine output); generated test
  idioms are tolerated via per-file ignores.

### Removed
- Legacy CI configs: `.github/workflows/python.yml` (obsolete OpenAPI-Generator
  stub), `.travis.yml`, `.gitlab-ci.yml`. GitHub Actions (`push.yml`,
  `release.yml`) are the sole CI.
