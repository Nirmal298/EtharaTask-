prompt: Employment Management System. Full Stack Application Prompt

Context and function
I need to build a modern Employment Management System. This system will managing employee operations, communication, attendance, payroll, leave requests, and performance tracking.  This system I have to make sure it is easy to use and works well. The Employment Management System must have an interface that people like to use. It has to be easy to get and work well on different devices.

The Employment Management System should have include centralizes dashboard , show employee statistics , department summaries and attendance and display  leave  status . This page should be easy to understand and help the people, in charge of hiring the heads of departments and the employees themselves. The Employment Management System should also have a communication and messaging module . When someone sends a message the system should keep a record of it. Automated email notifications should be send  for important events such as leave approvals,  employee onboarding,birthday , reminders, and announcements.

Objective
I want to make a website that shows all my work. This website should have
* The project Consist advanced frontend, backend, database, authentication, and DevOps capabilities.
*The system will have a user- interface.
* manage employment data secure and efficiently.
*The goal is to build a system that's both functional and visually appealing.
* I want to build a professional full-stack Employment Management System portfolio


UI and Animation Requirements

Dashboard Animations and Interactions
Implement smooth  entrance animations on dashboard widgets and metric cards on  initial page load.
Use animated charts for headcount trends, attrition rate, and department distribution.
Apply staggered transitions when loading employee lists and table rows.
Animate module transitions (Dashboard → Leave → Payroll) with smooth fade or slide effects
Include hover interactions on action cards, employee rows, and quick-action buttons
Ensure all animations are optimized :
#Use GPU-friendly properties (transform, opacity) only.
#Avoid layout thrashing.
#Do not block scroll or interaction performance.

Layout Requirements
The system must include:
Dashboard section with animated metric cards and real-time charts
Employee Management section with animated list reveal and profile transitions
Attendance section with animated calendar and status indicators
Leave Management section with animated approval workflow steps
Payroll section with animated salary breakdown and pay slip preview
Performance section with animated goal progress indicators and review timelines
Notification center with animated alert badges and in-app toast messages

The layout must be:
Fully responsive at mobile, tablet, desktop etc. 
Sidebar navigation bar  with smooth collapse .
Accessible at ARIA labels, keyboard navigation and  semantic HTML.
Optimized performance with lazy-loaded sections and skeleton loaders.


Contact and Request System Requirements
Modal Behavior

Clicking action buttons (Apply Leave, Add Employee, Approve, Send Reminder) must:
Open a modal form with an animated entrance and exit.
Lock background scroll while modal is open
Close on backdrop click or ESC key with exit animation

Form Fields

Employee Name (auto-filled from authenticated session and read-only)
Request Type (dropdown: Leave / Query / Document Request / Other)
Date Range or Target Date (date picker)
Reason or Message (required, multiline)
Supporting Document (optional file upload)

Validation

Client-side validation with inline error messages per field
Prevent form  submission if validation failed or any required fields are missing . 
Show loading state on submit button during API call
Display success confirmation or error message after submission

Backend Requirements

API Architecture

The  API  follows  different versions. such as / api /v1/....
Implement  JWT-based authentication. This means we will use a token to make sure only the right people can use our API. We will also make sure this token is changed regularly.
Role-Based Access Control (RBAC) and permission-based authorization implement  for protected routes.
Maintain  record of every API call. This record will have the method, endpoint, user and timestamp.


Data Processing Requirements

Implement  all user inputs to prevent XSS, SQL Injection, and NoSQL Injection attacks.
We need to check all the date ranges email formats, phone numbers and numeric fields on the server.
use  b-crypt for hashing password  . 
We need to encrypt some fields. These fields are sensitive.
They include  PAN number and bank account details.
We will use  AES-256 to encrypt these fields.
All the API responses have to be in a format. If it is successful then : { success: data: {... } Message: "Operation successful" }
If there is an error then look like this: { success: false error: "Error description," code: 400 }
If we are getting a list of things, from the API . like this: { data, total, page limit }
We have to prevent spam and abuse. We will use something called rate limiting. We might also use CAPTCHA on public-facing forms. This will help us make sure that people are not using our API in a way.

Output Requirements
Role-specific dashboards are fully functional with live data and animated widgets.
Complete CRUD operations working across all modules
Automated email notifications were triggered and delivered on all key events.
PDF payslip generation and download working end-to-end
Audit log accessible by Admin with filters for date, action type, and user
Confirmation message shown to user after every successful submission
Graceful error handling displayed when any backend operation fails
Animated approval status indicators updating in real time on state changes

Error Handling and Documentation
frontend errors  handle from  both field  with clear user-facing messages.
backend validation errors handle  with  HTTP status codes like 400, 401, 403, 404, 500.
Implement  global error boundary in the frontend to catch unexpected crashes.
Log all backend failures using Winston or an equivalent logger (info, warn, error levels).
Provide complete project documentation covering:
Folder and module structure
Setup and local installation instructions
Environment variable reference table with descriptions
Seed data instructions for local development and testing
Full API reference using Swagger or Open API specification
Deployment steps for Docker, Vercel, Railway, and AWS

Performance and Scalability
Paginate all list views server-side, to prevent large payload responses
Do not index outside fields of the database that Index into filters, searches, sorting and joins.
Redis in-memory store, Cache data which is frequently read and rarely changes (departments, roles and configs)
Debounce all search inputs with a minimum of 300 ms delay.
Lazy-load heavy dashboard charts, data visualizations and module components.
Rate-limited Authentication endpoints (max 5 times/minute per IP)
Design  API layer which  follow scalable service-oriented architecture principles.

Technology Stack
Frontend: React (or Next.js, Framer Motion for animations and transitions—Tailwind CSS for styling). Recharts or Chart.js for data visualizations
Backend: Node.js with Express (or Next.js API routes), Node mailer or SendGrid for sending emails,  environment configuration  use dotenv and secure environment variables .
Database: PostgreSQL (recommended) or MongoDB
Optional: Redis (for caching), Docker (for containerization), Prisma or Mongoose (ORMs), Swagger UI (interactive API documentation), MongoDB Atlas/Sup-abase (managed DB hosting)
