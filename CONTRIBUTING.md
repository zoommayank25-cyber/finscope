# Contributing to FinScope

Thank you for considering a contribution.

## Good first contributions
- Improve explanations in the finance calculators.
- Add tests for edge cases.
- Improve accessibility and mobile layout.
- Add a country or a well-documented public economic indicator.
- Improve error messages and documentation.

## Before you start
1. Search existing issues to avoid duplicates.
2. For a substantial change, open an issue to discuss the approach.
3. Keep pull requests focused on one change.
4. Explain what changed and why.
5. Add or update tests when calculations or data handling change.

## Local development
```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

## Financial calculation standards
- Document the formula and assumptions.
- Use clear units and percentage conventions.
- Add tests for normal, boundary and invalid inputs.
- Do not present educational estimates as personalised financial advice.

## Data standards
- Use reputable, public sources.
- Record the source and indicator identifier.
- Do not silently fill missing observations with zero.
- Respect source terms and attribution requirements.
