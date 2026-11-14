# Generator script for 100% Live TeleCRM Executive Analytics Dashboard
import json
import os

def generate_live_dashboard():
    with open('dashboard_data.json', 'r', encoding='utf-8') as f:
        live_telecrm_data = json.load(f)

    telecrm_live_json = json.dumps(live_telecrm_data)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KSR Datavizon - Executive Dashboard</title>
  
  <!-- Inter Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Chart.js 4.4.1 & Datalabels Plugin -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0/dist/chartjs-plugin-datalabels.min.js"></script>

  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      height: 100%;
      margin: 0;
      padding: 0;
      overflow: hidden; /* Outer viewport locked: only dashboard content area scrolls */
      background-color: #f1f5f9;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #0f172a;
      min-width: 1280px;
    }}

    /* Top Navigation Header (Fixed at top) */
    .dashboard-header {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      padding: 8px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      height: 54px;
      min-height: 54px;
      flex-shrink: 0;
      z-index: 50;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .brand-logo-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .brand-icon {{
      width: 32px;
      height: 32px;
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
      line-height: 1.1;
    }}

    .brand-text .title {{
      font-size: 17px;
      font-weight: 800;
      color: #1e3a8a;
      letter-spacing: -0.5px;
    }}

    .brand-text .subtitle {{
      font-size: 8px;
      font-weight: 700;
      color: #64748b;
      letter-spacing: 1.5px;
    }}

    .header-divider {{
      width: 1px;
      height: 28px;
      background: #e2e8f0;
    }}

    .header-titles h1 {{
      font-size: 17px;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.2;
    }}

    .header-titles p {{
      font-size: 11px;
      color: #64748b;
      font-weight: 500;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    /* Role & Counselor Portal Switcher */
    .role-switcher-box {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: #eff6ff;
      border: 1.5px solid #bfdbfe;
      padding: 5px 13px;
      border-radius: 8px;
      transition: all 0.2s ease;
    }}
    .role-switcher-box:hover {{
      border-color: #3b82f6;
      background: #e0f2fe;
    }}
    .role-switcher-text {{
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }}
    .role-switcher-label {{
      font-size: 8px;
      font-weight: 700;
      color: #2563eb;
      letter-spacing: 0.6px;
      text-transform: uppercase;
    }}
    .role-select {{
      background: transparent;
      border: none;
      font-size: 11.5px;
      font-weight: 700;
      color: #1e3a8a;
      cursor: pointer;
      outline: none;
      padding: 0;
    }}

    /* Data Badge Box */
    .data-as-of-box {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      padding: 6px 12px;
      border-radius: 6px;
    }}

    .data-as-of-box i {{
      color: #1976d2;
      font-size: 14px;
    }}

    .data-as-of-text {{
      display: flex;
      flex-direction: column;
      line-height: 1.2;
    }}

    .data-as-of-text span:first-child {{
      font-size: 9.5px;
      color: #64748b;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}

    .data-as-of-text span:last-child {{
      font-size: 11.5px;
      font-weight: 700;
      color: #0f172a;
    }}

    /* Skill Nation Badge */
    .skill-nation-badge {{
      display: flex;
      align-items: center;
      gap: 9px;
      background: #f0f7ff;
      border: 1px solid #bfdbfe;
      padding: 6px 12px;
      border-radius: 6px;
    }}

    .skill-nation-badge i {{
      color: #1d4ed8;
      font-size: 18px;
    }}

    .skill-nation-text {{
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }}

    .skill-nation-text span:first-child {{
      font-size: 11px;
      font-weight: 800;
      color: #1e3a8a;
      letter-spacing: 0.4px;
    }}

    .skill-nation-text span:last-child {{
      font-size: 9px;
      font-weight: 500;
      color: #2563eb;
    }}

    /* Layout Container (Fixed viewport height) */
    .dashboard-container {{
      display: flex;
      height: calc(100vh - 54px - 44px);
      width: 100%;
      overflow: hidden;
    }}

    /* Left Sidebar: Filters (Fixed/Stationary on Left: ONLY dashboard scrolls!) */
    .sidebar-filters {{
      width: 205px;
      min-width: 205px;
      background: #091b31;
      color: #ffffff;
      padding: 14px 12px 18px 12px;
      display: flex;
      flex-direction: column;
      gap: 11px;
      flex-shrink: 0;
      height: 100%;
      overflow-y: auto;
      z-index: 40;
      box-shadow: 2px 0 6px rgba(0,0,0,0.06);
    }}

    .sidebar-filters::-webkit-scrollbar {{
      width: 4px;
    }}

    .sidebar-filters::-webkit-scrollbar-thumb {{
      background: #1e3a8a;
      border-radius: 4px;
    }}

    .sidebar-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.8px;
      color: #ffffff;
      padding-bottom: 8px;
      border-bottom: 1px solid #1a365d;
    }}



    .filter-item {{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}

    .filter-item label {{
      font-size: 11px;
      font-weight: 600;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .filter-item label i {{
      color: #60a5fa;
      font-size: 11px;
    }}

    .filter-dropdown {{
      width: 100%;
      background: #112846;
      border: 1px solid #23466f;
      color: #f8fafc;
      font-family: inherit;
      font-size: 11.5px;
      padding: 6px 8px;
      border-radius: 4px;
      outline: none;
      cursor: pointer;
      transition: border-color 0.15s;
    }}

    .filter-dropdown:focus {{
      border-color: #38bdf8;
    }}

    .filter-subtext {{
      font-size: 9.5px;
      color: #38bdf8;
      background: #0c213d;
      border: 1px solid #1a365d;
      border-radius: 4px;
      padding: 4px 6px;
      margin-top: 3px;
      text-align: center;
      font-weight: 600;
      line-height: 1.2;
    }}

    .btn-clear-filters {{
      margin-top: 6px;
      background: #142a45;
      border: 1px solid #284b77;
      color: #cbd5e1;
      font-family: inherit;
      font-size: 11px;
      font-weight: 600;
      padding: 7px;
      border-radius: 4px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .btn-clear-filters:hover {{
      background: #1d3b63;
      color: #ffffff;
      border-color: #3b82f6;
    }}

    /* Main Dashboard Content Area (ONLY this area scrolls up and down!) */
    .dashboard-main {{
      flex: 1;
      height: 100%;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 14px 18px 56px 18px;
      background: #f1f5f9;
    }}

    /* View Switcher */
    .view-content {{
      display: none;
    }}

    .view-content.active {{
      display: block;
    }}

    /* Row 1: KPI Cards Grid */
    .kpi-cards-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 10px;
      margin-bottom: 12px;
    }}

    .kpi-card {{
      background: #ffffff;
      border-radius: 6px;
      padding: 10px 12px;
      border: 1px solid #e2e8f0;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }}

    .kpi-icon-wrap {{
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      flex-shrink: 0;
    }}

    .icon-leads {{ background: #2563eb; color: #ffffff; }}
    .icon-conv {{ background: #16a34a; color: #ffffff; }}
    .icon-rev {{ background: #d97706; color: #ffffff; }}
    .icon-rate {{ background: #9333ea; color: #ffffff; }}
    .icon-calls {{ background: #0284c7; color: #ffffff; }}
    .icon-duration {{ background: #dc2626; color: #ffffff; }}

    .kpi-body {{
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }}

    .kpi-label {{
      font-size: 10.5px;
      color: #64748b;
      font-weight: 600;
    }}

    .kpi-value {{
      font-size: 17px;
      font-weight: 800;
      color: #0f172a;
      margin: 2px 0;
    }}

    .kpi-trend {{
      font-size: 9.5px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 3px;
    }}

    .trend-up {{ color: #16a34a; }}
    .trend-down {{ color: #dc2626; }}

    /* Row 2: Leads Trend & Revenue Trend */
    .row-2-charts {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 14px;
    }}

    /* Card Panels */
    .card-panel {{
      background: #ffffff;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
      padding: 10px 14px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
      overflow: hidden;
    }}

    .card-panel[data-dashboard-tab] {{ cursor: pointer; }}

    .card-panel[data-dashboard-tab]:focus-visible {{ outline: 2px solid #2563eb; outline-offset: 2px; }}

    .card-panel-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }}

    .panel-title {{
      font-size: 12px;
      font-weight: 700;
      color: #0f172a;
    }}

    .panel-legend {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .legend-badge {{
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 10px;
      color: #64748b;
      font-weight: 500;
    }}

    .legend-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }}

    .dot-blue {{ background: #1976d2; }}
    .dot-green {{ background: #43a047; }}

    .canvas-container {{
      position: relative;
      width: 100%;
      height: 220px;
    }}

    .canvas-container-row2 {{
      height: 185px;
    }}

    .canvas-container-row3 {{
      height: 255px;
    }}

    .canvas-container-row4 {{
      height: 200px;
    }}

    /* Row 3: Funnel (1.15fr) + Source Donut (1fr) + Counselor Combo (1.2fr) */
    .row-3-charts {{
      display: grid;
      grid-template-columns: 1.18fr 1fr 1.22fr;
      gap: 14px;
      margin-bottom: 14px;
      align-items: stretch;
    }}

    /* Lead Status Funnel Custom Styling (Matches User's Exact Data Table) */
    .funnel-container {{
      display: flex;
      flex-direction: column;
      gap: 3.5px;
      margin-top: 4px;
      min-height: 215px;
      justify-content: space-between;
    }}

    .funnel-row {{
      display: grid;
      grid-template-columns: 142px 1fr 46px;
      align-items: center;
      gap: 6px;
      height: 20px;
    }}

    .funnel-label {{
      font-size: 10.5px;
      font-weight: 600;
      color: #1e293b;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .funnel-bar-track {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 18px;
    }}

    .funnel-bar-block {{
      height: 100%;
      border-radius: 3px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 10px;
      font-weight: 700;
      min-width: 24px;
      transition: width 0.3s ease;
      box-shadow: 0 1px 2px rgba(0,0,0,0.08);
    }}

    .funnel-pct {{
      font-size: 10px;
      font-weight: 600;
      color: #334155;
      text-align: right;
    }}

    .funnel-sub-footer {{
      margin-top: 6px;
      padding-top: 5px;
      border-top: 1px dashed #e2e8f0;
      display: flex;
      justify-content: space-between;
      font-size: 9.5px;
      color: #64748b;
    }}

    /* Row 4: Course Performance Table + Daily Payments + Payment Mode */
    .row-4-charts {{
      display: grid;
      grid-template-columns: 1.15fr 0.95fr 1.1fr;
      gap: 14px;
      margin-bottom: 24px;
      align-items: stretch;
    }}

    /* Custom Tables */
    .table-wrap {{
      overflow-y: auto;
      height: 200px;
    }}

    .compact-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 10px;
    }}

    .compact-table th {{
      background: #f8fafc;
      color: #475569;
      font-weight: 700;
      text-align: left;
      padding: 5px 6px;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 2;
    }}

    .compact-table td {{
      padding: 4.5px 6px;
      border-bottom: 1px solid #f1f5f9;
      color: #1e293b;
      line-height: 1.2;
    }}

    .compact-table tr:hover td {{
      background: #f8fafc;
    }}

    .text-right {{
      text-align: right;
    }}

    .text-center {{
      text-align: center;
    }}

    /* Payment Panel Dual Layout */
    .payment-dual-panel {{
      display: grid;
      grid-template-columns: 1fr 115px;
      gap: 8px;
      align-items: center;
      height: 200px;
    }}

    .payment-donut-side {{
      height: 195px;
      position: relative;
    }}

    .payment-summary-side {{
      background: #f8fafc;
      border-radius: 5px;
      border: 1px solid #e2e8f0;
      padding: 8px 10px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .summary-heading {{
      font-size: 10.5px;
      font-weight: 700;
      color: #1e293b;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 4px;
    }}

    .summary-metric {{
      display: flex;
      flex-direction: column;
    }}

    .summary-metric-lbl {{
      font-size: 9.5px;
      color: #64748b;
      font-weight: 500;
    }}

    .summary-metric-val {{
      font-size: 13.5px;
      font-weight: 800;
      color: #0f172a;
    }}

    .activity-kpi-grid {{
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 10px;
      margin-bottom: 14px;
    }}

    /* Tab 2 to 6 specific grids */
    .tab-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 14px;
    }}

    .tab-grid-3 {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 14px;
      margin-bottom: 14px;
    }}
  
    /* ==========================================================================
       Enhanced Sub-tab KPI Grid & Cards
       ========================================================================== */
    .kpi-grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-bottom: 14px;
    }}
    .kpi-sub-card {{
      background: #ffffff;
      border-radius: 8px;
      padding: 12px 14px;
      border: 1px solid #e2e8f0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      display: flex;
      align-items: center;
      gap: 12px;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}
    .kpi-sub-card:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);
    }}
    .kpi-sub-icon {{
      width: 38px;
      height: 38px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      flex-shrink: 0;
    }}
    .kpi-sub-icon.icon-blue {{ background: #eff6ff; color: #2563eb; }}
    .kpi-sub-icon.icon-green {{ background: #f0fdf4; color: #16a34a; }}
    .kpi-sub-icon.icon-amber {{ background: #fffbeb; color: #d97706; }}
    .kpi-sub-icon.icon-purple {{ background: #faf5ff; color: #9333ea; }}
    .kpi-sub-icon.icon-teal {{ background: #f0fdfa; color: #0d9488; }}
    .kpi-sub-body {{
      display: flex;
      flex-direction: column;
      overflow: hidden;
      min-width: 0;
    }}
    .kpi-sub-label {{
      font-size: 10px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .kpi-sub-value {{
      font-size: 17px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.25;
      margin-top: 2px;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }}
    .kpi-sub-hint {{
      font-size: 9.5px;
      color: #94a3b8;
      font-weight: 500;
      margin-top: 2px;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }}

    /* Leaderboard Visual Enhancements */
    .rank-pill {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      font-size: 10px;
      font-weight: 800;
    }}
    .rank-1 {{ background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }}
    .rank-2 {{ background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }}
    .rank-3 {{ background: #ffedd5; color: #c2410c; border: 1px solid #fed7aa; }}
    .rank-normal {{ background: #f8fafc; color: #64748b; border: 1px solid #e2e8f0; }}

    .prog-bar-container {{
      width: 100%;
      max-width: 90px;
      height: 6px;
      background: #f1f5f9;
      border-radius: 3px;
      overflow: hidden;
      display: inline-block;
      vertical-align: middle;
      margin-left: 6px;
    }}
    .prog-bar-fill {{
      height: 100%;
      border-radius: 3px;
    }}

    /* Quick Filter Pills */
    .pill-filters-bar {{
      display: flex;
      gap: 6px;
      align-items: center;
      flex-wrap: wrap;
      margin-bottom: 12px;
    }}
    .quick-pill-btn {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: #475569;
      padding: 4px 10px;
      border-radius: 14px;
      font-size: 10.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}
    .quick-pill-btn:hover {{
      background: #f8fafc;
      border-color: #94a3b8;
      color: #1e293b;
    }}
    .quick-pill-btn.active {{
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1d4ed8;
      font-weight: 700;
    }}

    /* Table Search and Toolbar */
    .table-toolbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 12px;
    }}
    .table-search-input {{
      width: min(100%, 340px);
      padding: 6px 11px;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font: inherit;
      font-size: 11px;
      color: #0f172a;
      outline: none;
      background: #ffffff;
    }}
    .table-search-input:focus {{
      border-color: #2563eb;
      box-shadow: 0 0 0 2px rgba(37,99,235,0.12);
    }}

    /* Badges */
    .badge-paid {{
      background: #f0fdf4;
      color: #16a34a;
      border: 1px solid #bbf7d0;
      padding: 2px 7px;
      border-radius: 10px;
      font-weight: 700;
      font-size: 10px;
      display: inline-block;
    }}
    .badge-counselor {{
      background: #eff6ff;
      color: #2563eb;
      padding: 2px 7px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 10px;
      display: inline-block;
    }}

  
    /* Bottom Navigation Bar */
    .bottom-tab-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #ffffff;
      border-top: 1px solid #e2e8f0;
      display: flex;
      justify-content: center;
      gap: 8px;
      padding: 6px 16px;
      z-index: 100;
      box-shadow: 0 -2px 6px rgba(0,0,0,0.06);
    }}
    .bottom-btn {{
      background: transparent;
      border: none;
      color: #475569;
      font-family: inherit;
      font-size: 11.5px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .bottom-btn i {{
      font-size: 12px;
    }}
    .bottom-btn:hover {{
      background: #f1f5f9;
      color: #0f172a;
    }}
    .bottom-btn.active {{
      background: #0f2744;
      color: #ffffff;
      font-weight: 700;
    }}

  </style>
</head>
<body>

  <!-- Top Header -->
  <header class="dashboard-header">
    <div class="header-left">
      <div class="brand-logo-wrap">
        <div class="brand-icon">
          <svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <polygon points="10,20 40,20 10,80" fill="#2563eb" />
            <polygon points="40,20 70,20 40,80 10,80" fill="#0284c7" />
            <polygon points="60,20 90,20 60,80 30,80" fill="#f97316" />
          </svg>
        </div>
        <div class="brand-text">
          <span class="title">KSR</span>
          <span class="subtitle">DATAVIZON</span>
        </div>
      </div>

      <div class="header-divider"></div>

      <div class="header-titles">
        <h1 id="dynViewTitle">Executive Dashboard</h1>
        <p>Overview of Leads, Sales & Revenue Performance</p>
      </div>
    </div>

    <div class="header-right">

      <!-- Switch to Dedicated Counselor Workspace -->
      <a href="counselor_dashboard.html" style="display: flex; align-items: center; gap: 6px; background: #f0fdf4; color: #16a34a; border: 1.5px solid #bbf7d0; padding: 6px 12px; border-radius: 8px; font-size: 11px; font-weight: 700; text-decoration: none; transition: all 0.2s ease;">
        <i class="fa-solid fa-headset" style="font-size: 13px;"></i>
        <span>Counselor Workspace &rarr;</span>
      </a>


      
      <!-- Live Data Source Badge -->
      <div class="data-as-of-box">
        <i class="fa-solid fa-database"></i>
        <div class="data-as-of-text">
          <span>Data Source</span>
          <span id="dynDataSource">TeleCRM Live</span>
        </div>
      </div>

      <!-- Data As Of -->
      <div class="data-as-of-box">
        <i class="fa-regular fa-calendar-check"></i>
        <div class="data-as-of-text">
          <span>Data As Of</span>
          <span id="dynDataAsOf">31 Oct 2026 11:59 PM</span>
        </div>
      </div>

      <!-- Skill Nation Badge -->
      <div class="skill-nation-badge">
        <i class="fa-solid fa-building-columns"></i>
        <div class="skill-nation-text">
          <span>THE SKILL NATION</span>
          <span>Shape Your Future</span>
        </div>
      </div>

    </div>
  </header>

  <!-- Layout Container -->
  <div class="dashboard-container">
    
    <!-- Left Sidebar: Filters -->
    <aside class="sidebar-filters">
      <div class="sidebar-title">
        <i class="fa-solid fa-filter"></i>
        <span>FILTERS</span>
        <span id="activeFilterBadge" style="font-size: 9.5px; font-weight: 600; color: #38bdf8; margin-left: auto; background: rgba(56, 189, 248, 0.15); padding: 2px 6px; border-radius: 10px; display: none;"></span>
      </div>

      <!-- Date Range -->
      <div class="filter-item">
        <label><i class="fa-regular fa-calendar"></i> Date Range</label>
        <select id="selDateRange" class="filter-dropdown" onchange="onDateRangeChange()" oninput="onDateRangeChange()">
          <option value="all" selected>This Month</option>
          <option value="today">Today</option>
          <option value="yesterday">Yesterday</option>
          <option value="last7">Last 7 Days</option>
          <option value="last14">Last 14 Days</option>
          <option value="custom">Custom Range</option>
        </select>
        <div class="filter-subtext" id="subtextDate">01 Oct 2026 - 31 Oct 2026</div>
      </div>

      <!-- Custom Date Range Picker Container -->
      <div id="customDateWrap" style="display: none; flex-direction: column; gap: 6px; background: #0c213d; padding: 8px; border-radius: 4px; border: 1px solid #1a365d;">
        <div style="display: flex; flex-direction: column; gap: 2px;">
          <span style="font-size: 9px; color: #94a3b8; font-weight: 700;">FROM DATE:</span>
          <input type="date" id="inputStartDate" value="2026-10-01" class="filter-dropdown" style="padding: 4px 6px; font-size: 11px;" onchange="applyCustomDates()" oninput="applyCustomDates()">
        </div>
        <div style="display: flex; flex-direction: column; gap: 2px;">
          <span style="font-size: 9px; color: #94a3b8; font-weight: 700;">TO DATE:</span>
          <input type="date" id="inputEndDate" value="2026-10-31" class="filter-dropdown" style="padding: 4px 6px; font-size: 11px;" onchange="applyCustomDates()" oninput="applyCustomDates()">
        </div>
      </div>

      <!-- Course -->
      <div class="filter-item">
        <label><i class="fa-solid fa-book-open"></i> Course</label>
        <select id="selCourse" class="filter-dropdown" onchange="applyUserFilters()" oninput="applyUserFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Counselor -->
      <div class="filter-item">
        <label><i class="fa-regular fa-user"></i> Counselor</label>
        <select id="selCounselor" class="filter-dropdown" onchange="applyUserFilters()" oninput="applyUserFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Source -->
      <div class="filter-item">
        <label><i class="fa-solid fa-bullhorn"></i> Source</label>
        <select id="selSource" class="filter-dropdown" onchange="applyUserFilters()" oninput="applyUserFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Lead Status -->
      <div class="filter-item">
        <label><i class="fa-solid fa-list-check"></i> Lead Status</label>
        <select id="selStatus" class="filter-dropdown" onchange="applyUserFilters()" oninput="applyUserFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Reset Filters Button -->
      <button class="btn-clear-filters" onclick="resetAllFilters()">
        <i class="fa-solid fa-rotate-left"></i>
        <span>Clear All Filters</span>
      </button>
    </aside>

    <!-- Main Dashboard Area -->
    <main class="dashboard-main">

      <!-- TAB 1: EXECUTIVE DASHBOARD -->
      <section id="viewExecutive" class="view-content active">

        <!-- Dynamic Filter Notification Banner -->
        <div id="activeFilterBanner" style="display: none; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e40af; padding: 7px 14px; border-radius: 6px; margin-bottom: 12px; font-size: 11px; font-weight: 600; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <i class="fa-solid fa-filter" style="color: #2563eb;"></i>
            <span id="activeFilterBannerText">Filters Applied</span>
          </div>
          <button type="button" onclick="resetAllFilters()" style="background: #2563eb; color: #ffffff; border: none; padding: 3px 10px; border-radius: 4px; font-size: 10px; font-weight: 700; cursor: pointer;">
            Clear Filters
          </button>
        </div>
        
        <!-- Row 1: 6 Top KPI Summary Cards -->
        <div class="kpi-cards-grid">
          
          <!-- 1. Total Leads -->
          <div class="kpi-card">
            <div class="kpi-icon-wrap icon-leads">
              <i class="fa-solid fa-users"></i>
            </div>
            <div class="kpi-body">
              <span class="kpi-label">Total Leads</span>
              <span class="kpi-value" id="kpiLeads">2,856</span>
              <span class="kpi-trend trend-up" id="kpiLeadsTrend">
                <i class="fa-solid fa-arrow-up"></i> 18.3% vs Prior
              </span>
            </div>
          </div>

          <!-- 2. Total Conversions -->
          <div class="kpi-card">
            <div class="kpi-icon-wrap icon-conv">
              <i class="fa-solid fa-circle-check"></i>
            </div>
            <div class="kpi-body">
              <span class="kpi-label">Total Conversions</span>
              <span class="kpi-value" id="kpiConversions">43</span>
              <span class="kpi-trend trend-up" id="kpiConvTrend">
                <i class="fa-solid fa-arrow-up"></i> 23.5% vs Prior
              </span>
            </div>
          </div>

          <!-- 3. Revenue -->
          <div class="kpi-card">
            <div class="kpi-icon-wrap icon-rev">
              <i class="fa-solid fa-sack-dollar"></i>
            </div>
            <div class="kpi-body">
              <span class="kpi-label">Revenue</span>
              <span class="kpi-value" id="kpiRevenue">₹3,97,000</span>
              <span class="kpi-trend trend-up" id="kpiRevTrend">
                <i class="fa-solid fa-arrow-up"></i> 21.7% vs Prior
              </span>
            </div>
          </div>

          <!-- 4. Conversion Rate -->
          <div class="kpi-card">
            <div class="kpi-icon-wrap icon-rate">
              <i class="fa-solid fa-percent"></i>
            </div>
            <div class="kpi-body">
              <span class="kpi-label">Conversion Rate</span>
              <span class="kpi-value" id="kpiConvRate">1.51%</span>
              <span class="kpi-trend trend-up" id="kpiRateTrend">
                <i class="fa-solid fa-arrow-up"></i> 3.2% vs Prior
              </span>
            </div>
          </div>

          <!-- 5. Total Calls -->
          <div class="kpi-card">
            <div class="kpi-icon-wrap icon-calls">
              <i class="fa-solid fa-phone"></i>
            </div>
            <div class="kpi-body">
              <span class="kpi-label">Total Calls</span>
              <span class="kpi-value" id="kpiCalls">4,148</span>
              <span class="kpi-trend trend-up" id="kpiCallsTrend">
                <i class="fa-solid fa-arrow-up"></i> 4,148 Calls
              </span>
            </div>
          </div>

          <!-- 6. Total Call Duration -->
          <div class="kpi-card">
            <div class="kpi-icon-wrap icon-duration">
              <i class="fa-regular fa-clock"></i>
            </div>
            <div class="kpi-body">
              <span class="kpi-label">Total Call Duration</span>
              <span class="kpi-value" id="kpiDuration">7,746 <span style="font-size: 11px; font-weight: 500; color: #64748b;">Mins</span></span>
              <span class="kpi-trend trend-up" id="kpiDurTrend">
                <i class="fa-solid fa-clock"></i> 129 Hours
              </span>
            </div>
          </div>

        </div>

        <!-- Row 2: Leads Trend & Revenue Trend -->
        <div class="row-2-charts">
          
          <div class="card-panel" data-dashboard-tab="Leads" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title" id="titleLeadsTrend">Leads Trend (This Month)</span>
              <div class="panel-legend">
                <div class="legend-badge"><span class="legend-dot dot-blue"></span> Leads</div>
                <div class="legend-badge"><span class="legend-dot dot-green"></span> Conversions</div>
              </div>
            </div>
            <div class="canvas-container canvas-container-row2">
              <canvas id="chartLeadsTrend"></canvas>
            </div>
          </div>

          <div class="card-panel" data-dashboard-tab="Revenue" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title" id="titleRevenueTrend">Revenue Trend (This Month)</span>
            </div>
            <div class="canvas-container canvas-container-row2">
              <canvas id="chartRevenueTrend"></canvas>
            </div>
          </div>

        </div>

        <!-- Row 3: Funnel + Leads by Source + Calls by Counselor -->
        <div class="row-3-charts">
          
          <div class="card-panel" data-dashboard-tab="Leads" role="link" tabindex="0">
            <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
              <span class="panel-title" id="titleFunnelCard">Lead Status Funnel</span>
              <span id="badgeFunnelPeriod" style="font-size: 10px; font-weight: 600; color: #1d4ed8; background: #dbeafe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe;">Today's Fresh Leads</span>
            </div>
            <div class="funnel-container" id="funnelList">
              <!-- Dynamically populated with 9 exact stages -->
            </div>
            <div class="funnel-sub-footer">
              <span><i class="fa-solid fa-hourglass-start" style="color: #f59e0b;"></i> In Queue: <strong style="color: #1e293b;" id="subQueueCount">37 (14.3%)</strong></span>
              <span><i class="fa-solid fa-ban" style="color: #ef4444;"></i> Direct Lost / Junk: <strong style="color: #1e293b;" id="subLostCount">87 (33.6%)</strong></span>
              <span><i class="fa-solid fa-phone-slash" style="color: #64748b;"></i> Not Reachable: <strong style="color: #1e293b;" id="subUnreachCount">3 (1.1%)</strong></span>
            </div>
          </div>

          <div class="card-panel" data-dashboard-tab="Leads" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title">Leads by Source</span>
            </div>
            <div class="canvas-container canvas-container-row3">
              <canvas id="chartSourceDonut"></canvas>
            </div>
          </div>

          <div class="card-panel" data-dashboard-tab="Sales" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title">Calls by Counselor</span>
              <div class="panel-legend">
                <div class="legend-badge"><span class="legend-dot dot-blue"></span> Total Calls</div>
                <div class="legend-badge"><span class="legend-dot dot-green"></span> Total Duration (Mins)</div>
              </div>
            </div>
            <div class="canvas-container canvas-container-row3">
              <canvas id="chartCounselorCombo"></canvas>
            </div>
          </div>

        </div>

        <!-- Row 4: Course Performance + Daily Payments Trend + Payment Mode -->
        <div class="row-4-charts">
          
          <div class="card-panel" data-dashboard-tab="Revenue" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title">Course Performance</span>
            </div>
            <div class="table-wrap">
              <table class="compact-table">
                <thead>
                  <tr>
                    <th>Course</th>
                    <th class="text-right">Leads</th>
                    <th class="text-right">Conversions</th>
                    <th class="text-right">Conversion %</th>
                    <th class="text-right">Revenue</th>
                  </tr>
                </thead>
                <tbody id="tbodyCourses">
                  <!-- Dynamically populated -->
                </tbody>
              </table>
            </div>
          </div>

          <div class="card-panel" data-dashboard-tab="Payments" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title" id="titleDailyPayments">Daily Payments Trend</span>
              <div class="panel-legend">
                <div class="legend-badge"><span class="legend-dot dot-blue"></span> Payments Count</div>
                <div class="legend-badge"><span class="legend-dot dot-green"></span> Revenue</div>
              </div>
            </div>
            <div class="canvas-container canvas-container-row4">
              <canvas id="chartDailyPayments"></canvas>
            </div>
          </div>

          <div class="card-panel" data-dashboard-tab="Payments" role="link" tabindex="0">
            <div class="card-panel-header">
              <span class="panel-title">Payment Mode</span>
            </div>
            <div class="payment-dual-panel">
              <div class="payment-donut-side">
                <canvas id="chartPaymentMode"></canvas>
              </div>
              <div class="payment-summary-side">
                <span class="summary-heading">Payment Summary</span>
                <div class="summary-metric">
                  <span class="summary-metric-lbl">Total Payments</span>
                  <span class="summary-metric-val" id="valSumPayments">14</span>
                </div>
                <div class="summary-metric">
                  <span class="summary-metric-lbl">Total Revenue</span>
                  <span class="summary-metric-val" id="valSumRevenue">₹3.97L</span>
                </div>
                <div class="summary-metric">
                  <span class="summary-metric-lbl">Avg. Order Value</span>
                  <span class="summary-metric-val" id="valSumAvgOrder">₹28,357</span>
                </div>
              </div>
            </div>
          </div>

        </div>

      </section>

      <!-- TAB 2: LEAD ANALYTICS -->
      <section id="viewLeads" class="view-content">
        
        <!-- Lead Intelligence KPI Ribbon -->
        <div class="kpi-grid-4">
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-blue"><i class="fa-solid fa-users"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Filtered Inquiries</span>
              <span class="kpi-sub-value" id="kpiLeadsTabTotal">2,856</span>
              <span class="kpi-sub-hint">Total leads matching filters</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-green"><i class="fa-solid fa-shield-halved"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Workable Lead Rate</span>
              <span class="kpi-sub-value" id="kpiLeadsTabWorkableRate">92.7%</span>
              <span class="kpi-sub-hint">Valid, non-junk inquiries</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-purple"><i class="fa-solid fa-bullseye"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Top Acquisition Channel</span>
              <span class="kpi-sub-value" id="kpiLeadsTabTopChannel">-</span>
              <span class="kpi-sub-hint">Highest volume traffic source</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-teal"><i class="fa-solid fa-book-open"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Top Inquired Course</span>
              <span class="kpi-sub-value" id="kpiLeadsTabTopCourse">-</span>
              <span class="kpi-sub-hint">Most popular student interest</span>
            </div>
          </div>
        </div>

        <div class="tab-grid-2">
          <div class="card-panel">
            <div class="card-panel-header"><span class="panel-title">Lead Stage Distribution</span></div>
            <div class="canvas-container"><canvas id="chartLeadStageBar"></canvas></div>
          </div>
          <div class="card-panel">
            <div class="card-panel-header"><span class="panel-title">Lead Quality (Workable vs Junk)</span></div>
            <div class="canvas-container"><canvas id="chartWorkableDonut"></canvas></div>
          </div>
        </div>
        <div class="card-panel" style="margin-bottom: 14px;">
          <div class="card-panel-header"><span class="panel-title">Lead Source Performance</span></div>
          <div class="canvas-container" style="height: 270px;"><canvas id="chartLeadSourcePerformance"></canvas></div>
        </div>
        <div class="card-panel" style="margin-bottom: 14px;">
          <div class="card-panel-header"><span class="panel-title">Conversion Rate by Course</span><span style="font-size: 10px; color: #64748b;">Top courses by lead volume</span></div>
          <div class="canvas-container" style="height: 300px;"><canvas id="chartCourseConversion"></canvas></div>
        </div>
        <div class="card-panel" style="margin-bottom: 14px;">
          <div class="card-panel-header"><span class="panel-title">Leads vs Admissions by Channel</span><span style="font-size: 10px; color: #64748b;">Admissions are converted leads</span></div>
          <div class="canvas-container" style="height: 280px;"><canvas id="chartChannelAdmissions"></canvas></div>
        </div>
      </section>

      <!-- TAB 3: SALES ACTIVITY -->
      <section id="viewSales" class="view-content">
        <div class="activity-kpi-grid">
          <div class="kpi-card"><div class="kpi-icon-wrap icon-calls"><i class="fa-solid fa-phone"></i></div><div class="kpi-body"><span class="kpi-label">Call Logs</span><span class="kpi-value" id="kpiActivityCalls">0</span></div></div>
          <div class="kpi-card"><div class="kpi-icon-wrap icon-conv"><i class="fa-solid fa-phone-volume"></i></div><div class="kpi-body"><span class="kpi-label">Connected Calls</span><span class="kpi-value" id="kpiActivityConnected">0</span></div></div>
          <div class="kpi-card"><div class="kpi-icon-wrap icon-duration"><i class="fa-solid fa-clock"></i></div><div class="kpi-body"><span class="kpi-label">Call Talk Time</span><span class="kpi-value" id="kpiActivityTalkTime">0m</span></div></div>
          <div class="kpi-card"><div class="kpi-icon-wrap icon-leads"><i class="fa-brands fa-whatsapp"></i></div><div class="kpi-body"><span class="kpi-label">WhatsApp Sent</span><span class="kpi-value" id="kpiActivityWaSent">0</span></div></div>
          <div class="kpi-card"><div class="kpi-icon-wrap icon-rate"><i class="fa-brands fa-whatsapp"></i></div><div class="kpi-body"><span class="kpi-label">WhatsApp Received</span><span class="kpi-value" id="kpiActivityWaReceived">0</span></div></div>
        </div>
        <div class="card-panel" style="margin-bottom: 14px;">
          <div class="card-panel-header"><span class="panel-title">Counselor Calls &amp; Connections</span></div>
          <div class="canvas-container" style="height: 260px;"><canvas id="chartCounselorActivity"></canvas></div>
        </div>
        <div class="tab-grid-2">
          <div class="card-panel">
            <div class="card-panel-header"><span class="panel-title">Call Duration by Counselor</span></div>
            <div class="canvas-container" style="height: 270px;"><canvas id="chartCounselorDuration"></canvas></div>
          </div>
          <div class="card-panel">
            <div class="card-panel-header"><span class="panel-title">30-Minute First Attempt SLA</span></div>
            <div class="canvas-container" style="height: 270px;"><canvas id="chartSlaCompliance"></canvas></div>
          </div>
        </div>
        <div class="card-panel" style="margin-bottom: 14px;">
          <div class="card-panel-header"><span class="panel-title">WhatsApp Messages Trend</span><span style="font-size: 10px; color: #64748b;">Sent and received activity</span></div>
          <div class="canvas-container" style="height: 250px;"><canvas id="chartWhatsAppActivity"></canvas></div>
        </div>
        <div class="card-panel">
          <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span class="panel-title">Counselor Calling & Efficiency Leaderboard</span>
            <span style="font-size: 10px; color: #64748b;">Ranked by outbound calls &amp; talk time</span>
          </div>
          <div class="table-wrap" style="max-height: 480px;">
            <table class="compact-table">
              <thead>
                <tr>
                  <th style="width: 36px; text-align: center;">#</th>
                  <th>Counselor</th>
                  <th class="text-right">Total Calls</th>
                  <th class="text-right">Connected Calls</th>
                  <th class="text-right" style="width: 150px;">Connection Rate</th>
                  <th class="text-right">Total Talk Time</th>
                  <th class="text-right">Avg Call Duration</th>
                </tr>
              </thead>
              <tbody id="tbodyCounselorLeaderboard">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>
        <div class="card-panel" style="margin-top: 14px;">
          <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span class="panel-title">Recent Call &amp; WhatsApp Logs</span>
            <span id="activityLogCount" style="font-size: 10px; color: #64748b;"></span>
          </div>
          <div class="table-toolbar">
            <div class="pill-filters-bar" style="margin-bottom: 0;">
              <button type="button" class="quick-pill-btn active" onclick="filterActivityLogs('ALL', this)"><i class="fa-solid fa-list-check"></i> All Activities</button>
              <button type="button" class="quick-pill-btn" onclick="filterActivityLogs('Call', this)"><i class="fa-solid fa-phone"></i> Calls Only</button>
              <button type="button" class="quick-pill-btn" onclick="filterActivityLogs('WhatsApp', this)"><i class="fa-brands fa-whatsapp"></i> WhatsApp Only</button>
            </div>
            <input type="search" id="searchActivityInput" class="table-search-input" placeholder="Search by lead, counselor, or outcome..." oninput="handleActivitySearch(this.value)">
          </div>
          <div class="table-wrap" style="max-height: 340px;">
            <table class="compact-table">
              <thead><tr><th>Date / Time</th><th>Activity</th><th>Counselor / Agent</th><th>Lead</th><th>Outcome</th><th class="text-right">Duration</th></tr></thead>
              <tbody id="tbodyActivityLogs"></tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 4: REVENUE DASHBOARD -->
      <section id="viewRevenue" class="view-content">
        
        <!-- Revenue Intelligence KPI Ribbon -->
        <div class="kpi-grid-4">
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-green"><i class="fa-solid fa-indian-rupee-sign"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Realized Revenue</span>
              <span class="kpi-sub-value" id="kpiRevTabTotal">₹3,97,000</span>
              <span class="kpi-sub-hint">Total fees realized from admissions</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-blue"><i class="fa-solid fa-user-graduate"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Paid Enrollments</span>
              <span class="kpi-sub-value" id="kpiRevTabPaidCount">43</span>
              <span class="kpi-sub-hint">Total converted students</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-amber"><i class="fa-solid fa-calculator"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Avg Realized Fee</span>
              <span class="kpi-sub-value" id="kpiRevTabAvgFee">₹9,233</span>
              <span class="kpi-sub-hint">Revenue per converted lead</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-purple"><i class="fa-solid fa-circle-check"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Top Revenue Course</span>
              <span class="kpi-sub-value" id="kpiRevTabTopCourse">-</span>
              <span class="kpi-sub-hint">Leading program by fee share</span>
            </div>
          </div>
        </div>

        <div class="tab-grid-2">
          <div class="card-panel">
            <div class="card-panel-header"><span class="panel-title">Revenue by Course Contribution</span></div>
            <div class="canvas-container"><canvas id="chartCourseRevDonut"></canvas></div>
          </div>
          <div class="card-panel">
            <div class="card-panel-header"><span class="panel-title">Daily Cumulative Revenue Trajectory</span></div>
            <div class="canvas-container"><canvas id="chartCumulRevenue"></canvas></div>
          </div>
        </div>

        <!-- Course Revenue Breakdown Table -->
        <div class="card-panel" style="margin-top: 14px;">
          <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span class="panel-title">Course-wise Revenue &amp; Enrollment Breakdown</span>
            <span style="font-size: 10px; color: #64748b;">Financial contribution by training program</span>
          </div>
          <div class="table-wrap" style="max-height: 420px;">
            <table class="compact-table">
              <thead>
                <tr>
                  <th>Course Name</th>
                  <th class="text-right">Paid Enrollments</th>
                  <th class="text-right">Realized Revenue</th>
                  <th class="text-right">Avg Fee / Student</th>
                  <th class="text-right" style="width: 170px;">Revenue Share</th>
                </tr>
              </thead>
              <tbody id="tbodyCourseRevenueTable">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

      </section>

      <!-- TAB 5: PAYMENTS -->
      <section id="viewPayments" class="view-content">
        
        <!-- Payments KPI Ribbon -->
        <div class="kpi-grid-4">
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-green"><i class="fa-solid fa-wallet"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Total Collections</span>
              <span class="kpi-sub-value" id="kpiPayTabTotal">₹3,97,000</span>
              <span class="kpi-sub-hint">Verified bank/gateway receipts</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-blue"><i class="fa-solid fa-receipt"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Transactions</span>
              <span class="kpi-sub-value" id="kpiPayTabCount">14</span>
              <span class="kpi-sub-hint">Logged payment entries</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-amber"><i class="fa-solid fa-coins"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Avg Transaction</span>
              <span class="kpi-sub-value" id="kpiPayTabAvg">₹28,357</span>
              <span class="kpi-sub-hint">Average logged installment</span>
            </div>
          </div>
          <div class="kpi-sub-card">
            <div class="kpi-sub-icon icon-teal"><i class="fa-solid fa-money-bill-transfer"></i></div>
            <div class="kpi-sub-body">
              <span class="kpi-sub-label">Top Payment Mode</span>
              <span class="kpi-sub-value" id="kpiPayTabTopMode">UPI</span>
              <span class="kpi-sub-hint">Most popular transfer channel</span>
            </div>
          </div>
        </div>

        <div class="card-panel">
          <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span class="panel-title">Verified Payment Records</span>
            <span style="font-size: 10px; color: #64748b;">Instant search &amp; payment method filtering</span>
          </div>

          <div class="table-toolbar">
            <div class="pill-filters-bar" style="margin-bottom: 0;">
              <button type="button" class="quick-pill-btn active" onclick="filterPaymentsMode('ALL', this)"><i class="fa-solid fa-layer-group"></i> All Modes</button>
              <button type="button" class="quick-pill-btn" onclick="filterPaymentsMode('UPI', this)"><i class="fa-solid fa-mobile-screen"></i> UPI</button>
              <button type="button" class="quick-pill-btn" onclick="filterPaymentsMode('Razorpay', this)"><i class="fa-solid fa-credit-card"></i> Razorpay</button>
              <button type="button" class="quick-pill-btn" onclick="filterPaymentsMode('Net Banking', this)"><i class="fa-solid fa-building-columns"></i> Net Banking</button>
              <button type="button" class="quick-pill-btn" onclick="filterPaymentsMode('Cash', this)"><i class="fa-solid fa-money-bill"></i> Cash / Other</button>
            </div>
            <input type="search" id="searchPaymentsInput" class="table-search-input" placeholder="Search by student, course, counselor, ID..." oninput="handlePaymentsSearch(this.value)">
          </div>

          <div class="table-wrap" style="max-height: 480px;">
            <table class="compact-table">
              <thead>
                <tr>
                  <th>Payment ID</th>
                  <th>Date</th>
                  <th>Lead Name</th>
                  <th>Enrolled Course</th>
                  <th>Counselor</th>
                  <th>Mode</th>
                  <th class="text-right">Amount</th>
                </tr>
              </thead>
              <tbody id="tbodyPaymentsLog">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 6: DATA DICTIONARY -->
      <section id="viewDataDict" class="view-content">
        <div class="card-panel">
          <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span class="panel-title">TeleCRM Data Fields &amp; KPI Definitions</span>
            <input type="search" id="searchDictInput" class="table-search-input" style="width: 250px;" placeholder="Filter definitions..." oninput="handleDictSearch(this.value)">
          </div>
          <div class="table-wrap" style="max-height: 480px; padding: 12px 6px;">
            <table class="compact-table">
              <thead>
                <tr>
                  <th>Metric / Field</th>
                  <th>Source File & Column</th>
                  <th>Business Definition & Formula</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight: 700;">Total Leads</td>
                  <td><code>telecrm-leads.csv</code> &bull; <code>Lead ID</code></td>
                  <td>Count of all inbound and outbound student inquiries registered in TeleCRM (<strong id="dictTotalLeads">0</strong> total leads in the current loaded dataset).</td>
                </tr>
                <tr>
                  <td style="font-weight: 700;">Total Conversions</td>
                  <td><code>telecrm-leads.csv</code> &bull; <code>Converted</code> / <code>Status</code></td>
                  <td>Leads marked 'Yes' or status 'Opted for Paid Sessions' (<strong id="dictTotalConversions">0</strong> converted leads).</td>
                </tr>
                <tr>
                  <td style="font-weight: 700;">Total Revenue</td>
                  <td><code>telecrm-activities.csv</code> &bull; <code>Payment</code> + Course LTV</td>
                  <td>Sum of recorded enrollment payments in the current loaded dataset (<strong id="dictTotalRevenue">₹0</strong> across <strong id="dictPaymentCount">0</strong> payments).</td>
                </tr>
                <tr>
                  <td style="font-weight: 700;">Conversion Rate</td>
                  <td>KPI Calculation</td>
                  <td><code>(Total Conversions / Total Leads) * 100</code> = <strong id="dictConversionRate">0.00%</strong> for the current loaded dataset.</td>
                </tr>
                <tr>
                  <td style="font-weight: 700;">Total Calls & Duration</td>
                  <td><code>telecrm-activities.csv</code> &bull; <code>Activity: Call</code></td>
                  <td>Sum of recorded calls and talk time in the current loaded dataset (<strong id="dictTotalCalls">0</strong> calls, <strong id="dictTotalDuration">0</strong> minutes).</td>
                </tr>
                <tr>
                  <td style="font-weight: 700;">Lead Status Funnel</td>
                  <td><code>telecrm-leads.csv</code> &bull; <code>Status</code> & <code>Stage</code></td>
                  <td>Progressive sales funnel stages from New -> Contacted -> Follow-up -> Interested -> Demo Scheduled -> Negotiation -> Paid -> Lost.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 7: LEAD JOURNEY -->
      <section id="viewJourney" class="view-content">
        <div class="card-panel" style="margin-bottom: 14px;">
          <div class="card-panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <span class="panel-title"><i class="fa-solid fa-timeline" style="color: #2563eb;"></i> Lead Timeline Explorer</span>
            <span style="font-size: 10px; color: #64748b;">Complete chronological touchpoints &amp; call history</span>
          </div>
          
          <!-- Featured Lead Quick Select Pills -->
          <div style="margin-bottom: 12px;">
            <span style="font-size: 10px; font-weight: 700; color: #475569; display: block; margin-bottom: 6px;">Featured Converted &amp; Active Leads:</span>
            <div class="pill-filters-bar" id="featuredLeadsPills">
              <!-- Dynamically populated -->
            </div>
          </div>

          <label for="journeySearchInput" style="font-size: 10px; font-weight: 700; color: #475569; display: block; margin-bottom: 5px;">Search by Name or TeleCRM Lead ID</label>
          <input id="journeySearchInput" type="search" autocomplete="off" placeholder="Start typing a name or lead ID (e.g. cf11d4)..." style="width: min(100%, 520px); padding: 9px 11px; border: 1px solid #cbd5e1; border-radius: 6px; font: inherit; font-size: 12px; color: #0f172a;">
          <div id="journeySearchResults" style="margin-top: 10px;"></div>
        </div>
        <div id="journeyDetails" class="card-panel">
          <div style="padding: 28px 16px; color: #64748b; text-align: center; font-size: 12px;">Select any lead above or search by name / ID to view their full chronological timeline.</div>
        </div>
      </section>

        </main>
  </div>

  <!-- Bottom Navigation Bar -->
  <footer class="bottom-tab-bar">
    <button type="button" class="bottom-btn active" data-tab-key="Executive" onclick="navTab('Executive', this)">
      <i class="fa-solid fa-chart-line"></i>
      <span>Executive Dashboard</span>
    </button>
    <button type="button" class="bottom-btn" data-tab-key="Leads" onclick="navTab('Leads', this)">
      <i class="fa-solid fa-user-group"></i>
      <span>Lead Analytics</span>
    </button>
    <button type="button" class="bottom-btn" data-tab-key="Sales" onclick="navTab('Sales', this)">
      <i class="fa-solid fa-headset"></i>
      <span>Sales Activity</span>
    </button>
    <button type="button" class="bottom-btn" data-tab-key="Revenue" onclick="navTab('Revenue', this)">
      <i class="fa-solid fa-chart-column"></i>
      <span>Revenue Dashboard</span>
    </button>
    <button type="button" class="bottom-btn" data-tab-key="Payments" onclick="navTab('Payments', this)">
      <i class="fa-solid fa-credit-card"></i>
      <span>Payments</span>
    </button>
    <button type="button" class="bottom-btn" data-tab-key="Journey" onclick="navTab('Journey', this)">
      <i class="fa-solid fa-route"></i>
      <span>Lead Journey</span>
    </button>
    <button type="button" class="bottom-btn" data-tab-key="DataDict" onclick="navTab('DataDict', this)">
      <i class="fa-solid fa-book-open"></i>
      <span>Data Dictionary</span>
    </button>
  </footer>

  <!-- Store Live Dataset Only -->
  <script>
    window.TELECRM_LIVE_DATA = {telecrm_live_json};
  </script>

  <!-- Dashboard JavaScript Logic -->
  <script>
    // Register ChartDataLabels plugin
    if (typeof ChartDataLabels !== 'undefined') {{
      Chart.register(ChartDataLabels);
    }}

    // Global Chart instances
    let chartLeadsTrend = null;
    let chartRevenueTrend = null;
    let chartSourceDonut = null;
    let chartCounselorCombo = null;
    let chartDailyPayments = null;
    let chartPaymentMode = null;
    let chartLeadStageBar = null;
    let chartLeadSourcePerformance = null;
    let chartCourseConversion = null;
    let chartChannelAdmissions = null;
    let chartCounselorActivity = null;
    let chartCounselorDuration = null;
    let chartSlaCompliance = null;
    let chartWhatsAppActivity = null;
    let chartWorkableDonut = null;
    let chartCourseRevDonut = null;
    let chartCumulRevenue = null;
    let selectedJourneyLeadId = '';
    let showAllJourneyEvents = false;

    function escapeHtml(value) {{
      return String(value ?? '').replace(/[&<>"']/g, char => ({{
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
      }}[char]));
    }}

    function formatINR(num) {{
      if (!num && num !== 0) return '₹0';
      return '₹' + Math.round(num).toLocaleString('en-IN');
    }}

    function formatLakhs(num) {{
      if (!num || num === 0) return '₹0';
      if (num >= 100000) {{
        const l = (num / 100000).toFixed(2).replace(/\\.?0+$/, '');
        return '₹' + l + 'L';
      }}
      if (num >= 1000) {{
        const k = (num / 1000).toFixed(1).replace(/\\.0$/, '');
        return '₹' + k + 'K';
      }}
      return '₹' + Math.round(num);
    }}

    function getLocalDateList(startDateStr, endDateStr) {{
      const list = [];
      const [sy, sm, sd] = startDateStr.split('-').map(Number);
      const [ey, em, ed] = endDateStr.split('-').map(Number);
      let cur = new Date(sy, sm - 1, sd, 12, 0, 0);
      const end = new Date(ey, em - 1, ed, 12, 0, 0);
      while (cur <= end) {{
        const y = cur.getFullYear();
        const m = String(cur.getMonth() + 1).padStart(2, '0');
        const d = String(cur.getDate()).padStart(2, '0');
        list.push(`${{y}}-${{m}}-${{d}}`);
        cur.setDate(cur.getDate() + 1);
      }}
      return list;
    }}

    const MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    function formatDayMonthLabel(dateStr) {{
      if (!dateStr) return '';
      const parts = dateStr.split('-');
      if (parts.length < 3) return dateStr;
      const d = parts[2];
      const m = Number(parts[1]);
      return `${{d}} ${{MONTH_NAMES[m - 1]}}`;
    }}

    function getLatestDataBounds() {{
      const t = window.TELECRM_LIVE_DATA;
      if (!t || !t.leads || t.leads.length === 0) return {{ min: '2026-10-01', max: '2026-10-31' }};
      let minD = t.leads[0].date;
      let maxD = t.leads[0].date;
      t.leads.forEach(l => {{
        if (l.date && l.date < minD) minD = l.date;
        if (l.date && l.date > maxD) maxD = l.date;
      }});
      return {{ min: minD, max: maxD }};
    }}

    function addDays(dateStr, days) {{
      const [y, m, d] = dateStr.split('-').map(Number);
      const dt = new Date(y, m - 1, d);
      dt.setDate(dt.getDate() + days);
      const ry = dt.getFullYear();
      const rm = String(dt.getMonth() + 1).padStart(2, '0');
      const rd = String(dt.getDate()).padStart(2, '0');
      return `${{ry}}-${{rm}}-${{rd}}`;
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      populateFilterOptions();
      attachFilterListeners();
      attachDashboardChartNavigation();
      attachJourneyListeners();
      updateDataDictionary();
      renderDashboard();
    }});

    function attachDashboardChartNavigation() {{
      document.querySelectorAll('[data-dashboard-tab]').forEach(panel => {{
        const openRelatedTab = () => navTab(panel.dataset.dashboardTab);
        panel.addEventListener('click', openRelatedTab);
        panel.addEventListener('keydown', event => {{
          if (event.key === 'Enter' || event.key === ' ') {{
            event.preventDefault();
            openRelatedTab();
          }}
        }});
      }});
    }}

    function updateDataDictionary() {{
      const data = window.TELECRM_LIVE_DATA;
      if (!data) return;
      const leads = data.leads || [];
      const calls = data.calls || [];
      const payments = data.payments || [];
      const conversions = leads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions').length;
      const paymentTotal = payments.reduce((sum, p) => sum + (Number(p.amount) || 0), 0);
      const callTotal = calls.reduce((sum, c) => sum + (Number(c.calls) || 0), 0);
      const durationTotal = calls.reduce((sum, c) => sum + (Number(c.duration) || 0), 0);
      const put = (id, value) => {{
        const element = document.getElementById(id);
        if (element) element.textContent = value;
      }};
      put('dictTotalLeads', leads.length.toLocaleString('en-IN'));
      put('dictTotalConversions', conversions.toLocaleString('en-IN'));
      put('dictTotalRevenue', formatINR(paymentTotal));
      put('dictPaymentCount', payments.length.toLocaleString('en-IN'));
      put('dictConversionRate', leads.length ? ((conversions / leads.length) * 100).toFixed(2) + '%' : '0.00%');
      put('dictTotalCalls', callTotal.toLocaleString('en-IN'));
      put('dictTotalDuration', Math.round(durationTotal).toLocaleString('en-IN'));
    }}

    function attachJourneyListeners() {{
      const input = document.getElementById('journeySearchInput');
      const results = document.getElementById('journeySearchResults');
      const details = document.getElementById('journeyDetails');

      function handleSearch() {{
        const allLeads = window.TELECRM_LIVE_DATA?.leads || [];
        const rawQuery = input ? input.value : '';
        const needle = String(rawQuery || '').trim().toLowerCase();

        if (!needle) {{
          selectedJourneyLeadId = '';
          if (results) results.innerHTML = '';
          renderLeadJourney(allLeads);
          return;
        }}

        // 1. Direct Exact ID Match
        const exactIdMatch = allLeads.find(l => String(l.id || '').toLowerCase() === needle);
        if (exactIdMatch) {{
          selectedJourneyLeadId = exactIdMatch.id;
          showAllJourneyEvents = false;
          if (results) {{
            results.innerHTML = `<div style="font-size: 11px; color: #166534; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 7px 12px; border-radius: 6px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
              <span><i class="fa-solid fa-check-circle" style="color: #16a34a; margin-right: 6px;"></i><strong>Exact Match Found:</strong> ${{escapeHtml(exactIdMatch.name || exactIdMatch.id)}} (ID: ${{escapeHtml(exactIdMatch.id)}})</span>
              <span class="badge" style="background: #dcfce7; color: #15803d; font-weight: 700;">${{escapeHtml(exactIdMatch.status)}}</span>
            </div>`;
          }}
          renderLeadJourney(allLeads);
          return;
        }}

        // 2. Search by ID substring, name, or phone across ALL 2,856 dataset leads
        const matches = allLeads.filter(l =>
          String(l.id || '').toLowerCase().includes(needle) ||
          String(l.name || '').toLowerCase().includes(needle)
        );

        if (matches.length === 1) {{
          // Single match -> immediately select and render
          selectedJourneyLeadId = matches[0].id;
          showAllJourneyEvents = false;
          if (results) {{
            results.innerHTML = `<div style="font-size: 11px; color: #166534; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 7px 12px; border-radius: 6px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
              <span><i class="fa-solid fa-user-check" style="color: #16a34a; margin-right: 6px;"></i><strong>1 Match:</strong> ${{escapeHtml(matches[0].name || matches[0].id)}} (ID: ${{escapeHtml(matches[0].id)}})</span>
              <span class="badge" style="background: #dcfce7; color: #15803d; font-weight: 700;">${{escapeHtml(matches[0].status)}}</span>
            </div>`;
          }}
          renderLeadJourney(allLeads);
          return;
        }}

        if (matches.length > 1) {{
          // Multiple matches: auto-display the first match and show selection buttons
          selectedJourneyLeadId = matches[0].id;
          renderJourneySearchResults(matches, rawQuery);
          renderLeadJourney(allLeads);
          return;
        }}

        // No match found
        selectedJourneyLeadId = '';
        if (results) {{
          results.innerHTML = `<div style="font-size: 11.5px; color: #991b1b; background: #fef2f2; border: 1px solid #fecaca; padding: 10px 14px; border-radius: 6px;">
            <i class="fa-solid fa-triangle-exclamation" style="margin-right: 6px;"></i>No lead found in dataset matching "<strong>${{escapeHtml(rawQuery)}}</strong>". Please verify the Lead ID (total ${{allLeads.length.toLocaleString('en-IN')}} leads in dataset).
          </div>`;
        }}
        if (details) {{
          details.innerHTML = `<div style="padding: 32px 16px; color: #64748b; text-align: center; font-size: 12px;">
            No journey data available for "<strong>${{escapeHtml(rawQuery)}}</strong>". Enter a valid Lead ID or click any featured lead above.
          </div>`;
        }}
      }}

      if (input) {{
        input.addEventListener('input', handleSearch);
        input.addEventListener('change', handleSearch);
        input.addEventListener('keydown', (e) => {{
          if (e.key === 'Enter') {{
            e.preventDefault();
            handleSearch();
          }}
        }});
      }}

      if (results) results.addEventListener('click', event => {{
        const button = event.target.closest('[data-journey-id]');
        if (!button) return;
        selectedJourneyLeadId = button.dataset.journeyId;
        showAllJourneyEvents = false;
        if (input) input.value = selectedJourneyLeadId;
        renderLeadJourney(window.TELECRM_LIVE_DATA?.leads || []);
      }});

      if (details) details.addEventListener('click', event => {{
        if (!event.target.closest('[data-show-all-journey]')) return;
        showAllJourneyEvents = true;
        renderLeadJourney(window.TELECRM_LIVE_DATA?.leads || []);
      }});
    }}

    function attachFilterListeners() {{
      const filterIds = ['selDateRange', 'selCourse', 'selCounselor', 'selSource', 'selStatus'];
      filterIds.forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{
          el.addEventListener('change', () => {{
            if (id === 'selDateRange') onDateRangeChange();
            else applyUserFilters();
          }});
          el.addEventListener('input', () => {{
            if (id === 'selDateRange') onDateRangeChange();
            else applyUserFilters();
          }});
        }}
      }});

      ['inputStartDate', 'inputEndDate'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{
          el.addEventListener('change', applyCustomDates);
          el.addEventListener('input', applyCustomDates);
        }}
      }});
    }}

    function populateFilterOptions() {{
      const t = window.TELECRM_LIVE_DATA;
      const selCourse = document.getElementById('selCourse');
      const selCounselor = document.getElementById('selCounselor');
      const selSource = document.getElementById('selSource');
      const selStatus = document.getElementById('selStatus');

      selCourse.innerHTML = '<option value="ALL">All</option>';
      selCounselor.innerHTML = '<option value="ALL">All</option>';
      selSource.innerHTML = '<option value="ALL">All</option>';
      selStatus.innerHTML = '<option value="ALL">All</option>';

      // Courses
      const cCounts = {{}};
      t.leads.forEach(l => {{
        const c = l.course || 'Unknown';
        cCounts[c] = (cCounts[c] || 0) + 1;
      }});
      Object.entries(cCounts)
        .sort((a,b) => b[1] - a[1])
        .forEach(([c, cnt]) => selCourse.add(new Option(`${{c}} (${{cnt}})`, c)));

      // Counselors
      const counsMap = {{}};
      t.leads.forEach(l => {{
        if (l.counselor && l.counselor !== 'Unknown' && l.counselor !== 'Unassigned') {{
          counsMap[l.counselor] = (counsMap[l.counselor] || 0) + 1;
        }}
      }});
      Object.entries(counsMap)
        .sort((a,b) => b[1] - a[1])
        .forEach(([name, cnt]) => selCounselor.add(new Option(`${{name}} (${{cnt}})`, name)));

      // Sources
      const sCounts = {{}};
      t.leads.forEach(l => {{
        const s = l.source || 'Call Logs';
        sCounts[s] = (sCounts[s] || 0) + 1;
      }});
      Object.entries(sCounts)
        .sort((a,b) => b[1] - a[1])
        .forEach(([s, cnt]) => selSource.add(new Option(`${{s}} (${{cnt}})`, s)));

      // Statuses
      const stCounts = {{}};
      t.leads.forEach(l => {{
        const st = l.status || 'New Lead';
        stCounts[st] = (stCounts[st] || 0) + 1;
      }});
      Object.entries(stCounts)
        .sort((a,b) => b[1] - a[1])
        .forEach(([st, cnt]) => selStatus.add(new Option(`${{st}} (${{cnt}})`, st)));
    }}

    function onDateRangeChange() {{
      const val = document.getElementById('selDateRange').value;
      const customWrap = document.getElementById('customDateWrap');
      let pTitle = 'This Month';

      if (val === 'custom') {{
        customWrap.style.display = 'flex';
        applyCustomDates();
        return;
      }} else {{
        customWrap.style.display = 'none';
      }}

      if (val === 'today') {{
        pTitle = 'Today';
      }} else if (val === 'yesterday') {{
        pTitle = 'Yesterday';
      }} else if (val === 'last7') {{
        pTitle = 'Last 7 Days';
      }} else if (val === 'last14') {{
        pTitle = 'Last 14 Days';
      }} else {{
        pTitle = 'This Month';
      }}

      document.getElementById('titleLeadsTrend').textContent = `Leads Trend (${{pTitle}})`;
      document.getElementById('titleRevenueTrend').textContent = `Revenue Trend (${{pTitle}})`;
      renderDashboard();
    }}

    function applyCustomDates() {{
      document.getElementById('titleLeadsTrend').textContent = 'Leads Trend (Custom Range)';
      document.getElementById('titleRevenueTrend').textContent = 'Revenue Trend (Custom Range)';
      renderDashboard();
    }}



    function onCounselorPortalChange() {{
      const portalEl = document.getElementById('selCounselorPortal');
      if (!portalEl) return;
      const selectedRole = portalEl.value;
      const selCounselor = document.getElementById('selCounselor');
      const titleElem = document.getElementById('dynViewTitle');
      const subtitleElem = document.querySelector('.header-titles p');
      const roleIcon = document.getElementById('roleIcon');

      if (selectedRole === 'ALL') {{
        selCounselor.value = 'ALL';
        selCounselor.disabled = false;
        if (titleElem) titleElem.textContent = 'Executive Dashboard';
        if (subtitleElem) subtitleElem.textContent = 'Company-Wide Leads, Sales & Revenue Performance (All Counselors)';
        if (roleIcon) {{
          roleIcon.className = 'fa-solid fa-user-shield';
          roleIcon.style.color = '#2563eb';
        }}
      }} else {{
        selCounselor.value = selectedRole;
        selCounselor.disabled = true; // Lock counselor filter to active counselor
        if (titleElem) titleElem.textContent = `Counselor Dashboard — ${{selectedRole}}`;
        if (subtitleElem) subtitleElem.textContent = `Personal Workspace: Your Assigned Leads, Calls & Conversions`;
        if (roleIcon) {{
          roleIcon.className = 'fa-solid fa-user-tie';
          roleIcon.style.color = '#16a34a';
        }}
      }}

      renderDashboard();
    }}

    function resetAllFilters() {{
      const portalVal = document.getElementById('selCounselorPortal') ? document.getElementById('selCounselorPortal').value : 'ALL';
      const bounds = getLatestDataBounds();
      document.getElementById('selDateRange').value = 'all';
      document.getElementById('customDateWrap').style.display = 'none';
      document.getElementById('inputStartDate').value = bounds.min;
      document.getElementById('inputEndDate').value = bounds.max;
      document.getElementById('selCourse').value = 'ALL';
      if (portalVal === 'ALL') {{
        document.getElementById('selCounselor').value = 'ALL';
        document.getElementById('selCounselor').disabled = false;
      }} else {{
        document.getElementById('selCounselor').value = portalVal;
        document.getElementById('selCounselor').disabled = true;
      }}
      document.getElementById('selSource').value = 'ALL';
      document.getElementById('selStatus').value = 'ALL';
      onDateRangeChange();
    }}

    function applyUserFilters() {{
      renderDashboard();
    }}

    /* ========================================================
       RENDER LIVE TELECRM CSV DATA DASHBOARD
       ======================================================== */
    let cachedFilteredLeads = [];

    function setFunnelMode(mode) {{
      // Retained for backward compatibility
      renderFunnel(cachedFilteredLeads);
    }}

    function renderFunnel(fLeads) {{
      cachedFilteredLeads = fLeads;
      const funnelContainer = document.getElementById('funnelList');
      if (!funnelContainer) return;
      funnelContainer.innerHTML = '';
      
      const bounds = getLatestDataBounds();
      const todayDate = bounds.max; // '2026-10-31'
      const dateRangeVal = document.getElementById('selDateRange') ? document.getElementById('selDateRange').value : 'all';
      const badge = document.getElementById('badgeFunnelPeriod');
      
      // In Funnel Chart, "New" strictly means Today's Fresh Leads
      let targetLeads = fLeads;
      if (dateRangeVal === 'all') {{
        targetLeads = fLeads.filter(l => l.date === todayDate);
        if (badge) badge.textContent = `Today's Fresh Leads (${{targetLeads.length}})`;
      }} else if (dateRangeVal === 'today') {{
        if (badge) badge.textContent = `Today's Fresh Leads (${{targetLeads.length}})`;
      }} else if (dateRangeVal === 'yesterday') {{
        if (badge) badge.textContent = `Yesterday's Leads (${{targetLeads.length}})`;
      }} else if (dateRangeVal === 'last7') {{
        if (badge) badge.textContent = `Last 7 Days Leads (${{targetLeads.length}})`;
      }} else if (dateRangeVal === 'last14') {{
        if (badge) badge.textContent = `Last 14 Days Leads (${{targetLeads.length}})`;
      }} else {{
        if (badge) badge.textContent = `Selected Period (${{targetLeads.length}})`;
      }}
      
      const totalFunnelLeads = targetLeads.length;

      // 9 Exact Stages Matching User's Data Table
      const countNew = totalFunnelLeads;
      const countContacted = targetLeads.filter(l => (l.calls_made > 0)).length;
      const countMissed = targetLeads.filter(l => (l.calls_made || 0) === 0).length;
      const countFollowUp = targetLeads.filter(l => l.status === 'Follow Up' || l.status === 'RNR - Followup').length;
      const countInterested = targetLeads.filter(l => l.status === 'Interested').length;
      const countDemo = targetLeads.filter(l => l.status === 'Enrolled for Free Sessions').length;
      const countNegotiation = targetLeads.filter(l => l.status === 'Priority Lead' || l.status === 'Job Related').length;
      const countPaid = targetLeads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions').length;
      const countLost = targetLeads.filter(l => l.status === 'Lost').length;

      // Sub-Breakdown of Missed / Not Called Yet
      const countFreshQueue = targetLeads.filter(l => (l.calls_made || 0) === 0 && l.status === 'New Lead').length;
      const countDirectLost = targetLeads.filter(l => (l.calls_made || 0) === 0 && l.status === 'Lost').length;
      const countNotReachable = targetLeads.filter(l => (l.calls_made || 0) === 0 && l.status === 'Not Reachable').length;

      const subQElem = document.getElementById('subQueueCount');
      const subLElem = document.getElementById('subLostCount');
      const subUElem = document.getElementById('subUnreachCount');
      if (subQElem) {{
        const qPct = totalFunnelLeads > 0 ? ((countFreshQueue / totalFunnelLeads) * 100).toFixed(1) + '%' : '0%';
        subQElem.textContent = `${{countFreshQueue}} (${{qPct}})`;
      }}
      if (subLElem) {{
        const lPct = totalFunnelLeads > 0 ? ((countDirectLost / totalFunnelLeads) * 100).toFixed(1) + '%' : '0%';
        subLElem.textContent = `${{countDirectLost}} (${{lPct}})`;
      }}
      if (subUElem) {{
        const uPct = totalFunnelLeads > 0 ? ((countNotReachable / totalFunnelLeads) * 100).toFixed(1) + '%' : '0%';
        subUElem.textContent = `${{countNotReachable}} (${{uPct}})`;
      }}

      const stages = [
        {{ name: "Today's Fresh Leads", count: countNew, color: '#0066f5' }},
        {{ name: "Contacted by Counselor", count: countContacted, color: '#0077e6' }},
        {{ name: "Missed / Not Called Yet", count: countMissed, color: '#ea580c' }},
        {{ name: "Follow-up's Scheduled", count: countFollowUp, color: '#0284c7' }},
        {{ name: "Interested Leads", count: countInterested, color: '#16a34a' }},
        {{ name: "Free Session / Demo", count: countDemo, color: '#eab308' }},
        {{ name: "Priority / Negotiation", count: countNegotiation, color: '#f97316' }},
        {{ name: "Paid / Converted Today", count: countPaid, color: '#9333ea' }},
        {{ name: "Total Lost Today", count: countLost, color: '#dc2626' }}
      ];

      stages.forEach(item => {{
        const pct = totalFunnelLeads > 0 ? ((item.count / totalFunnelLeads) * 100).toFixed(1) + '%' : '0%';
        let barWPct = 0;
        if (totalFunnelLeads > 0 && item.count > 0) {{
          const rawPct = (item.count / totalFunnelLeads) * 96;
          barWPct = Math.max(10, Math.round(rawPct));
        }}
        
        const row = document.createElement('div');
        row.className = 'funnel-row';
        row.innerHTML = `
          <span class="funnel-label" title="${{item.name}}">${{item.name}}</span>
          <div class="funnel-bar-track">
            <div class="funnel-bar-block" style="width: ${{item.count > 0 ? barWPct + '%' : '24px'}}; background-color: ${{item.color}};">
              ${{item.count.toLocaleString('en-IN')}}
            </div>
          </div>
          <span class="funnel-pct">${{pct}}</span>
        `;
        funnelContainer.appendChild(row);
      }});
    }}

    function renderDashboard() {{
      const t = window.TELECRM_LIVE_DATA;
      const dateRangeVal = document.getElementById('selDateRange').value;
      const courseVal = document.getElementById('selCourse').value;
      const counselorVal = document.getElementById('selCounselor').value;
      const sourceVal = document.getElementById('selSource').value;
      const statusVal = document.getElementById('selStatus').value;

      const bounds = getLatestDataBounds();
      let startDate = bounds.min;
      let endDate = bounds.max;

      if (dateRangeVal === 'today') {{
        startDate = bounds.max;
        endDate = bounds.max;
      }} else if (dateRangeVal === 'yesterday') {{
        startDate = addDays(bounds.max, -1);
        endDate = addDays(bounds.max, -1);
      }} else if (dateRangeVal === 'last7') {{
        startDate = addDays(bounds.max, -6);
        endDate = bounds.max;
      }} else if (dateRangeVal === 'last14') {{
        startDate = addDays(bounds.max, -13);
        endDate = bounds.max;
      }} else if (dateRangeVal === 'custom') {{
        startDate = document.getElementById('inputStartDate').value || bounds.min;
        endDate = document.getElementById('inputEndDate').value || bounds.max;
        if (startDate > endDate) {{
          const tmp = startDate;
          startDate = endDate;
          endDate = tmp;
        }}
      }}

      // Precompute lookup maps
      const leadMap = {{}};
      t.leads.forEach(l => {{ leadMap[l.id] = l; }});

      // Filter leads
      const fLeads = t.leads.filter(l => {{
        if (l.date < startDate || l.date > endDate) return false;
        if (courseVal !== 'ALL' && l.course !== courseVal) return false;
        if (counselorVal !== 'ALL' && l.counselor !== counselorVal) return false;
        if (sourceVal !== 'ALL' && l.source !== sourceVal) return false;
        if (statusVal !== 'ALL' && l.status !== statusVal) return false;
        return true;
      }});

      const filteredLeadIds = new Set(fLeads.map(l => l.id));

      // Filter calls (dynamically respects date, course, counselor, and source)
      const fCalls = t.calls.filter(c => {{
        if (c.date < startDate || c.date > endDate) return false;
        if (courseVal !== 'ALL' && c.course !== courseVal) return false;
        if (counselorVal !== 'ALL' && c.counselor !== counselorVal) return false;
        if (sourceVal !== 'ALL' && c.source !== sourceVal) return false;
        return true;
      }});

      // Filter payments: verified payments matching active filtered leads
      const fPayments = t.payments.filter(p => filteredLeadIds.has(p.lead_id));
      const portalActivityFilter = document.getElementById('selCounselorPortal')?.value !== 'ALL';
      const hasLeadActivityFilter = portalActivityFilter || courseVal !== 'ALL' || counselorVal !== 'ALL' || sourceVal !== 'ALL' || statusVal !== 'ALL';
      const fActivityEvents = (t.activity_events || []).filter(event =>
        event.date >= startDate && event.date <= endDate && (!hasLeadActivityFilter || filteredLeadIds.has(event.lead_id))
      );

      // Compute KPIs (100% exact from raw Excel columns)
      const totalLeads = fLeads.length;
      
      // Total Conversions matching filters (100% harmonized with Lead Status Funnel Paid row)
      const totalConv = fLeads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions').length;

      // Total verified revenue from active leads
      const totalRev = fLeads.reduce((acc, l) => acc + (Number(l.revenue) || 0), 0);

      const convRate = totalLeads > 0 ? ((totalConv / totalLeads) * 100).toFixed(2) + '%' : '0.00%';
      
      let totalCalls = 0;
      let totalDur = 0;
      if (statusVal !== 'ALL') {{
        totalCalls = fLeads.reduce((acc, l) => acc + (l.calls_made || 0), 0);
        totalDur = Math.round(fLeads.reduce((acc, l) => acc + (l.talk_time || 0), 0));
      }} else {{
        totalCalls = fCalls.reduce((acc, c) => acc + c.calls, 0);
        totalDur = Math.round(fCalls.reduce((acc, c) => acc + c.duration, 0));
      }}

      document.getElementById('kpiLeads').textContent = totalLeads.toLocaleString('en-IN');
      document.getElementById('kpiConversions').textContent = totalConv.toLocaleString('en-IN');
      document.getElementById('kpiRevenue').textContent = formatINR(totalRev);
      document.getElementById('kpiConvRate').textContent = convRate;
      document.getElementById('kpiCalls').textContent = totalCalls.toLocaleString('en-IN');
      document.getElementById('kpiDuration').innerHTML = `${{totalDur.toLocaleString('en-IN')}} <span style="font-size: 11px; font-weight: 500; color: #64748b;">Mins</span>`;

      // Trends labels & titles (resolved first so activeDesc has access to periodLabel)
      let periodLabel = 'This Month';
      let periodTitle = '(This Month)';
      if (dateRangeVal === 'last7') {{ periodLabel = 'Last 7 Days'; periodTitle = '(Last 7 Days)'; }}
      else if (dateRangeVal === 'last14') {{ periodLabel = 'Last 14 Days'; periodTitle = '(Last 14 Days)'; }}
      else if (dateRangeVal === 'today') {{ periodLabel = 'Today'; periodTitle = '(Today)'; }}
      else if (dateRangeVal === 'yesterday') {{ periodLabel = 'Yesterday'; periodTitle = '(Yesterday)'; }}
      else if (dateRangeVal === 'custom') {{ periodLabel = 'Custom Range'; periodTitle = `(${{formatDayMonthLabel(startDate)}} - ${{formatDayMonthLabel(endDate)}})`; }}

      const subtextElem = document.getElementById('subtextDate');
      const tLeadsElem = document.getElementById('titleLeadsTrend');
      const tRevElem = document.getElementById('titleRevenueTrend');

      // Active filters badge in sidebar & banner on top
      const portalVal = document.getElementById('selCounselorPortal') ? document.getElementById('selCounselorPortal').value : 'ALL';
      const isCounselorMode = (portalVal !== 'ALL');
      const isFiltered = isCounselorMode || (dateRangeVal !== 'all') || (courseVal !== 'ALL') || (counselorVal !== 'ALL') || (sourceVal !== 'ALL') || (statusVal !== 'ALL');

      const badgeElem = document.getElementById('activeFilterBadge');
      if (badgeElem) {{
        if (isFiltered) {{
          badgeElem.style.display = 'inline-block';
          badgeElem.textContent = `${{totalLeads.toLocaleString('en-IN')}} Leads`;
        }} else {{
          badgeElem.style.display = 'none';
        }}
      }}

      const bannerElem = document.getElementById('activeFilterBanner');
      const bannerTextElem = document.getElementById('activeFilterBannerText');
      if (bannerElem && bannerTextElem) {{
        if (isCounselorMode) {{
          bannerElem.style.display = 'flex';
          bannerElem.style.background = '#f0fdf4';
          bannerElem.style.borderColor = '#86efac';
          bannerElem.style.color = '#166534';
          const activeDesc = [];
          if (dateRangeVal !== 'all') activeDesc.push(`Period: ${{periodLabel}}`);
          if (courseVal !== 'ALL') activeDesc.push(`Course: ${{courseVal}}`);
          if (sourceVal !== 'ALL') activeDesc.push(`Source: ${{sourceVal}}`);
          if (statusVal !== 'ALL') activeDesc.push(`Status: ${{statusVal}}`);
          const extraInfo = activeDesc.length > 0 ? ` &bull; ${{activeDesc.join(' • ')}}` : '';
          bannerTextElem.innerHTML = `<strong>Counselor Workspace:</strong> Logged in as <strong>${{portalVal}}</strong>${{extraInfo}} &mdash; <strong>${{totalLeads.toLocaleString('en-IN')}}</strong> Leads Assigned, <strong>${{totalConv}}</strong> Conversions, <strong>${{formatINR(totalRev)}}</strong> Revenue`;
        }} else if (isFiltered) {{
          bannerElem.style.display = 'flex';
          bannerElem.style.background = '#eff6ff';
          bannerElem.style.borderColor = '#bfdbfe';
          bannerElem.style.color = '#1e40af';
          const activeDesc = [];
          if (dateRangeVal !== 'all') activeDesc.push(`Period: ${{periodLabel}}`);
          if (courseVal !== 'ALL') activeDesc.push(`Course: ${{courseVal}}`);
          if (counselorVal !== 'ALL') activeDesc.push(`Counselor: ${{counselorVal}}`);
          if (sourceVal !== 'ALL') activeDesc.push(`Source: ${{sourceVal}}`);
          if (statusVal !== 'ALL') activeDesc.push(`Status: ${{statusVal}}`);
          bannerTextElem.innerHTML = `<strong>Active Filter:</strong> ${{activeDesc.join(' &bull; ')}} &mdash; <strong>${{totalLeads.toLocaleString('en-IN')}}</strong> Leads, <strong>${{totalConv}}</strong> Conversions, <strong>${{formatINR(totalRev)}}</strong> Revenue`;
        }} else {{
          bannerElem.style.display = 'none';
        }}
      }}

      document.getElementById('kpiLeadsTrend').innerHTML = `<i class="fa-solid fa-users"></i> ${{totalLeads.toLocaleString('en-IN')}} in ${{periodLabel}}`;
      document.getElementById('kpiConvTrend').innerHTML = `<i class="fa-solid fa-check-circle"></i> ${{totalConv}} Enrolled (${{convRate}})`;
      document.getElementById('kpiRevTrend').innerHTML = `<i class="fa-solid fa-indian-rupee-sign"></i> ${{formatINR(totalRev)}} Verified`;
      document.getElementById('kpiRateTrend').innerHTML = `<i class="fa-solid fa-chart-pie"></i> ${{convRate}} of Total Leads`;
      document.getElementById('kpiCallsTrend').innerHTML = `<i class="fa-solid fa-phone"></i> ${{totalCalls.toLocaleString('en-IN')}} Calls Logged`;
      document.getElementById('kpiDurTrend').innerHTML = `<i class="fa-solid fa-clock"></i> ${{Math.round(totalDur / 60).toLocaleString('en-IN')}} Hours (${{totalDur.toLocaleString('en-IN')}}m)`;

      // Check if a single day is selected (Today, Yesterday, or single Custom Date)
      const isSingleDay = (startDate === endDate);

      const HOUR_LABELS_12H = [
        '12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM',
        '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM',
        '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM',
        '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM'
      ];

      let timelineLabels = [];
      let leadsSeries = [];
      let convSeries = [];
      let revSeries = [];
      let dailyPayCounts = [];

      if (isSingleDay) {{
        timelineLabels = HOUR_LABELS_12H;
        leadsSeries = new Array(24).fill(0);
        convSeries = new Array(24).fill(0);
        revSeries = new Array(24).fill(0);
        dailyPayCounts = new Array(24).fill(0);

        fLeads.forEach(l => {{
          const h = (l.hour !== undefined && l.hour !== null) ? Number(l.hour) : 0;
          if (h >= 0 && h < 24) leadsSeries[h] += 1;
        }});

        t.leads.forEach(l => {{
          if (courseVal !== 'ALL' && l.course !== courseVal) return;
          if (counselorVal !== 'ALL' && l.counselor !== counselorVal) return;
          if (sourceVal !== 'ALL' && l.source !== sourceVal) return;
          if (statusVal !== 'ALL' && l.status !== statusVal) return;
          if (l.converted === 1) {{
            const isMatch = (l.conv_date === startDate) || (!l.conv_date && l.date === startDate);
            if (isMatch) {{
              const h = (l.conv_hour !== undefined && l.conv_hour !== null) ? Number(l.conv_hour) : (Number(l.hour) || 0);
              if (h >= 0 && h < 24) convSeries[h] += 1;
            }}
          }}
        }});

        fPayments.forEach(p => {{
          const h = (p.hour !== undefined && p.hour !== null) ? Number(p.hour) : 0;
          if (h >= 0 && h < 24) {{
            revSeries[h] += (Number(p.amount) || 0);
            dailyPayCounts[h] += 1;
          }}
        }});

        if (subtextElem) subtextElem.textContent = `${{formatDayMonthLabel(startDate)}} 2026 (Hourly Timings)`;
        if (tLeadsElem) tLeadsElem.textContent = `Leads Trend (Hourly - ${{formatDayMonthLabel(startDate)}})`;
        if (tRevElem) tRevElem.textContent = `Revenue Trend (Hourly - ${{formatDayMonthLabel(startDate)}})`;
        const titlePayElem = document.getElementById('titleDailyPayments');
        if (titlePayElem) titlePayElem.textContent = `Hourly Payments Trend (${{formatDayMonthLabel(startDate)}})`;
      }} else {{
        // Multi-day Daily Trends Map (Deterministic & timezone-safe)
        const dateKeys = getLocalDateList(startDate, endDate);
        const dateMap = {{}};
        dateKeys.forEach(k => {{
          dateMap[k] = {{ leads: 0, conv: 0, revenue: 0, calls: 0, duration: 0 }};
        }});

        fLeads.forEach(l => {{
          if (dateMap[l.date]) {{
            dateMap[l.date].leads += 1;
          }}
        }});

        t.leads.forEach(l => {{
          if (courseVal !== 'ALL' && l.course !== courseVal) return;
          if (counselorVal !== 'ALL' && l.counselor !== counselorVal) return;
          if (sourceVal !== 'ALL' && l.source !== sourceVal) return;
          if (statusVal !== 'ALL' && l.status !== statusVal) return;
          if (l.converted === 1) {{
            const cDate = (l.conv_date && dateMap[l.conv_date]) ? l.conv_date : (dateMap[l.date] ? l.date : null);
            if (cDate && dateMap[cDate]) {{
              dateMap[cDate].conv += 1;
            }}
          }}
        }});

        fPayments.forEach(p => {{
          if (dateMap[p.date]) {{
            dateMap[p.date].revenue += (Number(p.amount) || 0);
          }}
        }});

        timelineLabels = dateKeys.map(formatDayMonthLabel);
        leadsSeries = dateKeys.map(k => dateMap[k].leads);
        convSeries = dateKeys.map(k => dateMap[k].conv);
        revSeries = dateKeys.map(k => dateMap[k].revenue);
        dailyPayCounts = dateKeys.map(k => fPayments.filter(p => p.date === k).length);

        if (subtextElem) subtextElem.textContent = `${{formatDayMonthLabel(startDate)}} 2026 - ${{formatDayMonthLabel(endDate)}} 2026`;
        if (tLeadsElem) tLeadsElem.textContent = `Leads Trend ${{periodTitle}}`;
        if (tRevElem) tRevElem.textContent = `Revenue Trend ${{periodTitle}}`;
        const titlePayElem = document.getElementById('titleDailyPayments');
        if (titlePayElem) titlePayElem.textContent = `Daily Payments Trend`;
      }}

      // 1. Leads Trend Chart (Leads above, Conversions below - zero collision!)
      const maxLiveLeadsVal = Math.max(...leadsSeries, 25);
      const ctxLeads = document.getElementById('chartLeadsTrend').getContext('2d');
      if (chartLeadsTrend) chartLeadsTrend.destroy();
      chartLeadsTrend = new Chart(ctxLeads, {{
        type: 'line',
        data: {{
          labels: timelineLabels,
          datasets: [
            {{
              label: 'Leads',
              data: leadsSeries,
              borderColor: '#1976d2',
              backgroundColor: '#1976d2',
              borderWidth: 2,
              pointRadius: isSingleDay ? 3 : (timelineLabels.length > 20 ? 2 : 4),
              pointBackgroundColor: '#1976d2',
              tension: 0.25,
              datalabels: {{
                display: (ctx) => isSingleDay ? (ctx.dataset.data[ctx.dataIndex] > 0) : (timelineLabels.length <= 14 && ctx.dataset.data[ctx.dataIndex] > 0),
                align: 'top',
                offset: 4,
                font: {{ weight: 'bold', size: 9 }},
                color: '#1976d2',
                formatter: (v) => v > 0 ? v : ''
              }}
            }},
            {{
              label: 'Conversions',
              data: convSeries,
              borderColor: '#43a047',
              backgroundColor: '#43a047',
              borderWidth: 2,
              pointRadius: isSingleDay ? 3 : (timelineLabels.length > 20 ? 2 : 4),
              pointBackgroundColor: '#43a047',
              tension: 0.25,
              datalabels: {{
                display: (ctx) => isSingleDay ? (ctx.dataset.data[ctx.dataIndex] > 0) : (timelineLabels.length <= 14 && ctx.dataset.data[ctx.dataIndex] > 0),
                align: 'bottom',
                offset: 4,
                font: {{ weight: 'bold', size: 9 }},
                color: '#2e7d32',
                formatter: (v) => v > 0 ? v : ''
              }}
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                title: (items) => isSingleDay ? `${{items[0].label}} (Timing)` : items[0].label,
                label: (ctx) => ` ${{ctx.dataset.label}}: ${{ctx.raw}}`
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              suggestedMax: Math.round(maxLiveLeadsVal * 1.25),
              ticks: {{ font: {{ size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{
                font: {{ size: 9 }},
                maxTicksLimit: isSingleDay ? 12 : 16
              }}
            }}
          }}
        }}
      }});

      // 2. Revenue Trend Chart (Peak revenue labels, zero-revenue clean)
      const maxLiveRevVal = Math.max(...revSeries, 50000);
      const ctxRev = document.getElementById('chartRevenueTrend').getContext('2d');
      if (chartRevenueTrend) chartRevenueTrend.destroy();
      chartRevenueTrend = new Chart(ctxRev, {{
        type: 'line',
        data: {{
          labels: timelineLabels,
          datasets: [{{
            label: 'Revenue',
            data: revSeries,
            borderColor: '#1976d2',
            backgroundColor: '#1976d2',
            borderWidth: 2,
            pointRadius: isSingleDay ? 3 : (timelineLabels.length > 20 ? 2 : 4),
            pointBackgroundColor: '#1976d2',
            tension: 0.25,
            datalabels: {{
              display: (ctx) => ctx.dataset.data[ctx.dataIndex] > 0,
              align: 'top',
              offset: 4,
              font: {{ weight: 'bold', size: 8.5 }},
              color: '#0f172a',
              formatter: (v) => v > 0 ? formatINR(v) : ''
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                title: (items) => isSingleDay ? `${{items[0].label}} (Timing)` : items[0].label,
                label: (ctx) => 'Revenue: ' + formatINR(ctx.raw)
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              suggestedMax: Math.round(maxLiveRevVal * 1.25),
              ticks: {{
                callback: (v) => v === 0 ? '₹0' : formatLakhs(v),
                font: {{ size: 9 }}
              }},
              grid: {{ color: '#f1f5f9' }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{
                font: {{ size: 9 }},
                maxTicksLimit: isSingleDay ? 12 : 16
              }}
            }}
          }}
        }}
      }});

      // 3. Lead Conversion Pipeline & Status Breakdown
      renderFunnel(fLeads);

      // 4. Leads by Source Donut (Clean Source Names in Legend, Numbers/Pct on Chart)
      const sourceMap = {{}};
      fLeads.forEach(l => {{
        let s = l.source || 'Other Sources';
        sourceMap[s] = (sourceMap[s] || 0) + 1;
      }});

      const allSorted = Object.entries(sourceMap).sort((a,b) => b[1] - a[1]);
      let topSources = allSorted.filter(x => x[0] !== 'Other Sources').slice(0, 5);
      let otherSourcesCount = allSorted.filter(x => !topSources.some(ts => ts[0] === x[0])).reduce((acc, x) => acc + x[1], 0);
      
      let sortedSources = [...topSources];
      if (otherSourcesCount > 0) {{
        sortedSources.push(['Other Sources', otherSourcesCount]);
      }}
      if (sortedSources.length === 0) {{
        sortedSources = [['No Leads', 0]];
      }}
      // Distinct, non-similar colors: Deep Blue, Vivid Orange, Emerald Green, Royal Purple, Rose Pink, Cyan
      const sourceColors = ['#2563eb', '#ea580c', '#16a34a', '#9333ea', '#e11d48', '#0891b2'];
      const totalSrcCount = sortedSources.reduce((a,x) => a + x[1], 0) || 1;

      const ctxSource = document.getElementById('chartSourceDonut').getContext('2d');
      if (chartSourceDonut) chartSourceDonut.destroy();
      chartSourceDonut = new Chart(ctxSource, {{
        type: 'doughnut',
        data: {{
          labels: sortedSources.map(s => s[0]),
          datasets: [{{
            data: sortedSources.map(s => s[1]),
            backgroundColor: sourceColors.slice(0, sortedSources.length),
            borderWidth: 2,
            borderColor: '#ffffff'
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          layout: {{ padding: {{ top: 8, bottom: 8, left: 6, right: 10 }} }},
          plugins: {{
            legend: {{
              position: 'right',
              labels: {{
                boxWidth: 9,
                font: {{ size: 9.5, weight: '500' }},
                padding: 7,
                color: '#334155'
              }}
            }},
            datalabels: {{
              display: (ctx) => {{
                const s = sortedSources[ctx.dataIndex];
                if (!s || s[1] <= 0) return false;
                const pct = s[1] / totalSrcCount;
                return pct >= 0.08; // Only show on slices >= 8% to completely eliminate any overlapping text
              }},
              color: '#ffffff',
              font: (ctx) => {{
                const val = sortedSources[ctx.dataIndex][1];
                const pct = val / totalSrcCount;
                return {{
                  weight: 'bold',
                  size: pct >= 0.20 ? 10 : 8.5
                }};
              }},
              anchor: 'center',
              align: 'center',
              offset: 0,
              textAlign: 'center',
              formatter: (val, ctx) => {{
                const s = sortedSources[ctx.dataIndex];
                if (!s || val <= 0) return '';
                const pct = ((val / totalSrcCount) * 100).toFixed(1);
                return [`${{val}}`, `(${{pct}}%)`];
              }}
            }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => {{
                  const s = sortedSources[ctx.dataIndex];
                  const pct = ((ctx.raw / totalSrcCount) * 100).toFixed(1);
                  return ` ${{s[0]}}: ${{ctx.raw.toLocaleString('en-IN')}} leads (${{pct}}%)`;
                }}
              }}
            }}
          }},
          cutout: '52%'
        }}
      }});

      // 5. Calls by Counselor Dual-Axis Combo (Calls inside bars, Duration above line)
      const counsMap = {{}};
      if (statusVal !== 'ALL') {{
        fLeads.forEach(l => {{
          if (l.counselor) {{
            if (!counsMap[l.counselor]) counsMap[l.counselor] = {{ calls: 0, dur: 0, connected: 0 }};
            counsMap[l.counselor].calls += (l.calls_made || 0);
            counsMap[l.counselor].dur += (l.talk_time || 0);
            counsMap[l.counselor].connected += (l.calls_conn || 0);
          }}
        }});
      }} else {{
        fCalls.forEach(c => {{
          if (!counsMap[c.counselor]) counsMap[c.counselor] = {{ calls: 0, dur: 0, connected: 0 }};
          counsMap[c.counselor].calls += c.calls;
          counsMap[c.counselor].dur += c.duration;
          counsMap[c.counselor].connected += (c.connected || 0);
        }});
      }}

      const allSortedCounselors = Object.entries(counsMap)
        .filter(([n]) => n && n !== 'Unknown' && n !== 'TeleCRM (system)' && n !== 'Unassigned')
        .sort((a,b) => b[1].calls - a[1].calls);
      let sortedCounselors = allSortedCounselors.slice(0, 6);

      if (sortedCounselors.length === 0) {{
        sortedCounselors = [[counselorVal !== 'ALL' ? counselorVal : 'None', {{ calls: 0, dur: 0 }}]];
      }}

      const cNames = sortedCounselors.map(x => x[0].split(' ')[0]);
      const cCalls = sortedCounselors.map(x => x[1].calls);
      const cDur = sortedCounselors.map(x => Math.round(x[1].dur));
      const maxLiveCalls = Math.max(...cCalls, 50);
      const maxLiveDur = Math.max(...cDur, 100);

      const ctxCouns = document.getElementById('chartCounselorCombo').getContext('2d');
      if (chartCounselorCombo) chartCounselorCombo.destroy();
      chartCounselorCombo = new Chart(ctxCouns, {{
        type: 'bar',
        data: {{
          labels: cNames,
          datasets: [
            {{
              type: 'bar',
              label: 'Total Calls',
              data: cCalls,
              backgroundColor: '#1976d2',
              borderRadius: 3,
              barPercentage: 0.48,
            maxBarThickness: 48,
              yAxisID: 'y',
              datalabels: {{
                anchor: 'center',
                align: 'center',
                font: {{ weight: 'bold', size: 9 }},
                color: '#ffffff',
                formatter: (v) => v > 0 ? v : ''
              }}
            }},
            {{
              type: 'line',
              label: 'Total Duration (Mins)',
              data: cDur,
              borderColor: '#43a047',
              backgroundColor: '#43a047',
              borderWidth: 2,
              pointRadius: 4,
              pointBackgroundColor: '#43a047',
              yAxisID: 'y1',
              tension: 0.2,
              datalabels: {{
                anchor: 'end',
                align: 'top',
                offset: 3,
                font: {{ weight: 'bold', size: 9 }},
                color: '#166534',
                formatter: (v) => v > 0 ? v : ''
              }}
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ display: false }} }},
          scales: {{
            y: {{
              beginAtZero: true,
              suggestedMax: Math.round(maxLiveCalls * 1.35),
              ticks: {{ font: {{ size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }},
            y1: {{
              position: 'right',
              beginAtZero: true,
              suggestedMax: Math.round(maxLiveDur * 1.35),
              ticks: {{ font: {{ size: 9 }}, color: '#166534' }},
              grid: {{ drawOnChartArea: false }}
            }},
            x: {{ grid: {{ display: false }}, ticks: {{ font: {{ size: 9 }} }} }}
          }}
        }}
      }});

      // 6. Course Performance Table (Derived directly from filtered leads)
      const cMap = {{}};
      fLeads.forEach(l => {{
        const c = l.course || 'Unknown / General';
        if (!cMap[c]) cMap[c] = {{ leads: 0, conv: 0, rev: 0 }};
        cMap[c].leads += 1;
        if (l.converted === 1 || l.status === 'Opted for Paid Sessions') {{
          cMap[c].conv += 1;
        }}
        cMap[c].rev += (Number(l.revenue) || 0);
      }});

      const tbody = document.getElementById('tbodyCourses');
      tbody.innerHTML = '';
      // Sort specific courses with revenue first, then by lead volume
      const sortedCList = Object.entries(cMap).sort((a,b) => {{
        if (b[1].rev !== a[1].rev) return b[1].rev - a[1].rev;
        return b[1].leads - a[1].leads;
      }});
      
      if (sortedCList.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 22px; color: #94a3b8; font-weight: 500;">No courses match the selected filters</td></tr>';
      }} else {{
        sortedCList.forEach(([courseName, d]) => {{
          const tr = document.createElement('tr');
          const cPct = d.leads > 0 ? ((d.conv / d.leads) * 100).toFixed(1) + '%' : '0.0%';
          tr.innerHTML = `
            <td style="font-weight: 600;" title="${{courseName}}">${{courseName}}</td>
            <td class="text-right">${{d.leads}}</td>
            <td class="text-right">${{d.conv}}</td>
            <td class="text-right">${{cPct}}</td>
            <td class="text-right" style="font-weight: 700;">${{formatINR(d.rev)}}</td>
          `;
          tbody.appendChild(tr);
        }});
      }}

      // 7. Daily / Hourly Payments Trend
      const maxLivePCount = Math.max(...dailyPayCounts, 5);
      const maxLivePRev = Math.max(...revSeries, 50000);

      const ctxPay = document.getElementById('chartDailyPayments').getContext('2d');
      if (chartDailyPayments) chartDailyPayments.destroy();
      chartDailyPayments = new Chart(ctxPay, {{
        type: 'bar',
        data: {{
          labels: timelineLabels,
          datasets: [
            {{
              type: 'bar',
              label: 'Payments Count',
              data: dailyPayCounts,
              backgroundColor: '#1976d2',
              borderRadius: 3,
              barPercentage: isSingleDay ? 0.6 : 0.45,
              yAxisID: 'y',
              datalabels: {{
                anchor: 'end',
                align: 'top',
                offset: 2,
                font: {{ weight: 'bold', size: 8.5 }},
                color: '#1e293b',
                formatter: (v) => v > 0 ? v : ''
              }}
            }},
            {{
              type: 'line',
              label: 'Revenue',
              data: revSeries,
              borderColor: '#43a047',
              backgroundColor: '#43a047',
              borderWidth: 2,
              pointRadius: isSingleDay ? 3 : (timelineLabels.length > 20 ? 2 : 4),
              yAxisID: 'y1',
              datalabels: {{ display: false }}
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                title: (items) => isSingleDay ? `${{items[0].label}} (Timing)` : items[0].label,
                label: (ctx) => ctx.dataset.type === 'bar' ? ` Payments: ${{ctx.raw}}` : ` Revenue: ${{formatINR(ctx.raw)}}`
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              suggestedMax: Math.round(maxLivePCount * 1.3),
              ticks: {{ font: {{ size: 9 }}, stepSize: Math.max(1, Math.round(maxLivePCount/4)) }},
              grid: {{ color: '#f1f5f9' }}
            }},
            y1: {{
              position: 'right',
              beginAtZero: true,
              suggestedMax: Math.round(maxLivePRev * 1.3),
              ticks: {{
                callback: (v) => v === 0 ? '₹0' : formatLakhs(v),
                font: {{ size: 9 }},
                color: '#166534'
              }},
              grid: {{ drawOnChartArea: false }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{
                font: {{ size: 9 }},
                maxTicksLimit: isSingleDay ? 12 : 16
              }}
            }}
          }}
        }}
      }});

      // 8. Payment Mode & Summary (Clean legend with names only, numbers on chart)
      const modeMap = {{ 'UPI': 0, 'Bank Transfer': 0, 'Card': 0, 'Cash': 0 }};
      fPayments.forEach(p => {{
        const m = p.mode || 'UPI';
        modeMap[m] = (modeMap[m] || 0) + (Number(p.amount) || 0);
      }});

      const totalPayModeSum = Object.values(modeMap).reduce((a,b) => a + b, 0) || 1;
      let payModesList = [
        {{ mode: 'UPI', amount: modeMap['UPI'], color: '#2563eb' }},
        {{ mode: 'Bank Transfer', amount: modeMap['Bank Transfer'], color: '#0d9488' }},
        {{ mode: 'Card', amount: modeMap['Card'], color: '#f59e0b' }},
        {{ mode: 'Cash', amount: modeMap['Cash'], color: '#8b5cf6' }}
      ].filter(x => x.amount > 0);

      if (payModesList.length === 0) {{
        payModesList = [{{ mode: 'No Payments', amount: 0, color: '#cbd5e1' }}];
      }}

      const ctxMode = document.getElementById('chartPaymentMode').getContext('2d');
      if (chartPaymentMode) chartPaymentMode.destroy();
      chartPaymentMode = new Chart(ctxMode, {{
        type: 'doughnut',
        data: {{
          labels: payModesList.map(x => x.mode),
          datasets: [{{
            data: payModesList.map(x => x.amount),
            backgroundColor: payModesList.map(x => x.color)
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          layout: {{ padding: {{ top: 8, bottom: 8, left: 6, right: 8 }} }},
          plugins: {{
            legend: {{ position: 'right', labels: {{ boxWidth: 7, font: {{ size: 8.5 }}, padding: 5 }} }},
            datalabels: {{
              display: (ctx) => payModesList[ctx.dataIndex] && payModesList[ctx.dataIndex].amount > 0,
              color: '#ffffff',
              font: {{ weight: 'bold', size: 8 }},
              anchor: 'center',
              align: 'center',
              offset: 0,
              textAlign: 'center',
              formatter: (val, ctx) => {{
                const p = payModesList[ctx.dataIndex];
                if (!p) return '';
                const pct = ((val / totalPayModeSum) * 100).toFixed(1);
                const amtStr = formatLakhs(val);
                if (pct < 6.0) return amtStr;
                return [`${{amtStr}}`, `(${{pct}}%)`];
              }}
            }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => {{
                  const p = payModesList[ctx.dataIndex];
                  const pct = ((ctx.raw / totalPayModeSum) * 100).toFixed(1);
                  return ` ${{p.mode}}: ${{formatINR(ctx.raw)}} (${{pct}}%)`;
                }}
              }}
            }}
          }},
          cutout: '54%'
        }}
      }});

      const sumPayments = fPayments.length;
      const sumRev = fPayments.reduce((acc, p) => acc + (Number(p.amount) || 0), 0);
      const avgVal = sumPayments > 0 ? Math.round(sumRev / sumPayments) : 0;

      document.getElementById('valSumPayments').textContent = sumPayments;
      document.getElementById('valSumRevenue').textContent = formatLakhs(sumRev);
      document.getElementById('valSumAvgOrder').textContent = formatINR(avgVal);

      // Populate Secondary Tabs
      renderSecondaryTabs(fLeads, fCalls, fPayments, fActivityEvents, timelineLabels, cMap, sortedCounselors, allSortedCounselors, revSeries, isSingleDay, startDate, endDate);
    }}

    function renderSecondaryTabs(fLeads, fCalls, fPayments, fActivityEvents, timelineLabels, cMap, sortedCounselors, allSortedCounselors, revSeries, isSingleDay, startDate, endDate) {{
      
      // 0. Lead Tab Intelligence KPIs (Tab 2)
      const kpiLTotal = document.getElementById('kpiLeadsTabTotal');
      if (kpiLTotal) kpiLTotal.textContent = fLeads.length.toLocaleString('en-IN');
      
      const unworkableStatuses = new Set(['Lost', 'Directly Marked Lost', 'Junk / Duplicate', 'Invalid Number', 'Not Interested']);
      const workableCount = fLeads.filter(l => !unworkableStatuses.has(l.status)).length;
      const workableRate = fLeads.length > 0 ? ((workableCount / fLeads.length) * 100).toFixed(1) + '%' : '0.0%';
      const kpiLWorkable = document.getElementById('kpiLeadsTabWorkableRate');
      if (kpiLWorkable) kpiLWorkable.textContent = workableRate;

      const chCounts = {{}};
      fLeads.forEach(l => {{
        const ch = l.source || 'Website / Direct';
        chCounts[ch] = (chCounts[ch] || 0) + 1;
      }});
      const topCh = Object.entries(chCounts).sort((a,b) => b[1] - a[1])[0];
      const kpiLChannel = document.getElementById('kpiLeadsTabTopChannel');
      if (kpiLChannel) kpiLChannel.textContent = topCh ? topCh[0] : 'Website / Direct';

      const crsCounts = {{}};
      fLeads.forEach(l => {{
        const crs = l.course || 'Unspecified';
        crsCounts[crs] = (crsCounts[crs] || 0) + 1;
      }});
      const topCrs = Object.entries(crsCounts).sort((a,b) => b[1] - a[1])[0];
      const kpiLCourse = document.getElementById('kpiLeadsTabTopCourse');
      if (kpiLCourse) kpiLCourse.textContent = topCrs ? topCrs[0] : 'Modern Data Engineering';

      // 1. Source attribution from the filtered lead records.
      const sourceMap = {{}};
      fLeads.forEach(l => {{
        const source = l.source || 'Unknown Source';
        if (!sourceMap[source]) sourceMap[source] = {{ leads: 0, converted: 0, revenue: 0 }};
        sourceMap[source].leads += 1;
        if (l.converted === 1 || l.status === 'Opted for Paid Sessions') sourceMap[source].converted += 1;
        sourceMap[source].revenue += Number(l.revenue) || 0;
      }});
      const rankedSources = Object.entries(sourceMap).sort((a, b) => b[1].leads - a[1].leads);
      const sourceRows = rankedSources.slice(0, 7).map(([name, stats]) => ({{ name, ...stats }}));
      if (rankedSources.length > 7) {{
        const other = rankedSources.slice(7).reduce((sum, [, stats]) => ({{
          leads: sum.leads + stats.leads,
          converted: sum.converted + stats.converted,
          revenue: sum.revenue + stats.revenue
        }}), {{ leads: 0, converted: 0, revenue: 0 }});
        sourceRows.push({{ name: 'Other Sources', ...other }});
      }}

      // --- CHART 1: Lead Source Performance (Horizontal Grouped Bar with Datalabels) ---
      const ctxSourcePerf = document.getElementById('chartLeadSourcePerformance').getContext('2d');
      if (chartLeadSourcePerformance) chartLeadSourcePerformance.destroy();
      chartLeadSourcePerformance = new Chart(ctxSourcePerf, {{
        type: 'bar',
        data: {{
          labels: sourceRows.map(x => x.name),
          datasets: [
            {{
              label: 'Total Inquiries',
              data: sourceRows.map(x => x.leads),
              backgroundColor: '#3b82f6',
              borderRadius: 6,
              barPercentage: 0.65,
            maxBarThickness: 48,
              datalabels: {{
                display: true,
                anchor: 'end',
                align: 'end',
                color: '#475569',
                font: {{ family: 'Inter', size: 9, weight: 700 }},
                formatter: v => v > 0 ? v.toLocaleString('en-IN') : ''
              }}
            }},
            {{
              label: 'Paid Admissions',
              data: sourceRows.map(x => x.converted),
              backgroundColor: '#10b981',
              borderRadius: 6,
              barPercentage: 0.65,
            maxBarThickness: 48,
              datalabels: {{
                display: true,
                anchor: 'end',
                align: 'end',
                color: '#059669',
                font: {{ family: 'Inter', size: 9, weight: 800 }},
                formatter: v => v > 0 ? `${{v}}` : ''
              }}
            }}
          ]
        }},
        options: {{
          indexAxis: 'y',
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ boxWidth: 12, usePointStyle: true, font: {{ family: 'Inter', size: 10, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              titleFont: {{ family: 'Inter', size: 11, weight: 700 }},
              bodyFont: {{ family: 'Inter', size: 10 }},
              callbacks: {{
                afterBody: items => {{
                  const row = sourceRows[items[0].dataIndex];
                  if (!row) return [];
                  const rate = row.leads ? ((row.converted / row.leads) * 100).toFixed(1) : '0.0';
                  return [
                    `Conversion Rate: ${{rate}}%`,
                    `Realized Revenue: ${{formatINR(row.revenue)}}`
                  ];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              beginAtZero: true,
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }},
            y: {{
              ticks: {{ font: {{ family: 'Inter', size: 9.5, weight: 600 }}, color: '#334155' }},
              grid: {{ display: false }}
            }}
          }}
        }}
      }});

      // --- CHART 2: Course Conversion Rate % (Bar Chart with Datalabels) ---
      const courseMap = {{}};
      fLeads.forEach(l => {{
        const course = l.course || 'Unknown Course';
        if (!courseMap[course]) courseMap[course] = {{ leads: 0, converted: 0 }};
        courseMap[course].leads += 1;
        if (l.converted === 1 || l.status === 'Opted for Paid Sessions') courseMap[course].converted += 1;
      }});
      const rankedCourses = Object.entries(courseMap)
        .sort((a, b) => b[1].leads - a[1].leads)
        .slice(0, 8);
      const courseConversionCanvas = document.getElementById('chartCourseConversion');
      if (chartCourseConversion) chartCourseConversion.destroy();
      chartCourseConversion = new Chart(courseConversionCanvas.getContext('2d'), {{
        type: 'bar',
        data: {{
          labels: rankedCourses.map(([course]) => course),
          datasets: [{{
            label: 'Conversion Rate %',
            data: rankedCourses.map(([, stats]) => stats.leads ? Number(((stats.converted / stats.leads) * 100).toFixed(1)) : 0),
            backgroundColor: rankedCourses.map(([, stats]) => {{
              const r = stats.leads ? (stats.converted / stats.leads) * 100 : 0;
              return r >= 5 ? '#10b981' : (r >= 2 ? '#3b82f6' : '#64748b');
            }}),
            borderRadius: 6,
            barPercentage: 0.55,
            maxBarThickness: 48,
            datalabels: {{
              display: true,
              anchor: 'end',
              align: 'top',
              color: '#0f172a',
              font: {{ family: 'Inter', size: 9.5, weight: 800 }},
              formatter: v => v > 0 ? `${{v}}%` : '0%'
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                afterLabel: item => {{
                  const stats = rankedCourses[item.dataIndex]?.[1];
                  return stats ? [
                    `Converted: ${{stats.converted}} students`,
                    `Total Inquiries: ${{stats.leads}}`,
                    `Course Conv Rate: ${{item.raw}}%`
                  ] : [];
                }}
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              ticks: {{ callback: value => `${{value}}%`, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }},
            x: {{
              ticks: {{ autoSkip: false, maxRotation: 20, minRotation: 0, font: {{ family: 'Inter', size: 9, weight: 600 }} }},
              grid: {{ display: false }}
            }}
          }}
        }}
      }});

      // --- CHART 3: Channel Inquiries vs Admissions ---
      const channelCanvas = document.getElementById('chartChannelAdmissions');
      if (chartChannelAdmissions) chartChannelAdmissions.destroy();
      chartChannelAdmissions = new Chart(channelCanvas.getContext('2d'), {{
        type: 'bar',
        data: {{
          labels: sourceRows.map(x => x.name),
          datasets: [
            {{
              label: 'Total Inquiries',
              data: sourceRows.map(x => x.leads),
              backgroundColor: '#94a3b8',
              borderRadius: 6,
              barPercentage: 0.65,
            maxBarThickness: 48,
              datalabels: {{
                display: true,
                anchor: 'end',
                align: 'top',
                color: '#64748b',
                font: {{ family: 'Inter', size: 9, weight: 700 }},
                formatter: v => v > 0 ? v : ''
              }}
            }},
            {{
              label: 'Paid Admissions',
              data: sourceRows.map(x => x.converted),
              backgroundColor: '#8b5cf6',
              borderRadius: 6,
              barPercentage: 0.65,
            maxBarThickness: 48,
              datalabels: {{
                display: true,
                anchor: 'end',
                align: 'top',
                color: '#6d28d9',
                font: {{ family: 'Inter', size: 9.5, weight: 800 }},
                formatter: v => v > 0 ? `${{v}}` : ''
              }}
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ boxWidth: 12, usePointStyle: true, font: {{ family: 'Inter', size: 10, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                afterBody: items => {{
                  const row = sourceRows[items[0].dataIndex];
                  if (!row) return [];
                  const rate = row.leads ? ((row.converted / row.leads) * 100).toFixed(1) : '0.0';
                  return [`Admission Efficiency: ${{rate}}%`];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              ticks: {{ autoSkip: false, maxRotation: 20, minRotation: 0, font: {{ family: 'Inter', size: 9, weight: 600 }} }},
              grid: {{ display: false }}
            }},
            y: {{
              beginAtZero: true,
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }}
          }}
        }}
      }});

      // Call logs and WhatsApp totals from filtered TeleCRM activity records.
      const callKinds = new Set(['Call', 'call', 'Incoming Call', 'Outgoing Call', 'Incoming call', 'Outgoing call', 'Missed incoming call']);
      const activityCallLogs = fActivityEvents.filter(event => callKinds.has(event.activity));
      const activityWaSent = fActivityEvents.filter(event => event.activity === 'WhatsApp sent').length;
      const activityWaReceived = fActivityEvents.filter(event => event.activity === 'WhatsApp received').length;
      let activityTalkTimeSeconds = activityCallLogs.reduce((acc, log) => acc + (Number(log.duration_sec) || Number(log.duration) || 0), 0);
      let activityConnected = activityCallLogs.filter(log => log.connected === true || (Number(log.duration_sec) || 0) > 0).length;
      let totalCallsCount = activityCallLogs.length;
      if (totalCallsCount === 0 && fCalls && fCalls.length > 0) {{
        totalCallsCount = fCalls.reduce((acc, c) => acc + (c.calls || 0), 0);
        activityConnected = fCalls.reduce((acc, c) => acc + (c.connected || 0), 0);
        activityTalkTimeSeconds = Math.round(fCalls.reduce((acc, c) => acc + (c.duration || 0), 0) * 60);
      }}

      const setVal = (id, val) => {{
        const element = document.getElementById(id);
        if (element) element.textContent = val;
      }};
      setVal('kpiActivityCalls', totalCallsCount.toLocaleString('en-IN'));
      setVal('kpiActivityConnected', activityConnected.toLocaleString('en-IN'));
      setVal('kpiActivityTalkTime', `${{Math.round(activityTalkTimeSeconds / 60).toLocaleString('en-IN')}}m`);
      setVal('kpiActivityWaSent', activityWaSent.toLocaleString('en-IN'));
      setVal('kpiActivityWaReceived', activityWaReceived.toLocaleString('en-IN'));

      // --- CHART 4: WhatsApp Messages Trend (Smooth Area Line Chart) ---
      const waDailyMap = {{}};
      timelineLabels.forEach(label => {{
        waDailyMap[label] = {{ sent: 0, received: 0 }};
      }});
      fActivityEvents.forEach(event => {{
        if (event.activity !== 'WhatsApp sent' && event.activity !== 'WhatsApp received') return;
        const rawDate = String(event.date || event.at || '').slice(0, 10);
        const label = formatDayMonthLabel(rawDate);
        if (!waDailyMap[label]) waDailyMap[label] = {{ sent: 0, received: 0 }};
        if (event.activity === 'WhatsApp sent') waDailyMap[label].sent += 1;
        if (event.activity === 'WhatsApp received') waDailyMap[label].received += 1;
      }});
      const waLabels = Object.keys(waDailyMap);
      const waCanvas = document.getElementById('chartWhatsAppActivity');
      if (chartWhatsAppActivity) chartWhatsAppActivity.destroy();
      chartWhatsAppActivity = new Chart(waCanvas.getContext('2d'), {{
        type: 'line',
        data: {{
          labels: waLabels,
          datasets: [
            {{
              label: 'WhatsApp Sent',
              data: waLabels.map(l => waDailyMap[l].sent),
              borderColor: '#4f46e5',
              backgroundColor: 'rgba(79, 70, 229, 0.10)',
              fill: true,
              tension: 0.35,
              borderWidth: 2.5,
              pointRadius: 2.5,
              pointHoverRadius: 6,
              pointBackgroundColor: '#4f46e5',
              datalabels: {{ display: false }}
            }},
            {{
              label: 'WhatsApp Received',
              data: waLabels.map(l => waDailyMap[l].received),
              borderColor: '#10b981',
              backgroundColor: 'rgba(16, 185, 129, 0.10)',
              fill: true,
              tension: 0.35,
              borderWidth: 2.5,
              pointRadius: 2.5,
              pointHoverRadius: 6,
              pointBackgroundColor: '#10b981',
              datalabels: {{ display: false }}
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ boxWidth: 12, usePointStyle: true, font: {{ family: 'Inter', size: 10, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              mode: 'index',
              intersect: false
            }}
          }},
          scales: {{
            x: {{
              ticks: {{ autoSkip: true, maxTicksLimit: isSingleDay ? 8 : 12, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ display: false }}
            }},
            y: {{
              beginAtZero: true,
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }}
          }}
        }}
      }});

      // --- CHART 5: Counselor Calling Activity (Grouped Bar with Connection Labels) ---
      const counselorRows = (allSortedCounselors && allSortedCounselors.length > 0) ? allSortedCounselors : Object.entries(cMap).map(([k, v]) => [k, {{ calls: v.leads || 0, dur: 0, connected: 0 }}]);
      const ctxCounselorActivity = document.getElementById('chartCounselorActivity').getContext('2d');
      if (chartCounselorActivity) chartCounselorActivity.destroy();
      chartCounselorActivity = new Chart(ctxCounselorActivity, {{
        type: 'bar',
        data: {{
          labels: counselorRows.map(([name]) => name),
          datasets: [
            {{
              label: 'Total Calls',
              data: counselorRows.map(([, c]) => c.calls || 0),
              backgroundColor: '#2563eb',
              borderRadius: 6,
              barPercentage: 0.6,
            maxBarThickness: 48,
              datalabels: {{
                display: true,
                anchor: 'end',
                align: 'top',
                color: '#1e40af',
                font: {{ family: 'Inter', size: 9.5, weight: 700 }},
                formatter: v => v > 0 ? v.toLocaleString('en-IN') : ''
              }}
            }},
            {{
              label: 'Connected Calls',
              data: counselorRows.map(([, c]) => c.connected || 0),
              backgroundColor: '#10b981',
              borderRadius: 6,
              barPercentage: 0.6,
            maxBarThickness: 48,
              datalabels: {{
                display: true,
                anchor: 'end',
                align: 'top',
                color: '#047857',
                font: {{ family: 'Inter', size: 9.5, weight: 800 }},
                formatter: (v, ctx) => {{
                  const calls = counselorRows[ctx.dataIndex]?.[1]?.calls || 0;
                  const pct = calls > 0 ? ((v / calls) * 100).toFixed(0) : 0;
                  return v > 0 ? `${{v}} (${{pct}}%)` : '';
                }}
              }}
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{ boxWidth: 12, usePointStyle: true, font: {{ family: 'Inter', size: 10, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                afterBody: items => {{
                  const c = counselorRows[items[0].dataIndex]?.[1];
                  if (!c) return [];
                  const rate = c.calls > 0 ? ((c.connected / c.calls) * 100).toFixed(1) : '0.0';
                  return [`Connection Success Rate: ${{rate}}%`];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              ticks: {{ autoSkip: false, maxRotation: 20, minRotation: 0, font: {{ family: 'Inter', size: 9.5, weight: 600 }} }},
              grid: {{ display: false }}
            }},
            y: {{
              beginAtZero: true,
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }}
          }}
        }}
      }});

      // --- CHART 6: Counselor Talk Time Duration (Horizontal Bar with Hour Callouts) ---
      const ctxCounselorDuration = document.getElementById('chartCounselorDuration').getContext('2d');
      if (chartCounselorDuration) chartCounselorDuration.destroy();
      chartCounselorDuration = new Chart(ctxCounselorDuration, {{
        type: 'bar',
        data: {{
          labels: counselorRows.map(([name]) => name),
          datasets: [{{
            label: 'Talk Time (Mins)',
            data: counselorRows.map(([, c]) => Math.round(c.dur || 0)),
            backgroundColor: '#0284c7',
            borderRadius: 6,
            barPercentage: 0.6,
            maxBarThickness: 48,
            datalabels: {{
              display: true,
              anchor: 'end',
              align: 'right',
              color: '#0369a1',
              font: {{ family: 'Inter', size: 9.5, weight: 800 }},
              formatter: v => {{
                const hrs = (v / 60).toFixed(1);
                return `${{v.toLocaleString('en-IN')}}m (${{hrs}}h)`;
              }}
            }}
          }}]
        }},
        options: {{
          indexAxis: 'y',
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                label: item => {{
                  const m = item.raw;
                  const h = (m / 60).toFixed(1);
                  return ` Talk Time: ${{m.toLocaleString('en-IN')}} minutes (${{h}} hours)`;
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              beginAtZero: true,
              ticks: {{ font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }},
            y: {{
              ticks: {{ font: {{ family: 'Inter', size: 9.5, weight: 600 }} }},
              grid: {{ display: false }}
            }}
          }}
        }}
      }});

      // --- CHART 7: First Call SLA Compliance % (Color Coded with Benchmark) ---
      const counselorSlaData = counselorRows.map(([name, stats]) => {{
        const matched = fLeads.filter(lead => lead.counselor === name);
        const withinSla = matched.filter(lead => lead.sla_status === 'Met' || (typeof lead.sla_minutes === 'number' && lead.sla_minutes <= 30));
        const attempted = matched.filter(lead => lead.sla_eligible && (lead.sla_status === 'Met' || lead.sla_status === 'Breached'));
        const rate = attempted.length > 0 ? Number(((withinSla.length / attempted.length) * 100).toFixed(1)) : 0;
        return {{ name, rate, withinSla: withinSla.length, attempted: attempted.length }};
      }});
      const ctxSla = document.getElementById('chartSlaCompliance').getContext('2d');
      if (chartSlaCompliance) chartSlaCompliance.destroy();
      chartSlaCompliance = new Chart(ctxSla, {{
        type: 'bar',
        data: {{
          labels: counselorSlaData.map(x => x.name),
          datasets: [{{
            label: 'Within 30m SLA %',
            data: counselorSlaData.map(x => x.rate),
            backgroundColor: counselorSlaData.map(x => x.rate >= 80 ? '#10b981' : (x.rate >= 50 ? '#3b82f6' : '#f59e0b')),
            borderRadius: 6,
            barPercentage: 0.55,
            maxBarThickness: 48,
            datalabels: {{
              display: true,
              anchor: 'end',
              align: 'top',
              color: '#0f172a',
              font: {{ family: 'Inter', size: 10, weight: 800 }},
              formatter: v => `${{v}}%`
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                afterLabel: item => {{
                  const row = counselorSlaData[item.dataIndex];
                  return row ? [
                    `Within SLA: ${{row.withinSla}} leads`,
                    `Total Attempted: ${{row.attempted}} leads`,
                    `Benchmark: 80% SLA Target`
                  ] : [];
                }}
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              max: 105,
              ticks: {{ callback: value => `${{value}}%`, font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }},
            x: {{
              ticks: {{ autoSkip: false, maxRotation: 20, minRotation: 0, font: {{ family: 'Inter', size: 9.5, weight: 600 }} }},
              grid: {{ display: false }}
            }}
          }}
        }}
      }});

      // Store events globally for interactive search/filter in activity logs
      window.activeActivityEvents = [...fActivityEvents]
        .filter(event => callKinds.has(event.activity) || event.activity === 'WhatsApp sent' || event.activity === 'WhatsApp received')
        .sort((a, b) => String(b.at).localeCompare(String(a.at)));
      window.activeLeadNamesMap = new Map(fLeads.map(lead => [lead.id, lead.name || lead.id]));
      renderActivityLogsTable();

      // Counselor Leaderboard with Rank, Badges, and Progress Bar (Tab 3)
      const tbodyL = document.getElementById('tbodyCounselorLeaderboard');
      if (tbodyL) {{
        tbodyL.innerHTML = '';
        counselorRows.forEach(([name, c], idx) => {{
          const callsCount = Number(c.calls) || 0;
          const connCalls = Number(c.connected) || 0;
          const connRateNum = callsCount > 0 ? (connCalls / callsCount) * 100 : 0;
          const connPct = connRateNum.toFixed(1) + '%';
          const totalDurMin = Math.round(Number(c.dur) || 0);
          const avgSec = callsCount > 0 ? Math.round((totalDurMin * 60) / callsCount) : 0;
          const avgMinStr = `${{Math.floor(avgSec / 60)}}m ${{avgSec % 60}}s`;
          const barColor = connRateNum >= 50 ? '#16a34a' : (connRateNum >= 30 ? '#2563eb' : '#d97706');
          
          let rankClass = 'rank-normal';
          if (idx === 0) rankClass = 'rank-1';
          else if (idx === 1) rankClass = 'rank-2';
          else if (idx === 2) rankClass = 'rank-3';

          const slaRow = counselorSlaData.find(s => s.name === name);
          const slaPct = slaRow ? `${{slaRow.rate}}%` : '0.0%';

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td style="text-align: center;"><span class="rank-pill ${{rankClass}}">${{idx + 1}}</span></td>
            <td style="font-weight: 700;">${{name}}</td>
            <td class="text-right">${{callsCount.toLocaleString('en-IN')}}</td>
            <td class="text-right">${{connCalls.toLocaleString('en-IN')}}</td>
            <td class="text-right">
              <span style="font-weight: 700; color: ${{barColor}};">${{connPct}}</span>
              <div class="prog-bar-container">
                <div class="prog-bar-fill" style="width: ${{Math.min(100, connRateNum)}}%; background: ${{barColor}};"></div>
              </div>
            </td>
            <td class="text-right">${{totalDurMin.toLocaleString('en-IN')}} mins</td>
            <td class="text-right">${{avgMinStr}}</td>
            <td class="text-right"><span style="font-weight: 600; color: #10b981;">${{slaPct}}</span></td>
          `;
          tbodyL.appendChild(tr);
        }});
        if (counselorRows.length === 0) {{
          tbodyL.innerHTML = '<tr><td colspan="8" class="text-center" style="padding: 22px; color: #94a3b8;">No counselor activity matches the selected filters</td></tr>';
        }}
      }}

      // --- CHART 8: Lead Stage Bar Chart (Categorized Colors & Datalabels) ---
      const stageCounts = {{}};
      fLeads.forEach(l => {{
        const s = l.stage || l.status || 'Unknown';
        stageCounts[s] = (stageCounts[s] || 0) + 1;
      }});
      const sortedStages = Object.entries(stageCounts).sort((a,b) => b[1] - a[1]);
      const ctxStage = document.getElementById('chartLeadStageBar').getContext('2d');
      if (chartLeadStageBar) chartLeadStageBar.destroy();
      const stageColors = sortedStages.map(([st]) => {{
        const s = st.toLowerCase();
        if (s.includes('new')) return '#0ea5e9';
        if (s.includes('contacted') || s.includes('screening')) return '#2563eb';
        if (s.includes('follow')) return '#f59e0b';
        if (s.includes('interested')) return '#10b981';
        if (s.includes('paid') || s.includes('converted')) return '#8b5cf6';
        if (s.includes('lost') || s.includes('junk')) return '#ef4444';
        return '#64748b';
      }});
      chartLeadStageBar = new Chart(ctxStage, {{
        type: 'bar',
        data: {{
          labels: sortedStages.map(x => x[0]),
          datasets: [{{
            label: 'Leads',
            data: sortedStages.map(x => x[1]),
            backgroundColor: stageColors,
            borderRadius: 6,
            barPercentage: 0.6,
            maxBarThickness: 48,
            datalabels: {{
              display: true,
              anchor: 'end',
              align: 'top',
              color: '#1e293b',
              font: {{ family: 'Inter', size: 9.5, weight: 800 }},
              formatter: v => v.toLocaleString('en-IN')
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                afterLabel: item => {{
                  const pct = fLeads.length > 0 ? ((item.raw / fLeads.length) * 100).toFixed(1) : 0;
                  return [`Share of Total Leads: ${{pct}}%`];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              ticks: {{ autoSkip: false, maxRotation: 20, minRotation: 0, font: {{ family: 'Inter', size: 9, weight: 600 }} }},
              grid: {{ display: false }}
            }},
            y: {{
              beginAtZero: true,
              ticks: {{ font: {{ family: 'Inter', size: 9 }} }},
              grid: {{ color: '#f1f5f9' }}
            }}
          }}
        }}
      }});

      // --- CHART 9: Workable vs Junk Donut (Dual-Tone with Percentage Datalabels) ---
      const unworkableCount = fLeads.filter(l => unworkableStatuses.has(l.status)).length;
      const ctxWork = document.getElementById('chartWorkableDonut').getContext('2d');
      if (chartWorkableDonut) chartWorkableDonut.destroy();
      const workTotal = (workableCount + unworkableCount) || 1;
      const workPct = ((workableCount / workTotal) * 100).toFixed(1);
      const lostPct = ((unworkableCount / workTotal) * 100).toFixed(1);
      chartWorkableDonut = new Chart(ctxWork, {{
        type: 'doughnut',
        data: {{
          labels: [`Workable (${{workPct}}%)`, `Lost/Junk (${{lostPct}}%)`],
          datasets: [{{
            data: [workableCount, unworkableCount],
            backgroundColor: ['#10b981', '#f43f5e'],
            borderWidth: 3,
            borderColor: '#ffffff',
            hoverOffset: 4,
            datalabels: {{
              display: true,
              color: '#ffffff',
              font: {{ family: 'Inter', size: 11, weight: 800 }},
              formatter: (v, ctx) => {{
                const p = ((v / workTotal) * 100).toFixed(0);
                return p > 5 ? `${{p}}%` : '';
              }}
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ boxWidth: 12, usePointStyle: true, font: {{ family: 'Inter', size: 10, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                label: item => ` ${{item.label}}: ${{item.raw.toLocaleString('en-IN')}} leads`
              }}
            }}
          }},
          cutout: '62%'
        }}
      }});

      // 4. Revenue Intelligence Ribbon & Course Breakdown (Tab 4)
      const totalRevVal = fLeads.reduce((acc, l) => acc + (Number(l.revenue) || 0), 0);
      const paidLeadsList = fLeads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions');
      const paidCount = paidLeadsList.length;
      const avgFeeVal = paidCount > 0 ? Math.round(totalRevVal / paidCount) : 0;
      
      const courseRevMap = {{}};
      fLeads.forEach(l => {{
        const cName = l.course || 'Other Courses';
        if (!courseRevMap[cName]) courseRevMap[cName] = {{ enrollments: 0, revenue: 0 }};
        if (l.converted === 1 || l.status === 'Opted for Paid Sessions') {{
          courseRevMap[cName].enrollments += 1;
        }}
        courseRevMap[cName].revenue += Number(l.revenue) || 0;
      }});
      const rankedRevCourses = Object.entries(courseRevMap)
        .filter(([_, stats]) => stats.revenue > 0 || stats.enrollments > 0)
        .sort((a, b) => b[1].revenue - a[1].revenue);

      const topRevCourse = rankedRevCourses.length > 0 ? rankedRevCourses[0][0] : 'Modern Data Engineering';

      const elRevTotal = document.getElementById('kpiRevTabTotal');
      if (elRevTotal) elRevTotal.textContent = formatINR(totalRevVal);
      const elRevPaid = document.getElementById('kpiRevTabPaidCount');
      if (elRevPaid) elRevPaid.textContent = paidCount.toLocaleString('en-IN');
      const elRevAvg = document.getElementById('kpiRevTabAvgFee');
      if (elRevAvg) elRevAvg.textContent = formatINR(avgFeeVal);
      const elRevTop = document.getElementById('kpiRevTabTopCourse');
      if (elRevTop) elRevTop.textContent = topRevCourse;

      // Course Revenue Table
      const tbodyCR = document.getElementById('tbodyCourseRevenueTable');
      if (tbodyCR) {{
        tbodyCR.innerHTML = '';
        if (rankedRevCourses.length === 0) {{
          tbodyCR.innerHTML = '<tr><td colspan="5" class="text-center" style="padding: 22px; color: #94a3b8;">No course revenue recorded for current filters</td></tr>';
        }} else {{
          rankedRevCourses.forEach(([cName, stats]) => {{
            const sharePct = totalRevVal > 0 ? ((stats.revenue / totalRevVal) * 100).toFixed(1) : '0.0';
            const avgCrsFee = stats.enrollments > 0 ? Math.round(stats.revenue / stats.enrollments) : 0;
            const tr = document.createElement('tr');
            tr.innerHTML = `
              <td style="font-weight: 700;">${{cName}}</td>
              <td class="text-right">${{stats.enrollments.toLocaleString('en-IN')}}</td>
              <td class="text-right" style="font-weight: 700; color: #16a34a;">${{formatINR(stats.revenue)}}</td>
              <td class="text-right">${{formatINR(avgCrsFee)}}</td>
              <td class="text-right">
                <span style="font-weight: 700;">${{sharePct}}%</span>
                <div class="prog-bar-container">
                  <div class="prog-bar-fill" style="width: ${{sharePct}}%; background: #16a34a;"></div>
                </div>
              </td>
            `;
            tbodyCR.appendChild(tr);
          }});
        }}
      }}

      // --- CHART 10: Revenue by Course Donut (Slice Datalabels & INR Tooltips) ---
      const topRevCourses = rankedRevCourses.slice(0, 5);
      const ctxCRev = document.getElementById('chartCourseRevDonut').getContext('2d');
      if (chartCourseRevDonut) chartCourseRevDonut.destroy();
      const donutColors = ['#2563eb', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'];
      chartCourseRevDonut = new Chart(ctxCRev, {{
        type: 'doughnut',
        data: {{
          labels: topRevCourses.map(x => x[0]),
          datasets: [{{
            data: topRevCourses.map(x => x[1].revenue),
            backgroundColor: donutColors,
            borderWidth: 3,
            borderColor: '#ffffff',
            hoverOffset: 5,
            datalabels: {{
              display: true,
              color: '#ffffff',
              font: {{ family: 'Inter', size: 10, weight: 800 }},
              formatter: (v, ctx) => {{
                const pct = totalRevVal > 0 ? ((v / totalRevVal) * 100).toFixed(0) : 0;
                return pct >= 8 ? `${{pct}}%` : '';
              }}
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ boxWidth: 12, usePointStyle: true, font: {{ family: 'Inter', size: 9.5, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                label: item => {{
                  const pct = totalRevVal > 0 ? ((item.raw / totalRevVal) * 100).toFixed(1) : 0;
                  return ` ${{item.label}}: ${{formatINR(item.raw)}} (${{pct}}%)`;
                }}
              }}
            }}
          }},
          cutout: '62%'
        }}
      }});

      // --- CHART 11: Cumulative Revenue Trajectory Line (Smooth Area with INR Formatting) ---
      const ctxCumul = document.getElementById('chartCumulRevenue').getContext('2d');
      if (chartCumulRevenue) chartCumulRevenue.destroy();
      let cumul = 0;
      const cumulData = revSeries.map(v => {{ cumul += v; return cumul; }});
      chartCumulRevenue = new Chart(ctxCumul, {{
        type: 'line',
        data: {{
          labels: timelineLabels,
          datasets: [{{
            label: 'Cumulative Realized Revenue',
            data: cumulData,
            borderColor: '#059669',
            backgroundColor: 'rgba(5, 150, 105, 0.12)',
            fill: true,
            tension: 0.35,
            borderWidth: 2.5,
            pointRadius: 2.5,
            pointHoverRadius: 6,
            pointBackgroundColor: '#059669',
            datalabels: {{ display: false }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                label: item => ` Cumulative Revenue: ${{formatINR(item.raw)}}`
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              ticks: {{
                callback: value => formatINR(value),
                font: {{ family: 'Inter', size: 9 }}
              }},
              grid: {{ color: '#f1f5f9' }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{
                font: {{ family: 'Inter', size: 9 }},
                autoSkip: true,
                maxTicksLimit: isSingleDay ? 8 : 12,
                maxRotation: 0,
                minRotation: 0
              }}
            }}
          }}
        }}
      }});

      // 6. Payments Intelligence Ribbon & Interactive Table (Tab 5)
      const payTotalVal = fPayments.reduce((acc, p) => acc + (Number(p.amount) || 0), 0);
      const payCountVal = fPayments.length;
      const payAvgVal = payCountVal > 0 ? Math.round(payTotalVal / payCountVal) : 0;
      
      const modeCounts = {{}};
      fPayments.forEach(p => {{
        const m = p.mode || 'UPI';
        modeCounts[m] = (modeCounts[m] || 0) + 1;
      }});
      const topMode = Object.entries(modeCounts).sort((a,b) => b[1] - a[1])[0];
      const topModeStr = topMode ? `${{topMode[0]}} (${{Math.round((topMode[1] / payCountVal) * 100)}}%)` : 'UPI';

      const elPayTotal = document.getElementById('kpiPayTabTotal');
      if (elPayTotal) elPayTotal.textContent = formatINR(payTotalVal);
      const elPayCount = document.getElementById('kpiPayTabCount');
      if (elPayCount) elPayCount.textContent = payCountVal.toLocaleString('en-IN');
      const elPayAvg = document.getElementById('kpiPayTabAvg');
      if (elPayAvg) elPayAvg.textContent = formatINR(payAvgVal);
      const elPayTop = document.getElementById('kpiPayTabTopMode');
      if (elPayTop) elPayTop.textContent = topModeStr;

      window.activePaymentsData = fPayments;
      renderPaymentsTable();

      // 7. Lead Journey Featured Picks (Tab 7)
      const featuredWrap = document.getElementById('featuredLeadsPills');
      if (featuredWrap) {{
        featuredWrap.innerHTML = '';
        const topPicks = [
          ...fLeads.filter(l => (Number(l.revenue) || 0) > 0).sort((a,b) => (Number(b.revenue)||0) - (Number(a.revenue)||0)).slice(0, 3),
          ...fLeads.filter(l => (l.calls_made || 0) > 10).sort((a,b) => (b.calls_made||0) - (a.calls_made||0)).slice(0, 2)
        ];
        topPicks.forEach(lead => {{
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'quick-pill-btn';
          const badgeStr = (Number(lead.revenue) || 0) > 0 ? ` (${{formatINR(lead.revenue)}})` : ` (${{lead.calls_made || 0}} calls)`;
          btn.innerHTML = `<i class="fa-solid fa-user-check"></i> ${{lead.name || lead.id}}${{badgeStr}}`;
          btn.onclick = () => {{
            const jInput = document.getElementById('journeySearchInput');
            if (jInput) jInput.value = lead.id;
            selectedJourneyLeadId = lead.id;
            showAllJourneyEvents = false;
            const allLeads = window.TELECRM_LIVE_DATA?.leads || [];
            renderLeadJourney(allLeads);
          }};
          featuredWrap.appendChild(btn);
        }});
      }}

    }}

    // Global Filter State & Functions for Enhanced Secondary Tabs
    let currentPaymentsFilterMode = 'ALL';
    let currentPaymentsSearchQuery = '';

    function filterPaymentsMode(mode, btn) {{
      currentPaymentsFilterMode = mode;
      document.querySelectorAll('#viewPayments .quick-pill-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderPaymentsTable();
    }}

    function handlePaymentsSearch(query) {{
      currentPaymentsSearchQuery = String(query || '').trim().toLowerCase();
      renderPaymentsTable();
    }}

    function renderPaymentsTable() {{
      const tbodyP = document.getElementById('tbodyPaymentsLog');
      if (!tbodyP) return;
      tbodyP.innerHTML = '';
      const list = window.activePaymentsData || [];
      const mode = currentPaymentsFilterMode || 'ALL';
      const q = currentPaymentsSearchQuery || '';

      const filtered = list.filter(p => {{
        if (mode !== 'ALL' && String(p.mode || '').toLowerCase() !== mode.toLowerCase()) return false;
        if (q) {{
          const searchHaystack = `${{p.id}} ${{p.name}} ${{p.course}} ${{p.counselor}} ${{p.mode}}`.toLowerCase();
          if (!searchHaystack.includes(q)) return false;
        }}
        return true;
      }});

      filtered.forEach((p, idx) => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><code>${{p.id || 'PAY-' + (1000 + idx)}}</code></td>
          <td>${{formatDayMonthLabel(p.date)}} ${{p.date ? p.date.slice(0, 4) : ''}}</td>
          <td style="font-weight: 600;">${{p.name || 'Lead ' + p.lead_id}}</td>
          <td>${{p.course}}</td>
          <td><span class="badge-counselor">${{p.counselor}}</span></td>
          <td>${{p.mode}}</td>
          <td class="text-right"><span class="badge-paid">${{formatINR(p.amount)}}</span></td>
        `;
        tbodyP.appendChild(tr);
      }});

      if (filtered.length === 0) {{
        tbodyP.innerHTML = '<tr><td colspan="7" class="text-center" style="padding: 22px; color: #94a3b8;">No payments match current search &amp; filter criteria</td></tr>';
      }}
    }}

    let currentActivityFilterType = 'ALL';
    let currentActivitySearchQuery = '';

    function filterActivityLogs(type, btn) {{
      currentActivityFilterType = type;
      document.querySelectorAll('#viewSales .quick-pill-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderActivityLogsTable();
    }}

    function handleActivitySearch(query) {{
      currentActivitySearchQuery = String(query || '').trim().toLowerCase();
      renderActivityLogsTable();
    }}

    function renderActivityLogsTable() {{
      const activityTable = document.getElementById('tbodyActivityLogs');
      if (!activityTable) return;
      const allEvents = window.activeActivityEvents || [];
      const leadNames = window.activeLeadNamesMap || new Map();
      const type = currentActivityFilterType || 'ALL';
      const q = currentActivitySearchQuery || '';

      const filtered = allEvents.filter(ev => {{
        if (type === 'Call' && !String(ev.activity || '').toLowerCase().includes('call')) return false;
        if (type === 'WhatsApp' && !String(ev.activity || '').toLowerCase().includes('whatsapp')) return false;
        if (q) {{
          const leadName = leadNames.get(ev.lead_id) || ev.lead_id || '';
          const haystack = `${{ev.activity}} ${{ev.agent}} ${{ev.outcome}} ${{leadName}}`.toLowerCase();
          if (!haystack.includes(q)) return false;
        }}
        return true;
      }}).slice(0, 100);

      const activityCountLabel = document.getElementById('activityLogCount');
      if (activityCountLabel) {{
        activityCountLabel.textContent = `Showing ${{filtered.length}} of ${{allEvents.length.toLocaleString('en-IN')}} activity logs`;
      }}

      if (filtered.length === 0) {{
        activityTable.innerHTML = '<tr><td colspan="6" class="text-center" style="padding: 22px; color: #94a3b8;">No call or WhatsApp logs match the selected filter/search</td></tr>';
        return;
      }}

      activityTable.innerHTML = filtered.map(event => {{
        const leadName = leadNames.get(event.lead_id) || event.lead_id || 'Unknown Lead';
        const atText = event.at ? String(event.at).replace('T', ' ').slice(0, 16) : (event.date || '-');
        const durText = typeof event.duration === 'number' && event.duration > 0 ? `${{event.duration}}s` : '-';
        const actIcon = String(event.activity).toLowerCase().includes('call') ? '<i class="fa-solid fa-phone" style="color: #2563eb;"></i>' : '<i class="fa-brands fa-whatsapp" style="color: #16a34a;"></i>';
        return `
          <tr>
            <td>${{atText}}</td>
            <td>${{actIcon}} ${{event.activity || '-'}}</td>
            <td style="font-weight: 600;">${{event.agent || '-'}}</td>
            <td>${{leadName}}</td>
            <td>${{event.outcome || '-'}}</td>
            <td class="text-right">${{durText}}</td>
          </tr>
        `;
      }}).join('');
    }}

    function handleDictSearch(query) {{
      const q = String(query || '').trim().toLowerCase();
      const rows = document.querySelectorAll('#viewDataDict tbody tr');
      rows.forEach(r => {{
        const text = r.textContent.toLowerCase();
        r.style.display = text.includes(q) ? '' : 'none';
      }});
    }}

    function renderJourneySearchResults(fLeads, query) {{
      const results = document.getElementById('journeySearchResults');
      if (!results) return;
      const needle = String(query || '').trim().toLowerCase();
      if (needle.length < 2) {{
        results.innerHTML = '<div style="font-size: 10px; color: #94a3b8;">Enter at least two characters to search the filtered leads.</div>';
        return;
      }}
      const matches = fLeads.filter(lead =>
        String(lead.id || '').toLowerCase().includes(needle) ||
        String(lead.name || '').toLowerCase().includes(needle)
      );
      if (!matches.length) {{
        results.innerHTML = '<div style="font-size: 11px; color: #64748b; padding: 8px 0;">No matching leads in the current filter selection.</div>';
        return;
      }}
      const shown = matches.slice(0, 15);
      results.innerHTML = `<div style="font-size: 10px; color: #64748b; margin-bottom: 6px;">${{matches.length > shown.length ? `Showing ${{shown.length}} of ${{matches.length}} matches` : `${{matches.length}} matching leads`}} — select a lead to open its journey.</div>` + shown.map(lead => `
        <button type="button" data-journey-id="${{escapeHtml(lead.id)}}" style="width:100%; display:flex; justify-content:space-between; gap:12px; text-align:left; padding:8px 10px; margin:4px 0; border:1px solid #e2e8f0; border-radius:5px; background:#f8fafc; color:#1e293b; font:inherit; cursor:pointer;">
          <span><strong>${{escapeHtml(lead.name || 'Unnamed lead')}}</strong><br><small style="color:#64748b;">${{escapeHtml(lead.id)}}</small></span>
          <span style="text-align:right; font-size:10px; color:#64748b;">${{escapeHtml(lead.status || 'Unknown')}}<br>${{escapeHtml(lead.counselor || 'Unassigned')}}</span>
        </button>`).join('');
    }}

    function renderLeadJourney(leadsArray) {{
      const details = document.getElementById('journeyDetails');
      if (!details) return;
      if (!selectedJourneyLeadId) {{
        details.innerHTML = '<div style="padding: 32px 16px; color: #64748b; text-align: center; font-size: 12.5px;"><i class="fa-solid fa-magnifying-glass" style="font-size: 20px; color: #94a3b8; display: block; margin-bottom: 8px;"></i>Enter any Lead ID in the search box above or click one of the featured leads to display the complete touchpoint journey.</div>';
        return;
      }}

      // Look across the entire database so sidebar date filters don't hide the searched lead
      const allLeads = window.TELECRM_LIVE_DATA?.leads || [];
      const lead = allLeads.find(item => item.id === selectedJourneyLeadId) || (Array.isArray(leadsArray) ? leadsArray.find(item => item.id === selectedJourneyLeadId) : null);

      if (!lead) {{
        selectedJourneyLeadId = '';
        details.innerHTML = '<div style="padding: 28px; color: #64748b; text-align: center; font-size: 12px;"><i class="fa-solid fa-circle-exclamation" style="color: #ef4444; margin-right: 6px;"></i>Lead ID not found in the dataset. Please enter a valid Lead ID.</div>';
        return;
      }}

      const timelineData = (window.TELECRM_LIVE_DATA.journeys || {{}})[lead.id] || {{ events: [] }};
      
      // Also combine with any specific activity_events for this lead
      const extraEvents = (window.TELECRM_LIVE_DATA.activity_events || []).filter(e => e.lead_id === lead.id);
      
      const rawEvents = [...(timelineData.events || [])];
      
      // Add extra events if not already represented
      const existingAts = new Set(rawEvents.map(e => e.at));
      extraEvents.forEach(ae => {{
        if (!existingAts.has(ae.at)) {{
          rawEvents.push({{
            at: ae.at || (ae.date + ' 00:00:00'),
            type: ae.activity || 'Activity',
            by: ae.by || 'Counselor',
            outcome: ae.outcome || '',
            duration: ae.duration_sec,
            text: ae.outcome ? `Call Outcome: ${{ae.outcome}}` : ''
          }});
        }}
      }});

      const events = rawEvents.sort((a, b) => String(a.at || '').localeCompare(String(b.at || '')));
      const visibleEvents = showAllJourneyEvents ? events : events.slice(-50);

      const timeline = visibleEvents.map(event => {{
        const eventType = event.type || 'Activity';
        const typeLow = eventType.toLowerCase();
        let iconHtml = '<i class="fa-solid fa-circle-dot" style="color: #3b82f6;"></i>';
        let badgeColor = '#eff6ff';
        let badgeTextColor = '#1d4ed8';

        if (typeLow.includes('call')) {{
          if (typeLow.includes('missed')) {{
            iconHtml = '<i class="fa-solid fa-phone-slash" style="color: #ef4444;"></i>';
            badgeColor = '#fef2f2'; badgeTextColor = '#b91c1c';
          }} else {{
            iconHtml = '<i class="fa-solid fa-phone" style="color: #2563eb;"></i>';
            badgeColor = '#eff6ff'; badgeTextColor = '#1d4ed8';
          }}
        }} else if (typeLow.includes('whatsapp')) {{
          iconHtml = '<i class="fa-brands fa-whatsapp" style="color: #16a34a;"></i>';
          badgeColor = '#f0fdf4'; badgeTextColor = '#15803d';
        }} else if (typeLow.includes('assignment') || typeLow.includes('assign')) {{
          iconHtml = '<i class="fa-solid fa-user-tag" style="color: #8b5cf6;"></i>';
          badgeColor = '#f5f3ff'; badgeTextColor = '#6d28d9';
        }} else if (typeLow.includes('stage') || typeLow.includes('status')) {{
          iconHtml = '<i class="fa-solid fa-arrow-right-arrow-left" style="color: #ea580c;"></i>';
          badgeColor = '#fff7ed'; badgeTextColor = '#c2410c';
        }} else if (typeLow.includes('converted') || typeLow.includes('payment') || typeLow.includes('paid')) {{
          iconHtml = '<i class="fa-solid fa-circle-check" style="color: #059669;"></i>';
          badgeColor = '#ecfdf5'; badgeTextColor = '#047857';
        }}

        const text = event.text || event.note || event.outcome || '';
        const durSec = Number(event.duration) || 0;
        const durText = durSec > 0 ? (durSec >= 60 ? `${{Math.floor(durSec / 60)}}m ${{durSec % 60}}s` : `${{durSec}}s`) : '';

        return `<div style="position:relative; padding:0 0 14px 22px; margin-left:8px; border-left:2px solid #e2e8f0;">
          <span style="position:absolute; left:-7px; top:2px; width:12px; height:12px; border-radius:50%; background:#ffffff; display:flex; align-items:center; justify-content:center; font-size:10px;">${{iconHtml}}</span>
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:6px; background:#f8fafc; border:1px solid #f1f5f9; padding:8px 12px; border-radius:6px;">
            <div>
              <span style="display:inline-block; padding:2px 8px; border-radius:4px; font-size:10px; font-weight:700; background:${{badgeColor}}; color:${{badgeTextColor}};">${{escapeHtml(eventType)}}</span>
              ${{event.outcome && event.outcome !== 'nan' ? `<span style="font-size:10px; font-weight:700; color:#475569; margin-left:6px; background:#f1f5f9; padding:2px 6px; border-radius:4px;">${{escapeHtml(event.outcome)}}</span>` : ''}}
              ${{durText ? `<span style="font-size:10px; font-weight:600; color:#0284c7; margin-left:6px;"><i class="fa-solid fa-clock" style="font-size:9px; margin-right:2px;"></i>${{durText}}</span>` : ''}}
            </div>
            <div style="font-size:10px; color:#64748b; font-weight:600;">
              ${{escapeHtml(event.at || '')}} ${{event.by ? `&bull; <span style="color:#0f172a; font-weight:700;">${{escapeHtml(event.by)}}</span>` : ''}}
            </div>
            ${{text && text !== 'nan' ? `<div style="width:100%; font-size:11px; line-height:1.45; color:#334155; margin-top:4px; padding-top:4px; border-top:1px dashed #e2e8f0; white-space:pre-wrap;">${{escapeHtml(text)}}</div>` : ''}}
          </div>
        </div>`;
      }}).join('');

      const created = lead.date ? `${{formatDayMonthLabel(lead.date)}} ${{lead.date.slice(0, 4)}}` : 'Unknown';
      const showAllButton = events.length > visibleEvents.length ? `<div style="text-align:center; margin:8px 0;"><button type="button" data-show-all-journey style="padding:6px 14px; border:1px solid #bfdbfe; border-radius:6px; background:#eff6ff; color:#1d4ed8; font:inherit; font-size:11px; font-weight:700; cursor:pointer;"><i class="fa-solid fa-angles-down" style="margin-right:4px;"></i>Show all ${{events.length.toLocaleString('en-IN')}} events (showing last ${{visibleEvents.length}})</button></div>` : '';

      const revBadge = (Number(lead.revenue) || 0) > 0 ? `<span style="display:inline-block; padding:2px 8px; border-radius:4px; background:#dcfce7; color:#15803d; font-weight:800; font-size:11px;">${{formatINR(lead.revenue)}} Paid</span>` : '<span style="color:#94a3b8; font-size:11px;">₹0</span>';

      details.innerHTML = `<div style="display:flex; flex-direction:column; gap:14px;">
        <!-- Lead Dossier Summary Card -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px; padding:12px 14px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px;">
          <div>
            <span class="summary-metric-lbl">Lead Name &amp; ID</span>
            <div style="font-size:13px; font-weight:800; color:#0f172a;">${{escapeHtml(lead.name || 'Unnamed lead')}}</div>
            <code style="font-size:10.5px; color:#2563eb; background:#eff6ff; padding:2px 5px; border-radius:4px; display:inline-block; margin-top:2px;">${{escapeHtml(lead.id)}}</code>
          </div>
          <div>
            <span class="summary-metric-lbl">Current Status &amp; Stage</span>
            <div style="font-size:12px; font-weight:700; color:#1e293b;"><span class="badge badge-success" style="font-size:10.5px;">${{escapeHtml(lead.status || 'Unknown')}}</span> &bull; ${{escapeHtml(lead.stage || 'Open')}}</div>
          </div>
          <div>
            <span class="summary-metric-lbl">Course Interest</span>
            <div style="font-size:12px; font-weight:700; color:#0f172a;">${{escapeHtml(lead.course || 'Unknown')}}</div>
          </div>
          <div>
            <span class="summary-metric-lbl">Assigned Counselor</span>
            <div style="font-size:12px; font-weight:700; color:#0f172a;"><i class="fa-solid fa-headset" style="color:#2563eb; margin-right:4px;"></i>${{escapeHtml(lead.counselor || 'Unassigned')}}</div>
          </div>
          <div>
            <span class="summary-metric-lbl">Calling Engagement</span>
            <div style="font-size:12px; font-weight:700; color:#0f172a;">${{lead.calls_made || 0}} Calls Made &bull; ${{lead.calls_conn || 0}} Conn (${{Math.round(lead.talk_time || 0)}}m)</div>
          </div>
          <div>
            <span class="summary-metric-lbl">Lifetime Revenue / Value</span>
            <div>${{revBadge}}</div>
          </div>
          <div>
            <span class="summary-metric-lbl">Lead Source &amp; Channel</span>
            <div style="font-size:11.5px; color:#475569;">${{escapeHtml(lead.source || 'Direct')}} (${{escapeHtml(lead.channel || 'Unmapped')}})</div>
          </div>
          <div>
            <span class="summary-metric-lbl">Created Date (IST)</span>
            <div style="font-size:11.5px; color:#475569;"><i class="fa-solid fa-calendar-day" style="margin-right:4px;"></i>${{escapeHtml(created)}}</div>
          </div>
        </div>

        <!-- Activity Timeline Header -->
        <div class="card-panel-header" style="margin-bottom:0; display:flex; justify-content:space-between; align-items:center;">
          <span class="panel-title"><i class="fa-solid fa-timeline" style="color:#2563eb; margin-right:6px;"></i>Full Chronological Touchpoint Journey</span>
          <span style="font-size:10.5px; font-weight:700; color:#475569; background:#f1f5f9; padding:3px 8px; border-radius:4px;">${{events.length.toLocaleString('en-IN')}} total events</span>
        </div>
        ${{showAllButton}}
        ${{timeline ? `<div style="padding-top:6px;">${{timeline}}</div>` : '<div style="padding:22px; color:#64748b; text-align:center; font-size:11.5px;">No journey events recorded in TeleCRM for this lead.</div>'}}
      </div>`;
    }}

    // Navigation Tabs with resize trigger
    function navTab(tabKey, btnElement) {{
      document.querySelectorAll('.view-content').forEach(v => v.classList.remove('active'));
      document.querySelectorAll('.bottom-btn').forEach(b => {{
        if (b.dataset.tabKey === tabKey) {{
          b.classList.add('active');
        }} else {{
          b.classList.remove('active');
        }}
      }});
      
      const targetId = 'view' + tabKey;
      const el = document.getElementById(targetId);
      if (el) el.classList.add('active');

      const titles = {{
        'Executive': 'Executive Dashboard',
        'Leads': 'Lead Pipeline & Conversion Analytics',
        'Sales': 'Counselor Calling & Sales Activity',
        'Revenue': 'Revenue & Monetization Trajectory',
        'Payments': 'Verified Transaction & Payment Logs',
        'DataDict': 'Data Dictionary & Pipeline Schema',
        'Journey': 'Individual Lead Journey'
      }};
      document.getElementById('dynViewTitle').textContent = titles[tabKey] || 'Executive Dashboard';

      // Instant re-render so whichever tab becomes visible has all charts rendered with non-zero dimensions
      renderDashboard();
      setTimeout(() => {{
        [
          chartLeadsTrend, chartRevenueTrend, chartSourceDonut, chartCounselorCombo,
          chartDailyPayments, chartPaymentMode, chartLeadStageBar, chartLeadSourcePerformance,
          chartCourseConversion, chartChannelAdmissions, chartCounselorActivity,
          chartCounselorDuration, chartSlaCompliance, chartWhatsAppActivity,
          chartWorkableDonut, chartCourseRevDonut, chartCumulRevenue
        ].forEach(c => {{
          if (c) {{
            c.resize();
            c.update('none');
          }}
        }});
      }}, 50);
    }}
  </script>
</body>
</html>'''

    with open('ksr_executive_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built ksr_executive_dashboard.html as the main executive dashboard with 100% Live TeleCRM data!")

if __name__ == '__main__':
    generate_live_dashboard()
