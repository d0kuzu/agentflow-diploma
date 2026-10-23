# Analysis of Existing Systems

**Project:** AgentFlow

**Diploma topic:** Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents

**Baseline:** `prob-period-1` — research and design only.

**Documentation checked:** 23 October 2026.

## Method and scope

Four systems were selected to cover visual integration workflows (n8n), LLM application workflows (Dify), a managed enterprise agent platform (Microsoft Copilot Studio), and BPMN process orchestration (Camunda). The comparison uses six consistent criteria and primary vendor documentation. It assesses documented capabilities, not measured quality, pricing, feature completeness, or performance. No vendor environment was configured or benchmarked for this review.

“Configurable” means that a maker must deliberately add, connect, or enable the feature. It does not mean that every deployment enforces it automatically. The linked documentation is a time-specific evidence base; editions, permissions, deployment choices, and workflow configuration can affect availability. The comparison does not assume that the products share a common definition of an agent, run, or workflow.

## Comparison matrix

| Criterion | n8n | Dify | Microsoft Copilot Studio | Camunda |
| --- | --- | --- | --- | --- |
| **1. Process authoring model** | Node-based workflows connecting applications and data transformations. [Overview](https://docs.n8n.io/) | Workflow and Chatflow graphs combine model, tool, and logic steps. [Workflow & Chatflow](https://docs.dify.ai/en/cloud/use-dify/build/workflow-chatflow) | Topics, tools, knowledge, and agents can be composed through generative orchestration. [Orchestration FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/faqs-generative-orchestration) | BPMN processes can contain agent loops and activities exposed as tools. [AI agents](https://docs.camunda.io/docs/components/agentic-orchestration/ai-agents/) |
| **2. LLM-directed tool selection** | AI Agent node selects among connected tools; a chat model and tools must be configured. [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent) | Agent node offers configurable strategies, including native function calling and ReAct. [Agent](https://docs.dify.ai/en/cloud/use-dify/nodes/agent) | Generative orchestration selects configured capabilities from their metadata and context. Dynamic tool use is configurable. [Tool configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) | AI Agent connector lets an LLM select tools within modeled process boundaries; implementation variants offer different loop control. [Connector](https://docs.camunda.io/docs/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent/) |
| **3. External system integration** | Application nodes and APIs connect systems; custom nodes are supported. [Overview](https://docs.n8n.io/) | HTTP Request node connects workflows to external APIs and web services. [HTTP Request](https://docs.dify.ai/en/cloud/use-dify/nodes/http-request) | Tools provide external capabilities; their inputs and authentication require configuration. [Tools](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) | Connectors, including REST and MCP, can expose external operations as agent tools. [Tool definitions](https://docs.camunda.io/docs/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent-tool-definitions/) |
| **4. Human review of actions** | Configurable review pauses selected tool calls for approval or denial. [Human review](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools.md) | A Human Input node pauses a workflow and routes it according to configured decisions and timeout handling. [Human Input](https://docs.dify.ai/en/cloud/use-dify/nodes/human-input) | The documented tool setting “Ask the end user before running” is configurable and defaults to No. It must be enabled where required. [Tool settings](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) | User tasks and explicitly modeled interception steps can provide human input or approval. They must be included in the process. [Connector](https://docs.camunda.io/docs/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent/), [Tool definitions](https://docs.camunda.io/docs/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent-tool-definitions/) |
| **5. Execution inspection** | Execution views support filtering, debugging, and re-running workflow executions. [Executions](https://docs.n8n.io/build/understand-workflows/understand-executions.md) | Logs expose conversation or workflow-run details, including traces and token/latency information; retention depends on the plan and log type. [Logs](https://docs.dify.ai/en/cloud/use-dify/monitor/logs) | Monitor summarizes agent metrics and offers component usage analytics. [Analytics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-overview) | Operate supports process-instance inspection, incident handling, and operational changes. [Operate](https://docs.camunda.io/docs/components/operate/operate-introduction/) |
| **6. Deployment and operating responsibility** | Cloud and self-hosted options; self-hosted editions differ by license configuration. [Overview](https://docs.n8n.io/), [Hosting](https://docs.n8n.io/deploy/host-n8n.md) | Cloud documentation and a Docker Compose self-hosting path are provided; self-hosting requires infrastructure setup. [Cloud workflows](https://docs.dify.ai/en/cloud/use-dify/build/workflow-chatflow), [Self-hosting](https://docs.dify.ai/en/self-host/deploy/quick-start/docker-compose) | Agents, apps, and flows are organized in Power Platform environments with roles and security requirements. [Environments](https://learn.microsoft.com/en-us/microsoft-copilot-studio/environments-first-run-experience) | SaaS and Self-Managed deployment models are documented; Self-Managed places deployment and operation on the adopter's infrastructure. [Self-Managed](https://docs.camunda.io/docs/self-managed/about-self-managed/) |

## Interpretation for AgentFlow

The comparison shows substantial overlap with the proposed project: all four systems document ways to combine language-model decisions with external operations, and all describe configurable human involvement. Therefore, “existing systems cannot combine AI agents and business automation” would be an unsupported problem statement. The engineering question is how to implement and assess a deliberately bounded design with explicit contracts and observable outcomes.

The following conclusions are **design decisions for the diploma**, not measured claims about the products:

- **n8n is a relevant integration reference.** Its separation between connected tools and agent selection suggests a small, explicitly configured adapter catalogue for AgentFlow. A custom implementation will require adapter development that a platform may already provide.
- **Dify is a relevant agent-workflow reference.** Its configurable agent strategies and run inspection motivate separate configuration and execution records. A diploma implementation should state which strategy it uses and expose its limitations.
- **Copilot Studio is a relevant governance reference.** Its tool settings show why “supports approval” and “requires approval by default” must be distinguished. AgentFlow's future approval policy should be enforced by application state and checked before a write.
- **Camunda is a relevant process-control reference.** Its modeled boundaries and incident operations motivate explicit execution states and recovery paths. AgentFlow does not aim to reproduce a general BPMN engine.

These implications follow from the capabilities cited in the matrix. They do not establish that custom development is faster, cheaper, more accurate, or more secure than adopting a platform.

## Proposed project positioning

AgentFlow is planned as a small Go-based research implementation consisting of an HTTP API gateway, authentication service, AI orchestration service, and database service. PostgreSQL, internal gRPC contracts, an OpenAI model-provider adapter, and a limited set of external integration adapters are proposed technologies. They are not implemented features in this tag.

The intended scope is a reproducible study of selected business workflows: accept a natural-language request, select permitted operations, validate inputs, execute adapters, and retain inspectable outcomes. This scope favors experimental control and visible engineering decisions. It also accepts the development cost of features supplied by the comparison platforms, such as connector catalogues, workflow editors, and operational tooling.

The initial comparison makes no ranking. A later implementation study should select a specific alternative and reproduce the same scenarios, permissions, initial data, expected outcomes, and failure conditions before making a comparative claim. Success rate, execution time, cost, recovery behavior, and user effort are **unmeasured** at `prob-period-1`.

## Evidence limitations

Product documentation establishes advertised and documented mechanisms, not their behavior under the project's workload. No unsupported “feature absent” claim is inferred from an omitted documentation section. Security, reliability, and usability depend on configuration and must be evaluated separately. This review records no interviews, product trials, or fabricated benchmark results.
