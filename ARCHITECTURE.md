# Architecture

## Overview

AI Spend Audit is a Flask-based web application designed to help startups analyze AI software expenses and identify potential savings opportunities.

---

## High-Level Flow

1. User submits AI tool usage data
2. Flask backend processes inputs
3. Audit engine evaluates optimization opportunities
4. Results are rendered dynamically
5. Reports can be shared publicly

---

## Components

### Frontend

- HTML templates
- Tailwind CSS
- JavaScript localStorage persistence

### Backend

- Flask application server
- Routing and request handling
- Audit recommendation engine

### Database

SQLite stores:
- lead information
- audit reports
- recommendations

### Testing

Pytest validates:
- audit logic
- savings calculations
- recommendation outputs

---

## Audit Engine

The audit engine compares:
- selected plans
- number of users
- use case

against pricing assumptions stored in:

```text id="jlwmc2"
data/pricing.json
