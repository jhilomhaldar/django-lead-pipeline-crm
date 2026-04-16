# 🏢 Room CRM

A modern, lightweight CRM (Customer Relationship Management) system built with Django.

---

## 🚀 Features

### 🔹 Lead Management
- Add, Edit, Delete Leads
- Search leads (name, email, company, phone)
- Status filtering (New, Contacted, Qualified, Lost)
- Pagination support
- Created date tracking

### 🔹 Dashboard
- Total Leads count
- Status-wise breakdown:
  - New Leads
  - Contacted Leads
  - Qualified Leads
  - Lost Leads

### 🔹 UI/UX
- Bootstrap 5 responsive design
- FontAwesome icons
- SweetAlert2 confirmation dialogs
- Sidebar + Navbar layout
- Clean card-based dashboard

---

## 🛠️ Tech Stack

- **Backend:** Python (Django)
- **Frontend:** HTML, Bootstrap 5, CSS
- **Icons:** FontAwesome
- **Database:** SQLite (default)
- **JS Libraries:** SweetAlert2

---

## 📂 Project Structure
django-lead-pipeline-crm/
│
├── crm/ # Main Django project
├── leads/ # Lead management module
├── dashboard/ # Dashboard module
├── accounts/ # Authentication (future use)
├── deals/ # Deals module (upcoming)
├── pipeline/ # Pipeline module (upcoming)
│
├── templates/ # HTML templates
├── static/ # CSS, JS, Images
├── db.sqlite3 # Database
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
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

### Open:

http://127.0.0.1:8000/
🔐 Admin Panel

Access admin here:

http://127.0.0.1:8000/admin/

## 📌 Upcoming Features

Deals Management (Lead → Deal conversion)
Pipeline Stages
Activity Tracking (Calls, Notes)
User Authentication & Roles
REST API Integration

## 👨‍💻 Author

Jhilom Haldar

## 📄 License

This project is for learning and development purposes.


---