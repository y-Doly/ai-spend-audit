# Tests

## Testing Strategy

The project uses Pytest for validating audit engine behavior and recommendation logic.

---

## Test Coverage

### Audit Engine

Validated:
- savings calculations
- recommendation generation
- tool-specific conditions
- total savings aggregation

---

## Example Test Cases

### ChatGPT

Checks whether Team plans for small teams trigger downgrade recommendations.

### GitHub Copilot

Checks whether Business plans generate optimization suggestions for small developer teams.

### Cursor

Ensures Business plans recommend lower-cost alternatives when team size is small.

### Claude

Validates Team-to-Pro downgrade logic.

### Gemini

Checks Ultra-to-Pro optimization recommendations.

---

## Running Tests

```bash
pytest
