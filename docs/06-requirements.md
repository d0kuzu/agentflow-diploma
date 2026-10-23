# 06 — Requirements and scope

**Project:** AgentFlow

**Diploma topic:** Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents

**Baseline:** `prob-period-1`, 23 October 2026

This is an analysis and design baseline. It contains requirements, diagrams, an API contract and a proposed verification protocol. An executable application, deployed service and experimental results are not included. All software capabilities below are **planned**; supplied documentation is an artifact, not evidence that its requirements have been implemented.

The proposed system supports conversational request intake, appointment coordination and conversation review for a small service organization. A requester describes a need, the system obtains missing information, consults configured tools, and either completes an allowed workflow or asks a person to intervene. An operator configures the assistant and reviews conversations. An administrator manages access and integrations. A researcher evaluates behavior using synthetic data.

## Priorities and acceptance

- **Must:** required for the evaluated prototype.
- **Should:** useful after the core workflow is demonstrated.
- **Could:** optional extension.

Acceptance criteria are proposed targets, not observed results. Runtime evidence must identify a later implementation commit and environment. The proposed evaluation design is in [09-verification-plan.md](09-verification-plan.md).

## Functional requirements

| ID | Requirement | Priority | Status | Acceptance criterion for a later implementation |
|---|---|---|---|---|
| FR-01 | Authenticate an operator and manage access/refresh sessions. | Must | Planned | Valid credentials issue usable tokens; incorrect credentials, expired access tokens and revoked refresh tokens are rejected in every defined negative test. |
| FR-02 | Create, retrieve and update an assistant configuration owned by an operator. | Must | Planned | An operator can manage their assistant; another operator cannot read or modify it, including when an identifier is guessed. |
| FR-03 | Accept a natural-language request and obtain missing information through dialogue. | Must | Planned | Intake cases preserve relevant facts across turns, ask for required missing fields, follow the supplied policy, and never report an action that did not happen. |
| FR-04 | Persist and retrieve dialogue and workflow state. | Must | Planned | A synthetic conversation is retrievable after restart with correct ordering, tool-call associations and action state; repeated delivery does not duplicate messages. |
| FR-05 | Select tools from an explicit allowlist and validate arguments before execution. | Must | Planned | Unknown tools, malformed JSON, missing fields and invalid dates produce no external write; every action is authorized for the current user and assistant. |
| FR-06 | Read availability and create an appointment after explicit requester confirmation and any policy-required operator approval. | Must | Planned | Busy fixture slots are never offered as free; a confirmed valid slot creates exactly one booking only after any policy-required operator approval; ambiguous, unconfirmed, rejected, or approval-pending requests create none. |
| FR-07 | Produce a concise summary of request facts and actual action status. | Should | Planned | A summary covers the gold request facts and observed action result without unsupported assertions or unnecessary personal data. |
| FR-08 | Let an authorized operator list, search and inspect conversations. | Must | Planned | List, search and direct-object retrieval return only conversations within the operator's authorized scope. |
| FR-09 | Expose aggregate workflow activity for operator review. | Should | Planned | Counts match a known fixture dataset and do not reveal another operator's data. |
| FR-10 | Escalate unsupported or high-impact actions to a person. | Must | Planned | The system records a pending-human state and performs no protected side effect until a permitted operator decision is recorded. |
| FR-11 | Prevent duplicate side effects on retries and concurrent replays. | Must | Planned | Three deliveries of the same logical action, including a concurrent replay, create exactly one external record and one canonical action outcome. |
| FR-12 | Support a reproducible synthetic API demonstration. | Must | Planned | A fresh local environment runs the documented authentication, intake, clarification, approval and history flow using only synthetic data; commands and observed responses are recorded. |

## Non-functional requirements

| ID | Requirement | Priority | Status | Acceptance criterion |
|---|---|---|---|---|
| NFR-01 | Authentication, authorization and tenant separation. | Must | Planned | All negative access tests pass at both gateway and internal-service boundaries; forged identity headers and cross-tenant identifiers never grant access. |
| NFR-02 | Minimize disclosure and keep secrets outside version control. | Must | Planned | Code and experiment artifacts contain no real secrets or customer records; responses/logs reveal no passwords, access tokens or unnecessary identifiers. |
| NFR-03 | Bound model/tool execution and fail explicitly. | Must | Planned | Each turn observes a configured deadline and maximum tool-call count; timeouts, empty model output and invalid tool results produce controlled errors and no false success claim. |
| NFR-04 | Record an auditable action trail. | Must | Planned | Each action attempt has a correlation ID, actor, tool, sanitized arguments, outcome and time; a reviewer can match user-facing claims to actual side effects. |
| NFR-05 | Achieve measurable quality and latency. | Should | Planned | Report task completion and median/p95 latency under document 09; provisional goals are ≥80% completion on functional cases and p95 ≤15 s on single-turn non-action cases. Freeze thresholds before experiments. |
| NFR-06 | Support reproducible builds and experiments. | Must | Planned | Record commit, runtime/dependency versions, sanitized configuration, model identifier, fixture hashes and commands; reruns generate comparable structured records. |
| NFR-07 | Permit integration substitution. | Should | Planned | Calendar, messaging and business-record test doubles can replace real services without using customer accounts or changing expected business behavior. |

## Scope of the first implementation

The proposed first implementation is an API/backend prototype with four Go services. An “AI agent” means a bounded model-driven conversation and tool-execution cycle. Planner, executor and reviewer are logical responsibilities; independently communicating autonomous agents are an optional research extension, not a first-period deliverable.

A web frontend, drag-and-drop process editor, general BPMN engine, model training, retrieval-augmented knowledge base and production deployment are outside this baseline. The design supports later exploration without claiming those features exist. Live third-party delivery, production capacity and superiority over scripted workflows require separate evidence.

The first-period design prototype is a proposed [OpenAPI contract](../prototypes/openapi.yaml) and [illustrative interaction flow](08-prototype.md). These can be inspected for consistency, but cannot be used as a running API.

## Traceability

| Workflow | Requirements | Diagram use cases | Proposed verification cases |
|---|---|---|---|
| Request intake and clarification | FR-03, FR-04, NFR-03 | UC-01, UC-02 | S01–S10, S33–S35 |
| Appointment coordination | FR-05, FR-06, FR-11 | UC-03, UC-04 | S11–S20, S29–S32 |
| Operator configuration and review | FR-01, FR-02, FR-07, FR-08, FR-09 | UC-05, UC-06, UC-07 | S21–S25, S36 |
| Controlled escalation and isolation | FR-10, NFR-01, NFR-02, NFR-04 | UC-08 | S26–S28, S37–S40 |

See the [use-case diagram](../diagrams/use-case.svg) and [architecture](07-architecture.md). Future work should maintain this matrix as implementation and test evidence become available.
