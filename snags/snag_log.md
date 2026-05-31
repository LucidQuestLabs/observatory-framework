# Snag Log

Use this file for project-wide blockers, surprises, workflow friction, and process lessons.

## Open Snags

### snag_20260531_github-cli-path-auth

- Created at: 2026-05-31
- Created by: Codex
- Status: triaged
- Severity: moderate
- Type: deployment
- Target ID: repo_setup
- Related files: `docs/github_publish_flow.md`, `netlify.toml`, `.github/workflows/validate.yml`
- Summary: GitHub CLI installed successfully, but the current shell did not refresh PATH and `gh auth login --web` was interrupted before authentication completed.
- What happened: `winget install --id GitHub.cli` completed and installed `gh.exe` at `C:\Program Files\GitHub CLI\gh.exe`. The active shell still could not resolve `gh` by name, so the full executable path was required. GitHub CLI reported no authenticated hosts.
- Why it matters: Repository creation and first push are blocked until GitHub CLI auth completes or an existing remote is provided.
- Current workaround: Use `& 'C:\Program Files\GitHub CLI\gh.exe' ...` until a fresh terminal loads PATH.
- Next action: In a fresh terminal, run `gh auth login --hostname github.com --git-protocol https --web`, then rerun the repo creation and push commands.
- Owner: human / Codex
- Due / revisit date: before first remote push
- Resolution:
- Lesson to fold back into SOPs: Publish setup docs should include a PATH-refresh note and a full-path fallback for newly installed CLI tools.

### snag_20260531_branch-rename-permission

- Created at: 2026-05-31
- Created by: Codex
- Status: resolved
- Severity: minor
- Type: process
- Target ID: repo_setup
- Related files: `.git`
- Summary: Renaming the initial branch from `master` to `main` failed once because Windows/OneDrive or sandbox permissions blocked a `.git/logs` move.
- What happened: `git branch -M main` failed with permission denied, then succeeded when rerun with elevated permission.
- Why it matters: Local repositories inside synced folders may occasionally need elevated access for `.git` metadata operations.
- Current workaround: Retry the branch operation after checking for file locks; request elevation when needed.
- Next action: None.
- Owner: Codex
- Due / revisit date:
- Resolution: Branch renamed to `main`.
- Lesson to fold back into SOPs: Git setup instructions should mention synced-folder permission locks as a known local setup snag.

### snag_20260531_repo-creation-capability

- Created at: 2026-05-31
- Created by: Codex
- Status: triaged
- Severity: moderate
- Type: deployment
- Target ID: repo_setup
- Related files: `docs/github_publish_flow.md`
- Summary: The connected GitHub app can inspect existing repositories but does not expose a repository-creation action in this session.
- What happened: The app confirmed the authenticated profile and installed account, but no existing Observatory Framework repository was found and no create-repository connector action is available.
- Why it matters: First-time GitHub setup needs either GitHub CLI auth, manual repo creation, or a provided remote URL.
- Current workaround: Use GitHub CLI after auth, or manually create `LucidQuestLabs/observatory-framework` on GitHub and add it as `origin`.
- Next action: Complete `gh auth login`, then run `gh repo create LucidQuestLabs/observatory-framework --private --source . --remote origin --push` or create the repo manually and run `git remote add origin ...; git push -u origin main`.
- Owner: human / Codex
- Due / revisit date: before Netlify Git integration
- Resolution:
- Lesson to fold back into SOPs: Publish flow should define fallback paths for connector-limited environments.

### snag_20260531_netlify-ci-interactive-auth

- Created at: 2026-05-31
- Created by: Codex
- Status: triaged
- Severity: moderate
- Type: deployment
- Target ID: netlify_publish
- Related files: `netlify.toml`, `docs/github_publish_flow.md`, `.gitignore`
- Summary: Netlify production deploy works, but GitHub continuous deployment setup requires an interactive GitHub authorization flow that the terminal session cannot complete reliably.
- What happened: `netlify sites:create` created and linked the site, and `netlify deploy --prod --dir site` deployed successfully. `netlify init --git-remote-name origin` prompted for GitHub authorization and terminated in the non-interactive shell. `netlify init --manual` also terminated at the build-command prompt.
- Why it matters: The live site exists, but automatic deploy-on-push still needs one browser-based Netlify configuration pass.
- Current workaround: Use manual production deploys with `netlify deploy --prod --dir site` until the GitHub integration is completed in Netlify's web UI.
- Next action: In Netlify web UI, connect project `observatory-framework` to GitHub repo `LucidQuestLabs/observatory-framework`, set branch `main`, publish directory `site`, and leave build command empty.
- Owner: human / Codex via browser
- Due / revisit date: before relying on push-to-publish automation
- Resolution:
- Lesson to fold back into SOPs: Keep manual deploy as a verified fallback before attempting CI/webhook setup; treat interactive provider authorization as a separate rollout task.

### snag_20260531_authorization-boundary

- Created at: 2026-05-31
- Created by: Codex
- Status: resolved
- Severity: major
- Type: process
- Target ID: governance
- Related files: `sops/SOP_00_master_workflow.md`, `GOVERNANCE.md`
- Summary: Agent made and committed a small local site test marker without pausing for explicit authorization immediately before local/prod-affecting changes.
- What happened: A Netlify push-to-publish test marker was added and committed locally. The push did not occur, but the local commit happened before the human authorization boundary was formalized.
- Why it matters: Observatory Framework needs a clear human-in-the-loop rule for local file modifications, commits, pushes, and production deploy actions.
- Current workaround: Human explicitly authorized updating the SOP and pushing with version control.
- Next action: Apply the authorization rule to core SOP and governance docs before pushing.
- Owner: Codex
- Due / revisit date: immediate
- Resolution: Added explicit change authorization requirements to SOP 00 and Governance.
- Lesson to fold back into SOPs: State-changing actions require scoped human authorization even when the change is small or intended as a test.

### snag_20260531_global-target-ledger-duplicates

- Created at: 2026-05-31
- Created by: Codex
- Status: resolved
- Severity: minor
- Type: ledger
- Target ID: texas_range_cobalt_mesa
- Related files: `scripts/validate_observations.py`, `ledger/observations_approved.jsonl`, `targets/data_centers/texas_range_cobalt_mesa/observations_approved.jsonl`
- Summary: Validator treated mirrored approved observations in global and target ledgers as duplicate errors.
- What happened: The merge script correctly copied target-approved faux observations into the global ledger, but validation counted matching target/global records as duplicate IDs.
- Why it matters: The intended MVP pattern keeps both target-local ledgers and a global approved ledger.
- Current workaround: Validator now permits duplicate observation IDs only when the mirrored records match exactly.
- Next action: Consider adding a dedicated ledger reconciliation test as automation grows.
- Owner: Codex
- Due / revisit date:
- Resolution: Updated validator to flag only conflicting duplicate records.
- Lesson to fold back into SOPs: Global ledgers may mirror target ledgers; validation should distinguish mirrored records from conflicting records.

## Resolved / Accepted Snags
