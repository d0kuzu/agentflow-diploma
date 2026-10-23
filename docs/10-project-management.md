# Project management and risks

## Responsibilities

| Member | GitHub | Proposed ownership |
| --- | --- | --- |
| Kobdabayev Dias, SE-2404 | [d0kuzu](https://github.com/d0kuzu) | Architecture, repository integration, agent orchestration |
| Bishimbay Bekarys, SE-2403 | [kLot2005](https://github.com/kLot2005) | Stakeholder validation, requirements, API interaction design |
| Tursunbaev Nursultan, SE2402 | [thedids10](https://github.com/thedids10) | Data model, evaluation dataset, test automation |

Supervisor: Қожахмет Жақсылык Ерданұлы. Assignments and dates below are proposals for team confirmation. No contribution or approval is attributed to a person without a corresponding record.

## Milestones

| Date | Proposed checkpoint | Exit condition |
| --- | --- | --- |
| 2026-10-24 | First submission | Research/design snapshot tagged; outstanding evidence and access requirements disclosed |
| 2026-10-30 | Scope confirmation | Supervisor review and stakeholder findings reflected in requirements |
| 2026-11-06 | Vertical slice | One synthetic inquiry flows through API, state storage, and deterministic baseline |
| 2026-11-20 | Agent prototype | Bounded tool-calling loop and policy validation demonstrated with mock integrations |
| 2026-12-04 | Evaluation checkpoint | Fixed scenario set run against both approaches; raw results and limitations recorded |

Dates after 24 October are an internal planning proposal, not confirmed university deadlines. Later pre-defense and final dates must be updated after confirmation.

## Initial task plan

YouTrack has not been created. The `PLAN-*` labels below are local planning references, not YouTrack issue IDs. Create real issues, preserve their assigned IDs, and replace these references before claiming task-system traceability. Priority P0 means required before a dependable submission or implementation baseline; P1 means the next implementation increment.

| Local reference | Priority | Proposed owner | Deadline | Expected outcome and acceptance criteria | Status |
| --- | --- | --- | --- | --- | --- |
| PLAN-001 | P0 | Dias | 2026-10-24 | Create YouTrack project, add all members, record project URL, assign prioritized tasks with deadlines | Not started |
| PLAN-002 | P0 | Dias | 2026-10-24 | Verify repository access for all members, supervisor, and committee; record successful access confirmation | Not verified |
| PLAN-003 | P0 | Bekarys | 2026-10-24 | Arrange 3–5 target-user discussions; publish anonymized findings with consent and trace each finding to requirements | Pending real evidence |
| PLAN-004 | P0 | Dias | 2026-10-24 | Obtain supervisor review of scope, requirements, and architecture; record actual feedback and response decisions | Pending review |
| PLAN-005 | P0 | Bekarys | 2026-10-30 | Review research/comparison sources and requirements; submit substantive changes through a peer-reviewed PR | Draft material available, review pending |
| PLAN-006 | P1 | Nursultan | 2026-11-06 | Design schema and migrations; automated tests cover creation, retrieval, ownership boundaries, and rollback/failure cases | Planned |
| PLAN-007 | P1 | Bekarys | 2026-11-06 | Implement API contract validation and synthetic intake endpoints; contract tests match the published schema | Planned |
| PLAN-008 | P1 | Dias | 2026-11-06 | Implement deterministic baseline for the selected workflow; same action permissions and inputs as the agent | Planned |
| PLAN-009 | P1 | Dias | 2026-11-20 | Implement bounded agent loop, argument validation, timeouts, audit events, and human escalation; invalid calls produce no side effect | Planned |
| PLAN-010 | P1 | Nursultan | 2026-11-20 | Freeze synthetic evaluation fixtures and expected outcomes before comparison; document scoring and repeat conditions | Planned |
| PLAN-011 | P1 | Nursultan | 2026-12-04 | Run matched evaluations; retain raw outputs, configuration, latency, cost, and failure classifications | Planned |
| PLAN-012 | P0 | All members | Each checkpoint | Submit individual work under own accounts, obtain review, link real tasks and changes, and tag the submission after checking artifact consistency | Ongoing process, not yet demonstrated |

## Contribution and review workflow

Each participant uses an individual identifiable Git account. For future work, create a branch such as `codex/REAL-TASK-ID-short-description`, open a pull request with the actual YouTrack ID and acceptance criteria, and request review by another member. Add the commit or PR URL to the corresponding issue. Mark the issue complete only after the criteria and review are satisfied. Keep `main` as the accepted baseline; establish branch protection after confirming repository access and GitHub plan capabilities.

The repository is being initialized at this checkpoint. Its initial commits do not demonstrate historical progressive development, peer review, or contributions by all members. Future commits must reflect real completed changes; do not backdate commits or manufacture activity. The supervisor should review selected significant changes at agreed checkpoints.

## Risks and dependencies

| Risk | Likelihood / impact | Mitigation and trigger | Proposed owner |
| --- | --- | --- | --- |
| User problem is insufficiently validated | High / high | Complete interviews; revise scope if recurring value is not supported | Bekarys |
| Scope exceeds available effort | Medium / high | Begin with one workflow and mock adapters; defer UI and broad integration catalogue | Dias |
| LLM produces invalid or unsafe action arguments | High / high | Schema validation, explicit permissions, iteration limits, confirmation, negative tests | Dias |
| Provider latency, cost, or availability varies | Medium / medium | Record exact configurations and retries; enforce budgets; keep deterministic baseline runnable | Dias |
| Cross-user data exposure | Medium / high | Ownership checks at application and data boundaries; adversarial integration tests | Nursultan |
| External adapter causes duplicate actions | Medium / high | Mock-first development, idempotency keys, retries with recorded outcomes | Bekarys |
| Evaluation overfits a small synthetic set | High / medium | Hold out cases, document dataset limits, report per-category failures and variance | Nursultan |
| Review or access evidence is missing | High / high | Confirm access and schedule supervisor review before each submission | Dias |
| Literature or product features change | Medium / medium | Record source dates and re-check claims at later checkpoints | Bekarys |

Dependencies include participant availability, supervisor feedback, YouTrack access, repository review access, a selected model provider for later tests, and a local database/runtime environment during implementation. No live provider credentials are required to inspect the current design release.
