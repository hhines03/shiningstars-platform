# shiningstars-platform
Full-stack business management platform built with Python (Django), Vue.js, and PostgreSQL.


## About The Project

This repository contains the source code for a full-stack management platform being developed for a client in the UK service and education sector. The primary objective is to solve critical business challenges in client management, scheduling, and billing, creating a scalable and efficient digital solution to support business growth.

This project is being managed using an agile, sprint-based methodology.

## Tech Stack

This project is being built with a modern, professional technology stack:

* **Backend:** Python with the Django framework
* **Frontend:** Vue.js
* **Database:** PostgreSQL
* **Deployment:** Heroku/Render (for backend) & Vercel (for frontend)

### 3. Data Model

The core data structure is based on a clear separation between actors (`User` model) and the data they manage (`Child` model):
* **`User` Model:** Represents entities that can log in. It contains a `role` field ('admin' or 'parent') to manage permissions.
* **`Child` Model:** Represents the children in care. It is linked to a `User` via a `parent_id` foreign key. This ensures a parent can only ever access their own child's data.


## Project Roadmap (MVP Features)

The following key features are planned for the Minimum Viable Product (MVP):

* [ ] Secure User Authentication (Admin & Parent roles)
* [ ] Admin Dashboard for Client & Staff Management
* [ ] Parent Portal for Viewing Child Information
* [ ] Dynamic Booking & Scheduling System 
* [ ] Automated Invoicing based on Bookings

## Contact

Harun Hines - https://www.linkedin.com/in/harun-hines-0b0bb2295/ - harunhines@gmail.com
