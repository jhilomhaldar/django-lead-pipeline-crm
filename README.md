# 🏢 Room CRM

A modern, lightweight CRM (Customer Relationship Management) system built with Django.

---

## 🚀 Features

### 🔹 Dashboard
- Total Leads count
- Status-wise breakdown (New, Contacted, Qualified, Lost)
- Charts (Won vs Lost, Trends)
- Clean executive overview

---

### 🔹 Lead Management
- Add, Edit, Delete Leads
- Search (name, email, company, phone)
- Status filtering
- Pagination support
- Lead detail view
- Deal & Task integration

---

### 🔹 Deal Management
- Add, Edit, Delete Deals
- Deal stages (New, Qualified, Proposal, Won, Lost)
- Pipeline view
- Lead linking
- Value-based filtering
- Quick Task creation from Deal

---

### 🔹 Task / Follow-up Module
- Create tasks linked to Lead / Deal
- Assign tasks to users
- Due date & time tracking
- Status management (Pending, In Progress, Completed, Cancelled)
- Priority levels (Low, Medium, High)

#### 🚀 Advanced Task Features
- 🔍 Filters (status, priority, assignee)
- 🔴 Overdue highlighting
- 🟡 Due Today highlighting
- 📊 Summary cards (Total, Overdue, Due Today, Completed)
- ⚡ Quick Complete button (1-click completion)
- 🔗 Create task from Lead & Deal

---

### 🔹 UI/UX
- Bootstrap 5 responsive design
- FontAwesome icons
- SweetAlert2 confirmations
- Sidebar navigation
- Clean card-based layout

---

## 🛠️ Tech Stack

- **Backend:** Python (Django)
- **Frontend:** HTML, Bootstrap 5, CSS
- **Database:** PostgreSQL (Primary) / SQLite (Development)
- **Icons:** FontAwesome
- **JS Libraries:** SweetAlert2
- **ORM:** Django ORM

---

## 📂 Project Structure
django-lead-pipeline-crm/
│
├── crm/ # Main project
├── dashboard/ # Dashboard module
├── leads/ # Lead management
├── deals/ # Deal management
├── tasks/ # Task / follow-up module
├── pipeline/ # Pipeline view
├── accounts/ # Authentication (future use)
│
├── templates/ # HTML templates
├── static/ # CSS / JS / Images
├── manage.py
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/jhilomhaldar/django-lead-pipeline-crm.git
cd django-lead-pipeline-crm
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django psycopg[binary]
```

### 4. Configure Database (PostgreSQL)

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'roomcrm',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Server

```bash
python manage.py runserver
```

# Open in Browser

http://127.0.0.1:8000/

# 🔐 Admin Panel

http://127.0.0.1:8000/admin/

# 📦 Data Migration (SQLite → PostgreSQL)

If migrating existing data:

# Switch to SQLite

```bash
python manage.py dumpdata leads deals tasks > data.json
```

# Switch to PostgreSQL

```bash
python manage.py loaddata data.json
```

# 📌 Upcoming Features

Activity Timeline (Calls, Meetings, Notes)
Notifications / Reminders
Role-based Access Control
REST API Integration
Email Automation
Reporting & Analytics

# 👨‍💻 Author

Jhilom Haldar

# License

This project is for learning and development purposes.

