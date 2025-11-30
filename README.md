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
bash
git clone <repo_url>
cd <project_folder>

-----------------------END---------------------
## My comments – Addressing Previous Feedback:

# Folder Structure/ Static Files:

Professor feedback: “Setup a proper folder structure… CSS/images should be in static folder.”

What I did: I organized the project the way Django recommends. All my CSS, images, and JS files are now in internships/static/, and I made a base.html template in internships/templates/internships/ that all the other pages use. This makes the layout consistent across the site.

# Minimum 5 Pages and Template Inheritance:

Professor feedback: “No base template and inheritance… only three pages.”

What I did: I created six pages: home.html, results.html, detail.html, login.html, create.html, and an optional saved page. All of them extend base.html so the navigation and design are the same on every page.

# (GET and POST)

Professor feedback: “You need at least one page that utilizes a form and has proper GET and POST.”

What I did: I added POST forms for admin login (admin_login() in views.py) and admin account creation (create_admin() in views.py). The search on the Results page uses a GET form to filter internships. All the forms are included in the templates (login.html and create.html).

# Redirection after login and signin

Professor feedback: “No redirection after signing up or logging in.”

What I did: After a successful admin login or creating a new admin account, users are now redirected to the Results page automatically.

# Database

Professor feedback: “Need SQLite database with at least two tables, no database committed.”

What I did: I created the Internship model in internships/models.py and set up the default SQLite database in settings.py. I added a .gitignore to make sure db.sqlite3 isn’t pushed to GitHub. Database setup is handled properly using migrations:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# permissions and messages

Professor feedback: “Program crashes if accessing pages without proper login, messages not defined.”

What I did: Only logged-in admins can view internship details or delete entries. If a user isn’t logged in, they now see clear messages:

“You need to log in to view more details”

“You need to log in as an admin to delete an entry”

All messages are shown in Bootstrap modals for consistency.

# Pop-Ups

Professor feedback: “No styling applied, no pop-up messages for success/error.”

What I did: I added Bootstrap via CDN in base.html to style the pages. Since all pages extend base.html, the pop-up modals for success and error messages show consistently across the site.

--------------------------------------------
# REFERENCES:
I mostly used info from these sites plus reddit and other forums for troubleshooting and debugging errors I was getting

## 1. Django Basics & Structure

Django official documentation – project structure, apps, templates:
https://docs.djangoproject.com/en/4.2/

Django template inheritance:
https://docs.djangoproject.com/en/4.2/topics/templates/#template-inheritance

## 2. Forms & Authentication

Django forms and POST/GET handling:
https://docs.djangoproject.com/en/4.2/topics/forms/

Django authentication system:
https://docs.djangoproject.com/en/4.2/topics/auth/

Creating superuser and login setup:
https://docs.djangoproject.com/en/4.2/ref/django-admin/#createsuperuser

## 3. Database & Models

Django models and SQLite integration:
https://docs.djangoproject.com/en/4.2/topics/db/models/

Migrations in Django:
https://docs.djangoproject.com/en/4.2/topics/migrations/

## 4. Bootstrap & Styling

Bootstrap official documentation (CSS/JS/CDN):
https://getbootstrap.com/docs/5.3/getting-started/introduction/

Bootstrap Modals (for pop-up messages):
https://getbootstrap.com/docs/5.3/components/modal/

## 5. APIs

Adzuna Jobs API documentation (for fetching internship data):
https://developer.adzuna.com/docs/search

## 6. Git & GitHub

Ignoring files with .gitignore:
https://git-scm.com/docs/gitignore

Pushing and pulling to GitHub:
https://docs.github.com/en/get-started/using-git

## 7. Environment Variables

Using .env files and os.environ in Python:
https://pypi.org/project/python-dotenv/
