# TODO

- [ ] Commit the OpenAPI regeneration recipe: pin the Document360 spec URL,
      generator version (7.11.0), and the config that produces the nested
      `d361api.d361api` layout, so the client can be regenerated deterministically.
- [ ] Decide whether the double-nested `d361api/d361api/` layout is intended; if
      not, flatten to the standard OpenAPI layout and update `__init__` re-exports.
- [ ] `mypy` reports ~523 errors in the generated package (generator idioms:
      `TYPE_CHECKING` reassignments, `Any | None`). It is not in CI; either wire a
      generated-code exclude for mypy or accept it as untyped-gate.
- [ ] Configure PyPI trusted publishing (the release workflow currently expects a
      `PYPI_TOKEN` secret; migrate to OIDC).
- [ ] Trim the committed `docs/*.md` reference set or move it behind a docs build.
