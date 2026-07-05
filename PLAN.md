# Plan

`d361api` is a generated client; its job is to stay a faithful, typed mirror of
the Document360 REST API. Work here is maintenance, not feature design.

## Near term
- Make regeneration reproducible. Capture the spec source and generator invocation
  in a script so a Document360 API change is a one-command refresh, not a manual
  restructure that drifts from the tests (as happened before 2.2.8).
- Keep the test suite offline and green after each regeneration. The hand-written
  smoke tests (`test_configuration.py`, `test_api_client.py`, `test_apis.py`,
  `test_integration.py`, `test_models.py`) guard the public surface used by the
  sibling `d361` package.

## Later
- Resolve the nested-vs-flat layout question and settle on one.
- Bring generated code under `mypy` without hand-edits (generator template tweaks
  or a scoped exclude).
- Move to PyPI trusted publishing (OIDC) and drop the token secret.
