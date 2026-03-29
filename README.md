# 🏡 Online Gram Panchayat Website

This is a **Django-based web application** designed to manage and digitalize the Gram Panchayat system.  
It helps villagers and administrators to connect, manage complaints, events, and village-related data online.  

---

## 🚀 Features
- 🧑‍💼 **Sarpanch & Member Details** – Add and manage sarpanch and sabhya (members) details.  
- 🏘 **Village Details** – Maintain records of the village information.  
- 📢 **Complaints System** – Citizens can register and track their complaints.  
- 🎉 **Events & Celebrations** – Add and view upcoming events.  
- 📞 **Contact Information** – Easy access to Gram Panchayat contacts.  
- 🔒 **Admin Panel** – Secure login for managing all modules.  

---

## 🛠 Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** PostgreSQL
- **Version Control:** Git & GitHub  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sandip-2006/panchyat.git
   ```

2. Create and activate virtual environment:
    ```bash
    python -m venv env
    env\Scripts\activate   # Windows
    source env/bin/activate  # Linux/Mac
    ```
3. Install dependencies:
    ``` bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the server:
    ```bash
    python manage.py runserver
    ```
6. Open in browser:
    ```bash
    http://127.0.0.1:8000/
    ```