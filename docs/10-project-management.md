# Project management and risks

## Responsibilities

| Member | GitHub | Proposed ownership |
| --- | --- | --- |
| Kobdabayev Dias, SE-2404 | [d0kuzu](https://github.com/d0kuzu) | Architecture, repository integration, agent orchestration |
| Bishimbay Bekarys, SE-2403 | [kLot2005](https://github.com/kLot2005) | Stakeholder validation, requirements, API interaction design |
| Tursunbaev Nursultan, SE2402 | [thedids10](https://github.com/thedids10) | Data model, evaluation dataset, test automation |

Supervisor: Қожахмет Жақсылык Ерданұлы. The task register below distinguishes actual YouTrack assignments from proposed ownership. Dates after the first submission remain an internal planning proposal. No contribution or approval is attributed to a person without a corresponding record.

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

The [AgentFlow Diploma YouTrack project](https://agentflow-diploma.youtrack.cloud/projects/AFD) and [task board](https://agentflow-diploma.youtrack.cloud/agiles/204-1/218-1) were created on 23 October 2026 during preparation for submission. The real issue IDs below replace the earlier local planning references and are included in the refreshed `prob-period-1` snapshot. Critical priority covers required submission work; Normal covers the next implementation increment. Full acceptance criteria, evidence links, and deadlines are recorded in issue descriptions; a dedicated Due Date field has not been configured.

All 16 tasks have actual assignees: Dias (`admin`) has eight, Bekarys (`bekars.bihimbai2005`) has four, and Nursultan (`thedids10`) has four. Invitations have been sent to both teammates, but invitation acceptance and successful access are not yet confirmed. Supervisor account details are still missing, and reviewer access remains unverified. Assignment does not establish completed work. The status column records the tracker state at this update; consult YouTrack for later changes.

| YouTrack issue | Priority | Assignment | Deadline | Expected outcome and acceptance criteria | Status |
| --- | --- | --- | --- | --- | --- |
| [AFD-1](https://agentflow-diploma.youtrack.cloud/issue/AFD-1/Publish-initial-research-and-design-baseline) | Critical | Dias (`admin`) | 2026-10-24 | Publish the initial research/design package, verification record, and tagged snapshot | Done; registered retrospectively |
| [AFD-2](https://agentflow-diploma.youtrack.cloud/issue/AFD-2/Configure-YouTrack-project-real-assignees-and-task-traceability) | Critical | Dias (`admin`) | 2026-10-24 | Configure the tracker, add real members, and link assigned prioritized tasks to evidence | Backlog; project and assignments configured, invitation acceptance pending |
| [AFD-3](https://agentflow-diploma.youtrack.cloud/issue/AFD-3/Verify-repository-and-tracker-access-for-team-and-reviewers) | Critical | Dias (`admin`) | 2026-10-24 | Verify repository and tracker access for the team, supervisor, and committee | Backlog; supervisor details and team/reviewer access confirmation pending |
| [AFD-4](https://agentflow-diploma.youtrack.cloud/issue/AFD-4/Validate-relevance-through-35-real-stakeholder-discussions) | Critical | Bekarys (`bekars.bihimbai2005`) | 2026-10-24 | Record 3–5 real stakeholder discussions or qualifying client evidence and trace findings to requirements | Backlog; real evidence pending |
| [AFD-5](https://agentflow-diploma.youtrack.cloud/issue/AFD-5/Obtain-supervisor-review-and-document-response-decisions) | Critical | Dias (`admin`) | 2026-10-24 | Obtain actual supervisor feedback and record response decisions and revisions | Backlog; review pending |
| [AFD-6](https://agentflow-diploma.youtrack.cloud/issue/AFD-6/Review-literature-existing-systems-and-technology-comparisons) | Critical | Bekarys (`bekars.bihimbai2005`) | 2026-10-24 | Review the literature, existing-system comparison, and technology choices; link substantive findings and revisions | Backlog; drafts prepared, review pending |
| [AFD-7](https://agentflow-diploma.youtrack.cloud/issue/AFD-7/Review-scope-requirements-and-API-design-against-validated-needs) | Critical | Bekarys (`bekars.bihimbai2005`) | 2026-10-24 | Review scope, requirement priorities, acceptance criteria, and API design against actual findings | Backlog; drafts prepared, review pending |
| [AFD-8](https://agentflow-diploma.youtrack.cloud/issue/AFD-8/Review-architecture-diagrams-and-verification-plan) | Critical | Nursultan (`thedids10`) | 2026-10-24 | Review diagram consistency and the proposed baseline, scenarios, metrics, and evaluation conditions | Backlog; drafts prepared, review pending |
| [AFD-9](https://agentflow-diploma.youtrack.cloud/issue/AFD-9/Establish-genuine-individual-contributions-and-peer-review-records) | Critical | Dias (`admin`); each member contributes individually | 2026-10-24 | Establish actual task-linked individual contributions, substantive reviews, and resulting revisions | Backlog; workflow drafted, human reviews pending |
| [AFD-10](https://agentflow-diploma.youtrack.cloud/issue/AFD-10/Implement-database-schema-migrations-and-ownership-tests) | Normal | Nursultan (`thedids10`) | 2026-11-06 | Implement schema and migrations with creation, retrieval, ownership-boundary, and rollback tests | Backlog |
| [AFD-11](https://agentflow-diploma.youtrack.cloud/issue/AFD-11/Implement-synthetic-inquiry-API-and-contract-validation) | Normal | Bekarys (`bekars.bihimbai2005`) | 2026-11-06 | Implement synthetic intake endpoints and contract tests matching the reviewed schema | Backlog |
| [AFD-12](https://agentflow-diploma.youtrack.cloud/issue/AFD-12/Implement-deterministic-workflow-baseline) | Normal | Dias (`admin`) | 2026-11-06 | Implement a deterministic workflow with the same inputs and action permissions as the future agent | Backlog |
| [AFD-13](https://agentflow-diploma.youtrack.cloud/issue/AFD-13/Implement-bounded-LLM-agent-with-validated-tool-calls) | Normal | Dias (`admin`) | 2026-11-20 | Implement bounded tool calling, validation, timeouts, audit events, and escalation; invalid calls cause no side effects | Backlog |
| [AFD-14](https://agentflow-diploma.youtrack.cloud/issue/AFD-14/Create-and-freeze-reproducible-evaluation-fixtures) | Normal | Nursultan (`thedids10`) | 2026-11-20 | Freeze reproducible synthetic fixtures, expected outcomes, scoring rules, and repeat conditions before comparison | Backlog |
| [AFD-15](https://agentflow-diploma.youtrack.cloud/issue/AFD-15/Run-matched-baseline-and-agent-evaluations-and-report-limitations) | Normal | Nursultan (`thedids10`) | 2026-12-04 | Run matched evaluations and retain raw outputs, configuration, latency, cost, and failure classifications | Backlog |
| [AFD-16](https://agentflow-diploma.youtrack.cloud/issue/AFD-16/Clarify-booking-approval-and-document-the-contribution-workflow) | Critical | Dias (`admin`) | 2026-10-24 | Clarify booking approval in requirements and architecture, document the contribution workflow, and obtain human review before acceptance | Review; draft PR prepared, human review and merge pending |

[AFD-1](https://agentflow-diploma.youtrack.cloud/issue/AFD-1/Publish-initial-research-and-design-baseline) links the [initial commit](https://github.com/d0kuzu/agentflow-diploma/commit/8004069aeec039780b450278b3702964b4f2631f); its later registration does not establish earlier tracker usage. [AFD-16](https://agentflow-diploma.youtrack.cloud/issue/AFD-16/Clarify-booking-approval-and-document-the-contribution-workflow) links [commit 6478df1](https://github.com/d0kuzu/agentflow-diploma/commit/6478df1bc95a2cffe57a80f3b6143942809a5133) and [draft PR #1](https://github.com/d0kuzu/agentflow-diploma/pull/1). These corrections are included in the refreshed pre-submission snapshot, while human review and merge into `main` remain pending. A Review state does not mean a peer has reviewed or approved the change.

## Contribution and review workflow

Each participant uses an individual identifiable Git account. Follow [CONTRIBUTING.md](../CONTRIBUTING.md): create a branch such as `codex/REAL-TASK-ID-short-description`, open a pull request with the actual YouTrack ID and acceptance criteria, and request review by another member. Add the commit or PR URL to the corresponding issue. Mark the issue complete only after the criteria and review are satisfied. Keep `main` as the accepted baseline; establish branch protection after confirming repository access and GitHub plan capabilities.

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
