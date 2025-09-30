# Project Specification: Web Application with Flask, MySQL, Tailwind

## Overview
This project is a web application for managing operational, reporting, and monitoring modules.  
It will be built using **Flask (Python)** as backend, **MySQL** as the database, and **Tailwind CSS** for the frontend.  
The application is role-based (Admin, Coordinator, Field Officer), supports dark mode, captcha at login, export features, and visual alerts for outdated data rows.

---

## Tech Stack
- Backend: Flask + Flask-Login + SQLAlchemy ORM
- Database: MySQL (schema provided in `schema.sql`)
- Frontend: Jinja2 templates + Tailwind CSS
- Charts: Chart.js
- Export: Excel (openpyxl/pandas), PDF (reportlab/weasyprint)
- Authentication: Session-based login with captcha
- Alerts: Tailwind alerts, consistent across all pages
- Dark Mode: Toggle with Tailwind `dark:` utilities
- File Storage: Local `/static/uploads/` for photos & receipts

---

## UI/UX Rules
1. Sidebar with folders → subfolders → pages (multi-level navigation).
2. Breadcrumb visible on each page.
3. Tailwind design: simple, clean, padding `p-4`, rounded corners `2xl`.
4. Alerts: consistent Tailwind component (`success`, `info`, `warning`, `error`).
5. Captcha verification in login form.
6. Dark mode toggle, stored in localStorage.
7. Outdated rows in tables must be red with pulse animation.
8. Export buttons (Excel/PDF) on all reporting/monitoring pages.

---

## Roles & Permissions
- **Admin**: manage master data, reports, system operations.
- **Coordinator**: dashboard, monitoring, approve transactions, view reports.
- **Field Officer**: input transactions, upload photos, print receipts.

---

## Database (schema.sql)
Tables include:
- users (id, username, password_hash, role, area_code, active, imei, created_at, last_login)
- areas (code, name)
- officers (id, user_id, rbm_code, coordinator_id, active, imei)
- transactions (id, idpel, periode, total, payment_type, officer_id, status, created_at)
- talangan_transactions (...)
- wa_logs (...)
- print_logs (...)
- monitoring_logs (...)
- anomalies (...)
- report_exports (...)

---

## Features & Pages
### A. Authentication
- Login page with captcha.
- Logout clears session.
- Change password page.

### B. Dashboard
- 6-month histogram (stacked, per customer type).
- MoM line charts (daily & accumulated).
- Refresh button.

### C. Master Data
- Coordinator management
- Officer management (with toggle active, reset IMEI)
- Reset UMT updates

### D. Reports & Monitoring
- Rekap per RBM
- Rekap per Coordinator
- Rekap per Officer
- Rekap per Area
- Rekap Tunggakan
- WA sending monitoring
- Log monitoring
- Daily settlement monitoring
- Bluetooth print monitoring
- Morning-Evening settlement monitoring
- Monthly reports

### E. Talangan (Advance Fund)
- Balance monitoring
- Daily target monitoring
- Daily transaction totals
- Detail payments (cash/installments)
- Input settlement
- Approval process
- Photo downloads

### F. Information
- Customer information lookup

### G. HO Anomaly Module
- Daily anomaly reports
- Recap per officer
- Recap per date
- Anomaly master data management

### H. Utility
- Change password
- Logout

---

## Visual Behavior for Outdated Rows
- Rows highlighted red + pulse animation if data is outdated.
- Tooltip or ⚠️ icon shows explanation.

---

## Deliverables
1. Flask project with routes, templates, static files.
2. schema.sql with DDL + seed data.
3. Tailwind templates for all pages.
4. Captcha in login form.
5. Role-based decorators for access control.
6. Chart.js implementation in dashboard.
7. Export Excel/PDF.
8. Readme with setup instructions (import schema.sql in phpMyAdmin, run `flask run`).

## Rules
- Do not use dummy data hardcoded in HTML templates.
- All tables, charts, and visual elements must fetch data from the database (MySQL).
- Only use sample seed data provided in `schema.sql`.
- If a page requires data and none exists, display an empty state (e.g., "No data available").