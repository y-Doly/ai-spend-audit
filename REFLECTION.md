# Reflection

## Project Overview

AI Spend Audit was built to help startups identify unnecessary spending across multiple AI tools and recommend lower-cost alternatives.

The project combines Flask backend development, frontend UI implementation, database integration, and CI/CD automation.

---

## What Went Well

- Modular project structure improved maintainability
- Flask routing and template rendering became easier over time
- GitHub Actions CI was successfully configured
- Tailwind CSS improved UI development speed
- SQLite integration simplified data persistence

---

## Challenges Faced

### Git and GitHub

Handling merge conflicts and remote synchronization initially caused issues.

### Flask Debugging

Several problems occurred with:
- undefined Jinja variables
- incorrect imports
- routing errors

### SMTP Integration

Email authentication using Gmail SMTP created authentication failures due to app password requirements.

### GitHub Actions

The workflow initially failed because the folder was named:

```text id="jlwmfy"
workflow
