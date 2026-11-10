# FinScope

**An open-source learning dashboard for personal finance and public economic data.**

FinScope is an early-stage educational project. It currently includes transparent finance calculators and a small dashboard for selected World Bank indicators.

> FinScope is for education and exploration, not investment, tax, legal, or financial advice.

## Try the live app

**[Open FinScope](https://zoommayank25-cyber-finscope-app-y2omhb.streamlit.app/)**

## Features

- Simple interest calculator
- Compound interest calculator with selectable compounding frequency
- Total investment return calculator
- Inflation-adjusted future cost estimator
- World Bank indicator explorer for selected countries
- CSV export for retrieved observations
- Unit tests for core calculation functions

## Run locally

Python 3.10 or newer is recommended.

```bash
git clone https://github.com/zoommayank25-cyber/finscope.git
cd finscope
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\\Scripts\\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Data source

Economic observations are retrieved from the [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation). The app displays annual observations and does not independently verify or modify source data.

## Contributing

Good first contributions include improving calculator explanations, adding tests, improving accessibility, and adding well-documented public indicators. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Please start with an existing issue or open one to discuss a substantial change.

## Project status

This is an early MVP. See [PROJECT_PLAN.md](PROJECT_PLAN.md) for planned improvements.

## Licence

MIT. See [LICENSE](LICENSE).
