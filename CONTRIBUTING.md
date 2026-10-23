# Team contribution and review process

Each team member contributes through their own GitHub account. Record actual work rather than assigning completed work retrospectively to someone who has not reviewed or contributed it.

## Before starting a task

Create a real YouTrack issue with one responsible member, a priority, a deadline, an expected deliverable, and observable acceptance criteria. Link it to the relevant requirement or submission item. If the tracker is not available yet, record the provisioning blocker explicitly; local planning labels are not YouTrack IDs.

## Submit a change

1. Create a task branch from the current accepted baseline, normally `codex/REAL-TASK-ID-description` once the issue exists.
2. Make a coherent change with a descriptive commit message that includes the actual issue ID.
3. Run `python scripts/check_repository.py` and any checks needed for the changed artifact. Describe the checks actually performed.
4. Open a Pull Request with the problem, result, issue link, acceptance criteria, and validation evidence. Add the PR or commit URL to the YouTrack issue.
5. Request a substantive review by another team member. Record feedback and resulting revisions; do not mark a review complete merely because a request was sent.
6. Merge only after the acceptance criteria and required review are satisfied. Update the issue with the merged change and final status.

An AI-assisted consistency check is supporting verification, not a review performed by another student or by the supervisor. Each reviewer must use their own account and inspect the substance of the change.

## Record individual contributions

For each submitted contribution, keep the contributor's full name, area of responsibility, concrete completed deliverable, real YouTrack issue ID, and commit or PR link. Planned work should be labelled planned. A new task assignment does not establish completed work, and an initial repository upload does not establish prior progressive contributions.

## Supervisor and stakeholder evidence

Use the evidence register and supervisor review record for actual discussions and comments. Link the resulting requirement or design changes. Preserve consent and confidentiality; publish only an appropriate anonymized summary. Templates, interview guides, and review agendas do not count as completed discussions or feedback.

## Submission version

Before a submission, check access, complete the required reviews, and ensure every uploaded artifact corresponds to the selected Git tag. Do not move a submitted tag. Changes after a tag must be described as later changes until a corrected submission version is explicitly agreed.
