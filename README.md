# Internship Finder

**Concentration:** Information Networking & Telecommunications (Web/Mobile Development)

---

## Issue & Solution
Tech students often struggle to find internships without prior experience after graduation.  

Internship Finder is made for college students to search internships efficiently, while admins manage the content.

---

## Technologies Used

- **Django**: Handles backend logic, URLs, views, database models, admin controls, authentication (login/register), and template rendering.  

- **Adzuna API**: Fetches internship listings including title, company, description, and URL.  

- **Bootstrap**: Styles pages, buttons, forms, and modals for a responsive and clean UI.  

- **Modal Pop-ups**: Show success/error messages for login, account creation, and admin actions.

---

## Features

### Admin Authentication and Management
- Admin login and creation via Django’s authentication system.

- Only admins can:

  - View detailed internship information.

  - Delete database internships.

### Internship Search
- Fetches internship listings from Adzuna API.

- Database internships are combined with API results (only visible to admins).

### Bootstrap & Modal
- Pop-ups confirm actions such as successful login, account creation, or display errors.

---

## Pages Overview

### 1. Home Page
- Displays "Welcome to Internship Finder".

- Buttons:

  - **Internships** → Results Page (requires admin login)

  - **Create Account** → Create Admin Page

  - **Login as User or Admin** → Login Page

### 2. Results Page
- Lists all internships from Adzuna API.

- Search field filters internship titles.

- Only admins can:

  - View database internships.

  - Click "Delete" button next to each database internship to remove it permanently.

- Each internship title links to the Internship Detail Page (admins only).

### 3. Internship Detail Page
- Shows internship details (admins only):

  - Internship Title

  - Company Name

  - Description

  - Link to company site

- Button: "Back to Internships" → returns to Results Page.

### 4. Admin Login Page
- Fields: Username, Password

- Buttons:

  - **Login**

    - Success → modal message → redirects to Results Page.

    - Failure → modal message: "Admin Not Found or Username-Password Incorrect".

### 5. Create Admin Page

- Fields: Username, Password

- Buttons:

  - **Create User**

    - Success → modal message → redirects to Results Page.
    
    - Failure → modal message: "User Already Exists".


---

## Running the Project

1. **Clone the repository**  
```bash
git clone <repo_url>
cd <project_folder>

---

## My comments – Addressing Previous Feedback:

1. Folder Structure and Static Files

Professor feedback: “Setup a proper folder structure… CSS/images should be in static folder.”

What I did: I organized the project following Django conventions. All CSS, images, and JS files are in internships/static/, and I created a base template at internships/templates/internships/base.html that all other pages extend.

2. Minimum 5 Pages and Template Inheritance

Professor feedback: “No base template and inheritance… only three pages.”

What I did: I implemented six pages—home.html, results.html, detail.html, login.html, create.html, and an optional saved page—all extending base.html for consistent layout and navigation.

3. Form Handling (GET and POST)

Professor feedback: “You need at least one page that utilizes a form and has proper GET and POST.”

What I did: I added POST forms for admin login (views.py → admin_login()) and admin creation (views.py → create_admin()). The results page uses a GET form for internship search. All forms are implemented in the templates (login.html and create.html).

4. Redirection After Login/Signup

Professor feedback: “No redirection after signing up or logging in.”

What I did: I made sure that after a successful admin login or account creation, the user is redirected to the Results page.

5. Database Handling

Professor feedback: “Need SQLite database with at least two tables, no database committed.”

What I did: I created the Internship model in internships/models.py and configured the default SQLite database in settings.py. I also added .gitignore to exclude db.sqlite3 from GitHub. Database setup is handled properly with migrations:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

6. User Permissions / Messages

Professor feedback: “Program crashes if accessing pages without proper login, messages not defined.”

What I did: Only logged-in admins can view internship details or delete entries. Unauthorized users now see clear messages:

“You need to log in to view more details”

“You need to log in as an admin to delete an entry”

Messages are displayed consistently through Bootstrap modals in base.html.

7. Styling / Pop-Ups

Professor feedback: “No styling applied, no pop-up messages for success/error.”

What I did: I included Bootstrap via CDN in base.html for styling. All pages inherit from base.html, so pop-up modals for success/error messages display consistently across the site.
