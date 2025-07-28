# System Health Monitoring Tool

## Features
- Checks: Disk encryption, OS updates, Antivirus, Sleep settings
- Runs every 30 mins and only sends data when state changes
- Reports to HTTP endpoint (`/api/report`)
- Optional frontend dashboard (React + Tailwind)

## How to Run (Daemon)
```bash
python -m utils.daemon

## Optional Dashboard
```bash
cd dashboard
npm install
npm run dev
