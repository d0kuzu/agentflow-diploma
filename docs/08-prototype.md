# 08 — API design prototype

**Project:** AgentFlow

**Diploma topic:** Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents

**Baseline:** `prob-period-1`, 23 October 2026

The prototype in this milestone is a **design artifact**, consisting of a proposed [OpenAPI contract](../prototypes/openapi.yaml) and the interaction walkthrough below. It is not a runnable backend, deployed website, frontend, screenshot of an application or record of API execution. Every response shown is an illustrative expected response.

The contract uses the reserved placeholder host `agentflow.example.invalid`. It must not be interpreted as a deployed endpoint. No real person, customer account, password or provider credential is used in the examples.

## Intended interaction

1. An operator authenticates and configures an assistant with an explicit policy and tool allowlist.
2. An authorized API client creates a conversation for a synthetic requester.
3. The requester describes a task. The assistant asks for missing information rather than guessing.
4. The requester confirms a proposed date and time. The system validates availability and prepares an action.
5. When policy requires human approval, an authorized operator approves or rejects the pending action.
6. A later conversation read reports the actual execution outcome and auditable action status.

Requester confirmation and operator approval are distinct: the former captures intent, while the latter grants permission under the workflow policy. An approval response must not be presented as proof that the external action already succeeded.

## Contract overview

| Method and proposed path | Purpose | Planned access / outcome |
|---|---|---|
| `GET /health` | Basic process health. | Public; `200` does not imply all dependencies are ready. |
| `POST /auth/login` | Obtain an operator access token. | Credentials; invalid login returns `401`. |
| `GET /assistants` | List authorized assistant configurations. | Bearer token; ownership-scoped list. |
| `POST /assistants` | Create a configuration. | Authorized operator; owner is derived from identity. |
| `GET /assistants/{assistantId}` | Read an authorized configuration. | Bearer token; unknown or inaccessible identifier returns `404`. |
| `PATCH /assistants/{assistantId}` | Update a configuration. | Authorized owner/operator; inaccessible identifier returns `404`. |
| `GET /conversations` | List authorized conversations. | Bearer token; bounded pagination. |
| `POST /conversations` | Start a conversation. | Authorized API client; `201` creates state only. |
| `GET /conversations/{conversationId}` | Read dialogue and action status. | Ownership-scoped read. |
| `POST /conversations/{conversationId}/messages` | Submit a text turn. | Bearer token and idempotency key; bounded processing. |
| `POST /conversations/{conversationId}/actions/{actionId}/decision` | Approve or reject a pending action. | Permitted operator; approval returns `202` with action state, not external success. |

This is an initial contract subset. Refresh/logout, aggregate analytics, search filters and provider callbacks remain specified at the requirement level; their complete API contracts are later work. Requester-channel authentication, role assignment and account provisioning must be decided before implementation.

## Illustrative requests and responses

All UUIDs below are synthetic. `DEMO_ACCESS_TOKEN` is a placeholder rather than an issued token. Examples are written as HTTP messages to make the contract inspectable without implying a running application.

### 1. Configure an assistant

```http
POST /assistants HTTP/1.1
Host: agentflow.example.invalid
Authorization: Bearer DEMO_ACCESS_TOKEN
Content-Type: application/json

{
  "name": "Synthetic service assistant",
  "instructions": "Collect the requested service, date and time. Ask for missing facts. Never claim a booking before tool success.",
  "allowed_tools": ["check_availability", "create_appointment", "summarize_conversation"],
  "require_approval_for_writes": true
}
```

Illustrative `201` body:

```json
{
  "id": "11111111-1111-4111-8111-111111111111",
  "name": "Synthetic service assistant",
  "instructions": "Collect the requested service, date and time. Ask for missing facts. Never claim a booking before tool success.",
  "allowed_tools": ["check_availability", "create_appointment", "summarize_conversation"],
  "require_approval_for_writes": true
}
```

### 2. Open a synthetic conversation

```http
POST /conversations HTTP/1.1
Host: agentflow.example.invalid
Authorization: Bearer DEMO_ACCESS_TOKEN
Content-Type: application/json

{
  "assistant_id": "11111111-1111-4111-8111-111111111111",
  "requester_reference": "synthetic-requester-01"
}
```

Illustrative `201` body:

```json
{
  "id": "22222222-2222-4222-8222-222222222222",
  "assistant_id": "11111111-1111-4111-8111-111111111111",
  "status": "awaiting_input",
  "messages": [],
  "actions": []
}
```

### 3. Clarify an incomplete request

```http
POST /conversations/22222222-2222-4222-8222-222222222222/messages HTTP/1.1
Host: agentflow.example.invalid
Authorization: Bearer DEMO_ACCESS_TOKEN
Idempotency-Key: scenario-01-turn-01
Content-Type: application/json

{"text":"I would like to arrange a 30-minute consultation."}
```

Illustrative `200` body, with no side effect:

```json
{
  "conversation_id": "22222222-2222-4222-8222-222222222222",
  "status": "awaiting_input",
  "assistant_message": "Which date and time would you prefer, and in which time zone?",
  "actions": []
}
```

### 4. Prepare a confirmed action

For the walkthrough, assume the synthetic fixture declares `2026-11-02T10:00:00+05:00` available. This is an example fixture condition, not a live availability check. A second message confirms that exact slot. After validation, the illustrative response contains:

```json
{
  "conversation_id": "22222222-2222-4222-8222-222222222222",
  "status": "pending_approval",
  "assistant_message": "Your requested slot is awaiting operator approval. The appointment has not yet been booked.",
  "actions": [
    {
      "id": "33333333-3333-4333-8333-333333333333",
      "tool": "create_appointment",
      "status": "pending_approval",
      "summary": "Create a 30-minute consultation on 2026-11-02 at 10:00 +05:00."
    }
  ]
}
```

### 5. Record an operator decision

```http
POST /conversations/22222222-2222-4222-8222-222222222222/actions/33333333-3333-4333-8333-333333333333/decision HTTP/1.1
Host: agentflow.example.invalid
Authorization: Bearer DEMO_ACCESS_TOKEN
Idempotency-Key: scenario-01-action-01-approve
Content-Type: application/json

{"decision":"approve","reason":"Requester confirmed the synthetic fixture slot."}
```

Illustrative `202` body:

```json
{
  "id": "33333333-3333-4333-8333-333333333333",
  "tool": "create_appointment",
  "status": "approved",
  "summary": "Approved for execution; external success has not yet been observed."
}
```

A later `GET /conversations/{conversationId}` must reflect `succeeded` only after the adapter reports and records success. A rejected decision must produce no external write. Reusing an idempotency key with an incompatible payload should return `409`.

## Design-review checks

- Confirm every example conforms to its schema and uses the same identifiers and state vocabulary.
- Review who may create an assistant, access a conversation and approve an action; do not infer authority from a JSON owner field.
- Verify that responses distinguish clarification, pending approval, acceptance for execution, success and failure.
- Review timeout, malformed-tool, duplicate-action and ownership cases before implementation.
- When an implementation is available, replace illustrative evidence with separately labelled captured transcripts tied to the implementation commit.

The current artifact demonstrates interface and workflow design. It provides no measured accuracy, latency, authentication guarantee or integration result.
