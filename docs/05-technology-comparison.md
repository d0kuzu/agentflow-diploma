# Technology Comparison and Proposed Decisions

**Project:** AgentFlow

**Diploma topic:** Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents

**Baseline:** `prob-period-1` — initial research and design only.

**Primary documentation checked:** 23 October 2026.

## Decision context

The proposed architecture has four logical components: `api-gateway`, `auth-service`, `ai-service`, and `database-service`. Their names describe planned responsibilities; this tag ships no implementation of these services. The initial API material is a design contract, not evidence of a running backend.

The main constraints are a bounded diploma scope, inspectable behavior, typed service contracts, controlled access to external systems, and repeatable evaluation. The comparisons below distinguish documented technology capabilities from project-specific engineering judgment. They do not claim a measured performance advantage. Exact runtime, dependency, database, and model versions will be selected and pinned when implementation begins.

## Decision 1: Backend implementation language

| Option | Relevant documented capability | Project tradeoff |
| --- | --- | --- |
| **Go — proposed** | Goroutines and channels support concurrent work and synchronization. The Go guidance also shows why concurrency must be bounded. [Effective Go](https://go.dev/doc/effective_go#concurrency) | One implementation language across the four components simplifies the planned build and interface conventions. The project must still implement cancellation, concurrency limits, provider adaptation, and execution state. |
| **Python with FastAPI** | Supports asynchronous request handling and runs ordinary synchronous route functions in a thread pool. [Concurrency documentation](https://fastapi.tiangolo.com/async/) | A credible choice for an agent-oriented service and Python-based experiments. Choosing it would require a Python backend design or a mixed-language boundary; neither is inherently incorrect. |
| **JavaScript/TypeScript on Node.js** | Uses an event loop and worker pool; its guidance explains the need to avoid blocking callbacks and long-running work. [Node.js concurrency guidance](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop) | A credible choice for asynchronous API integration. CPU-heavy work and long tasks require deliberate scheduling, and a TypeScript toolchain would need to be introduced. |

**Design decision:** Propose Go for all four backend components. This is a consistency and scope decision, not evidence that Go produces better language-model decisions or universally lower latency. The experiment should separate local service time from model-provider and external-API time before attributing bottlenecks to the language.

## Decision 2: Service communication

| Option | Relevant documented capability | Project tradeoff |
| --- | --- | --- |
| **gRPC with Protocol Buffers — proposed internally** | Defines methods and message types, generates client/server code, supports several RPC styles, and exposes deadlines. Cancellation does not roll back effects already made. [gRPC concepts](https://grpc.io/docs/what-is-grpc/core-concepts/) | Suitable for the proposed typed database-service boundary. Requires schema/code-generation management and explicit compatibility rules. An RPC failure may leave an ambiguous business outcome. |
| **HTTP/JSON with OpenAPI** | HTTP provides standard request/response semantics; OpenAPI describes HTTP interfaces independently of implementation language and can support generated clients and tests. [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.txt), [OpenAPI](https://www.openapis.org/what-is-openapi) | Suitable for the public gateway and external integrations. It is also a valid internal alternative; request validation and error contracts still need implementation. |
| **Asynchronous messaging with RabbitMQ** | Consumer acknowledgements and publisher confirms address different delivery/processing stages; applications must choose appropriate acknowledgement behavior. [RabbitMQ acknowledgements](https://www.rabbitmq.com/docs/confirms) | Useful if later workflows must survive long waits or execute independently of an HTTP request. Adds a broker, delivery-state handling, correlation, and duplicate-processing concerns to the initial scope. |

**Design decision:** Use HTTP/JSON at the API gateway and for external HTTP integrations; propose gRPC for internal database-service calls. Specify other internal contracts before implementation rather than assuming every service must use the same transport. Defer a message broker until a documented long-running workflow requirement justifies it.

Retries are an application decision. The planned design should attach operation identifiers, reconcile ambiguous outcomes, and avoid automatically repeating an external write solely because its response timed out. These are proposed safeguards, not features already delivered by this baseline.

## Decision 3: Persistent storage

| Option | Relevant documented capability | Project tradeoff |
| --- | --- | --- |
| **PostgreSQL — proposed** | Offers transaction isolation levels and structured JSON storage; `jsonb` supports indexing. [Transactions](https://www.postgresql.org/docs/current/transaction-iso.html), [JSON types](https://www.postgresql.org/docs/current/datatype-json.html) | Fits a proposed relational model for users, requests, tool executions, and their relationships, while allowing bounded JSON payloads. Requires schema migrations, backup planning, and explicit transaction boundaries. |
| **MongoDB** | Single-document operations are atomic, and transactions can span multiple documents and collections. [MongoDB transactions](https://www.mongodb.com/docs/manual/core/transactions/) | A valid alternative for document-oriented execution records. The project would need to choose embedding versus references and enforce its consistency rules; lack of transactions is not a valid reason to reject it. |
| **SQLite** | Provides embedded local storage; supports concurrent readers but only one writer at a time per database file. Its documentation identifies cases where client/server storage fits better. [Appropriate uses](https://www.sqlite.org/whentouse.html) | Attractive for a small local prototype or fixture store. The proposed separately accessed persistence service and future concurrent writes favor evaluating a server database first; the workload is not yet measured. |

**Design decision:** Propose PostgreSQL behind `database-service`. The database service will own persistence operations rather than allowing the model to submit arbitrary SQL. Transactional records and flexible tool payloads can share one storage engine, reducing the initial need for multiple databases.

PostgreSQL transactions do not make an external business API and a local database update one atomic operation. The implementation plan must therefore define execution states, reconciliation, and idempotency separately. Vector storage and document retrieval remain optional extensions, not prerequisites for the first action-oriented prototype.

## Decision 4: Agent orchestration and model integration

| Option | Relevant documented capability | Project tradeoff |
| --- | --- | --- |
| **Application-owned Go loop with OpenAI tool calling — proposed** | OpenAI function calling supplies structured tool requests; the application executes its own functions and returns results. Strict mode constrains arguments to a supported schema when configured correctly. [Official OpenAI documentation](https://developers.openai.com/api/docs/guides/function-calling) | Gives the diploma direct control over permitted adapters, state transitions, and measurement points. Requires implementing loop limits, error handling, approvals, persistence, and observability. Schema conformance does not establish permission or business correctness. |
| **LangGraph runtime** | Provides stateful orchestration with durable execution, streaming, human involvement, and a mixture of deterministic and model-driven steps. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Could reduce the amount of orchestration infrastructure to implement. Adopting its documented Python runtime would introduce an additional runtime or change the service-language choice; its concepts remain useful design references. |
| **n8n workflow with an AI Agent node** | A connected model selects among configured tools, and selected tool calls can be routed for human review. [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent), [Human review](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools.md) | Could accelerate workflow assembly and integration. A platform-based solution would shift the diploma contribution toward configuration and integration instead of implementing the proposed orchestration service. |

**Design decision:** Propose a small application-owned loop in `ai-service` with an OpenAI provider adapter and explicit integration adapters. It should accept a limited tool catalogue, validate arguments, check permissions and any required approval, execute one permitted operation, and use the resulting observation to determine the next step. Step limits and a terminal failure state are required design elements.

This is an orchestration comparison, not a current model-quality ranking. The initial baseline selects neither a specific model identifier nor a price/performance claim. A later provider/model choice should record availability, API compatibility, configuration, and test results. Provider replacement would require explicit adapter work and re-evaluation; it is not assumed to be automatic.

## Proposed responsibility map

| Component | Planned responsibility | Boundary to preserve |
| --- | --- | --- |
| `api-gateway` | Accept HTTP requests, validate the external contract, propagate request identity, and expose status/results. | A successful HTTP response must not falsely imply that all external actions completed. |
| `auth-service` | Establish identity and supply authorization information. | Model-generated text cannot grant permissions or change roles. |
| `ai-service` | Coordinate the model-provider adapter, tool catalogue, execution loop, and integration adapters. | Distinguish proposed actions, validated actions, completed actions, and ambiguous outcomes. |
| `database-service` | Expose typed persistence operations over gRPC and manage PostgreSQL state. | Enforce persistence rules independently of model output; avoid arbitrary model-generated SQL. |

This map is a proposal for subsequent implementation. Authentication, approval, durability, and access-control guarantees must not be inferred from the existence of a component name or design document.

## Validation needed before finalizing the choices

No project performance figures have been collected. The following work is planned:

1. Implement a narrow end-to-end workflow using controlled fixtures and a clearly defined expected final state.
2. Verify the gateway and gRPC contracts, including malformed inputs, permission failures, deadlines, and unavailable dependencies.
3. Test concurrent requests and duplicate operation identifiers against persistence and adapter behavior.
4. Record model calls, tool-selection errors, schema failures, business-rule violations, final-state correctness, latency, and token usage where available.
5. Repeat scenarios with fixed configurations; use the results to decide whether a different orchestration runtime, transport, or persistence design is justified.

These checks operationalize the reliability questions in the [literature review](03-literature-review.md). They are an evaluation plan and must not be presented as completed experiments.
