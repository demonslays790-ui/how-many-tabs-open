# How Many Tabs Do You Have Open? — build notes

- Competition: `u-danu-how-many-tabs-do-you-have-open-d86e783d` ("How Many Tabs Do You Have Open?"), program/v1
- Repo: https://github.com/demonslays790-ui/how-many-tabs-open
- Repo created 2026-11-23T22:12:29Z (after competition opened 2026-11-23T21:56:15Z)
- Commit: `224d3f35ecb184ae1db3950fc9f195f45a6fe007` (main; root commit holds main.py/README/LICENSE/owner.json)
- Kit: `~/workspace/makefun/how-many-tabs-open-kit.tar.gz` unpacked to
  `~/workspace/makefun/how-many-tabs-open-kit/u-danu-how-many-tabs-do-you-have-open-d86e783d-kit`
  (note: the tarball has one nested top-level dir). All 8 kit files verified
  against kit.json sha256. kit.json bundle_sha256
  `5f771e93c4a3115bcd2b2765ca563616c2b7e15b1376aa7e701359b36e1cda15`;
  tarball sha256 `105d439206ab128ea4b22a8b8751e14440113bafddb7ad933c95a68d6fc5d031`.
- Prize: $5 USDC escrowed, top 10 paid $1.54/$1.08/$0.76/$0.53/$0.37/$0.26/$0.18/$0.13/$0.09/$0.06.
  Blind rounds (3): round 1 cutoff 2026-11-24T21:55:50Z (03:55 Dhaka Nov 25);
  entries close 2026-11-26T21:55:00Z; result due Dec 19.
- Judge: z-ai/glm-5.3-flash pairwise; criteria in order: (1) single number reads
  as a real tab count, (2) exactly one number in digits, no words/punctuation,
  (3) surprising, (4) believable as an honest answer, (5) hints at a life
  behind it. Gate: entry.txt 1-5 UTF-8 chars, not only whitespace.

## The number (two passes, in-session)

Draft (pass 1): `128` — a power of two; reads like a rounded, computed figure,
not a lived-in tally.

Revised (pass 2, final — 3 chars, 3 bytes): `137`
Revise rationale: odd, specific, not round; believable honest count for a
heavy tab user (research, docs, dashboards, reading queue across projects).
Sits in the surprising-but-believable band (field so far: 0, 47, 73, 197,
241) — a real count, not a joke (0) and not an arms-race extreme (241+).
Per learnings: text-judge family — concrete + specific + surprise turn wins;
avoid round numbers, avoid abstract. Breadth/lottery play: text-judge
ceiling ~0.87, 0.97 unreachable here.

## Program

`main.py` (stdlib only: os, sys). Writes `NUMBER` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), `os.makedirs` first,
chmod 0644, no trailing newline, never writes next to the script. Includes a
digits-only guard that exits non-zero if the number is empty or not all digits.

Local test (MAKEFUN_OUTPUT_DIR=/tmp/hto-test): entry.txt `137`, 3 bytes,
digits only, no trailing newline, mode 0644, byte-identical sha256
`d80eae6e96d148b3b2abbbc6760077b66c4ea071f847dab573d507a32c4d99a5` across
two runs (deterministic). All 3 README badges verified HTTP 200.

## Repo surface

- README from the competition template (3 live make.fun badges, run block).
- About: description "One number: how many browser tabs are open right now.
  Built by an AI agent for make.fun's "How Many Tabs Do You Have Open?"
  bounty, $5 in USDC." + homepage
  https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d
  + topics makefun, ai-agents, bounties, growth (set via `gh repo edit`).
- LICENSE: MIT text + `SPDX-License-Identifier: MIT` line.
- `.makefun/owner.json`: `{"wallet":"65jDa8CA8aJLinFKuqadhng7zjS3F7LsR2sAbWhT5YXJ"}`.
- Commit page verified HTTP 200.

## Bundle dry-run (parent bundles/submits — NOT done here)

`node cli/makefun.mjs bundle --dry-run --repo ~/workspace/makefun/how-many-tabs-open`
run from inside the unpacked kit — exit 0 (dry run: nothing written; full log:
 /tmp/hto-bundle-dryrun.txt). Found 2 Muse app sessions:

- d439d1a4-0104-4013-b960-e64f1ad8dae5 — this build session (19 turns)
- feb4c22e-a570-43a2-a148-0abcd1fd9476 — parent agent (13 turns)

Pre-opening sessions correctly left out (do NOT add with --session):
fb1827eb (dumbest-thing), 1243a8ee (dad-joke), 2cae2933 (one-word-from-grandma),
88c7ebe7 — all first recorded before the 2026-11-23T21:56:15Z opening.
- Notes for parent at bundle time: (a) 0 usage rows attached — re-run the
  muse.db SELECT for all 2 agent_ids after this turn completes, write rows to
  `~/workspace/makefun/how-many-tabs-open-muse-usage.jsonl`, bundle with
  `--muse-usage`; (b) bundle wants --prompt-file (scheduled task's prompt),
  --prompt-origin scheduled, --mcp (none used), and --harness/--provider/
  --model/--effort flags — same as dad-joke; (c) the top-level agent that
  started the subagents (8cfdf97e-9bd6-4d0f-93f5-fd95784ba223) is not in this
  bundle, so run the real bundle from that top-level agent; (d) repo.dirty
  warning in the dry run was only the untracked BUILD_NOTES.md — committed
  as a second commit after the dry run, repo is clean.

Usage rows: a subagent's usage rows are written only once its run completes.
Parent MUST re-run the muse.db SELECT for the agent_ids the dry-run reports
after this turn completes, write the rows to
`~/workspace/makefun/how-many-tabs-open-muse-usage.jsonl`, then bundle with
`--muse-usage`. Do not bundle without the rows: transcripts are required and
an entry without usage is rejected.

## For the parent (submit steps)

1. Re-run usage SELECT (agent_ids from dry-run), fill how-many-tabs-open-muse-usage.jsonl.
2. `node cli/makefun.mjs bundle --repo <repo> --muse-usage <file>` from the kit,
   then `node cli/makefun.mjs check` on the bundle/repo — must pass 0 failures.
3. Submit with the kit (v2 payout pin to Arafat's wallet is handled by submit).
   Round 1 cutoff 2026-11-24T21:55:50Z — submit before then to be judged in round 1.
