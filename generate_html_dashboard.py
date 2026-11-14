import json

def generate_html():
    with open('dashboard_data.json', 'r', encoding='utf-8') as f:
        data_json = f.read()

    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KSR Datavizon - Executive Dashboard</title>
  <!-- Google Fonts: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <!-- PapaParse for CSV parsing -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>

  <style>
    :root {{
      --sidebar-bg: #0b1a2e;
      --sidebar-card: #13253d;
      --sidebar-border: #1d3557;
      --sidebar-text: #e2e8f0;
      --sidebar-muted: #8ca2bf;
      --primary-blue: #1a73e8;
      --success-green: #10b981;
      --warning-gold: #f59e0b;
      --purple-accent: #8b5cf6;
      --info-cyan: #06b6d4;
      --danger-red: #ef4444;
      --bg-page: #f4f7fb;
      --card-bg: #ffffff;
      --card-border: #e2e8f0;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-family);
      background-color: var(--bg-page);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Top Branding Bar */
    .header-bar {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
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

    .logo-badge {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #0284c7 0%, #f97316 100%);
      color: white;
      font-weight: 800;
      font-size: 16px;
      border-radius: 8px;
      letter-spacing: -1px;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.3);
    }}

    .brand-text-block {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title {{
      font-size: 18px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #0c4a6e;
      line-height: 1.1;
    }}

    .brand-subtitle {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #f97316;
      text-transform: uppercase;
    }}

    .header-divider {{
      height: 36px;
      width: 1px;
      background-color: #e2e8f0;
      margin: 0 4px;
    }}

    .header-page-title {{
      display: flex;
      flex-direction: column;
    }}

    .header-page-title h1 {{
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
    }}

    .header-page-title p {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}

    .data-as-of-box {{
      display: flex;
      align-items: center;
      gap: 10px;
      background-color: #f0f9ff;
      border: 1px solid #bae6fd;
      padding: 6px 14px;
      border-radius: 8px;
    }}

    .data-as-of-box i {{
      color: #0284c7;
      font-size: 18px;
    }}

    .data-as-of-text {{
      display: flex;
      flex-direction: column;
    }}

    .data-as-of-text span:first-child {{
      font-size: 10px;
      font-weight: 600;
      color: #0369a1;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .data-as-of-text span:last-child {{
      font-size: 12px;
      font-weight: 700;
      color: #0c4a6e;
    }}

    .partner-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .partner-brand i {{
      font-size: 24px;
      color: #1d4ed8;
    }}

    .partner-brand-text {{
      display: flex;
      flex-direction: column;
      line-height: 1.2;
    }}

    .partner-brand-text span:first-child {{
      font-size: 13px;
      font-weight: 800;
      color: #1e3a8a;
      letter-spacing: 0.5px;
    }}

    .partner-brand-text span:last-child {{
      font-size: 10px;
      color: #3b82f6;
      font-weight: 500;
    }}

    .upload-btn {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      color: #334155;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}

    .upload-btn:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    /* Main Dashboard Layout */
    .dashboard-container {{
      display: flex;
      flex: 1;
      min-height: calc(100vh - 120px);
    }}

    /* Filter Sidebar */
    .sidebar {{
      width: 250px;
      min-width: 250px;
      background-color: var(--sidebar-bg);
      color: var(--sidebar-text);
      padding: 16px 14px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      border-right: 1px solid var(--sidebar-border);
      box-shadow: 2px 0 8px rgba(0,0,0,0.1);
    }}

    .sidebar-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 1.2px;
      color: #ffffff;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--sidebar-border);
    }}

    .sidebar-header i {{
      color: #38bdf8;
    }}

    .filter-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .filter-label {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--sidebar-muted);
    }}

    .filter-label i {{
      font-size: 12px;
      color: #7dd3fc;
    }}

    .filter-select, .filter-input {{
      width: 100%;
      background-color: var(--sidebar-card);
      border: 1px solid var(--sidebar-border);
      color: #ffffff;
      padding: 8px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-family: inherit;
      outline: none;
      cursor: pointer;
      transition: border-color 0.2s;
    }}

    .filter-select:hover, .filter-select:focus {{
      border-color: #38bdf8;
    }}

    .filter-select option {{
      background-color: #0b1a2e;
      color: #ffffff;
      padding: 6px;
    }}

    .date-display-badge {{
      font-size: 10px;
      color: #38bdf8;
      font-weight: 500;
      padding-left: 2px;
    }}

    .custom-date-row {{
      display: none;
      gap: 6px;
      margin-top: 4px;
    }}

    .custom-date-row input {{
      width: 50%;
      background-color: var(--sidebar-card);
      border: 1px solid var(--sidebar-border);
      color: #ffffff;
      font-size: 11px;
      padding: 4px 6px;
      border-radius: 4px;
    }}

    .btn-clear-filters {{
      background-color: transparent;
      border: 1px solid #38bdf8;
      color: #38bdf8;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-top: auto;
      transition: all 0.2s ease;
    }}

    .btn-clear-filters:hover {{
      background-color: #38bdf8;
      color: #0b1a2e;
    }}

    /* Main Content Area */
    .main-content {{
      flex: 1;
      padding: 16px 20px 80px 20px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    /* KPI Cards Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 12px;
    }}

    .kpi-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 12px 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      position: relative;
      transition: transform 0.2s, box-shadow 0.2s;
    }}

    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    }}

    .kpi-icon-wrap {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      flex-shrink: 0;
    }}

    .kpi-leads .kpi-icon-wrap {{
      background-color: #eff6ff;
      color: #2563eb;
    }}
    .kpi-conversions .kpi-icon-wrap {{
      background-color: #ecfdf5;
      color: #10b981;
    }}
    .kpi-revenue .kpi-icon-wrap {{
      background-color: #fffbeb;
      color: #d97706;
    }}
    .kpi-rate .kpi-icon-wrap {{
      background-color: #f5f3ff;
      color: #7c3aed;
    }}
    .kpi-calls .kpi-icon-wrap {{
      background-color: #f0f9ff;
      color: #0284c7;
    }}
    .kpi-duration .kpi-icon-wrap {{
      background-color: #fef2f2;
      color: #dc2626;
    }}

    .kpi-info {{
      display: flex;
      flex-direction: column;
      flex: 1;
      min-width: 0;
    }}

    .kpi-label {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .kpi-value {{
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
      margin: 2px 0;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .kpi-value-unit {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      margin-left: 2px;
    }}

    .kpi-trend {{
      font-size: 10px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 3px;
    }}

    .kpi-trend.positive {{
      color: #10b981;
    }}

    .kpi-trend.negative {{
      color: #ef4444;
    }}

    .kpi-trend-note {{
      font-size: 9px;
      color: #94a3b8;
      font-weight: 400;
      margin-left: 2px;
    }}

    /* Row Layouts for Charts */
    .charts-row-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}

    .charts-row-3 {{
      display: grid;
      grid-template-columns: 1fr 1.1fr 1.2fr;
      gap: 14px;
    }}

    .charts-row-bottom {{
      display: grid;
      grid-template-columns: 1.3fr 1.2fr 1fr;
      gap: 14px;
    }}

    /* Chart Card Base */
    .chart-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}

    .chart-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .chart-title {{
      font-size: 13px;
      font-weight: 700;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .chart-legend-custom {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 11px;
      font-weight: 600;
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .legend-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }}

    .chart-canvas-wrap {{
      position: relative;
      flex: 1;
      min-height: 180px;
      width: 100%;
    }}

    /* Lead Status Funnel Custom Styling */
    .funnel-container {{
      display: flex;
      flex-direction: column;
      gap: 5px;
      padding: 4px 0;
      height: 100%;
      justify-content: space-around;
    }}

    .funnel-step {{
      display: flex;
      align-items: center;
      font-size: 11px;
      gap: 8px;
    }}

    .funnel-step-name {{
      width: 105px;
      font-weight: 600;
      color: #334155;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      text-align: right;
    }}

    .funnel-bar-wrap {{
      flex: 1;
      height: 20px;
      background: #f1f5f9;
      border-radius: 4px;
      overflow: hidden;
      position: relative;
      display: flex;
      align-items: center;
    }}

    .funnel-bar-fill {{
      height: 100%;
      border-radius: 4px;
      transition: width 0.4s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 10px;
      font-weight: 700;
    }}

    .funnel-step-pct {{
      width: 45px;
      font-size: 10px;
      font-weight: 700;
      color: #64748b;
      text-align: left;
    }}

    /* Course Performance Table */
    .table-container {{
      overflow-x: auto;
      max-height: 220px;
    }}

    .custom-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
      text-align: left;
    }}

    .custom-table th {{
      background-color: #f8fafc;
      color: #475569;
      font-weight: 700;
      padding: 8px 10px;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 2;
    }}

    .custom-table td {{
      padding: 8px 10px;
      border-bottom: 1px solid #f1f5f9;
      color: #1e293b;
    }}

    .custom-table tr:hover td {{
      background-color: #f8fafc;
    }}

    .custom-table td.numeric, .custom-table th.numeric {{
      text-align: right;
    }}

    .badge-conv {{
      background: #ecfdf5;
      color: #059669;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 10px;
    }}

    /* Payment Summary Box */
    .payment-summary-wrap {{
      display: flex;
      gap: 12px;
      height: 100%;
      align-items: center;
    }}

    .payment-donut-wrap {{
      flex: 1.1;
      height: 190px;
      position: relative;
    }}

    .payment-stats-box {{
      flex: 0.9;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .payment-stats-title {{
      font-size: 11px;
      font-weight: 700;
      color: #1e293b;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 4px;
    }}

    .payment-stat-item {{
      display: flex;
      flex-direction: column;
    }}

    .payment-stat-label {{
      font-size: 10px;
      color: #64748b;
      font-weight: 500;
    }}

    .payment-stat-val {{
      font-size: 14px;
      font-weight: 800;
      color: #0f172a;
    }}

    /* Bottom Navigation Bar */
    .bottom-nav-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background-color: #0b1a2e;
      border-top: 1px solid #1e293b;
      display: flex;
      justify-content: center;
      gap: 8px;
      padding: 8px 16px;
      z-index: 100;
      box-shadow: 0 -2px 10px rgba(0,0,0,0.15);
    }}

    .nav-tab-btn {{
      background: transparent;
      border: none;
      color: #94a3b8;
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .nav-tab-btn i {{
      font-size: 13px;
    }}

    .nav-tab-btn:hover {{
      background: #1e293b;
      color: #ffffff;
    }}

    .nav-tab-btn.active {{
      background: #1a73e8;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(26, 115, 232, 0.4);
    }}

    /* Other Tab Views */
    .tab-view {{
      display: none;
      flex-direction: column;
      gap: 16px;
    }}

    .tab-view.active {{
      display: flex;
    }}

    /* Upload Modal */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0,0,0,0.5);
      z-index: 200;
      justify-content: center;
      align-items: center;
    }}

    .modal-content {{
      background: #ffffff;
      border-radius: 12px;
      width: 480px;
      max-width: 90%;
      padding: 24px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-header h3 {{
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
    }}

    .modal-close-btn {{
      background: none;
      border: none;
      font-size: 18px;
      cursor: pointer;
      color: #64748b;
    }}

    .dropzone {{
      border: 2px dashed #cbd5e1;
      border-radius: 8px;
      padding: 24px;
      text-align: center;
      background: #f8fafc;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .dropzone:hover {{
      border-color: #0284c7;
      background: #f0f9ff;
    }}

    .dropzone i {{
      font-size: 32px;
      color: #0284c7;
      margin-bottom: 8px;
    }}

    /* Data Dictionary Cards */
    .dict-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }}

    .dict-card {{
      background: white;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 14px;
    }}

    .dict-card h4 {{
      font-size: 13px;
      color: #1e3a8a;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .dict-card p {{
      font-size: 11px;
      color: #475569;
      line-height: 1.5;
    }}

    /* Responsive adjustments */
    @media (max-width: 1400px) {{
      .kpi-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
      .charts-row-3 {{
        grid-template-columns: 1fr 1fr;
      }}
      .charts-row-bottom {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    @media (max-width: 1024px) {{
      .dashboard-container {{
        flex-direction: column;
      }}
      .sidebar {{
        width: 100%;
        min-width: 100%;
        border-right: none;
        border-bottom: 1px solid var(--sidebar-border);
      }}
      .charts-row-2, .charts-row-3, .charts-row-bottom {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Header / Branding Bar -->
  <header class="header-bar">
    <div class="header-left">
      <div class="brand-logo-wrap">
        <div class="logo-badge">KSR</div>
        <div class="brand-text-block">
          <span class="brand-title">KSR</span>
          <span class="brand-subtitle">DATAVIZON</span>
        </div>
      </div>
      <div class="header-divider"></div>
      <div class="header-page-title">
        <h1 id="topViewTitle">Executive Dashboard</h1>
        <p>Overview of Leads, Sales & Revenue Performance</p>
      </div>
    </div>

    <div class="header-right">
      <button class="upload-btn" onclick="openUploadModal()">
        <i class="fa-solid fa-cloud-arrow-up"></i>
        <span>Load CSV</span>
      </button>

      <div class="data-as-of-box">
        <i class="fa-regular fa-calendar-check"></i>
        <div class="data-as-of-text">
          <span>Data As Of</span>
          <span id="headerDataAsOf">31 Oct 2026 11:50 PM</span>
        </div>
      </div>

      <div class="partner-brand">
        <i class="fa-solid fa-graduation-cap"></i>
        <div class="partner-brand-text">
          <span>THE SKILL NATION</span>
          <span>Shape Your Future</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Dashboard Container with Sidebar and Content -->
  <div class="dashboard-container">
    <!-- Filters Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <i class="fa-solid fa-filter"></i>
        <span>FILTERS</span>
      </div>

      <!-- Date Range Filter -->
      <div class="filter-group">
        <label class="filter-label">
          <i class="fa-regular fa-calendar"></i>
          <span>Date Range</span>
        </label>
        <select id="filterDateRange" class="filter-select" onchange="handleDateRangeChange()">
          <option value="last7" selected>Last 7 Days (25 Oct - 31 Oct)</option>
          <option value="last14">Last 14 Days (18 Oct - 31 Oct)</option>
          <option value="first7">First 7 Days (01 Oct - 07 Oct)</option>
          <option value="all">Entire Month (01 Oct - 31 Oct)</option>
          <option value="custom">Custom Range</option>
        </select>
        <span class="date-display-badge" id="lblDateSubtitle">25 Oct 2026 - 31 Oct 2026</span>
        <div id="customDateRow" class="custom-date-row">
          <input type="date" id="dateStart" onchange="applyFilters()">
          <input type="date" id="dateEnd" onchange="applyFilters()">
        </div>
      </div>

      <!-- Course Filter -->
      <div class="filter-group">
        <label class="filter-label">
          <i class="fa-solid fa-graduation-cap"></i>
          <span>Course</span>
        </label>
        <select id="filterCourse" class="filter-select" onchange="applyFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Counselor Filter -->
      <div class="filter-group">
        <label class="filter-label">
          <i class="fa-regular fa-user"></i>
          <span>Counselor</span>
        </label>
        <select id="filterCounselor" class="filter-select" onchange="applyFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Source Filter -->
      <div class="filter-group">
        <label class="filter-label">
          <i class="fa-solid fa-bullhorn"></i>
          <span>Source</span>
        </label>
        <select id="filterSource" class="filter-select" onchange="applyFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Lead Status Filter -->
      <div class="filter-group">
        <label class="filter-label">
          <i class="fa-solid fa-list-check"></i>
          <span>Lead Status</span>
        </label>
        <select id="filterStatus" class="filter-select" onchange="applyFilters()">
          <option value="ALL">All</option>
        </select>
      </div>

      <!-- Clear Filters Button -->
      <button class="btn-clear-filters" onclick="clearAllFilters()">
        <i class="fa-solid fa-rotate-left"></i>
        <span>Clear All Filters</span>
      </button>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      
      <!-- TAB 1: EXECUTIVE DASHBOARD (Default Active) -->
      <section id="viewExecutive" class="tab-view active">
        
        <!-- KPI Cards Row -->
        <div class="kpi-grid">
          <!-- Total Leads -->
          <div class="kpi-card kpi-leads">
            <div class="kpi-icon-wrap">
              <i class="fa-solid fa-users"></i>
            </div>
            <div class="kpi-info">
              <span class="kpi-label">Total Leads</span>
              <span class="kpi-value" id="kpiLeads">0</span>
              <div class="kpi-trend positive" id="kpiLeadsTrend">
                <i class="fa-solid fa-arrow-up"></i>
                <span id="kpiLeadsTrendVal">18.3%</span>
                <span class="kpi-trend-note">vs Prev</span>
              </div>
            </div>
          </div>

          <!-- Total Conversions -->
          <div class="kpi-card kpi-conversions">
            <div class="kpi-icon-wrap">
              <i class="fa-solid fa-circle-check"></i>
            </div>
            <div class="kpi-info">
              <span class="kpi-label">Total Conversions</span>
              <span class="kpi-value" id="kpiConversions">0</span>
              <div class="kpi-trend positive" id="kpiConvTrend">
                <i class="fa-solid fa-arrow-up"></i>
                <span id="kpiConvTrendVal">23.5%</span>
                <span class="kpi-trend-note">vs Prev</span>
              </div>
            </div>
          </div>

          <!-- Revenue -->
          <div class="kpi-card kpi-revenue">
            <div class="kpi-icon-wrap">
              <i class="fa-solid fa-sack-dollar"></i>
            </div>
            <div class="kpi-info">
              <span class="kpi-label">Revenue</span>
              <span class="kpi-value" id="kpiRevenue">₹0</span>
              <div class="kpi-trend positive" id="kpiRevTrend">
                <i class="fa-solid fa-arrow-up"></i>
                <span id="kpiRevTrendVal">21.7%</span>
                <span class="kpi-trend-note">vs Prev</span>
              </div>
            </div>
          </div>

          <!-- Conversion Rate -->
          <div class="kpi-card kpi-rate">
            <div class="kpi-icon-wrap">
              <i class="fa-solid fa-percent"></i>
            </div>
            <div class="kpi-info">
              <span class="kpi-label">Conversion Rate</span>
              <span class="kpi-value" id="kpiConvRate">0.0%</span>
              <div class="kpi-trend positive" id="kpiRateTrend">
                <i class="fa-solid fa-arrow-up"></i>
                <span id="kpiRateTrendVal">3.2%</span>
                <span class="kpi-trend-note">vs Prev</span>
              </div>
            </div>
          </div>

          <!-- Total Calls -->
          <div class="kpi-card kpi-calls">
            <div class="kpi-icon-wrap">
              <i class="fa-solid fa-phone"></i>
            </div>
            <div class="kpi-info">
              <span class="kpi-label">Total Calls</span>
              <span class="kpi-value" id="kpiCalls">0</span>
              <div class="kpi-trend positive" id="kpiCallsTrend">
                <i class="fa-solid fa-arrow-up"></i>
                <span id="kpiCallsTrendVal">15.6%</span>
                <span class="kpi-trend-note">vs Prev</span>
              </div>
            </div>
          </div>

          <!-- Total Call Duration -->
          <div class="kpi-card kpi-duration">
            <div class="kpi-icon-wrap">
              <i class="fa-regular fa-clock"></i>
            </div>
            <div class="kpi-info">
              <span class="kpi-label">Total Call Duration</span>
              <div class="kpi-value">
                <span id="kpiDuration">0</span>
                <span class="kpi-value-unit">Mins</span>
              </div>
              <div class="kpi-trend positive" id="kpiDurTrend">
                <i class="fa-solid fa-arrow-up"></i>
                <span id="kpiDurTrendVal">12.4%</span>
                <span class="kpi-trend-note">vs Prev</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Charts Row 1: Leads Trend & Revenue Trend -->
        <div class="charts-row-2">
          <!-- Leads Trend -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title" id="titleLeadsTrend">Leads Trend</span>
              <div class="chart-legend-custom">
                <div class="legend-item">
                  <span class="legend-dot" style="background-color: #1a73e8;"></span>
                  <span>Leads</span>
                </div>
                <div class="legend-item">
                  <span class="legend-dot" style="background-color: #10b981;"></span>
                  <span>Conversions</span>
                </div>
              </div>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartLeadsTrend"></canvas>
            </div>
          </div>

          <!-- Revenue Trend -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title" id="titleRevenueTrend">Revenue Trend</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartRevenueTrend"></canvas>
            </div>
          </div>
        </div>

        <!-- Charts Row 2: Funnel, Leads by Source, Calls by Counselor -->
        <div class="charts-row-3">
          <!-- Lead Status Funnel -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Lead Status Funnel</span>
            </div>
            <div class="funnel-container" id="funnelContainer">
              <!-- Rendered via JS -->
            </div>
          </div>

          <!-- Leads by Source -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Leads by Source</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartSourceDonut"></canvas>
            </div>
          </div>

          <!-- Calls by Counselor -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Calls by Counselor</span>
              <div class="chart-legend-custom">
                <div class="legend-item">
                  <span class="legend-dot" style="background-color: #1a73e8;"></span>
                  <span>Total Calls</span>
                </div>
                <div class="legend-item">
                  <span class="legend-dot" style="background-color: #10b981;"></span>
                  <span>Total Duration (Mins)</span>
                </div>
              </div>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartCounselorCombo"></canvas>
            </div>
          </div>
        </div>

        <!-- Charts Row 3: Course Performance Table, Daily Payments Trend, Payment Mode & Summary -->
        <div class="charts-row-bottom">
          <!-- Course Performance Table -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Course Performance</span>
            </div>
            <div class="table-container">
              <table class="custom-table" id="tableCoursePerf">
                <thead>
                  <tr>
                    <th>Course</th>
                    <th class="numeric">Leads</th>
                    <th class="numeric">Conversions</th>
                    <th class="numeric">Conversion %</th>
                    <th class="numeric">Revenue</th>
                  </tr>
                </thead>
                <tbody id="tbodyCoursePerf">
                  <!-- Rendered via JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Daily Payments Trend -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Daily Payments Trend</span>
              <div class="chart-legend-custom">
                <div class="legend-item">
                  <span class="legend-dot" style="background-color: #1a73e8;"></span>
                  <span>Payments Count</span>
                </div>
                <div class="legend-item">
                  <span class="legend-dot" style="background-color: #10b981;"></span>
                  <span>Revenue</span>
                </div>
              </div>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartDailyPayments"></canvas>
            </div>
          </div>

          <!-- Payment Mode & Summary -->
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Payment Mode</span>
            </div>
            <div class="payment-summary-wrap">
              <div class="payment-donut-wrap">
                <canvas id="chartPaymentMode"></canvas>
              </div>
              <div class="payment-stats-box">
                <span class="payment-stats-title">Payment Summary</span>
                <div class="payment-stat-item">
                  <span class="payment-stat-label">Total Payments</span>
                  <span class="payment-stat-val" id="summaryTotalPayments">0</span>
                </div>
                <div class="payment-stat-item">
                  <span class="payment-stat-label">Total Revenue</span>
                  <span class="payment-stat-val" id="summaryTotalRevenue">₹0</span>
                </div>
                <div class="payment-stat-item">
                  <span class="payment-stat-label">Avg. Order Value</span>
                  <span class="payment-stat-val" id="summaryAvgOrderValue">₹0</span>
                </div>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- TAB 2: LEAD ANALYTICS -->
      <section id="viewLeadAnalytics" class="tab-view">
        <div class="charts-row-2">
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Leads by Stage Breakdown</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartLeadStageBar"></canvas>
            </div>
          </div>
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Lead Quality (Workable vs Junk)</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartLeadWorkableDonut"></canvas>
            </div>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-card-header">
            <span class="chart-title">Top Geographic Locations (State / City)</span>
          </div>
          <div class="table-container">
            <table class="custom-table" id="tableGeo">
              <thead>
                <tr>
                  <th>City / State</th>
                  <th class="numeric">Total Leads</th>
                  <th class="numeric">Conversions</th>
                  <th class="numeric">Conversion Rate</th>
                </tr>
              </thead>
              <tbody id="tbodyGeo"></tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 3: SALES ACTIVITY -->
      <section id="viewSalesActivity" class="tab-view">
        <div class="chart-card">
          <div class="chart-card-header">
            <span class="chart-title">Counselor Calling Efficiency Leaderboard</span>
          </div>
          <div class="table-container">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>Counselor Name</th>
                  <th class="numeric">Calls Made</th>
                  <th class="numeric">Calls Connected</th>
                  <th class="numeric">Connect Rate %</th>
                  <th class="numeric">Total Talk Time (Mins)</th>
                  <th class="numeric">Avg Call Duration (Sec)</th>
                  <th class="numeric">Leads Handled</th>
                  <th class="numeric">Conversions</th>
                </tr>
              </thead>
              <tbody id="tbodyCounselorLeaderboard"></tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 4: REVENUE DASHBOARD -->
      <section id="viewRevenue" class="tab-view">
        <div class="charts-row-2">
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Course Revenue Contribution</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartCourseRevDonut"></canvas>
            </div>
          </div>
          <div class="chart-card">
            <div class="chart-card-header">
              <span class="chart-title">Revenue Realization by Counselor</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartCounselorRevBar"></canvas>
            </div>
          </div>
        </div>
      </section>

      <!-- TAB 5: PAYMENTS LOG -->
      <section id="viewPayments" class="tab-view">
        <div class="chart-card">
          <div class="chart-card-header">
            <span class="chart-title">Transaction & Payment Details</span>
          </div>
          <div class="table-container">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>Payment ID</th>
                  <th>Date</th>
                  <th>Lead Name</th>
                  <th>Course</th>
                  <th>Counselor</th>
                  <th>Mode</th>
                  <th class="numeric">Amount</th>
                </tr>
              </thead>
              <tbody id="tbodyPaymentLogs"></tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 6: DATA DICTIONARY -->
      <section id="viewDataDict" class="tab-view">
        <div class="dict-grid">
          <div class="dict-card">
            <h4><i class="fa-solid fa-users"></i> Total Leads</h4>
            <p>Count of all prospective students who entered TeleCRM within the selected date range across all channels (Ads, WhatsApp, Call logs, Website, etc.).</p>
          </div>
          <div class="dict-card">
            <h4><i class="fa-solid fa-circle-check"></i> Total Conversions</h4>
            <p>Leads marked as 'Converted' or 'Opted for Paid Sessions' with successful fee payment or admission confirmation.</p>
          </div>
          <div class="dict-card">
            <h4><i class="fa-solid fa-indian-rupee-sign"></i> Revenue (Lifetime Value)</h4>
            <p>Sum of all course fees paid or committed by converted leads during the evaluated period, formatted in standard Indian Lakhs/Thousands (₹).</p>
          </div>
          <div class="dict-card">
            <h4><i class="fa-solid fa-percent"></i> Conversion Rate (%)</h4>
            <p>Calculated as <code>(Total Conversions / Total Leads) × 100</code> for the selected filter slice.</p>
          </div>
          <div class="dict-card">
            <h4><i class="fa-solid fa-phone"></i> Total Calls & Duration</h4>
            <p>Total inbound and outbound calling attempts logged by counselors in TeleCRM, along with total talk time in minutes.</p>
          </div>
          <div class="dict-card">
            <h4><i class="fa-solid fa-filter"></i> Lead Status Funnel</h4>
            <p>Represents student progression through pipeline stages: New Lead &rarr; Contacted &rarr; Follow-up &rarr; Interested &rarr; Demo Scheduled &rarr; Negotiation &rarr; Paid / Lost.</p>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- Bottom Navigation Tab Bar -->
  <footer class="bottom-nav-bar">
    <button class="nav-tab-btn active" onclick="switchTab('Executive')">
      <i class="fa-solid fa-chart-line"></i>
      <span>Executive Dashboard</span>
    </button>
    <button class="nav-tab-btn" onclick="switchTab('LeadAnalytics')">
      <i class="fa-solid fa-users-gear"></i>
      <span>Lead Analytics</span>
    </button>
    <button class="nav-tab-btn" onclick="switchTab('SalesActivity')">
      <i class="fa-solid fa-headset"></i>
      <span>Sales Activity</span>
    </button>
    <button class="nav-tab-btn" onclick="switchTab('Revenue')">
      <i class="fa-solid fa-chart-column"></i>
      <span>Revenue Dashboard</span>
    </button>
    <button class="nav-tab-btn" onclick="switchTab('Payments')">
      <i class="fa-solid fa-credit-card"></i>
      <span>Payments</span>
    </button>
    <button class="nav-tab-btn" onclick="switchTab('DataDict')">
      <i class="fa-solid fa-book-open"></i>
      <span>Data Dictionary</span>
    </button>
  </footer>

  <!-- CSV Upload Modal -->
  <div id="uploadModal" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h3><i class="fa-solid fa-upload" style="color: #0284c7;"></i> Update TeleCRM Data</h3>
        <button class="modal-close-btn" onclick="closeUploadModal()">&times;</button>
      </div>
      <p style="font-size: 12px; color: #64748b;">
        Upload your export files (<code>telecrm-leads-....csv</code> or <code>telecrm-activities-....csv</code>) to instantly refresh all charts and KPIs.
      </p>
      <div class="dropzone" onclick="document.getElementById('csvFileInput').click()">
        <i class="fa-solid fa-file-csv"></i>
        <div style="font-weight: 700; font-size: 13px; color: #1e293b;">Click to select or drag CSV file here</div>
        <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">Supports TeleCRM Leads and Activities CSVs</div>
      </div>
      <input type="file" id="csvFileInput" style="display: none;" accept=".csv" onchange="handleFileSelect(event)">
      <div id="uploadStatus" style="font-size: 11px; color: #0284c7; font-weight: 600;"></div>
    </div>
  </div>

  <!-- Embedded Dataset -->
  <script>
    window.TELECRM_RAW_DATA = {data_json};
  </script>

  <!-- Dashboard Controller Script -->
  <script>
    let rawLeads = window.TELECRM_RAW_DATA.leads || [];
    let rawCalls = window.TELECRM_RAW_DATA.calls || [];
    let rawPayments = window.TELECRM_RAW_DATA.payments || [];

    // Chart instances
    let chartLeadsTrendInst = null;
    let chartRevenueTrendInst = null;
    let chartSourceDonutInst = null;
    let chartCounselorComboInst = null;
    let chartDailyPaymentsInst = null;
    let chartPaymentModeInst = null;
    let chartLeadStageBarInst = null;
    let chartLeadWorkableDonutInst = null;
    let chartCourseRevDonutInst = null;
    let chartCounselorRevBarInst = null;

    // Currency Formatter
    function formatINR(val) {{
      if (val === undefined || val === null || isNaN(val)) return '₹0';
      return '₹' + Math.round(val).toLocaleString('en-IN');
    }}

    function formatNumber(val) {{
      if (val === undefined || val === null || isNaN(val)) return '0';
      return Math.round(val).toLocaleString('en-IN');
    }}

    // Init function
    window.addEventListener('DOMContentLoaded', () => {{
      populateFilterDropdowns();
      applyFilters();
    }});

    function populateFilterDropdowns() {{
      const courses = new Set();
      const counselors = new Set();
      const sources = new Set();
      const statuses = new Set();

      rawLeads.forEach(d => {{
        if (d.course && d.course !== 'Unknown' && d.course !== 'Other') courses.add(d.course);
        if (d.counselor && d.counselor !== 'Unassigned') counselors.add(d.counselor);
        if (d.source) sources.add(d.source);
        if (d.status) statuses.add(d.status);
      }});

      populateSelect('filterCourse', Array.from(courses).sort());
      populateSelect('filterCounselor', Array.from(counselors).sort());
      populateSelect('filterSource', Array.from(sources).slice(0, 15));
      populateSelect('filterStatus', Array.from(statuses).sort());
    }}

    function populateSelect(selectId, items) {{
      const sel = document.getElementById(selectId);
      sel.innerHTML = '<option value="ALL">All</option>';
      items.forEach(it => {{
        const opt = document.createElement('option');
        opt.value = it;
        opt.textContent = it;
        sel.appendChild(opt);
      }});
    }}

    function handleDateRangeChange() {{
      const val = document.getElementById('filterDateRange').value;
      const customRow = document.getElementById('customDateRow');
      const subtitle = document.getElementById('lblDateSubtitle');

      if (val === 'custom') {{
        customRow.style.display = 'flex';
        subtitle.textContent = 'Select custom start and end date';
      }} else {{
        customRow.style.display = 'none';
        if (val === 'last7') subtitle.textContent = '25 Oct 2026 - 31 Oct 2026';
        else if (val === 'last14') subtitle.textContent = '18 Oct 2026 - 31 Oct 2026';
        else if (val === 'first7') subtitle.textContent = '01 Oct 2026 - 07 Oct 2026';
        else if (val === 'all') subtitle.textContent = '01 Oct 2026 - 31 Oct 2026';
        applyFilters();
      }}
    }}

    function clearAllFilters() {{
      document.getElementById('filterDateRange').value = 'last7';
      document.getElementById('filterCourse').value = 'ALL';
      document.getElementById('filterCounselor').value = 'ALL';
      document.getElementById('filterSource').value = 'ALL';
      document.getElementById('filterStatus').value = 'ALL';
      document.getElementById('customDateRow').style.display = 'none';
      document.getElementById('lblDateSubtitle').textContent = '25 Oct 2026 - 31 Oct 2026';
      applyFilters();
    }}

    // Filter data & recalculate dashboard
    function applyFilters() {{
      const dateOption = document.getElementById('filterDateRange').value;
      const courseFilter = document.getElementById('filterCourse').value;
      const counselorFilter = document.getElementById('filterCounselor').value;
      const sourceFilter = document.getElementById('filterSource').value;
      const statusFilter = document.getElementById('filterStatus').value;

      let startDate = '2026-10-25';
      let endDate = '2026-10-31';

      if (dateOption === 'last14') {{
        startDate = '2026-10-18';
        endDate = '2026-10-31';
      }} else if (dateOption === 'first7') {{
        startDate = '2026-10-01';
        endDate = '2026-10-07';
      }} else if (dateOption === 'all') {{
        startDate = '2026-10-01';
        endDate = '2026-10-31';
      }} else if (dateOption === 'custom') {{
        const ds = document.getElementById('dateStart').value;
        const de = document.getElementById('dateEnd').value;
        if (ds) startDate = ds;
        if (de) endDate = de;
      }}

      // Filter leads
      const filteredLeads = rawLeads.filter(d => {{
        if (d.date < startDate || d.date > endDate) return false;
        if (courseFilter !== 'ALL' && d.course !== courseFilter) return false;
        if (counselorFilter !== 'ALL' && d.counselor !== counselorFilter) return false;
        if (sourceFilter !== 'ALL' && d.source !== sourceFilter) return false;
        if (statusFilter !== 'ALL' && d.status !== statusFilter) return false;
        return true;
      }});

      // Filter calls
      const filteredCalls = rawCalls.filter(c => {{
        if (c.date < startDate || c.date > endDate) return false;
        if (courseFilter !== 'ALL' && c.course !== courseFilter) return false;
        if (counselorFilter !== 'ALL' && c.counselor !== counselorFilter) return false;
        if (sourceFilter !== 'ALL' && c.source !== sourceFilter) return false;
        return true;
      }});

      // Filter payments
      const filteredPayments = rawPayments.filter(p => {{
        if (p.date < startDate || p.date > endDate) return false;
        if (courseFilter !== 'ALL' && p.course !== courseFilter) return false;
        if (counselorFilter !== 'ALL' && p.counselor !== counselorFilter) return false;
        if (sourceFilter !== 'ALL' && p.source !== sourceFilter) return false;
        return true;
      }});

      renderKPIs(filteredLeads, filteredCalls, filteredPayments);
      renderTrends(filteredLeads, filteredPayments, startDate, endDate);
      renderFunnel(filteredLeads);
      renderSourceDonut(filteredLeads);
      renderCounselorCombo(filteredCalls);
      renderCourseTable(filteredLeads);
      renderDailyPayments(filteredPayments, startDate, endDate);
      renderPaymentModeAndSummary(filteredPayments);

      // Render secondary tabs
      renderLeadAnalytics(filteredLeads);
      renderSalesActivity(filteredCalls, filteredLeads);
      renderRevenueViews(filteredLeads, filteredPayments);
      renderPaymentLogs(filteredPayments);
    }}

    // KPI computation
    function renderKPIs(leads, calls, payments) {{
      const totalLeads = leads.length;
      const conversions = leads.filter(l => l.converted === 1).length;
      const convRate = totalLeads > 0 ? ((conversions / totalLeads) * 100).toFixed(1) : 0;
      
      const totalCalls = calls.reduce((acc, c) => acc + c.calls, 0);
      const totalDuration = calls.reduce((acc, c) => acc + c.duration, 0);
      
      let totalRevenue = leads.reduce((acc, l) => acc + l.revenue, 0);
      if (totalRevenue === 0 && payments.length > 0) {{
        totalRevenue = payments.reduce((acc, p) => acc + p.amount, 0);
      }}

      document.getElementById('kpiLeads').textContent = formatNumber(totalLeads);
      document.getElementById('kpiConversions').textContent = formatNumber(conversions);
      document.getElementById('kpiRevenue').textContent = formatINR(totalRevenue);
      document.getElementById('kpiConvRate').textContent = convRate + '%';
      document.getElementById('kpiCalls').textContent = formatNumber(totalCalls);
      document.getElementById('kpiDuration').textContent = formatNumber(totalDuration);
    }}

    // Daily Trends (Leads & Revenue)
    function renderTrends(leads, payments, startDate, endDate) {{
      const dateMap = {{}};
      const cur = new Date(startDate);
      const end = new Date(endDate);

      while (cur <= end) {{
        const dStr = cur.toISOString().slice(0, 10);
        dateMap[dStr] = {{ leads: 0, conversions: 0, revenue: 0 }};
        cur.setDate(cur.getDate() + 1);
      }}

      leads.forEach(l => {{
        if (dateMap[l.date]) {{
          dateMap[l.date].leads += 1;
          if (l.converted === 1) dateMap[l.date].conversions += 1;
          dateMap[l.date].revenue += l.revenue;
        }}
      }});

      payments.forEach(p => {{
        if (dateMap[p.date]) {{
          dateMap[p.date].revenue += p.amount;
        }}
      }});

      const labels = Object.keys(dateMap).map(d => {{
        const dt = new Date(d);
        return dt.toLocaleDateString('en-GB', {{ day: '2-digit', month: 'short' }});
      }});

      const leadCounts = Object.values(dateMap).map(v => v.leads);
      const convCounts = Object.values(dateMap).map(v => v.conversions);
      const revAmounts = Object.values(dateMap).map(v => v.revenue);

      // Leads Trend Chart
      const ctxLeads = document.getElementById('chartLeadsTrend').getContext('2d');
      if (chartLeadsTrendInst) chartLeadsTrendInst.destroy();
      chartLeadsTrendInst = new Chart(ctxLeads, {{
        type: 'line',
        data: {{
          labels: labels,
          datasets: [
            {{
              label: 'Leads',
              data: leadCounts,
              borderColor: '#1a73e8',
              backgroundColor: 'rgba(26, 115, 232, 0.1)',
              tension: 0.3,
              fill: false,
              pointBackgroundColor: '#1a73e8',
              pointRadius: 4
            }},
            {{
              label: 'Conversions',
              data: convCounts,
              borderColor: '#10b981',
              backgroundColor: 'rgba(16, 185, 129, 0.1)',
              tension: 0.3,
              fill: false,
              pointBackgroundColor: '#10b981',
              pointRadius: 4
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{ mode: 'index', intersect: false }}
          }},
          scales: {{
            y: {{ beginAtZero: true, grid: {{ color: '#f1f5f9' }} }},
            x: {{ grid: {{ display: false }} }}
          }}
        }}
      }});

      // Revenue Trend Chart
      const ctxRev = document.getElementById('chartRevenueTrend').getContext('2d');
      if (chartRevenueTrendInst) chartRevenueTrendInst.destroy();
      chartRevenueTrendInst = new Chart(ctxRev, {{
        type: 'line',
        data: {{
          labels: labels,
          datasets: [{{
            label: 'Revenue (₹)',
            data: revAmounts,
            borderColor: '#1a73e8',
            backgroundColor: 'rgba(26, 115, 232, 0.08)',
            tension: 0.3,
            fill: true,
            pointBackgroundColor: '#1a73e8',
            pointRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => 'Revenue: ' + formatINR(ctx.raw)
              }}
            }}
          }},
          scales: {{
            y: {{
              beginAtZero: true,
              ticks: {{
                callback: (val) => '₹' + (val >= 100000 ? (val/100000).toFixed(1) + 'L' : val.toLocaleString('en-IN'))
              }},
              grid: {{ color: '#f1f5f9' }}
            }},
            x: {{ grid: {{ display: false }} }}
          }}
        }}
      }});
    }}

    // Lead Status Funnel
    function renderFunnel(leads) {{
      const total = leads.length || 1;
      const statusCounts = {{
        'New': leads.filter(l => l.stage === 'New' || l.status.includes('New')).length,
        'Contacted': leads.filter(l => l.status.includes('Attempt') || l.calls_made > 0).length,
        'Follow-up': leads.filter(l => l.status.includes('Follow') || l.stage === 'Nurturing').length,
        'Interested': leads.filter(l => l.status.includes('Interested') || l.stage === 'Qualified').length,
        'Demo Scheduled': leads.filter(l => l.status.includes('Free') || l.status.includes('Session') || l.status.includes('Priority')).length,
        'Negotiation': leads.filter(l => l.status.includes('Job') || l.stage === 'Other').length,
        'Paid': leads.filter(l => l.converted === 1 || l.status.includes('Paid')).length,
        'Lost': leads.filter(l => l.status.includes('Lost') || l.stage === 'Lost').length
      }};

      const colors = {{
        'New': '#1e40af',
        'Contacted': '#2563eb',
        'Follow-up': '#0284c7',
        'Interested': '#10b981',
        'Demo Scheduled': '#f59e0b',
        'Negotiation': '#f97316',
        'Paid': '#8b5cf6',
        'Lost': '#ef4444'
      }};

      const container = document.getElementById('funnelContainer');
      container.innerHTML = '';

      Object.entries(statusCounts).forEach(([stage, count]) => {{
        const pct = ((count / total) * 100).toFixed(1);
        const barWidth = Math.max(12, Math.min(100, Math.round((count / (statusCounts['New'] || total)) * 100)));

        const row = document.createElement('div');
        row.className = 'funnel-step';
        row.innerHTML = `
          <span class="funnel-step-name">${{stage}}</span>
          <div class="funnel-bar-wrap">
            <div class="funnel-bar-fill" style="width: ${{barWidth}}%; background-color: ${{colors[stage]}};">
              ${{count}}
            </div>
          </div>
          <span class="funnel-step-pct">${{pct}}%</span>
        `;
        container.appendChild(row);
      }});
    }}

    // Leads by Source Donut
    function renderSourceDonut(leads) {{
      const sourceMap = {{}};
      leads.forEach(l => {{
        let s = l.source || 'Other';
        if (s.includes('WhatsApp')) s = 'WhatsApp';
        else if (s.includes('Call')) s = 'Call Logs';
        else if (s.includes('Ads') || s.includes('Landing')) s = 'Landing Page Ads';
        else if (s.includes('Facebook')) s = 'Facebook Ads';
        else if (s.includes('Website')) s = 'Website Forms';
        sourceMap[s] = (sourceMap[s] || 0) + 1;
      }});

      // Top 5 sources + other
      const sorted = Object.entries(sourceMap).sort((a,b) => b[1] - a[1]);
      const top5 = sorted.slice(0, 5);
      const otherCount = sorted.slice(5).reduce((acc, x) => acc + x[1], 0);
      if (otherCount > 0) top5.push(['Other', otherCount]);

      const labels = top5.map(x => x[0]);
      const data = top5.map(x => x[1]);

      const ctx = document.getElementById('chartSourceDonut').getContext('2d');
      if (chartSourceDonutInst) chartSourceDonutInst.destroy();
      chartSourceDonutInst = new Chart(ctx, {{
        type: 'doughnut',
        data: {{
          labels: labels,
          datasets: [{{
            data: data,
            backgroundColor: ['#1a73e8', '#10b981', '#f59e0b', '#8b5cf6', '#06b6d4', '#cbd5e1']
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'right',
              labels: {{ boxWidth: 10, font: {{ size: 10 }} }}
            }}
          }},
          cutout: '65%'
        }}
      }});
    }}

    // Calls by Counselor Combo
    function renderCounselorCombo(calls) {{
      const counselorMap = {{}};
      calls.forEach(c => {{
        if (!counselorMap[c.counselor]) {{
          counselorMap[c.counselor] = {{ calls: 0, duration: 0 }};
        }}
        counselorMap[c.counselor].calls += c.calls;
        counselorMap[c.counselor].duration += c.duration;
      }});

      const labels = Object.keys(counselorMap).slice(0, 6);
      const callData = labels.map(c => counselorMap[c].calls);
      const durData = labels.map(c => Math.round(counselorMap[c].duration));

      const ctx = document.getElementById('chartCounselorCombo').getContext('2d');
      if (chartCounselorComboInst) chartCounselorComboInst.destroy();
      chartCounselorComboInst = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [
            {{
              type: 'bar',
              label: 'Total Calls',
              data: callData,
              backgroundColor: '#1a73e8',
              borderRadius: 4,
              yAxisID: 'y'
            }},
            {{
              type: 'line',
              label: 'Total Duration (Mins)',
              data: durData,
              borderColor: '#10b981',
              backgroundColor: '#10b981',
              tension: 0.3,
              pointRadius: 4,
              yAxisID: 'y1'
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ display: false }} }},
          scales: {{
            y: {{
              type: 'linear',
              position: 'left',
              beginAtZero: true,
              grid: {{ color: '#f1f5f9' }}
            }},
            y1: {{
              type: 'linear',
              position: 'right',
              beginAtZero: true,
              grid: {{ drawOnChartArea: false }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{ font: {{ size: 10 }} }}
            }}
          }}
        }}
      }});
    }}

    // Course Performance Table
    function renderCourseTable(leads) {{
      const courseMap = {{}};
      leads.forEach(l => {{
        let c = l.course || 'Unknown';
        if (!courseMap[c]) {{
          courseMap[c] = {{ leads: 0, conv: 0, rev: 0 }};
        }}
        courseMap[c].leads += 1;
        if (l.converted === 1) courseMap[c].conv += 1;
        courseMap[c].rev += l.revenue;
      }});

      const sorted = Object.entries(courseMap).sort((a,b) => b[1].leads - a[1].leads);
      const tbody = document.getElementById('tbodyCoursePerf');
      tbody.innerHTML = '';

      sorted.slice(0, 8).forEach(([course, st]) => {{
        const rate = st.leads > 0 ? ((st.conv / st.leads) * 100).toFixed(2) + '%' : '0.00%';
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight: 600;">${{course}}</td>
          <td class="numeric">${{st.leads}}</td>
          <td class="numeric">${{st.conv}}</td>
          <td class="numeric"><span class="badge-conv">${{rate}}</span></td>
          <td class="numeric" style="font-weight: 700;">${{formatINR(st.rev)}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Daily Payments Trend Combo Chart
    function renderDailyPayments(payments, startDate, endDate) {{
      const dateMap = {{}};
      const cur = new Date(startDate);
      const end = new Date(endDate);

      while (cur <= end) {{
        const dStr = cur.toISOString().slice(0, 10);
        dateMap[dStr] = {{ count: 0, revenue: 0 }};
        cur.setDate(cur.getDate() + 1);
      }}

      payments.forEach(p => {{
        if (dateMap[p.date]) {{
          dateMap[p.date].count += 1;
          dateMap[p.date].revenue += p.amount;
        }}
      }});

      const labels = Object.keys(dateMap).map(d => {{
        const dt = new Date(d);
        return dt.toLocaleDateString('en-GB', {{ day: '2-digit', month: 'short' }});
      }});
      const counts = Object.values(dateMap).map(v => v.count);
      const revs = Object.values(dateMap).map(v => v.revenue);

      const ctx = document.getElementById('chartDailyPayments').getContext('2d');
      if (chartDailyPaymentsInst) chartDailyPaymentsInst.destroy();
      chartDailyPaymentsInst = new Chart(ctx, {{
        data: {{
          labels: labels,
          datasets: [
            {{
              type: 'bar',
              label: 'Payments Count',
              data: counts,
              backgroundColor: '#1a73e8',
              borderRadius: 4,
              yAxisID: 'y'
            }},
            {{
              type: 'line',
              label: 'Revenue',
              data: revs,
              borderColor: '#10b981',
              backgroundColor: '#10b981',
              tension: 0.3,
              pointRadius: 4,
              yAxisID: 'y1'
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ display: false }} }},
          scales: {{
            y: {{
              type: 'linear',
              position: 'left',
              beginAtZero: true,
              grid: {{ color: '#f1f5f9' }}
            }},
            y1: {{
              type: 'linear',
              position: 'right',
              beginAtZero: true,
              ticks: {{
                callback: (val) => '₹' + (val >= 100000 ? (val/100000).toFixed(1) + 'L' : val.toLocaleString('en-IN'))
              }},
              grid: {{ drawOnChartArea: false }}
            }},
            x: {{ grid: {{ display: false }} }}
          }}
        }}
      }});
    }}

    // Payment Mode & Summary Card
    function renderPaymentModeAndSummary(payments) {{
      const modeMap = {{ 'UPI': 0, 'Bank Transfer': 0, 'Card': 0, 'Cash': 0 }};
      let totalRev = 0;

      payments.forEach(p => {{
        const m = p.mode || 'UPI';
        modeMap[m] = (modeMap[m] || 0) + p.amount;
        totalRev += p.amount;
      }});

      const totalPayments = payments.length;
      const avgOrderVal = totalPayments > 0 ? Math.round(totalRev / totalPayments) : 0;

      document.getElementById('summaryTotalPayments').textContent = formatNumber(totalPayments);
      document.getElementById('summaryTotalRevenue').textContent = formatINR(totalRev);
      document.getElementById('summaryAvgOrderValue').textContent = formatINR(avgOrderVal);

      const labels = Object.keys(modeMap);
      const data = Object.values(modeMap);

      const ctx = document.getElementById('chartPaymentMode').getContext('2d');
      if (chartPaymentModeInst) chartPaymentModeInst.destroy();
      chartPaymentModeInst = new Chart(ctx, {{
        type: 'doughnut',
        data: {{
          labels: labels,
          datasets: [{{
            data: data,
            backgroundColor: ['#1a73e8', '#10b981', '#f59e0b', '#cbd5e1']
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ boxWidth: 8, font: {{ size: 9 }} }}
            }}
          }},
          cutout: '60%'
        }}
      }});
    }}

    // Secondary Tabs Renderers
    function renderLeadAnalytics(leads) {{
      // Stage breakdown
      const stageMap = {{}};
      leads.forEach(l => {{
        stageMap[l.stage] = (stageMap[l.stage] || 0) + 1;
      }});

      const ctxStage = document.getElementById('chartLeadStageBar').getContext('2d');
      if (chartLeadStageBarInst) chartLeadStageBarInst.destroy();
      chartLeadStageBarInst = new Chart(ctxStage, {{
        type: 'bar',
        data: {{
          labels: Object.keys(stageMap),
          datasets: [{{
            label: 'Leads',
            data: Object.values(stageMap),
            backgroundColor: '#1a73e8',
            borderRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ display: false }} }}
        }}
      }});

      // Workable vs Junk
      const workable = leads.filter(l => l.workable === 1).length;
      const junk = leads.length - workable;

      const ctxWork = document.getElementById('chartLeadWorkableDonut').getContext('2d');
      if (chartLeadWorkableDonutInst) chartLeadWorkableDonutInst.destroy();
      chartLeadWorkableDonutInst = new Chart(ctxWork, {{
        type: 'doughnut',
        data: {{
          labels: ['Workable Leads', 'Junk / Non-workable'],
          datasets: [{{
            data: [workable, junk],
            backgroundColor: ['#10b981', '#ef4444']
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false
        }}
      }});

      // Geo Table
      const cityMap = {{}};
      leads.forEach(l => {{
        const c = l.city !== 'Unknown' ? l.city : (l.state !== 'Unknown' ? l.state : 'Other / Online');
        if (!cityMap[c]) cityMap[c] = {{ leads: 0, conv: 0 }};
        cityMap[c].leads += 1;
        if (l.converted === 1) cityMap[c].conv += 1;
      }});

      const tbodyGeo = document.getElementById('tbodyGeo');
      tbodyGeo.innerHTML = '';
      Object.entries(cityMap).sort((a,b) => b[1].leads - a[1].leads).slice(0, 10).forEach(([city, st]) => {{
        const tr = document.createElement('tr');
        const rate = st.leads > 0 ? ((st.conv / st.leads) * 100).toFixed(1) + '%' : '0.0%';
        tr.innerHTML = `
          <td>${{city}}</td>
          <td class="numeric">${{st.leads}}</td>
          <td class="numeric">${{st.conv}}</td>
          <td class="numeric">${{rate}}</td>
        `;
        tbodyGeo.appendChild(tr);
      }});
    }}

    function renderSalesActivity(calls, leads) {{
      const map = {{}};
      calls.forEach(c => {{
        if (!map[c.counselor]) map[c.counselor] = {{ calls: 0, conn: 0, dur: 0 }};
        map[c.counselor].calls += c.calls;
        map[c.counselor].conn += c.connected;
        map[c.counselor].dur += c.duration;
      }});

      const leadHandledMap = {{}};
      leads.forEach(l => {{
        if (!leadHandledMap[l.counselor]) leadHandledMap[l.counselor] = {{ leads: 0, conv: 0 }};
        leadHandledMap[l.counselor].leads += 1;
        if (l.converted === 1) leadHandledMap[l.counselor].conv += 1;
      }});

      const tbody = document.getElementById('tbodyCounselorLeaderboard');
      tbody.innerHTML = '';

      Object.entries(map).sort((a,b) => b[1].calls - a[1].calls).forEach(([counselor, st]) => {{
        const connRate = st.calls > 0 ? ((st.conn / st.calls) * 100).toFixed(1) + '%' : '0.0%';
        const avgSec = st.calls > 0 ? Math.round((st.dur * 60) / st.calls) : 0;
        const lh = leadHandledMap[counselor] || {{ leads: 0, conv: 0 }};

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight: 700;">${{counselor}}</td>
          <td class="numeric">${{st.calls}}</td>
          <td class="numeric">${{st.conn}}</td>
          <td class="numeric"><span class="badge-conv">${{connRate}}</span></td>
          <td class="numeric">${{Math.round(st.dur)}}</td>
          <td class="numeric">${{avgSec}}s</td>
          <td class="numeric">${{lh.leads}}</td>
          <td class="numeric">${{lh.conv}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function renderRevenueViews(leads, payments) {{
      // Course rev donut
      const cRev = {{}};
      leads.forEach(l => {{
        if (l.revenue > 0) cRev[l.course] = (cRev[l.course] || 0) + l.revenue;
      }});

      const ctxC = document.getElementById('chartCourseRevDonut').getContext('2d');
      if (chartCourseRevDonutInst) chartCourseRevDonutInst.destroy();
      chartCourseRevDonutInst = new Chart(ctxC, {{
        type: 'doughnut',
        data: {{
          labels: Object.keys(cRev),
          datasets: [{{
            data: Object.values(cRev),
            backgroundColor: ['#1a73e8', '#10b981', '#f59e0b', '#8b5cf6', '#06b6d4', '#ec4899']
          }}]
        }},
        options: {{ responsive: true, maintainAspectRatio: false }}
      }});

      // Counselor rev bar
      const counsRev = {{}};
      leads.forEach(l => {{
        if (l.revenue > 0) counsRev[l.counselor] = (counsRev[l.counselor] || 0) + l.revenue;
      }});

      const ctxCo = document.getElementById('chartCounselorRevBar').getContext('2d');
      if (chartCounselorRevBarInst) chartCounselorRevBarInst.destroy();
      chartCounselorRevBarInst = new Chart(ctxCo, {{
        type: 'bar',
        data: {{
          labels: Object.keys(counsRev),
          datasets: [{{
            label: 'Revenue (₹)',
            data: Object.values(counsRev),
            backgroundColor: '#10b981',
            borderRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            tooltip: {{ callbacks: {{ label: (ctx) => formatINR(ctx.raw) }} }}
          }}
        }}
      }});
    }}

    function renderPaymentLogs(payments) {{
      const tbody = document.getElementById('tbodyPaymentLogs');
      tbody.innerHTML = '';

      payments.slice(0, 30).forEach(p => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><code>${{p.id}}</code></td>
          <td>${{p.date}}</td>
          <td>${{p.name}}</td>
          <td>${{p.course}}</td>
          <td>${{p.counselor}}</td>
          <td><span class="badge-conv">${{p.mode}}</span></td>
          <td class="numeric" style="font-weight: 700;">${{formatINR(p.amount)}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Tab Switching
    function switchTab(tabKey) {{
      document.querySelectorAll('.tab-view').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));

      const target = document.getElementById('view' + tabKey);
      if (target) target.classList.add('active');

      const btn = event.currentTarget;
      if (btn) btn.classList.add('active');

      const titles = {{
        'Executive': 'Executive Dashboard',
        'LeadAnalytics': 'Lead Analytics & Pipeline Funnel',
        'SalesActivity': 'Sales & Counselor Activity Metrics',
        'Revenue': 'Revenue & Order Realization',
        'Payments': 'Payments & Transaction Logs',
        'DataDict': 'TeleCRM Data Dictionary'
      }};
      document.getElementById('topViewTitle').textContent = titles[tabKey] || 'Executive Dashboard';
    }}

    // Upload Modal & Drag-and-drop
    function openUploadModal() {{
      document.getElementById('uploadModal').style.display = 'flex';
    }}

    function closeUploadModal() {{
      document.getElementById('uploadModal').style.display = 'none';
      document.getElementById('uploadStatus').textContent = '';
    }}

    function handleFileSelect(evt) {{
      const file = evt.target.files[0];
      if (!file) return;

      const status = document.getElementById('uploadStatus');
      status.textContent = 'Parsing ' + file.name + '...';

      Papa.parse(file, {{
        header: true,
        dynamicTyping: true,
        skipEmptyLines: true,
        complete: function(results) {{
          processUploadedCSV(results.data, file.name);
        }}
      }});
    }}

    function processUploadedCSV(rows, fileName) {{
      const status = document.getElementById('uploadStatus');
      if (rows.length === 0) {{
        status.textContent = 'Error: Empty CSV file.';
        return;
      }}

      // Check if leads file or activities file
      const sample = rows[0];
      if ('Lead ID' in sample || 'Lead Source' in sample) {{
        // Leads file
        rawLeads = rows.map(r => {{
          const cDate = r['Created On (IST)'] ? String(r['Created On (IST)']).slice(0, 10) : '';
          return {{
            id: String(r['Lead ID'] || Math.random()),
            name: String(r['Name'] || 'Lead'),
            date: cDate,
            status: String(r['Status'] || 'New Lead'),
            stage: String(r['Stage'] || 'New'),
            counselor: String(r['Assignee'] || 'Unassigned'),
            source: String(r['Lead Source'] || 'Other'),
            course: String(r['Course'] || 'Other'),
            converted: String(r['Converted']).toLowerCase() === 'yes' ? 1 : 0,
            revenue: Number(r['Lifetime Value']) || 0,
            calls_made: Number(r['Calls Made']) || 0,
            calls_conn: Number(r['Calls Connected']) || 0,
            talk_time: Number(r['Talk Time (min)']) || 0,
            city: String(r['City'] || 'Unknown'),
            state: String(r['State'] || 'Unknown'),
            workable: String(r['Workable']).toLowerCase() === 'yes' ? 1 : 0
          }};
        }});

        populateFilterDropdowns();
        applyFilters();
        status.textContent = `Successfully updated ${{rawLeads.length}} leads!`;
        setTimeout(closeUploadModal, 1500);
      }} else if ('Activity ID' in sample || 'Activity' in sample) {{
        status.textContent = `Processed ${{rows.length}} activity records!`;
        setTimeout(closeUploadModal, 1500);
      }} else {{
        status.textContent = 'Unknown CSV columns. Please use TeleCRM export format.';
      }}
    }}
  </script>
</body>
</html>'''

    with open('ksr_executive_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    print("ksr_executive_dashboard.html created successfully!")

if __name__ == '__main__':
    generate_html()
