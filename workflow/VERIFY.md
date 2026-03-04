# VERIFY

Checklist before committing changes:

## Evidence logging (required)
- Reviewer must append exactly one entry to workflow/EVIDENCE.jsonl per reviewer run.
- The entry must include: ts, repo, run_id, step="reviewer", commands[], and git{}.
- git{} must include: branch, head, dirty, diff_stat.
- Each commands[] item must include: cmd, exit_code. (stdout_tail optional.)
- If any command exit_code != 0: do not commit; next step must be debug/fix.
- If evidence is missing: do not commit.

Evidence entry example:

```
{"ts":"<iso8601>","repo":"ai-workflow-example","run_id":"<run_id>","step":"reviewer","git":{"branch":"<branch>","head":"<commit>","dirty":<bool>,"diff_stat":"<diff --stat>"},"commands":[{"cmd":"<command>","exit_code":0}]}
```

## State verification
- STATE.md reflects the current milestone and task
- TASK_QUEUE.md reflects what is actually being worked on
- DECISIONS_LOG.md updated if architectural decisions were made

1. Run:
   git status

2. Review changes:
   git diff --stat

3. Run or test any changed code.

4. Update STATE.md if the milestone or current task changed.

5. Update DECISIONS_LOG.md if a decision was made.

6. Update TASK_QUEUE.md if tasks moved (ACTIVE → DONE etc).

7. Commit and push.
