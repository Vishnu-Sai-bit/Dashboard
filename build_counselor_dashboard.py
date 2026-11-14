import json
import os
import sys

def generate_counselor_dashboard():
    with open('dashboard_data.json', 'r', encoding='utf-8') as f:
        data_json_str = f.read()

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KSR Datavision — Counselor Workspace</title>
  
  <!-- Font & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  
  <!-- Chart.js & Plugins -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0"></script>

  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #f1f5f9;
      color: #0f172a;
      line-height: 1.45;
      font-size: 13px;
    }}

    /* Top Navigation Header */
    .top-header {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}

    .header-inner {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 10px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}

    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-icon {{
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: linear-gradient(135deg, #16a34a 0%, #059669 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 16px;
      box-shadow: 0 2px 4px rgba(22, 163, 74, 0.25);
    }}

    .brand-title {{
      font-size: 15px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.3px;
    }}

    .brand-subtitle {{
      font-size: 11px;
      font-weight: 600;
      color: #16a34a;
      background: #dcfce7;
      padding: 1px 7px;
      border-radius: 10px;
      margin-left: 6px;
    }}

    /* Counselor Identity Bar */
    .counselor-picker-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: #f8fafc;
      padding: 4px 12px;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
    }}

    .counselor-picker-wrap label {{
      font-size: 11px;
      font-weight: 700;
      color: #475569;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }}

    .counselor-select {{
      font-family: inherit;
      font-size: 12.5px;
      font-weight: 700;
      color: #0f172a;
      background: transparent;
      border: none;
      outline: none;
      cursor: pointer;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn-switch-admin {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .btn-switch-admin:hover {{
      background: #dbeafe;
      border-color: #93c5fd;
    }}

    /* Filter Bar */
    .filter-bar {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      padding: 8px 20px;
    }}

    .filter-inner {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .filter-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .filter-item {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11.5px;
      font-weight: 600;
      color: #475569;
    }}

    .filter-select {{
      padding: 4px 8px;
      font-size: 11.5px;
      font-weight: 600;
      color: #1e293b;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      outline: none;
      cursor: pointer;
    }}

    /* Main Container */
    .main-wrap {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 16px 20px 40px;
    }}

    /* Counselor Banner */
    .counselor-banner {{
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: #ffffff;
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 4px 10px rgba(15, 23, 42, 0.08);
    }}

    .banner-profile {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .profile-avatar {{
      width: 46px;
      height: 46px;
      border-radius: 50%;
      background: #16a34a;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 700;
      border: 2px solid #86efac;
    }}

    .profile-info h2 {{
      font-size: 16px;
      font-weight: 800;
      letter-spacing: -0.2px;
    }}

    .profile-info p {{
      font-size: 11.5px;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 2px;
    }}

    /* KPI Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 12px;
      margin-bottom: 16px;
    }}

    .kpi-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }}

    .kpi-card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}

    .kpi-title {{
      font-size: 10.5px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.2px;
    }}

    .kpi-icon {{
      width: 24px;
      height: 24px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
    }}

    .icon-blue {{ background: #eff6ff; color: #2563eb; }}
    .icon-green {{ background: #f0fdf4; color: #16a34a; }}
    .icon-amber {{ background: #fffbeb; color: #d97706; }}
    .icon-purple {{ background: #faf5ff; color: #9333ea; }}
    .icon-red {{ background: #fef2f2; color: #dc2626; }}

    .kpi-value {{
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
      line-height: 1.2;
    }}

    .kpi-sub {{
      font-size: 10px;
      font-weight: 600;
      color: #64748b;
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* Main Workspace Grid (Row 2) */
    .workspace-grid {{
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }}

    .card-panel {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 14px 16px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }}

    .panel-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 8px;
    }}

    .panel-title {{
      font-size: 13px;
      font-weight: 700;
      color: #1e293b;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Funnel Styling (Exact 9 Stages) */
    .funnel-container {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .funnel-row {{
      display: grid;
      grid-template-columns: 140px 1fr 46px;
      align-items: center;
      gap: 8px;
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
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px dashed #e2e8f0;
      display: flex;
      justify-content: space-between;
      font-size: 9.5px;
      color: #64748b;
    }}

    /* Interactive Action Queue Table */
    .leads-table-wrap {{
      overflow-x: auto;
      max-height: 400px;
    }}

    .action-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
    }}

    .action-table th {{
      background: #f8fafc;
      color: #475569;
      font-weight: 700;
      text-align: left;
      padding: 7px 10px;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 2;
    }}

    .action-table td {{
      padding: 6.5px 10px;
      border-bottom: 1px solid #f1f5f9;
      color: #1e293b;
    }}

    .action-table tr:hover {{
      background: #f8fafc;
    }}

    .badge-status {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 10px;
      font-size: 9.5px;
      font-weight: 700;
    }}

    .st-new {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
    .st-followup {{ background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }}
    .st-interested {{ background: #fefce8; color: #a16207; border: 1px solid #fef08a; }}
    .st-paid {{ background: #faf5ff; color: #7e22ce; border: 1px solid #e9d5ff; }}
    .st-lost {{ background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; }}

    /* Quick Filter Pills for Table */
    .table-pills {{
      display: flex;
      gap: 6px;
      align-items: center;
      margin-bottom: 8px;
    }}

    .pill-btn {{
      padding: 3px 9px;
      font-size: 10.5px;
      font-weight: 600;
      border-radius: 12px;
      border: 1px solid #cbd5e1;
      background: #f8fafc;
      color: #475569;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .pill-btn.active {{
      background: #16a34a;
      color: #ffffff;
      border-color: #16a34a;
    }}

    /* Action Badges */
    .btn-action-call {{
      background: #16a34a;
      color: #ffffff;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 700;
      border: none;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="top-header">
    <div class="header-inner">
      <div class="brand-wrap">
        <div class="brand-icon">
          <i class="fa-solid fa-headset"></i>
        </div>
        <div class="brand-title">
          KSR DATAVISION
          <span class="brand-subtitle">COUNSELOR WORKSPACE</span>
        </div>
      </div>

      <!-- Counselor Profile Selector -->
      <div class="counselor-picker-wrap">
        <label><i class="fa-solid fa-user-circle"></i> Counselor:</label>
        <select id="selCounselor" class="counselor-select" onchange="onCounselorChange()">
          <option value="Nandeeshwar Reddy">Nandeeshwar Reddy</option>
          <option value="Satish Reddy">Satish Reddy</option>
          <option value="Charishma">Charishma</option>
          <option value="Chaitanya">Chaitanya</option>
          <option value="Sagar">Sagar</option>
          <option value="Mahesh Reddy">Mahesh Reddy</option>
          <option value="Pavithra">Pavithra</option>
        </select>
      </div>

      <!-- Actions & Switchers -->
      <div class="header-actions">
        <a href="index.html" class="btn-switch-admin">
          <i class="fa-solid fa-user-shield"></i>
          <span>Switch to Admin Portal</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Filter Bar -->
  <div class="filter-bar">
    <div class="filter-inner">
      <div class="filter-group">
        <div class="filter-item">
          <i class="fa-regular fa-calendar"></i>
          <span>Date Range:</span>
          <select id="selDateRange" class="filter-select" onchange="renderCounselorView()">
            <option value="today" selected>Today (31 Oct 2026)</option>
            <option value="yesterday">Yesterday (30 Oct 2026)</option>
            <option value="all">This Month (Full Month)</option>
            <option value="last7">Last 7 Days</option>
            <option value="last14">Last 14 Days</option>
          </select>
        </div>

        <div class="filter-item">
          <i class="fa-solid fa-book-open"></i>
          <span>Course:</span>
          <select id="selCourse" class="filter-select" onchange="renderCounselorView()">
            <option value="ALL">All Courses</option>
          </select>
        </div>
      </div>

      <div style="font-size: 11px; color: #64748b; font-weight: 600;" id="filterStatusText">
        Showing records assigned to you
      </div>
    </div>
  </div>

  <!-- Main Content -->
  <main class="main-wrap">

    <!-- Counselor Profile Header Banner -->
    <div class="counselor-banner">
      <div class="banner-profile">
        <div class="profile-avatar" id="counsAvatar">N</div>
        <div class="profile-info">
          <h2 id="counsName">Nandeeshwar Reddy</h2>
          <p>
            <span id="counsEmail"><i class="fa-regular fa-envelope"></i> staff-nandeeshwar@ksrdatavision.com</span>
            &bull;
            <span><i class="fa-solid fa-shield-halved"></i> Dedicated Workspace</span>
          </p>
        </div>
      </div>


    </div>

    <!-- 7 Personal KPI Cards -->
    <div class="kpi-grid">
      <!-- 1. My Leads in Period -->
      <div class="kpi-card">
        <div class="kpi-card-header">
          <span class="kpi-title">My Leads</span>
          <div class="kpi-icon icon-blue"><i class="fa-solid fa-users"></i></div>
        </div>
        <div class="kpi-value" id="kpiMyLeads">259</div>
        <div class="kpi-sub" id="kpiMyLeadsSub">Assigned in period</div>
      </div>

      <!-- 2. Today's Fresh Leads -->
      <div class="kpi-card">
        <div class="kpi-card-header">
          <span class="kpi-title">Fresh Leads</span>
          <div class="kpi-icon icon-blue"><i class="fa-solid fa-bolt"></i></div>
        </div>
        <div class="kpi-value" id="kpiTodayFresh">139</div>
        <div class="kpi-sub">Received Today</div>
      </div>

      <!-- 3. Uncalled Queue (Action Req!) -->
      <div class="kpi-card" style="border-left: 3px solid #f59e0b;">
        <div class="kpi-card-header">
          <span class="kpi-title" style="color: #b45309;">Uncalled Queue</span>
          <div class="kpi-icon icon-amber"><i class="fa-solid fa-hourglass-start"></i></div>
        </div>
        <div class="kpi-value" id="kpiQueueCount" style="color: #b45309;">0</div>
        <div class="kpi-sub" id="kpiQueueSub">Pending first call</div>
      </div>

      <!-- 4. Follow-up Tasks -->
      <div class="kpi-card">
        <div class="kpi-card-header">
          <span class="kpi-title">Follow-ups</span>
          <div class="kpi-icon icon-green"><i class="fa-solid fa-calendar-check"></i></div>
        </div>
        <div class="kpi-value" id="kpiFollowups">33</div>
        <div class="kpi-sub">Scheduled for Today</div>
      </div>

      <!-- 5. My Conversions -->
      <div class="kpi-card">
        <div class="kpi-card-header">
          <span class="kpi-title">Conversions</span>
          <div class="kpi-icon icon-green"><i class="fa-solid fa-circle-check"></i></div>
        </div>
        <div class="kpi-value" id="kpiConversions">0</div>
        <div class="kpi-sub" id="kpiConvRate">0.00% Conv. Rate</div>
      </div>

      <!-- 6. Calls Made Today -->
      <div class="kpi-card">
        <div class="kpi-card-header">
          <span class="kpi-title">Calls Made</span>
          <div class="kpi-icon icon-blue"><i class="fa-solid fa-phone"></i></div>
        </div>
        <div class="kpi-value" id="kpiCallsMade">71</div>
        <div class="kpi-sub" id="kpiCallsSub">Calls logged</div>
      </div>

      <!-- 7. Talk Time -->
      <div class="kpi-card">
        <div class="kpi-card-header">
          <span class="kpi-title">Talk Time</span>
          <div class="kpi-icon icon-purple"><i class="fa-regular fa-clock"></i></div>
        </div>
        <div class="kpi-value" id="kpiTalkTime">173m</div>
        <div class="kpi-sub" id="kpiTalkTimeSub">2.9 Hours</div>
      </div>
    </div>

    <!-- Row 2: Funnel + Hourly Calling Performance -->
    <div class="workspace-grid">

      <!-- Lead Status Funnel for this Counselor -->
      <div class="card-panel">
        <div class="panel-header">
          <span class="panel-title"><i class="fa-solid fa-filter" style="color: #2563eb;"></i> My Lead Status Funnel</span>
          <span id="badgeCounselorFunnel" style="font-size: 10px; font-weight: 600; color: #1d4ed8; background: #dbeafe; padding: 2px 8px; border-radius: 12px; border: 1px solid #bfdbfe;">Today's Leads</span>
        </div>
        <div class="funnel-container" id="funnelList">
          <!-- Dynamically populated -->
        </div>
        <div class="funnel-sub-footer">
          <span><i class="fa-solid fa-hourglass-start" style="color: #f59e0b;"></i> In Queue: <strong style="color: #1e293b;" id="subQueueCount">0</strong></span>
          <span><i class="fa-solid fa-ban" style="color: #ef4444;"></i> Direct Lost: <strong style="color: #1e293b;" id="subLostCount">0</strong></span>
          <span><i class="fa-solid fa-phone-slash" style="color: #64748b;"></i> Not Reachable: <strong style="color: #1e293b;" id="subUnreachCount">0</strong></span>
        </div>
      </div>

      <!-- Hourly Calling Distribution & Connect Rate -->
      <div class="card-panel">
        <div class="panel-header">
          <span class="panel-title"><i class="fa-solid fa-phone-volume" style="color: #16a34a;"></i> My Hourly Calling &amp; Connect Rate</span>
          <span style="font-size: 10.5px; color: #64748b; font-weight: 600;" id="titleHourlyCounselor">Today (12 AM - 11 PM)</span>
        </div>
        <div style="height: 230px; position: relative;">
          <canvas id="chartCounselorHourly"></canvas>
        </div>
      </div>

    </div>

    <!-- Row 3: Pipeline Status Breakdown + Course Admissions Intelligence -->
    <div class="workspace-grid" style="margin-bottom: 16px;">
      <!-- Pipeline Status Donut -->
      <div class="card-panel">
        <div class="panel-header">
          <span class="panel-title"><i class="fa-solid fa-chart-pie" style="color: #8b5cf6;"></i> My Pipeline &amp; Status Distribution</span>
          <span style="font-size: 10.5px; color: #64748b; font-weight: 600;">Active Cohort Share</span>
        </div>
        <div style="height: 230px; position: relative;">
          <canvas id="chartCounselorPipeline"></canvas>
        </div>
      </div>

      <!-- Course Admissions Bar Chart -->
      <div class="card-panel">
        <div class="panel-header">
          <span class="panel-title"><i class="fa-solid fa-book-open" style="color: #2563eb;"></i> Course Inquiries &amp; Admissions</span>
          <span style="font-size: 10.5px; color: #64748b; font-weight: 600;">Top Performing Courses</span>
        </div>
        <div style="height: 230px; position: relative;">
          <canvas id="chartCounselorCourses"></canvas>
        </div>
      </div>
    </div>

    <!-- Row 4: 30-Day Calling Volume & Talk Time Trajectory -->
    <div class="card-panel" style="margin-bottom: 16px;">
      <div class="panel-header">
        <span class="panel-title"><i class="fa-solid fa-chart-line" style="color: #059669;"></i> My Daily Calling &amp; Talk Time Trajectory</span>
        <span style="font-size: 10.5px; color: #64748b; font-weight: 600;" id="titleDailyTrajectory">30-Day Calling Momentum</span>
      </div>
      <div style="height: 220px; position: relative;">
        <canvas id="chartCounselorDailyTrend"></canvas>
      </div>
    </div>

    <!-- Row 3: Actionable Leads Queue Table -->
    <div class="card-panel">
      <div class="panel-header">
        <div style="display: flex; align-items: center; gap: 12px;">
          <span class="panel-title"><i class="fa-solid fa-list-check" style="color: #2563eb;"></i> My Leads & Follow-up Queue</span>
          <span id="badgeTableCount" style="font-size: 10.5px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 8px; border-radius: 10px;">Showing 0 leads</span>
        </div>
        <input type="text" id="inputSearchLeads" placeholder="Search by name, course..." style="padding: 4px 10px; font-size: 11px; border: 1px solid #cbd5e1; border-radius: 5px; outline: none; width: 220px;" oninput="onSearchTable()">
      </div>

      <!-- Table Filter Pills -->
      <div class="table-pills">
        <button class="pill-btn active" data-pill="ALL" onclick="setTablePill('ALL', this)">All Assigned Leads</button>
        <button class="pill-btn" data-pill="TODAY" onclick="setTablePill('TODAY', this)">Today's Fresh Leads</button>
        <button class="pill-btn" data-pill="QUEUE" onclick="setTablePill('QUEUE', this)"><i class="fa-solid fa-triangle-exclamation"></i> Uncalled Queue</button>
        <button class="pill-btn" data-pill="FOLLOWUP" onclick="setTablePill('FOLLOWUP', this)"><i class="fa-solid fa-clock"></i> Follow-ups</button>
        <button class="pill-btn" data-pill="INTERESTED" onclick="setTablePill('INTERESTED', this)"><i class="fa-solid fa-star"></i> Interested</button>
        <button class="pill-btn" data-pill="CONVERTED" onclick="setTablePill('CONVERTED', this)"><i class="fa-solid fa-circle-check"></i> Enrolled / Converted</button>
        <button class="pill-btn" data-pill="LOST" onclick="setTablePill('LOST', this)">Lost</button>
      </div>

      <!-- Leads Table -->
      <div class="leads-table-wrap">
        <table class="action-table">
          <thead>
            <tr>
              <th>Lead Name</th>
              <th>Phone</th>
              <th>Course</th>
              <th>Created On</th>
              <th>Status</th>
              <th class="text-right">Calls Made</th>
              <th class="text-right">Talk Time</th>
              <th>Action Needed</th>
            </tr>
          </thead>
          <tbody id="tbodyCounselorLeads">
            <!-- Dynamically populated -->
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <script>
    window.TELECRM_LIVE_DATA = {data_json_str};
  </script>

  <script>
    if (typeof ChartDataLabels !== 'undefined') {{
      Chart.register(ChartDataLabels);
    }}

    let chartCounselorHourly = null;
    let chartCounselorPipeline = null;
    let chartCounselorCourses = null;
    let chartCounselorDailyTrend = null;
    let activeTablePill = 'ALL';
    let currentTableSearch = '';

    const HOUR_LABELS_12H = [
      '12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM',
      '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM',
      '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM',
      '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM'
    ];

    function initCounselorPage() {{
      const t = window.TELECRM_LIVE_DATA;
      
      // Populate courses in dropdown
      const selCourse = document.getElementById('selCourse');
      const courses = [...new Set(t.leads.map(l => l.course))].filter(Boolean).sort();
      courses.forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c;
        opt.textContent = c;
        selCourse.appendChild(opt);
      }});

      renderCounselorView();
    }}

    function onCounselorChange() {{
      renderCounselorView();
    }}

    function onSearchTable() {{
      currentTableSearch = document.getElementById('inputSearchLeads').value.toLowerCase().trim();
      renderTableOnly();
    }}

    function setTablePill(pillKey, btn) {{
      activeTablePill = pillKey;
      document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderTableOnly();
    }}

    let cachedFilteredCounselorLeads = [];

    function renderCounselorView() {{
      const t = window.TELECRM_LIVE_DATA;
      const counselorName = document.getElementById('selCounselor').value;
      const dateRangeVal = document.getElementById('selDateRange').value;
      const courseVal = document.getElementById('selCourse').value;

      // Update Counselor Banner Info
      document.getElementById('counsName').textContent = counselorName;
      document.getElementById('counsAvatar').textContent = counselorName.charAt(0);
      document.getElementById('counsEmail').innerHTML = `<i class="fa-regular fa-envelope"></i> staff-${{counselorName.toLowerCase().replace(/\\s+/g, '.')}}@ksrdatavision.com`;

      // Calculate Counselor Month Totals for Banner
      const cAllMonthLeads = t.leads.filter(l => l.counselor === counselorName);
      const cMonthConv = cAllMonthLeads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions').length;
      const cMonthRev = cAllMonthLeads.reduce((acc, l) => acc + (Number(l.revenue) || 0), 0);

      const elBLeads = document.getElementById('bannerTotalLeads');
      if (elBLeads) elBLeads.textContent = cAllMonthLeads.length.toLocaleString('en-IN');
      const elBConv = document.getElementById('bannerTotalConv');
      if (elBConv) elBConv.textContent = cMonthConv.toLocaleString('en-IN');
      const elBRev = document.getElementById('bannerTotalRev');
      if (elBRev) elBRev.textContent = '₹' + Math.round(cMonthRev).toLocaleString('en-IN');

      // Date filtering
      const dates = t.leads.map(l => l.date).filter(Boolean).sort();
      const maxDate = dates[dates.length - 1] || '2026-10-31';

      let startDate = '2026-10-01';
      let endDate = maxDate;

      if (dateRangeVal === 'today') {{
        startDate = maxDate;
        endDate = maxDate;
      }} else if (dateRangeVal === 'yesterday') {{
        startDate = '2026-10-30';
        endDate = '2026-10-30';
      }} else if (dateRangeVal === 'last7') {{
        startDate = '2026-10-25';
        endDate = maxDate;
      }} else if (dateRangeVal === 'last14') {{
        startDate = '2026-10-18';
        endDate = maxDate;
      }}

      // Filter counselor leads
      const fLeads = cAllMonthLeads.filter(l => {{
        if (dateRangeVal !== 'all' && (l.date < startDate || l.date > endDate)) return false;
        if (courseVal !== 'ALL' && l.course !== courseVal) return false;
        return true;
      }});

      cachedFilteredCounselorLeads = fLeads;

      // Calculate Counselor KPIs
      const myLeadsCount = fLeads.length;
      const todayFreshCount = fLeads.filter(l => l.date === maxDate).length;
      const queueCount = fLeads.filter(l => l.status === 'New Lead').length;
      const followupsCount = fLeads.filter(l => l.status === 'Follow Up' || l.status === 'RNR - Followup').length;
      const convCount = fLeads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions').length;
      const convRate = myLeadsCount > 0 ? ((convCount / myLeadsCount) * 100).toFixed(2) + '%' : '0.00%';
      const callsMade = fLeads.reduce((acc, l) => acc + (l.calls_made || 0), 0);
      const talkTime = Math.round(fLeads.reduce((acc, l) => acc + (l.talk_time || 0), 0));

      document.getElementById('kpiMyLeads').textContent = myLeadsCount.toLocaleString('en-IN');
      document.getElementById('kpiTodayFresh').textContent = todayFreshCount.toLocaleString('en-IN');
      document.getElementById('kpiQueueCount').textContent = queueCount.toLocaleString('en-IN');
      document.getElementById('kpiFollowups').textContent = followupsCount.toLocaleString('en-IN');
      document.getElementById('kpiConversions').textContent = convCount.toLocaleString('en-IN');
      document.getElementById('kpiConvRate').textContent = `${{convRate}} Conv. Rate`;
      document.getElementById('kpiCallsMade').textContent = callsMade.toLocaleString('en-IN');
      document.getElementById('kpiTalkTime').textContent = `${{talkTime.toLocaleString('en-IN')}}m`;
      document.getElementById('kpiTalkTimeSub').textContent = `${{Math.round(talkTime / 60)}} Hours (${{talkTime}} mins)`;

      // Render Counselor Funnel
      renderCounselorFunnel(fLeads, maxDate, dateRangeVal);

      // Render All 4 Advanced Counselor Charts
      renderCounselorHourlyChart(counselorName, fLeads, startDate, endDate, dateRangeVal);
      renderCounselorPipelineChart(fLeads);
      renderCounselorCoursesChart(fLeads);
      renderCounselorDailyTrendChart(counselorName, fLeads, startDate, endDate, dateRangeVal);

      // Render Leads Table
      renderTableOnly();
    }}

    function renderCounselorFunnel(fLeads, maxDate, dateRangeVal) {{
      const funnelContainer = document.getElementById('funnelList');
      if (!funnelContainer) return;
      funnelContainer.innerHTML = '';

      let targetLeads = fLeads;
      const badge = document.getElementById('badgeCounselorFunnel');
      if (dateRangeVal === 'all') {{
        targetLeads = fLeads.filter(l => l.date === maxDate);
        if (badge) badge.textContent = `Today's Fresh Leads (${{targetLeads.length}})`;
      }} else {{
        if (badge) badge.textContent = `Filtered Leads (${{targetLeads.length}})`;
      }}

      const total = targetLeads.length;
      const countNew = total;
      const countContacted = targetLeads.filter(l => (l.calls_made > 0)).length;
      const countMissed = targetLeads.filter(l => (l.calls_made || 0) === 0).length;
      const countFollowUp = targetLeads.filter(l => l.status === 'Follow Up' || l.status === 'RNR - Followup').length;
      const countInterested = targetLeads.filter(l => l.status === 'Interested').length;
      const countDemo = targetLeads.filter(l => l.status === 'Enrolled for Free Sessions').length;
      const countNegotiation = targetLeads.filter(l => l.status === 'Priority Lead' || l.status === 'Job Related').length;
      const countPaid = targetLeads.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions').length;
      const countLost = targetLeads.filter(l => l.status === 'Lost').length;

      const countFreshQueue = targetLeads.filter(l => l.status === 'New Lead').length;
      const countDirectLost = targetLeads.filter(l => (l.calls_made || 0) === 0 && l.status === 'Lost').length;
      const countNotReachable = targetLeads.filter(l => l.status === 'Not Reachable').length;

      document.getElementById('subQueueCount').textContent = countFreshQueue;
      document.getElementById('subLostCount').textContent = countDirectLost;
      document.getElementById('subUnreachCount').textContent = countNotReachable;

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
        const pct = total > 0 ? ((item.count / total) * 100).toFixed(1) + '%' : '0%';
        let barWPct = 0;
        if (total > 0 && item.count > 0) {{
          const rawPct = (item.count / total) * 96;
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

    // --- CHART 1: Hourly Calling Performance (Dual Bar: Calls vs Connected + Connect Rate %) ---
    function renderCounselorHourlyChart(counselorName, fLeads, startDate, endDate, dateRangeVal) {{
      const t = window.TELECRM_LIVE_DATA;
      const hourlyCalls = new Array(24).fill(0);
      const hourlyConn = new Array(24).fill(0);

      // Pull from verified calls aggregation
      const relevantCalls = (t.calls || []).filter(c => {{
        if (counselorName !== 'ALL' && c.counselor !== counselorName) return false;
        if (dateRangeVal !== 'all' && (c.date < startDate || c.date > endDate)) return false;
        return true;
      }});

      if (relevantCalls.length > 0) {{
        relevantCalls.forEach(c => {{
          const h = (c.hour !== undefined && c.hour !== null) ? Number(c.hour) : 0;
          if (h >= 0 && h < 24) {{
            hourlyCalls[h] += (c.calls || 0);
            hourlyConn[h] += (c.connected || 0);
          }}
        }});
      }} else {{
        // Fallback to fLeads
        fLeads.forEach(l => {{
          const h = (l.hour !== undefined && l.hour !== null) ? Number(l.hour) : 0;
          if (h >= 0 && h < 24) {{
            hourlyCalls[h] += (l.calls_made || 0);
            hourlyConn[h] += (l.calls_conn || 0);
          }}
        }});
      }}

      const maxCalls = Math.max(...hourlyCalls, 1);
      const titleElem = document.getElementById('titleHourlyCounselor');
      if (titleElem) {{
        titleElem.textContent = dateRangeVal === 'today' ? 'Today (12 AM - 11 PM)' : (dateRangeVal === 'yesterday' ? 'Yesterday (12 AM - 11 PM)' : 'Hourly Calling Distribution');
      }}

      const ctx = document.getElementById('chartCounselorHourly').getContext('2d');
      if (chartCounselorHourly) chartCounselorHourly.destroy();

      chartCounselorHourly = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: HOUR_LABELS_12H,
          datasets: [
            {{
              label: 'Total Calls',
              data: hourlyCalls,
              backgroundColor: '#2563eb',
              borderRadius: 5,
              barPercentage: 0.7,
              maxBarThickness: 24,
              datalabels: {{
                display: v => v > 0,
                anchor: 'end',
                align: 'top',
                color: '#1e40af',
                font: {{ family: 'Inter', size: 8.5, weight: 700 }},
                formatter: v => v > 0 ? v : ''
              }}
            }},
            {{
              label: 'Connected Calls',
              data: hourlyConn,
              backgroundColor: '#10b981',
              borderRadius: 5,
              barPercentage: 0.7,
              maxBarThickness: 24,
              datalabels: {{
                display: (ctx) => hourlyConn[ctx.dataIndex] > 0,
                anchor: 'end',
                align: 'top',
                color: '#047857',
                font: {{ family: 'Inter', size: 8.5, weight: 800 }},
                formatter: (v, ctx) => {{
                  const total = hourlyCalls[ctx.dataIndex] || 0;
                  const pct = total > 0 ? Math.round((v / total) * 100) : 0;
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
              display: true,
              position: 'top',
              labels: {{ boxWidth: 10, usePointStyle: true, font: {{ family: 'Inter', size: 9.5, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                title: items => `Hour: ${{items[0].label}}`,
                afterBody: items => {{
                  const idx = items[0].dataIndex;
                  const calls = hourlyCalls[idx] || 0;
                  const conn = hourlyConn[idx] || 0;
                  const rate = calls > 0 ? ((conn / calls) * 100).toFixed(1) : 0;
                  return [`Connect Rate: ${{rate}}%`];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{ grid: {{ display: false }}, ticks: {{ font: {{ family: 'Inter', size: 9, weight: 600 }} }} }},
            y: {{
              beginAtZero: true,
              suggestedMax: Math.round(maxCalls * 1.3),
              grid: {{ color: '#f1f5f9' }},
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }}
            }}
          }}
        }}
      }});
    }}

    // --- CHART 2: Pipeline & Status Breakdown Donut Chart ---
    function renderCounselorPipelineChart(fLeads) {{
      const statusMap = {{
        'New Lead': 0,
        'Follow Up': 0,
        'Interested': 0,
        'Enrolled / Paid': 0,
        'Priority / Job Related': 0,
        'Lost': 0
      }};

      fLeads.forEach(l => {{
        const s = l.status || 'New Lead';
        if (l.converted === 1 || s === 'Opted for Paid Sessions') statusMap['Enrolled / Paid'] += 1;
        else if (s === 'New Lead') statusMap['New Lead'] += 1;
        else if (s === 'Follow Up' || s === 'RNR - Followup') statusMap['Follow Up'] += 1;
        else if (s === 'Interested' || s === 'Enrolled for Free Sessions') statusMap['Interested'] += 1;
        else if (s === 'Priority Lead' || s === 'Job Related') statusMap['Priority / Job Related'] += 1;
        else if (s === 'Lost') statusMap['Lost'] += 1;
        else statusMap['Follow Up'] += 1;
      }});

      const total = fLeads.length || 1;
      const pipelineData = [
        {{ label: 'New Lead', count: statusMap['New Lead'], color: '#0ea5e9' }},
        {{ label: 'Follow Up', count: statusMap['Follow Up'], color: '#f59e0b' }},
        {{ label: 'Interested', count: statusMap['Interested'], color: '#10b981' }},
        {{ label: 'Enrolled / Paid', count: statusMap['Enrolled / Paid'], color: '#8b5cf6' }},
        {{ label: 'Priority / Job', count: statusMap['Priority / Job Related'], color: '#f97316' }},
        {{ label: 'Lost', count: statusMap['Lost'], color: '#ef4444' }}
      ].filter(x => x.count > 0);

      const ctx = document.getElementById('chartCounselorPipeline').getContext('2d');
      if (chartCounselorPipeline) chartCounselorPipeline.destroy();

      chartCounselorPipeline = new Chart(ctx, {{
        type: 'doughnut',
        data: {{
          labels: pipelineData.map(x => x.label),
          datasets: [{{
            data: pipelineData.map(x => x.count),
            backgroundColor: pipelineData.map(x => x.color),
            borderWidth: 2,
            borderColor: '#ffffff',
            hoverOffset: 4,
            datalabels: {{
              display: (ctx) => {{
                const val = pipelineData[ctx.dataIndex]?.count || 0;
                return (val / total) >= 0.07;
              }},
              color: '#ffffff',
              font: {{ family: 'Inter', size: 10, weight: 800 }},
              formatter: (v) => {{
                const p = Math.round((v / total) * 100);
                return `${{p}}%`;
              }}
            }}
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          layout: {{ padding: {{ top: 6, bottom: 6, left: 6, right: 10 }} }},
          plugins: {{
            legend: {{
              position: 'right',
              labels: {{
                boxWidth: 10,
                font: {{ family: 'Inter', size: 9.5, weight: 600 }},
                padding: 6,
                generateLabels: (chart) => {{
                  return pipelineData.map((item, idx) => ({{
                    text: `${{item.label}}: ${{item.count}} (${{Math.round((item.count / total) * 100)}}%)`,
                    fillStyle: item.color,
                    strokeStyle: '#fff',
                    lineWidth: 1,
                    index: idx
                  }}));
                }}
              }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                label: item => ` ${{item.label}}: ${{item.raw}} leads (${{((item.raw / total) * 100).toFixed(1)}}%)`
              }}
            }}
          }},
          cutout: '56%'
        }}
      }});
    }}

    // --- CHART 3: Top Courses Inquiries vs Paid Admissions ---
    function renderCounselorCoursesChart(fLeads) {{
      const courseMap = {{}};
      fLeads.forEach(l => {{
        const c = l.course || 'Unknown';
        if (!courseMap[c]) courseMap[c] = {{ leads: 0, converted: 0 }};
        courseMap[c].leads += 1;
        if (l.converted === 1 || l.status === 'Opted for Paid Sessions') courseMap[c].converted += 1;
      }});

      const sorted = Object.entries(courseMap)
        .sort((a,b) => b[1].leads - a[1].leads)
        .slice(0, 6);

      const labels = sorted.map(x => x[0].length > 24 ? x[0].slice(0, 22) + '...' : x[0]);
      const leadsCounts = sorted.map(x => x[1].leads);
      const convCounts = sorted.map(x => x[1].converted);

      const ctx = document.getElementById('chartCounselorCourses').getContext('2d');
      if (chartCounselorCourses) chartCounselorCourses.destroy();

      chartCounselorCourses = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [
            {{
              label: 'Inquiries',
              data: leadsCounts,
              backgroundColor: '#3b82f6',
              borderRadius: 4,
              maxBarThickness: 16,
              barPercentage: 0.65,
              datalabels: {{
                display: v => v > 0,
                anchor: 'end',
                align: 'right',
                color: '#1e40af',
                font: {{ family: 'Inter', size: 8.5, weight: 700 }},
                formatter: v => v > 0 ? v : ''
              }}
            }},
            {{
              label: 'Admissions',
              data: convCounts,
              backgroundColor: '#10b981',
              borderRadius: 4,
              maxBarThickness: 16,
              barPercentage: 0.65,
              datalabels: {{
                display: v => v > 0,
                anchor: 'end',
                align: 'right',
                color: '#047857',
                font: {{ family: 'Inter', size: 8.5, weight: 800 }},
                formatter: v => v > 0 ? v : ''
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
              labels: {{ boxWidth: 10, usePointStyle: true, font: {{ family: 'Inter', size: 9.5, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6
            }}
          }},
          scales: {{
            x: {{
              beginAtZero: true,
              grid: {{ color: '#f1f5f9' }},
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }}
            }},
            y: {{
              grid: {{ display: false }},
              ticks: {{ font: {{ family: 'Inter', size: 9, weight: 600 }} }}
            }}
          }}
        }}
      }});
    }}

    // --- CHART 4: 30-Day Calling Volume & Talk Time Trajectory ---
    function renderCounselorDailyTrendChart(counselorName, fLeads, startDate, endDate, dateRangeVal) {{
      const t = window.TELECRM_LIVE_DATA;
      const dateMap = {{}};

      // Build date list
      const dates = [];
      const [sy, sm, sd] = startDate.split('-').map(Number);
      const [ey, em, ed] = endDate.split('-').map(Number);
      let cur = new Date(sy, sm - 1, sd, 12, 0, 0);
      const end = new Date(ey, em - 1, ed, 12, 0, 0);
      while (cur <= end) {{
        const y = cur.getFullYear();
        const m = String(cur.getMonth() + 1).padStart(2, '0');
        const d = String(cur.getDate()).padStart(2, '0');
        const key = `${{y}}-${{m}}-${{d}}`;
        dates.push(key);
        dateMap[key] = {{ calls: 0, talkTime: 0 }};
        cur.setDate(cur.getDate() + 1);
      }}

      // Aggregate calls
      const relevantCalls = (t.calls || []).filter(c => {{
        if (counselorName !== 'ALL' && c.counselor !== counselorName) return false;
        return c.date >= startDate && c.date <= endDate;
      }});

      if (relevantCalls.length > 0) {{
        relevantCalls.forEach(c => {{
          if (dateMap[c.date]) {{
            dateMap[c.date].calls += (c.calls || 0);
            dateMap[c.date].talkTime += (c.duration || 0);
          }}
        }});
      }} else {{
        fLeads.forEach(l => {{
          if (dateMap[l.date]) {{
            dateMap[l.date].calls += (l.calls_made || 0);
            dateMap[l.date].talkTime += (l.talk_time || 0);
          }}
        }});
      }}

      const MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      const labels = dates.map(d => {{
        const p = d.split('-');
        return `${{p[2]}} ${{MONTH_NAMES[Number(p[1]) - 1]}}`;
      }});

      const callsData = dates.map(d => dateMap[d].calls);
      const timeData = dates.map(d => Math.round(dateMap[d].talkTime));

      const maxCalls = Math.max(...callsData, 10);
      const maxTime = Math.max(...timeData, 30);

      const titleElem = document.getElementById('titleDailyTrajectory');
      if (titleElem) {{
        titleElem.textContent = dates.length === 1 ? `Calling Activity (${{labels[0]}})` : `Daily Trend (${{labels[0]}} - ${{labels[labels.length - 1]}})`;
      }}

      const ctx = document.getElementById('chartCounselorDailyTrend').getContext('2d');
      if (chartCounselorDailyTrend) chartCounselorDailyTrend.destroy();

      chartCounselorDailyTrend = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [
            {{
              type: 'bar',
              label: 'Calls Logged',
              data: callsData,
              backgroundColor: '#38bdf8',
              borderRadius: 4,
              maxBarThickness: 18,
              yAxisID: 'y',
              datalabels: {{
                display: ctx => callsData[ctx.dataIndex] > 0 && dates.length <= 15,
                anchor: 'end',
                align: 'top',
                color: '#0284c7',
                font: {{ family: 'Inter', size: 8, weight: 700 }},
                formatter: v => v > 0 ? v : ''
              }}
            }},
            {{
              type: 'line',
              label: 'Talk Time (Mins)',
              data: timeData,
              borderColor: '#059669',
              backgroundColor: 'rgba(5, 150, 105, 0.10)',
              fill: true,
              borderWidth: 2,
              pointRadius: dates.length > 20 ? 2 : 4,
              pointBackgroundColor: '#059669',
              tension: 0.3,
              yAxisID: 'y1',
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
              labels: {{ boxWidth: 10, usePointStyle: true, font: {{ family: 'Inter', size: 9.5, weight: 600 }} }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.94)',
              padding: 10,
              cornerRadius: 6,
              callbacks: {{
                label: (ctx) => ctx.dataset.type === 'bar' ? ` Calls: ${{ctx.raw}} calls` : ` Talk Time: ${{ctx.raw}} minutes (${{(ctx.raw / 60).toFixed(1)}}h)`
              }}
            }}
          }},
          scales: {{
            y: {{
              type: 'linear',
              position: 'left',
              beginAtZero: true,
              suggestedMax: Math.round(maxCalls * 1.3),
              grid: {{ color: '#f1f5f9' }},
              ticks: {{ precision: 0, font: {{ family: 'Inter', size: 9 }} }}
            }},
            y1: {{
              type: 'linear',
              position: 'right',
              beginAtZero: true,
              suggestedMax: Math.round(maxTime * 1.3),
              grid: {{ drawOnChartArea: false }},
              ticks: {{
                font: {{ family: 'Inter', size: 9 }},
                color: '#059669',
                callback: v => `${{v}}m`
              }}
            }},
            x: {{
              grid: {{ display: false }},
              ticks: {{
                font: {{ family: 'Inter', size: 9, weight: 600 }},
                maxTicksLimit: 16
              }}
            }}
          }}
        }}
      }});
    }}

    function renderTableOnly() {{
      const tbody = document.getElementById('tbodyCounselorLeads');
      tbody.innerHTML = '';

      let list = cachedFilteredCounselorLeads;

      // Filter by active pill
      if (activeTablePill === 'TODAY') {{
        list = list.filter(l => l.date === '2026-10-31');
      }} else if (activeTablePill === 'QUEUE') {{
        list = list.filter(l => l.status === 'New Lead');
      }} else if (activeTablePill === 'FOLLOWUP') {{
        list = list.filter(l => l.status === 'Follow Up' || l.status === 'RNR - Followup');
      }} else if (activeTablePill === 'INTERESTED') {{
        list = list.filter(l => l.status === 'Interested');
      }} else if (activeTablePill === 'CONVERTED') {{
        list = list.filter(l => l.converted === 1 || l.status === 'Opted for Paid Sessions');
      }} else if (activeTablePill === 'LOST') {{
        list = list.filter(l => l.status === 'Lost');
      }}

      // Filter by search
      if (currentTableSearch) {{
        list = list.filter(l => {{
          return (l.name && l.name.toLowerCase().includes(currentTableSearch)) ||
                 (l.course && l.course.toLowerCase().includes(currentTableSearch)) ||
                 (l.status && l.status.toLowerCase().includes(currentTableSearch));
        }});
      }}

      document.getElementById('badgeTableCount').textContent = `Showing ${{list.length}} leads`;

      if (list.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="8" style="text-align: center; padding: 24px; color: #94a3b8; font-weight: 500;">No leads found matching current filter/search</td></tr>';
        return;
      }}

      // Render top 100 leads for smooth scrolling
      list.slice(0, 100).forEach(l => {{
        const tr = document.createElement('tr');
        
        // Status class
        let stClass = 'st-new';
        if (l.status === 'Follow Up' || l.status === 'RNR - Followup') stClass = 'st-followup';
        else if (l.status === 'Interested') stClass = 'st-interested';
        else if (l.converted === 1 || l.status === 'Opted for Paid Sessions') stClass = 'st-paid';
        else if (l.status === 'Lost') stClass = 'st-lost';

        // Action needed badge
        let actionBadge = '<span style="color: #64748b; font-size: 10px;">Reviewed</span>';
        if (l.status === 'New Lead') {{
          actionBadge = '<button class="btn-action-call"><i class="fa-solid fa-phone"></i> Call Now</button>';
        }} else if (l.status === 'Follow Up' || l.status === 'RNR - Followup') {{
          actionBadge = '<span style="color: #15803d; font-weight: 700; font-size: 10px;"><i class="fa-regular fa-clock"></i> Follow-up Due</span>';
        }} else if (l.converted === 1 || l.status === 'Opted for Paid Sessions') {{
          actionBadge = '<span style="color: #7e22ce; font-weight: 700; font-size: 10px;"><i class="fa-solid fa-check-circle"></i> Enrolled</span>';
        }} else if (l.status === 'Interested') {{
          actionBadge = '<span style="color: #a16207; font-weight: 700; font-size: 10px;"><i class="fa-solid fa-star"></i> High Priority</span>';
        }}

        tr.innerHTML = `
          <td style="font-weight: 700;">${{l.name || 'Lead-' + l.id.slice(0,6)}}</td>
          <td><code>${{l.phone || 'PH-****' + l.id.slice(-4)}}</code></td>
          <td>${{l.course || 'Unknown'}}</td>
          <td>${{l.date}}</td>
          <td><span class="badge-status ${{stClass}}">${{l.status}}</span></td>
          <td class="text-right">${{l.calls_made || 0}}</td>
          <td class="text-right">${{Math.round(l.talk_time || 0)}}m</td>
          <td>${{actionBadge}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    window.addEventListener('DOMContentLoaded', initCounselorPage);
  </script>
</body>
</html>'''

    with open('counselor_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built counselor_dashboard.html!")

if __name__ == '__main__':
    generate_counselor_dashboard()
