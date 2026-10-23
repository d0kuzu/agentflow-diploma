# Baseline verification record

This record concerns the research and design materials for `prob-period-1`, prepared on 23 October 2026. It does not report application tests or experimental results.

## Reproducible repository check

Run from the repository root with Python 3.10 or newer:

```sh
python scripts/check_repository.py
```

The check validates required deliverables, local Markdown link targets, SVG XML and matching editable source files. It also screens the public material for application source files, executable artifacts, credential filenames, and several common credential-shaped strings. This limited screening does not establish that every possible sensitive value is detectable.

Final check status: **passed** on 23 October 2026. The check covered 15 required deliverables, 18 Markdown files and their local links, three SVG diagrams with corresponding editable notation sources, and 28 public text files. No application implementation, executable artifact, or common credential-pattern match was found in the public material.

All three SVG diagrams were rendered and visually inspected for legibility, clipping, and alignment with their notation sources. API design spot checks found 11 unique operation identifiers and existing target names for 64 local references; all five illustrative JSON response bodies parsed successfully. The illustrated states and responses were also reviewed against the declared contract. These spot checks are not a full OpenAPI schema-validator run.

## Scope of verification

The documents distinguish proposed functionality, provisional targets, and unperformed experiments. Their plan is subject to stakeholder validation and supervisor review. External references are identified in the research documents; the local checker does not revalidate remote URLs, citation interpretation, or Markdown anchor names.

The API prototype describes intended behavior. No application server, database deployment, live provider call, stakeholder interview, comparative benchmark, peer approval, or supervisor review is recorded as completed by this check.
