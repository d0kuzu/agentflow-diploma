# AgentFlow

**Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents**

AgentFlow is a diploma project investigating how an LLM agent can convert conversational requests into controlled business actions. The initial scope covers inquiry intake, collection of missing information, request classification, conversation summaries, and appointment requests in a synthetic service-business scenario.

**Current stage:** research and design, `prob-period-1`, 23 October 2026. This version contains project documentation, architectural diagrams, an API design prototype, and an evaluation plan. Application implementation and empirical evaluation are planned. No running application or measured improvement is claimed for this release.

## Problem and intended users

Small service teams may handle customer inquiries across messaging channels, calendars, and separate records. Repeated data entry and incomplete requests can increase handling effort. These are working problem hypotheses; their frequency and severity must be established through interviews and workflow observations.

The intended users are service operators, managers configuring automation, and customers submitting requests. The intended outcome is a prototype that can perform a bounded set of actions through explicit tool contracts, preserve an execution record, and transfer ambiguous or sensitive cases to a human operator.

## Team and supervision

The following allocation is the initial plan and should be confirmed by the team. It records responsibility, not completed contributions.

| Participant | Group | GitHub | Proposed responsibility |
| --- | --- | --- | --- |
| Kobdabayev Dias | SE-2404 | [d0kuzu](https://github.com/d0kuzu) | Architecture, backend coordination, agent orchestration |
| Bishimbay Bekarys | SE-2403 | [kLot2005](https://github.com/kLot2005) | Requirements, API interaction design, integration contracts |
| Tursunbaev Nursultan | SE2402 | [thedids10](https://github.com/thedids10) | Data design, evaluation fixtures, automated verification |

**Supervisor:** Қожахмет Жақсылык Ерданұлы.

## Scope and selected direction

The proposed system separates an API gateway, authentication, an AI orchestration service, and persistence. The provisional technology choices are Go, HTTP/JSON, gRPC/protobuf, PostgreSQL, and an LLM provider with structured tool calling. These are design decisions to validate, not implemented capabilities. See the [technology comparison](docs/05-technology-comparison.md).

The initial implementation will use synthetic records and mock external adapters. A general visual workflow builder, unrestricted autonomous actions, real customer migration, production deployment, and training a foundation model are outside the first prototype.

## Documentation

| Material | Location |
| --- | --- |
| Project proposal and scope | [Proposal](docs/01-project-proposal.md) |
| Relevance, assumptions, and validation plan | [Evidence register](docs/02-relevance-and-evidence.md) |
| Literature review | [Literature](docs/03-literature-review.md) |
| Existing system comparison | [Systems](docs/04-existing-systems.md) |
| Technology comparison | [Technology](docs/05-technology-comparison.md) |
| Requirements and acceptance criteria | [Requirements](docs/06-requirements.md) |
| Architecture and diagrams | [Architecture](docs/07-architecture.md), [diagram files](diagrams/) |
| API design prototype | [Prototype](docs/08-prototype.md) |
| Verification and evaluation plan | [Evaluation](docs/09-verification-plan.md) |
| Responsibilities, milestones, risks, and tasks | [Project management](docs/10-project-management.md) |
| Supervisor review record | [Supervision](docs/11-supervisor-feedback.md) |
| Exact submission and outstanding requirements | [Submission checklist](docs/12-submission.md) |

**YouTrack:** not created yet. The [local task plan](docs/10-project-management.md#initial-task-plan) contains proposed owners, priorities, outcomes, deadlines, and acceptance criteria. It does not replace the required YouTrack project or real task links.

## Repository structure

```text
docs/          Research, decisions, requirements, planning, and review records
diagrams/      Editable diagram sources and readable SVG exports
prototypes/    API contract and synthetic interaction examples
tests/         Supporting synthetic evaluation materials
scripts/       Repository material checks
.github/       Contribution and review template
```

Application source and dependency configuration will be introduced with implementation tasks. The API contract describes intended behavior; it is not a deployed API.

## View and validate this version

```sh
git clone https://github.com/d0kuzu/agentflow-diploma.git
cd agentflow-diploma
git checkout prob-period-1
python scripts/check_repository.py
```

The check uses Python 3.10 or newer and the standard library only. Read the Markdown files in GitHub and open SVG diagrams in a browser. The prototype document explains the API examples. There is no application setup or server command at this stage; those instructions must accompany the first runnable implementation.

The check verifies repository structure, local document links, required deliverables, and SVG well-formedness. It does not prove implementation correctness, stakeholder validation, scientific completeness, or supervisor approval.

## Submission and development process

Repository: [agentflow-diploma](https://github.com/d0kuzu/agentflow-diploma).

Stage snapshot: [prob-period-1](https://github.com/d0kuzu/agentflow-diploma/tree/prob-period-1).

This is the initial submission. The team must record future development progressively using individual accounts, real task references, feature branches, and substantive reviews. The initial commit is not evidence of earlier development or contributions from all team members. Submitted tags must not be moved or replaced. See the [submission checklist](docs/12-submission.md) for material gaps that still need real-world evidence or access setup.
