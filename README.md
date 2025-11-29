# CAMIS-Microservice-Integration

## 💡 Overview
This project proposes a **decoupled microservice architecture** to integrate modern features (Alerts, Parent Portal, Fee Tracking) into an existing Student Information System (simulating CAMIS). It demonstrates proficiency in using the right tool for the job by combining two powerful Python frameworks.

## 🏛️ Architecture & Framework Roles

This architecture separates the system into two distinct services connected via a centralized API: 

[Image of the Docker containerization process]


### 1. The Alert Gateway (FastAPI Service)
Handles high-speed, critical tasks.

* **Role:** Real-time API for external systems (like CAMIS) to trigger events (e.g., missed attendance).
* **Key Features:** Asynchronous (async/await) processing for low-latency SMS/Email alerts.
* **Skills Showcased:** Modern Microservices, High-Performance APIs, Asynchronous Python.

### 2. The User & Reporting Platform (Django Service)
Handles complex data management and user interactions.

* **Role:** Manages the Parent Portal, Admin Dashboard, Fee Tracking database, and Audit Logs.
* **Key Features:** Robust user authentication, built-in Admin Interface for auditing, and complex report generation.
* **Skills Showcased:** Full-Stack Web Development, ORM (Database Management), User Security.

## 🛠 Technology Stack

| Component | Framework/Tool | Purpose |
| :--- | :--- | :--- |
| **API Backend** | **FastAPI** | High-speed alert processing and API calls. |
| **Web Platform** | **Django** | Parent Portal and Admin Dashboard. |
| **Database** | PostgreSQL/SQLite | Managed by Django ORM for complex data (Fees, Chat logs). |
| **Deployment** | Docker | Containerizing both services for easy deployment (demonstrates DevOps). |
| **Data Validation** | Pydantic (in FastAPI) | Ensures all incoming alert data is correctly structured. |

## 🚀 Key Integration Features Modeled
1.  **Attendance Alerts:** CAMIS triggers FastAPI API when attendance is missed; FastAPI sends automated SMS.
2.  **Parent/Teacher Chat:** Hosted on the Django Portal, storing chat history in the Django database.
3.  **Fee Notifications:** Scheduled job in Django checks outstanding balances and pushes alert data to the FastAPI API for sending notifications.
