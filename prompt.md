# Project Improvement Specification

## Overview
This document describes the issues and missing features found in the Flask + MySQL + Tailwind web application.  
The AI agent must analyze and fix these issues. All templates, logic, and CRUD features must be completed and functional.  
**Do not use dummy hardcoded data in HTML**. All data must come from the MySQL database.

---

## Errors to Fix (Current Routes)
1. `/master-data/officers`  
   - Error: `sqlalchemy.exc.AmbiguousForeignKeysError` (ambiguous join between `officers` and `users`).  
   - Fix: Explicit `foreign_keys` or `onclause` in relationship.  

2. `/reports/area`  
   - Error: `sqlalchemy.exc.InvalidRequestError` (multiple FROM clauses).  
   - Fix: Use `.select_from()` and explicit `join` ON conditions.  

3. Missing template files (must be created and functional):  
   - `/reports/wa-monitoring` → `reports/wa_monitoring.html`  
   - `/reports/log-monitoring` → `reports/log_monitoring.html`  
   - `/reports/daily-settlement` → `reports/daily_settlement.html`  
   - `/reports/bluetooth-print` → `reports/bluetooth_print.html`  
   - `/talangan/balance` → `talangan/balance.html`  
   - `/talangan/daily-target` → `talangan/daily_target.html`  
   - `/talangan/transactions` → `talangan/transactions.html`  
   - `/talangan/detail-payments` → `talangan/detail_payments.html`  
   - `/talangan/input-settlement` → `talangan/input_settlement.html`  
   - `/talangan/approval` → `talangan/approval.html`  
   - `/anomaly/daily-reports` → `anomaly/daily_reports.html`  
   - `/anomaly/recap-officer` → `anomaly/recap_officer.html`  
   - `/anomaly/recap-date` → `anomaly/recap_date.html`  
   - `/anomaly/master-data` → `anomaly/master_data.html`

---

## Pages That Exist But Are Not Fully Functional
1. `/master-data/reset-umt`  
   - Reset options (checkbox + button) not working. Must connect to DB and update relevant tables.  

2. `/reports/rbm`  
   - Export PDF button not implemented. Must generate PDF using ReportLab/WeasyPrint.  

3. `/information/customer-lookup`  
   - Search not working. Must query database by `idpel` or `nama`.  

4. `/master-data/coordinators`  
   - Button "Add Coordinator" not showing form.  
   - Edit/Delete actions not working.  
   - Must add filtering by Area/UP3 before showing table.  

---

## Enhancements to Implement
- **Master Coordinators**:  
  - Add Area/UP3 filter dropdown (Serang, Cilegon, Anyer, etc).  
  - After selecting area, show coordinators from that area.  

- **Master Officers**:  
  - In table, add working actions:  
    - Reset IMEI button (triggers DB update).  
    - Active/Non-active button (toggle status in DB).  
  - Use proper button (SVG animation) instead of plain checkbox.  

- **CRUD Logic**:  
  - For all missing templates, ensure full CRUD works (Add, Edit, Delete).  
  - Tie all actions to database queries (SQLAlchemy).  

---

## Rules
- Do not use dummy hardcoded data in HTML.  
- All data must come from database.  
- All templates must exist and routes must render without error.  
- All buttons must trigger real DB logic (reset, add, edit, delete, export).  
- Error 505 and ambiguous joins must be fixed by adjusting SQLAlchemy relationships with explicit clauses.  

---

## Deliverables
1. Fixed routes with working joins.  
2. All missing templates created (`.html` files in correct folder).  
3. All CRUD actions implemented and functional.  
4. Export PDF implemented on reports.  
5. Customer lookup search working.  
6. Filtering by area on Master Coordinators.  
7. Reset IMEI and Active/Non-active buttons functional in Master Officers.  
8. Documentation updated in README.  
