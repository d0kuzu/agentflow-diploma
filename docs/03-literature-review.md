# Literature Review

**Project:** AgentFlow

**Diploma topic:** Development of an Intelligent Business Process Automation System Based on Large Language Models and AI Agents

**Baseline:** `prob-period-1` — initial research and design; no implemented system or measured project results.

**Sources checked:** 23 October 2026.

## Scope and selection method

This focused narrative review examines how language models select tools, interact with external systems, recover from failures, and can be evaluated against business outcomes. Sources were selected for direct relevance to these mechanisms and for primary research evidence. The review contains 12 scientific research papers, including conference publications and research preprints. Eleven were first released in 2022–2026; the 2020 retrieval-augmented generation paper is retained as a foundational exception. This is not an exhaustive systematic review, and it does not establish the absence of related work.

The central design question is: **How can a language model translate a business request into permitted API operations while preserving verifiable execution state?** The proposed system will use model output as an action proposal; application code will validate and execute permitted operations. The implications below are the project's interpretation of the evidence, not claims that the papers implemented AgentFlow.

## Structured analysis

| Research source | Approach and reported evidence | Limitation for this diploma | Implication for the proposed design |
| --- | --- | --- | --- |
| Karpas et al., **MRKL Systems** (2022), research preprint. [Paper](https://arxiv.org/abs/2205.00445) | Combines language models with external knowledge and discrete reasoning modules; presents an architecture and its Jurassic-X realization. | An architectural proposal does not establish correctness of arbitrary business transactions or deployment-specific authorization. | Keep language interpretation separate from deterministic integration adapters and business checks. |
| Yao et al., **ReAct** (2023; first preprint 2022). [Paper](https://arxiv.org/abs/2210.03629) | Interleaves reasoning, actions, and observations; evaluates question answering, fact verification, and interactive tasks. | Results on those tasks cannot be transferred directly to multi-step enterprise processes or their permission rules. | Use a bounded tool–observation loop; record tool events and outcomes for inspection. Do not equate a plausible explanation with successful execution. |
| Schick et al., **Toolformer** (2023). [Paper](https://arxiv.org/abs/2302.04761) | Learns API selection, arguments, and use of results through self-supervised training; experiments include calculation, search, translation, and a calendar. | The training approach and selected tools do not demonstrate safe writes across an organization's changing APIs. | Use explicit tool schemas and evaluate argument accuracy. Training a new tool-use model is outside the initial scope. |
| Patil et al., **Gorilla** (2023 preprint). [Paper](https://arxiv.org/abs/2305.15334) | Combines fine-tuning with documentation retrieval; evaluates API generation using APIs from machine-learning repositories and adaptation to documentation changes. | Correct API-call generation in the studied libraries does not establish correct end-to-end business outcomes. | Version tool descriptions with adapters; test missing, renamed, and changed parameters independently of overall task success. |
| Qin et al., **ToolLLM** (2023 preprint). [Paper](https://arxiv.org/abs/2307.16789) | Constructs ToolBench from real REST APIs, synthetic instructions, and solution paths; develops a search procedure, retriever, and automatic evaluation. | Synthetic tasks and automatic evaluation introduce assumptions; external API availability also affects repeatability. | Start with a small, fixed adapter catalogue and controlled fixtures; separate model errors from unavailable-service errors. |
| Li et al., **API-Bank** (2023, EMNLP). [Paper](https://arxiv.org/abs/2304.08244) | Provides a runnable benchmark covering API planning, retrieval, and calling, with annotated tool-use dialogues and error analysis. | Benchmark APIs and dialogues do not represent the project's future business domain automatically. | Evaluate tool selection, parameter construction, and execution as distinct stages; create a project-specific scenario set. |
| Liu et al., **AgentBench** (2024, ICLR; first preprint 2023). [Paper](https://arxiv.org/abs/2308.03688) | Evaluates agents in eight interactive environments and identifies difficulties in long-horizon reasoning, decisions, and instruction following. | A combined benchmark result may hide failure patterns relevant to one process, such as a duplicated write. | Report results by process and failure category, with explicit limits on steps and retries. |
| Shinn et al., **Reflexion** (2023). [Paper](https://arxiv.org/abs/2303.11366) | Stores linguistic feedback in episodic memory to improve subsequent trials without changing model weights; studies decision-making, coding, and reasoning. | Learning through another trial is not equivalent to safely retrying an external action that may already have succeeded. | Consider feedback-assisted recovery only after checking action state. Idempotency and retry policy must be implemented outside the model. |
| Yao et al., **τ-bench** (2024), research preprint. [Paper](https://arxiv.org/abs/2406.12045) | Tests interactions among agents, simulated users, API tools, and domain rules; compares final database state with a goal and measures repeated-run reliability. | Simulated users and the selected domains limit transfer to real users; published model scores are not AgentFlow measurements. | Use state-based success criteria and repeat scenarios. Evaluate rule compliance alongside task completion. |
| Debenedetti et al., **AgentDojo** (2024). [Paper](https://arxiv.org/abs/2406.13352) | Evaluates tasks and prompt-injection attacks in environments where agents consume untrusted tool data; reports challenges for both utility and defenses. | Passing a finite attack suite cannot prove complete resistance to future attacks or different adapters. | Treat retrieved text and tool output as data; enforce tool permissions in code and include adversarial fixtures in evaluation. |
| Lewis et al., **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (2020, NeurIPS). [Paper](https://arxiv.org/abs/2005.11401) | Combines parametric generation with a retrieved document index; evaluates knowledge-intensive NLP tasks. | Retrieval for answering questions does not itself perform, authorize, or verify a business operation. | Consider document retrieval as an optional context component, separate from action execution. It is not a claimed feature of this initial baseline. |
| Chen et al., **EigenData** (2026), research preprint. [Paper](https://arxiv.org/abs/2603.05553) | Coordinates database, environment, and trajectory generation; reports errors and repairs in BFCL-V3 and introduces outcome-based evaluation. | These are the authors' reported results for their pipeline and benchmark; they do not certify other datasets or this project. | Review test fixtures and expected outcomes manually. Accept equivalent correct action sequences when final state and policy constraints are satisfied. |

## Synthesis and research gap

The architecture and tool-use papers support a separation between language interpretation and executable operations. MRKL motivates modular boundaries, ReAct motivates iterative feedback, and Gorilla and ToolLLM motivate attention to the quality and versioning of tool descriptions. None of these mechanisms alone establishes whether a requested state change was authorized and actually occurred. This is a synthesis of their different study scopes, rather than a new empirical finding. [MRKL](https://arxiv.org/abs/2205.00445), [ReAct](https://arxiv.org/abs/2210.03629), [Gorilla](https://arxiv.org/abs/2305.15334), [ToolLLM](https://arxiv.org/abs/2307.16789).

The evaluation papers motivate separate measurements for individual calls and complete processes. API-Bank distinguishes planning and API use; AgentBench examines longer interactive tasks; τ-bench checks final state and repeated reliability. EigenData adds a reason to audit the evaluator itself. Consequently, a response that says “completed” will not be accepted as evidence of successful automation. [API-Bank](https://arxiv.org/abs/2304.08244), [AgentBench](https://arxiv.org/abs/2308.03688), [τ-bench](https://arxiv.org/abs/2406.12045), [EigenData](https://arxiv.org/abs/2603.05553).

The diploma therefore addresses a bounded engineering and evaluation problem: designing a Go-based system that connects natural-language requests to a limited catalogue of business operations and produces inspectable execution evidence. Its intended contribution is the integration and evaluation of these mechanisms in selected workflows, not the invention of tool calling, an assertion of product superiority, or a claim that existing platforms cannot provide similar features.

## Evaluation implications — planned, not measured

The following are requirements for a later evaluation protocol. No participant study, interview, dataset collection, benchmark run, or improvement percentage is claimed in this baseline.

| Question | Proposed evidence | Interpretation constraint |
| --- | --- | --- |
| Does the workflow reach its intended outcome? | Compare final state with a reviewed expected state; inspect required side effects. | A fluent final answer is insufficient. |
| Are calls valid and permitted? | Log selected tool, validated arguments, authorization decision, and adapter result. | Schema validity and authorization are separate checks. |
| Are outcomes repeatable? | Repeat fixed scenarios with the same configuration and report the distribution of successes. | Do not generalize from one successful demonstration. |
| Can execution recover safely? | Inject timeouts, rejected requests, unavailable tools, and ambiguous outcomes. | A retry must not create a duplicate business operation. |
| Does untrusted text alter permissions? | Include tool-output and document fixtures containing conflicting instructions. | Record both attack resistance and successful legitimate-task completion. |
| What resources are needed? | Measure end-to-end latency, model calls, token usage where exposed, and execution steps. | These quantities remain unmeasured until an implementation and test harness exist. |

## Bibliography

All links below point to primary research records checked on **2026-10-23**. Years refer to the cited publication or initial preprint as stated; availability on arXiv does not by itself indicate peer review.

1. Karpas, E., et al. (2022). *MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning*. arXiv:2205.00445. [Research record](https://arxiv.org/abs/2205.00445)
2. Yao, S., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023; arXiv:2210.03629. [Research record](https://arxiv.org/abs/2210.03629)
3. Schick, T., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. arXiv:2302.04761. [Research record](https://arxiv.org/abs/2302.04761)
4. Patil, S. G., Zhang, T., Wang, X., and Gonzalez, J. E. (2023). *Gorilla: Large Language Model Connected with Massive APIs*. arXiv:2305.15334. [Research record](https://arxiv.org/abs/2305.15334)
5. Qin, Y., et al. (2023). *ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs*. arXiv:2307.16789. [Research record](https://arxiv.org/abs/2307.16789)
6. Li, M., et al. (2023). *API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs*. EMNLP 2023; arXiv:2304.08244. [Research record](https://arxiv.org/abs/2304.08244)
7. Liu, X., et al. (2024). *AgentBench: Evaluating LLMs as Agents*. ICLR 2024; arXiv:2308.03688. [Research record](https://arxiv.org/abs/2308.03688)
8. Shinn, N., et al. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. arXiv:2303.11366. [Research record](https://arxiv.org/abs/2303.11366)
9. Yao, S., Shinn, N., Razavi, P., and Narasimhan, K. (2024). *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*. arXiv:2406.12045. [Research record](https://arxiv.org/abs/2406.12045)
10. Debenedetti, E., et al. (2024). *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. arXiv:2406.13352. [Research record](https://arxiv.org/abs/2406.13352)
11. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020; arXiv:2005.11401. [Research record](https://arxiv.org/abs/2005.11401)
12. Chen, J., Qi, J., Gao, M., Wang, W.-C., Wang, H., and Jin, D. (2026). *EigenData: A Self-Evolving Multi-Agent Platform for Function-Calling Data Synthesis, Auditing, and Repair*. arXiv:2603.05553. [Research record](https://arxiv.org/abs/2603.05553)
