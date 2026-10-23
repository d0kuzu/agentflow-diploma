# Project proposal and scope

## Project identity

**Title:** Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents.

**Working name:** AgentFlow. **Stage:** initial research and design. **Submission:** `prob-period-1`, 23 October 2026.

The team is Kobdabayev Dias (SE-2404), Bishimbay Bekarys (SE-2403), and Tursunbaev Nursultan (SE2402), supervised by Қожахмет Жақсылык Ерданұлы. Responsibilities are proposed in the [management plan](10-project-management.md).

## Problem statement

A service operator receiving an incomplete inquiry must identify the customer's intent, ask for missing information, record the request, and coordinate a next action. Conventional rules can make a fixed process predictable, but handling variable language and incomplete input requires additional interpretation. An LLM can provide that interpretation, yet its outputs can be incorrect or unsuitable for execution. The engineering problem is to connect language interpretation to a small, auditable set of business operations with validation and human escalation.

The frequency, cost, and commercial importance of this problem remain hypotheses for the intended user group. The [evidence plan](02-relevance-and-evidence.md) defines how they will be tested. Literature motivates the technical investigation; it does not establish demand from the team's target users.

## Aim and research questions

The aim is to design, implement, and evaluate an intelligent business process automation prototype that uses an LLM agent to interpret inquiries and execute bounded actions through validated interfaces.

The primary question is whether the prototype increases correct completion of variable-language requests compared with a deterministic baseline under the same synthetic scenarios and action permissions. Secondary questions concern operator interventions, invalid action attempts, response latency, and model usage cost. All improvements are hypotheses until measured.

## Objectives

1. Validate the target workflow through three to five discussions with representative users or an appropriately documented client agreement.
2. Review relevant scientific work and compare existing systems using consistent, evidence-backed criteria.
3. Specify functional requirements, non-functional requirements, and observable acceptance criteria.
4. Design component boundaries, persistence, tool contracts, authentication, and human escalation.
5. Implement a reproducible prototype with synthetic data and mock adapters before connecting external services.
6. Compare the prototype with a deterministic baseline using a fixed scenario set and documented measurement conditions.

## Scope

The first workflow will receive an inquiry, identify its intent, collect required fields, maintain conversation state, produce a summary, and prepare a request for an appointment or operator follow-up. State-changing operations will require validated arguments and policy checks. Irreversible or ambiguous operations will be sent to an operator. The API design is the initial interaction prototype because a user interface is not required to test the backend research questions.

The project will initially support one service-business workflow and English-language synthetic examples. Additional languages and workflows require separate evaluation. A model-provider adapter is planned to avoid placing provider-specific behavior throughout the application.

Excluded from the initial prototype are a general visual workflow designer, financial transactions, medical or legal decisions, training or fine-tuning a foundation model, large-scale customer migration, and production reliability claims. Live messaging/calendar adapters are later extensions, subject to sandbox validation.

## Expected outcomes and engineering complexity

Expected artifacts are a source-controlled prototype, requirements and architecture, API specifications, automated tests, a reproducible evaluation dataset and harness, and an analysis of measured strengths and limitations. The engineering complexity lies in stateful conversations, structured model outputs, validation of tool requests, distributed component contracts, access control, failure handling, and repeatable evaluation.

The initial design proposes four services, but this is not an assumption that microservices are always preferable. The team will assess whether separate deployment provides enough value to justify operational overhead for the diploma scope. A modular monolith remains a documented alternative in the technology comparison.

## Current deliverables and next decision

This release supplies the analysis/design materials and an API contract prototype. No application implementation or experimental result is included. The next checkpoint is supervisor review of workflow scope and requirements, followed by stakeholder validation and a small vertical implementation slice.
