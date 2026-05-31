# GitHub Push-to-Publish Flow

This repository is ready for a simple GitHub-to-Netlify deployment flow.

## Local Git Baseline

- Default branch: `main`
- Static publish directory: `site`
- Netlify config: `netlify.toml`
- CI workflow: `.github/workflows/validate.yml`

## Create the GitHub Repository

Create a new GitHub repository under `LucidQuestLabs`, then connect this local repository:

```powershell
git remote add origin https://github.com/LucidQuestLabs/observatory-framework.git
git push -u origin main
```

If you choose a different repository name, replace the remote URL.

If GitHub CLI is installed during the session and `gh` is not yet on PATH, either open a fresh terminal or call it directly:

```powershell
& 'C:\Program Files\GitHub CLI\gh.exe' auth login --hostname github.com --git-protocol https --web
& 'C:\Program Files\GitHub CLI\gh.exe' repo create LucidQuestLabs/observatory-framework --private --source . --remote origin --push
```

Use `--public` instead of `--private` only when the baseline is intentionally public.

## Netlify Setup

In Netlify:

1. Add a new site from Git.
2. Select the GitHub repository.
3. Set the production branch to `main`.
4. Set publish directory to `site`.
5. Leave build command empty.
6. Deploy.

If the site already exists from CLI setup, open project `observatory-framework` in Netlify and connect it to GitHub from the project settings instead of creating a second site.

The included `netlify.toml` already declares:

```toml
[build]
  publish = "site"
  command = ""
```

## Publishing Rules

- Public reports should land in `reports/public/`.
- Run `python scripts/export_public_report.py` to copy public Markdown reports into `site/reports/`.
- Do not place restricted, private, or embargoed sources in `site/`.
- Treat `site/` as public-facing.

## Push Flow

```powershell
python scripts\validate_observations.py
python -m py_compile scripts\validate_observations.py scripts\merge_approved_observations.py scripts\build_dossier.py scripts\source_snapshot_helper.py scripts\export_public_report.py
git status --short
git add .
git commit -m "Describe the corpus update"
git push
```

GitHub Actions will re-run corpus validation after push. Netlify will deploy the static site when the GitHub push reaches `main`.

## Manual Deploy Fallback

If GitHub continuous deployment is not connected yet, publish the current static site directly:

```powershell
& 'C:\Users\bucke\AppData\Roaming\npm\netlify.cmd' deploy --prod --dir site
```

Current project:

- Netlify site: `observatory-framework`
- Production URL: `https://observatory-framework.netlify.app`
- Admin URL: `https://app.netlify.com/projects/observatory-framework`
