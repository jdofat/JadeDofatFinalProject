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
