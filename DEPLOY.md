# Deploy FinScope on Streamlit Community Cloud

This guide publishes the app as a public website. You do not need to buy a server.

## Before you start

- A GitHub account with access to this repository.
- The FinScope repository must be public.
- The app entry point is `app.py`.

## Deploy

1. Open https://share.streamlit.io/ and sign in with GitHub.
2. Choose **Create app**.
3. Select repository `zoommayank25-cyber/finscope`.
4. Select branch `main`.
5. Set the main file path to `app.py`.
6. Choose **Deploy** and wait for the build to finish.
7. Open the generated `.streamlit.app` URL and test both the Finance calculators and Economic indicators pages.

## If deployment fails

- Open **Manage app → Logs** and read the first traceback.
- Confirm the app is using Python 3.10 or newer.
- Confirm `requirements.txt` is present at the repository root.
- Do not add API keys: the current World Bank Indicators API integration is public and does not require one.
- If you change dependencies, commit the updated `requirements.txt` and redeploy.

## After it is live

- Add the public app URL to the repository's GitHub **About** website field.
- Add the URL to the README.
- Ask a few people to try the app and report reproducible issues. Do not claim usage numbers until you can measure them.
