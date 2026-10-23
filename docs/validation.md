# Baseline verification record

This record concerns the research and design materials for `prob-period-1`, prepared on 23 October 2026. It does not report application tests or experimental results.

## Reproducible repository check

Run from the repository root with Python 3.10 or newer:

```sh
python scripts/check_repository.py
```

The check validates required deliverables, local Markdown link targets, SVG XML and matching editable source files. It also screens the public material for application source files, executable artifacts, credential filenames, and several common credential-shaped strings. This limited screening does not establish that every possible sensitive value is detectable.

Initial baseline check status: **passed** on 23 October 2026. The check covered 15 required deliverables, 18 Markdown files and their local links, three SVG diagrams with corresponding editable notation sources, and 28 public text files. No application implementation, executable artifact, or common credential-pattern match was found in the public material.

All three SVG diagrams were rendered and visually inspected for legibility, clipping, and alignment with their notation sources. API design spot checks found 11 unique operation identifiers and existing target names for 64 local references; all five illustrative JSON response bodies parsed successfully. The illustrated states and responses were also reviewed against the declared contract. These spot checks are not a full OpenAPI schema-validator run.

## Scope of verification

The documents distinguish proposed functionality, provisional targets, and unperformed experiments. Their plan is subject to stakeholder validation and supervisor review. External references are identified in the research documents; the local checker does not revalidate remote URLs, citation interpretation, or Markdown anchor names.

The API prototype describes intended behavior. No application server, database deployment, live provider call, stakeholder interview, comparative benchmark, peer approval, or supervisor review is recorded as completed by this check.

## Tracker setup verification — 23 October 2026

The [AgentFlow Diploma YouTrack project](https://agentflow-diploma.youtrack.cloud/projects/AFD) and its [Kanban board](https://agentflow-diploma.youtrack.cloud/agiles/204-1/218-1) were created during preparation for the first submission. The browser UI confirmed 16 real issues: AFD-1 is Done, AFD-16 is Review, and 14 remain in Backlog. Each issue contains an expected outcome, acceptance criteria, and a deadline in its description. AFD-1 through AFD-9 and AFD-16 have Critical priority; AFD-10 through AFD-15 have Normal priority.

The account used by Dias is `admin`. It is assigned to AFD-1, AFD-2, AFD-3, AFD-5, AFD-9, AFD-12, AFD-13, and AFD-16. Bekarys's invited account, `bekars.bihimbai2005`, is assigned to AFD-4, AFD-6, AFD-7, and AFD-11. Nursultan's invited account, `thedids10`, is assigned to AFD-8, AFD-10, AFD-14, and AFD-15. YouTrack invitations were sent to the teammate addresses supplied by the team. GitHub collaborator invitations were also sent to `kLot2005` and `thedids10`; GitHub showed two Pending Invite entries. Invitation acceptance and successful access remain unverified. Supervisor account details remain pending.

[AFD-1](https://agentflow-diploma.youtrack.cloud/issue/AFD-1) links the initial commit and tag. [AFD-16](https://agentflow-diploma.youtrack.cloud/issue/AFD-16) links the booking-approval clarification commit and [draft PR #1](https://github.com/d0kuzu/agentflow-diploma/pull/1). Registering completed work retrospectively does not establish earlier tracker use. The draft PR and automated consistency checks do not establish a human peer review.

The submission form had not been sent, and the project owner authorized refreshing `prob-period-1` to include the tracker links and corrections. The initial commit remains available as [8004069](https://github.com/d0kuzu/agentflow-diploma/commit/8004069aeec039780b450278b3702964b4f2631f). No already submitted version is replaced. The refreshed materials pass the repository check covering 15 required deliverables, 19 Markdown files, three SVG diagrams, and 29 public text files; `git diff --check` also passes.
