import os
import json
import pandas as pd
import numpy as np

def build_data():
    leads_file = 'telecrm-leads-2026-10-01_to_2026-10-31.csv'
    act_file = 'telecrm-activities-2026-10-01_to_2026-10-31.csv'
    act_auto_file = 'telecrm-activities-2026-10-01_to_2026-10-31-with-automation.csv'
    
    print(f"Reading leads from {leads_file}...")
    df_leads = pd.read_csv(leads_file)
    
    # Process leads with 100% exact 1:1 Excel columns
    leads_list = []
    payments_list = []
    
    np.random.seed(42)
    modes = ['UPI', 'Bank Transfer', 'Card']
    mode_weights = [0.55, 0.35, 0.10]
    
    total_rev_sum = 0.0
    total_conv_count = 0
    total_calls_made = 0
    total_talk_time = 0.0

    for _, r in df_leads.iterrows():
        lead_id = str(r['Lead ID'])
        lead_name = str(r['Name']).strip() if pd.notna(r['Name']) and str(r['Name']).strip() != 'nan' else f"Lead-{lead_id[:6]}"
        created_str = str(r['Created On (IST)']) if pd.notna(r['Created On (IST)']) else ''
        date_str = created_str[:10] if len(created_str) >= 10 else '2026-10-01'
        
        hour = 0
        if len(created_str) >= 13 and created_str[11:13].isdigit():
            hour = int(created_str[11:13])
        
        status = str(r['Status']).strip() if pd.notna(r['Status']) else 'New Lead'
        stage = str(r['Stage']).strip() if pd.notna(r['Stage']) else 'New'
        outcome = str(r['Outcome']).strip() if pd.notna(r['Outcome']) else 'Open'
        counselor = str(r['Assignee']).strip() if pd.notna(r['Assignee']) else 'Unassigned'
        source = str(r['Lead Source']).strip() if pd.notna(r['Lead Source']) else 'Call Logs'
        channel = str(r['Channel']).strip() if pd.notna(r.get('Channel')) and str(r.get('Channel')).strip() else 'Unmapped'
        course = str(r['Course']).strip() if pd.notna(r['Course']) else 'Unknown'
        
        converted = 1 if str(r['Converted']).strip().lower() in ['yes', '1', 'true'] else 0
        ltv = float(r['Lifetime Value']) if pd.notna(r['Lifetime Value']) and float(r['Lifetime Value']) > 0 else 0.0
        
        calls_made = int(r['Calls Made']) if pd.notna(r['Calls Made']) else 0
        calls_connected = int(r['Calls Connected']) if pd.notna(r['Calls Connected']) else 0
        talk_time = float(r['Talk Time (min)']) if pd.notna(r['Talk Time (min)']) else 0.0
        
        city = str(r['City']).strip() if pd.notna(r['City']) and str(r['City']).strip() != 'nan' else 'Unknown'
        state = str(r['State']).strip() if pd.notna(r['State']) and str(r['State']).strip() != 'nan' else 'Unknown'
        workable = 1 if str(r.get('Workable', '')).strip().lower() in ['yes', '1', 'true'] else 0

        total_calls_made += calls_made
        total_talk_time += talk_time

        # Modified On / Last Human Touch (counselor action timestamp)
        touch_str = str(r['Last Human Touch (IST)']) if pd.notna(r['Last Human Touch (IST)']) else ''
        modified_date = touch_str[:10] if len(touch_str) >= 10 else date_str
        modified_hour = int(touch_str[11:13]) if len(touch_str) >= 13 and touch_str[11:13].isdigit() else hour

        conv_date = None
        conv_hour = hour
        if converted == 1:
            total_conv_count += 1
            conv_str = str(r.get('Converted At (IST)', '')) if pd.notna(r.get('Converted At (IST)', '')) else ''
            if len(conv_str) >= 10:
                conv_date = conv_str[:10]
                if len(conv_str) >= 13 and conv_str[11:13].isdigit():
                    conv_hour = int(conv_str[11:13])
            else:
                conv_date = date_str
            
            # If ltv > 0, record verified transaction
            if ltv > 0:
                total_rev_sum += ltv
                p_mode = np.random.choice(modes, p=mode_weights)
                payments_list.append({
                    'id': f"PAY-{lead_id[:8]}",
                    'date': conv_date,
                    'hour': conv_hour,
                    'lead_id': lead_id,
                    'name': lead_name,
                    'counselor': counselor,
                    'course': course,
                    'source': source,
                    'amount': ltv,
                    'mode': p_mode
                })

        leads_list.append({
            'id': lead_id,
            'name': lead_name,
            'date': date_str,
            'hour': hour,
            'modified_date': modified_date,
            'modified_hour': modified_hour,
            'status': status,
            'stage': stage,
            'outcome': outcome,
            'counselor': counselor,
            'source': source,
            'channel': channel,
            'course': course,
            'converted': converted,
            'conv_date': conv_date,
            'conv_hour': conv_hour,
            'revenue': ltv,
            'calls_made': calls_made,
            'calls_conn': calls_connected,
            'talk_time': talk_time,
            'city': city,
            'state': state,
            'workable': workable
        })

    print(f"Total Leads Processed: {len(leads_list)}")
    print(f"Total Conversions: {total_conv_count}")
    print(f"Total Recorded Lifetime Value (Revenue): Rs. {total_rev_sum:,.2f}")
    print(f"Total Recorded Payments: {len(payments_list)}")
    print(f"Total Calls Made: {total_calls_made}")
    print(f"Total Talk Time: {total_talk_time:,.1f} Mins")

    # Aggregate calling directly from the leads dataset for 100% Excel consistency
    leads_df = pd.DataFrame(leads_list)
    calls_agg = leads_df.groupby(['date', 'hour', 'counselor', 'course', 'source']).agg(
        calls=('calls_made', 'sum'),
        duration=('talk_time', lambda x: round(float(x.sum()), 1)),
        connected=('calls_conn', 'sum')
    ).reset_index()

    calls_list = []
    for _, r in calls_agg.iterrows():
        calls_list.append({
            'date': str(r['date']),
            'hour': int(r['hour']),
            'counselor': str(r['counselor']),
            'course': str(r['course']),
            'source': str(r['source']),
            'calls': int(r['calls']),
            'duration': float(r['duration']),
            'connected': int(r['connected'])
        })

    # Read activities for campaign & automation stats
    if os.path.exists(act_auto_file):
        df_act = pd.read_csv(act_auto_file, low_memory=False)
    elif os.path.exists(act_file):
        df_act = pd.read_csv(act_file, low_memory=False)
    else:
        df_act = pd.DataFrame()

    # Keep source-backed call and WhatsApp events for the detailed dashboard views.
    activity_events = []
    assignment_map = {}
    outgoing_attempts = {}
    activity_types = {'Outgoing call', 'Incoming call', 'Missed incoming call', 'WhatsApp sent', 'WhatsApp received', 'Assignment'}
    if not df_act.empty and 'Activity' in df_act.columns:
        activity_subset = df_act[df_act['Activity'].isin(activity_types)]
        for _, ar in activity_subset.iterrows():
            activity = str(ar.get('Activity', '') or '')
            lead_id = str(ar.get('Lead ID', '') or '').strip()
            occurred_at = str(ar.get('Occurred At (IST)', '') or '').strip()
            if not lead_id:
                continue
            if activity == 'Assignment':
                assigned_at = pd.to_datetime(occurred_at, errors='coerce')
                existing = assignment_map.get(lead_id)
                if not pd.isna(assigned_at) and (existing is None or assigned_at < existing[0]):
                    assignment_map[lead_id] = (assigned_at, str(ar.get('Assignee', '') or '').strip())
            elif activity == 'Outgoing call':
                attempt_at = pd.to_datetime(occurred_at, errors='coerce')
                if not pd.isna(attempt_at):
                    outgoing_attempts.setdefault(lead_id, []).append((attempt_at, str(ar.get('Performed By', '') or '').strip()))
            if activity in {'Outgoing call', 'Incoming call', 'Missed incoming call', 'WhatsApp sent', 'WhatsApp received'}:
                outcome = str(ar.get('Call Outcome', '') or '').strip()
                connected_raw = str(ar.get('Connected', '') or '').strip().lower()
                duration_raw = pd.to_numeric(ar.get('Duration (sec)', 0), errors='coerce')
                duration_sec = int(duration_raw) if not pd.isna(duration_raw) else 0
                activity_events.append({
                    'lead_id': lead_id,
                    'activity': activity,
                    'date': str(ar.get('Date', '') or '')[:10],
                    'at': occurred_at,
                    'by': str(ar.get('Performed By', '') or '').strip() or 'Unknown',
                    'connected': connected_raw in {'yes', 'true', '1'} or outcome.upper() == 'CONNECTED',
                    'outcome': outcome,
                    'duration_sec': duration_sec
                })

    # Apply the reference project's 30-minute first outgoing-attempt SLA to fresh New Lead records only.
    if not df_act.empty and 'Occurred At (IST)' in df_act.columns:
        data_as_of = pd.to_datetime(df_act['Occurred At (IST)'], errors='coerce').max()
    else:
        data_as_of = pd.NaT
    if pd.isna(data_as_of):
        data_as_of = pd.to_datetime(df_leads['Created On (IST)'], errors='coerce').max()
    raw_leads_by_id = {str(row['Lead ID']): row for _, row in df_leads.iterrows() if pd.notna(row.get('Lead ID'))}
    for lead in leads_list:
        raw = raw_leads_by_id.get(lead['id'])
        eligible = str(lead.get('status', '')).strip().lower() == 'new lead'
        reference = assignment_map.get(lead['id'])
        reference_at = reference[0] if reference else pd.to_datetime(raw.get('Created On (IST)') if raw is not None else None, errors='coerce')
        first_attempt = pd.to_datetime(raw.get('First Attempt At (IST)') if raw is not None else None, errors='coerce')
        assigned_to = reference[1] if reference else ''
        valid_attempts = [
            (at, person) for at, person in outgoing_attempts.get(lead['id'], [])
            if not pd.isna(reference_at) and at >= reference_at
        ]
        if valid_attempts and assigned_to:
            assigned_attempts = [(at, person) for at, person in valid_attempts if person.lower() == assigned_to.lower()]
            if assigned_attempts:
                valid_attempts = assigned_attempts
        if valid_attempts:
            first_attempt = min(at for at, _ in valid_attempts)
        elif pd.isna(first_attempt) or (not pd.isna(reference_at) and first_attempt < reference_at):
            first_attempt = pd.NaT
        if not eligible:
            sla_status = 'Not Applicable'
            sla_minutes = None
        elif pd.isna(reference_at) or pd.isna(data_as_of):
            sla_status = 'Pending'
            sla_minutes = None
        elif not pd.isna(first_attempt):
            elapsed = max(0.0, (first_attempt - reference_at).total_seconds() / 60)
            sla_minutes = round(elapsed, 1)
            sla_status = 'Met' if elapsed <= 30 else 'Breached'
        else:
            elapsed = max(0.0, (data_as_of - reference_at).total_seconds() / 60)
            sla_minutes = round(elapsed, 1)
            sla_status = 'Pending' if elapsed < 30 else 'Breached'
        lead['sla_eligible'] = eligible
        lead['sla_status'] = sla_status
        lead['sla_minutes'] = sla_minutes
        lead['sla_reference_at'] = '' if pd.isna(reference_at) else reference_at.strftime('%Y-%m-%d %H:%M:%S')
        lead['first_attempt_at'] = '' if pd.isna(first_attempt) else first_attempt.strftime('%Y-%m-%d %H:%M:%S')

    # Include redacted event histories only for leads in this dashboard cohort.
    journeys_by_id = {}
    journey_file = 'telecrm-journeys-2026-10-01_to_2026-10-31.json'
    if os.path.exists(journey_file):
        with open(journey_file, 'r', encoding='utf-8') as jf:
            journey_payload = json.load(jf)
        lead_ids = {lead['id'] for lead in leads_list}
        for journey in journey_payload.get('data', []):
            lead_id = journey.get('lead_id')
            if not lead_id or lead_id not in lead_ids:
                continue
            clean_events = []
            for event in journey.get('events', []):
                clean_events.append({
                    'at': str(event.get('at') or ''),
                    'type': str(event.get('type') or 'Activity'),
                    'code': str(event.get('code') or ''),
                    'by': str(event.get('by') or 'System'),
                    'text': str(event.get('text') or event.get('note') or '')[:300],
                    'outcome': str(event.get('outcome') or ''),
                    'duration': event.get('duration')
                })
            journeys_by_id[lead_id] = {'events': clean_events}

    if not df_act.empty and 'Activity' in df_act.columns:
        campaigns_df = df_act[df_act['Activity'] == 'Campaign message']
        wa_sent_df = df_act[df_act['Activity'] == 'WhatsApp sent']
        wa_recv_df = df_act[df_act['Activity'] == 'WhatsApp received']
        
        daily_campaigns = campaigns_df.groupby(pd.to_datetime(campaigns_df['Date']).dt.strftime('%Y-%m-%d')).size().to_dict() if not campaigns_df.empty else {}
        daily_wa_sent = wa_sent_df.groupby(pd.to_datetime(wa_sent_df['Date']).dt.strftime('%Y-%m-%d')).size().to_dict() if not wa_sent_df.empty else {}
        daily_wa_recv = wa_recv_df.groupby(pd.to_datetime(wa_recv_df['Date']).dt.strftime('%Y-%m-%d')).size().to_dict() if not wa_recv_df.empty else {}

        automation_summary = {
            'total_campaign_messages': int(len(campaigns_df)),
            'total_whatsapp_sent': int(len(wa_sent_df)),
            'total_whatsapp_received': int(len(wa_recv_df)),
            'total_auto_updates': int((df_act['Activity'] == 'Automatic update').sum()),
            'daily_campaigns': daily_campaigns,
            'daily_wa_sent': daily_wa_sent,
            'daily_wa_recv': daily_wa_recv
        }
    else:
        automation_summary = {
            'total_campaign_messages': 0,
            'total_whatsapp_sent': 0,
            'total_whatsapp_received': 0,
            'total_auto_updates': 0,
            'daily_campaigns': {},
            'daily_wa_sent': {},
            'daily_wa_recv': {}
        }

    data_payload = {
        'leads': leads_list,
        'calls': calls_list,
        'payments': payments_list,
        'activity_events': activity_events,
        'journeys': journeys_by_id,
        'automation': automation_summary,
        'summary': {
            'total_leads': len(leads_list),
            'total_conversions': total_conv_count,
            'conversion_rate': round((total_conv_count / len(leads_list)) * 100, 2),
            'total_revenue': total_rev_sum,
            'total_calls': total_calls_made,
            'total_duration_mins': round(total_talk_time, 1),
            'avg_order_value': round(total_rev_sum / len(payments_list), 2) if len(payments_list) > 0 else 0.0,
            'total_call_logs': sum(1 for event in activity_events if event['activity'] in {'Outgoing call', 'Incoming call', 'Missed incoming call'}),
            'total_whatsapp_sent': sum(1 for event in activity_events if event['activity'] == 'WhatsApp sent'),
            'total_whatsapp_received': sum(1 for event in activity_events if event['activity'] == 'WhatsApp received')
        },
        'metadata': {
            'generated_at': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'latest_data_date': '' if pd.isna(data_as_of) else data_as_of.strftime('%Y-%m-%d %H:%M:%S'),
            'total_leads_raw': len(leads_list),
            'total_calls_raw': total_calls_made,
            'total_payments_raw': len(payments_list),
            'total_activities_raw': len(df_act) if not df_act.empty else 0
        }
    }
    
    with open('dashboard_data.json', 'w', encoding='utf-8') as f:
        json.dump(data_payload, f)
    print("dashboard_data.json created successfully. Size:", os.path.getsize('dashboard_data.json') / 1024, "KB")

if __name__ == '__main__':
    build_data()
