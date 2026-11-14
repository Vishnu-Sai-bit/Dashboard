# KSR Datavizon - TeleCRM Analytics & Executive Intelligence Dashboard

Interactive, self-contained executive analytics portal and counselor workspace built for **KSR Datavizon**, powered by TeleCRM data.

---

## Overview

- **Executive Portal (`index.html`)**:
  - **7 Core Views**:
    1. **Executive Dashboard**: Company-wide KPIs, Lead Funnel, Source Distribution, Counselor Calling Performance, and Revenue & Collection Velocity.
    2. **Lead Analytics**: Stage breakdown, Workable vs. Junk quality ratio, conversion rates by course, and admissions by channel.
    3. **Sales Activity**: Counselor calling volumes, connected calls, talk time, 30-minute first-attempt SLA compliance, and WhatsApp engagement.
    4. **Revenue Dashboard**: Course contribution mix, daily cumulative revenue trajectory, and enrollment fee breakdown.
    5. **Payments**: Transaction-level verified fee records, payment modes (UPI, Net Banking, Cards), and counselor attribution.
    6. **Lead Journey**: Chronological multi-channel timeline explorer (calls, WhatsApp messages, status changes, notes) with instant lead search across all 2,856 leads.
    7. **Data Dictionary**: Business definitions, formulas, and source mappings for all metrics.
  - **Interactive Multi-Filter Engine**: Filter dynamically by Date Range (Today, Yesterday, Last 7 Days, Last 14 Days, This Month, Custom Date Range), Course, Counselor, Lead Source, and Lead Status.

- **Counselor Workspace (`counselor_dashboard.html`)**:
  - Dedicated personal portal tailored for counselors (Nandeeshwar Reddy, Sagar, Chaitanya, Charishma, Satish Reddy, Mahesh Reddy, Pavithra).
  - 7 Personal KPI cards (Assigned Leads, Today's Fresh Leads, Uncalled Queue, Follow-up Tasks, Calls Made, Connect Rate, Conversions & Revenue).
  - 4 Dynamic charts: Hourly Calling & Connect Rate, Pipeline Stage Donut, Course Inquiries & Admissions, and 30-Day Daily Trajectory.
  - Actionable Leads Queue table with status pills and instant name/course search.

---

## Key Metrics (October 2026 Cohort)

- **Total Inbound & Outbound Leads**: 2,856
- **Paid Admissions / Conversions**: 43 (1.51% conversion rate)
- **Verified Collected Revenue**: ₹3,97,000
- **Total Calls Logged**: 4,148
- **Total Call Duration**: 7,746 minutes (~129 hours)

---

## Repository Files

| File | Description |
|---|---|
| `index.html` | Primary standalone Executive Dashboard (ready to open in browser or deploy on GitHub Pages) |
| `counselor_dashboard.html` | Standalone Counselor Workspace |
| `dashboard_data.json` | Master consolidated structured database powering both dashboards |
| `build_exact_dashboard.py` | Python build script for `index.html` |
| `build_counselor_dashboard.py` | Python build script for `counselor_dashboard.html` |
| `process_telecrm_data.py` | ETL pipeline extracting raw TeleCRM CSVs and journey logs into `dashboard_data.json` |
| `README.md` | Documentation and architecture guide |
| `.gitignore` | Ignores local caches and duplicate artifacts |

---

## How to Run & Build

1. **View Dashboards Directly**:
   Double-click `index.html` or `counselor_dashboard.html` to open in any modern web browser. Both files are completely standalone and self-contained with no external server required.

2. **Re-process Data and Rebuild**:
   ```bash
   python process_telecrm_data.py
   python build_exact_dashboard.py
   python build_counselor_dashboard.py
   ```
