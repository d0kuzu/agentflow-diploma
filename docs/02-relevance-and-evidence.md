# Relevance and evidence register

The project investigates a plausible need for reducing repetitive handling of conversational business requests. This release separates literature-supported technical motivation from unverified assumptions about the intended users. No interview, client agreement, deployment result, or competitor migration is presented as verified evidence.

## Evidence available in this release

| ID | Evidence or assumption | Status | What it supports | What it does not establish |
| --- | --- | --- | --- | --- |
| E-01 | Scientific publications reviewed in the literature table | Secondary evidence, linked sources | Motivation for tool use, agent evaluation, and control of unreliable outputs | Demand or measured benefit for the selected users |
| E-02 | Official documentation for compared systems | Secondary evidence, linked sources | Feasibility and available alternatives | Performance superiority or absence of configurable features |
| H-01 | Operators spend time asking for missing request details | User-workflow hypothesis | A candidate intake scenario | Frequency, cost, or representative prevalence |
| H-02 | Natural-language variation reduces coverage of fixed rules | Technical hypothesis | A reason to compare rules with an LLM | That an LLM will outperform a well-tuned baseline |
| H-03 | Operators need a readable record and control over external actions | Requirement hypothesis | Proposed audit and approval requirements | User acceptance or a validated interface |

Supporting sources are in the [literature review](03-literature-review.md) and [system comparison](04-existing-systems.md). Requirement priorities remain provisional until target-user discussions and supervisor review.

## Planned stakeholder validation

Recruit three to five representatives across service operators, team managers, and staff coordinating appointments or follow-ups. Seek consent to record anonymized notes and separate permission for any direct quote. Do not collect customer records or credentials. An interview can be summarized without identifying the business.

Each discussion should cover a recent ordinary inquiry: how it arrived, what fields were missing, which tools were used, how the next action was selected, where errors occurred, and what would require human approval. Ask about existing workarounds before describing the proposed solution to reduce confirmation bias.

Suggested prompts:

1. Walk through one typical request and one difficult request.
2. Which steps repeat, and where is information entered twice?
3. How do you decide that a request is ready for the next action?
4. What mistakes would make automation unacceptable?
5. Which actions could be automated, and which need confirmation?
6. What record would help you inspect and correct an automated action?
7. Which available alternative would you choose if this project did not exist?

## Recording and analysis protocol

For each discussion, record an anonymized participant ID, role, date, consent status, observed workflow, participant statements, analyst interpretation, and requirement changes. Keep factual notes separate from interpretation. Confirm the summary with the participant where feasible. Store consent and any identifying evidence privately; publish only approved, anonymized summaries.

| Participant ID | Role | Date | Consent | Evidence summary | Requirements affected |
| --- | --- | --- | --- | --- | --- |
| To be recorded after a real discussion | Pending | Pending | Pending | No discussion recorded in this release | Pending |

Analyze recurring pain points and counterexamples. If fewer than three discussions are obtained, report the limitation explicitly and do not claim saturation. If the workflow is not a meaningful problem for participants, revise the scope instead of treating the original hypotheses as confirmed.

## Completion criterion

This requirement is complete only when three to five substantive discussions or a substantive real-client agreement are documented, findings are linked to requirements, and confidential details are handled appropriately. A planned interview guide alone does not satisfy the committee's evidence requirement. This item remains outstanding for `prob-period-1`.
