import os
import glob
import sys
import subprocess
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

def find_latest_file(patterns):
    matched_files = []
    for pat in patterns:
        matched_files.extend(glob.glob(pat))
    if not matched_files:
        return None
    # Sort by modification time descending
    matched_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return matched_files[0]

def update_pipeline():
    print("=" * 65)
    print("  KSR DATAVISION — AUTOMATED TELECRM DASHBOARD UPDATER")
    print("=" * 65)
    
    # 1. Detect Leads File
    lead_patterns = [
        'telecrm-leads*.csv',
        '*leads*.csv',
        '*leads*.xlsx'
    ]
    leads_file = find_latest_file(lead_patterns)
    if not leads_file:
        print("[ERROR] No leads CSV or Excel file found matching '*leads*.csv' or '*.xlsx'!")
        sys.exit(1)
    
    print(f"[1/4] Found Leads File: {leads_file} ({round(os.path.getsize(leads_file)/1024, 1)} KB)")

    # 2. Detect Activities File
    act_patterns = [
        'telecrm-activities*with-automation*.csv',
        'telecrm-activities*.csv',
        '*activities*.csv',
        '*activities*.xlsx'
    ]
    act_file = find_latest_file(act_patterns)
    if not act_file:
        print("[WARNING] No activities CSV found. Proceeding with leads file only.")
    else:
        print(f"[2/4] Found Activities File: {act_file} ({round(os.path.getsize(act_file)/1024, 1)} KB)")

    # 3. Process Data into dashboard_data.json
    print("\n[3/4] Processing TeleCRM Raw Records into JSON Payload...")
    # Import and run processing
    import process_telecrm_data
    # Run build_data
    process_telecrm_data.build_data()

    # 4. Compile Standalone Dashboard HTML
    print("\n[4/4] Compiling Standalone HTML Executive & Counselor Dashboards...")
    import build_exact_dashboard
    build_exact_dashboard.generate_live_dashboard()

    import build_counselor_dashboard
    build_counselor_dashboard.generate_counselor_dashboard()

    print("\n" + "=" * 65)
    print("  UPDATE COMPLETE! 100% SUCCESS")
    print("=" * 65)
    print(f"  • Admin Dashboard:     admin_dashboard.html ({round(os.path.getsize('admin_dashboard.html')/1024, 1)} KB)")
    print(f"  • Counselor Dashboard: counselor_dashboard.html ({round(os.path.getsize('counselor_dashboard.html')/1024, 1)} KB)")
    print(f"  • Main Portal:         index.html ({round(os.path.getsize('index.html')/1024, 1)} KB)")
    print(f"  • Generated Mirror:    ksr_executive_dashboard.html")
    print(f"  • Output JSON:         dashboard_data.json")
    print("=" * 65)
    print("  Admins can open 'admin_dashboard.html' (or 'index.html').")
    print("  Counselors can open 'counselor_dashboard.html' to see only their data.")
    print("=" * 65)

if __name__ == '__main__':
    update_pipeline()
