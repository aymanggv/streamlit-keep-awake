# GitHub Actions Ping Workflow

This repository includes a GitHub Actions workflow to keep your Streamlit app awake by sending periodic pings.

## Workflow: `ping.yml`

- **Location:** `.github/workflows/ping.yml`
- **Purpose:** Pings your Streamlit app every hour to prevent it from going to sleep.
- **Schedule:** Runs every hour on the hour.
- **Manual trigger:** You can manually trigger the workflow via the "Actions" tab in GitHub.

### Workflow snippet

```yaml
on:
  schedule:
    - cron: '0 * * * *'  # Every hour at minute 0
  workflow_dispatch:      # Enables manual triggering
```

### How to customize
To change the ping interval, update the cron expression. For example:

- Every 30 minutes: '*/30 * * * *'
- Every 10 minutes: '*/10 * * * *'


### Notes
- The cron syntax uses UTC timezone by default.
- Ensure the URL in the workflow is your deployed Streamlit app endpoint.

