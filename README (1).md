# LushLook 💄
### Beauty at your doorstep.

LushLook is a home-beauty-services platform concept connecting customers with beauty professionals. Customers can explore services and request appointments.

> **Status:** GitHub-ready starter scaffold. Replace demo content with your actual implementation, add your own screenshots, and test everything before presenting it as a completed product.

## Planned features
- Browse home beauty services
- View service descriptions and indicative prices
- Submit appointment requests
- Save booking requests in MySQL when configured
- Future scope: customer/beautician accounts, verified profiles, availability calendar, payment gateway, maps, ratings and reviews

## Technology
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Database: MySQL
- Tools: VS Code, Git and GitHub

This starter uses Flask for a basic API. If your college implementation uses Flutter or another backend, update the repository to match your actual code.

## Structure
```text
LushLook/
├── frontend/ (HTML, CSS, JavaScript)
├── backend/ (Flask API)
├── database/ (MySQL schema)
├── docs/ (project overview)
├── screenshots/
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
└── LICENSE
```

## Run locally
1. Install Python 3.10+ and MySQL Server.
2. Create and activate a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies: `pip install -r backend/requirements.txt`
4. Copy `.env.example` to `.env` and enter your local MySQL settings. Never upload `.env`.
5. Run `database/schema.sql` in MySQL Workbench or the MySQL command line.
6. Start the API: `python backend/app.py`
7. Open `frontend/index.html` in a browser.

The booking form only reports success when the API and database save the request.

## API
- `GET /api/health` — server status
- `GET /api/services` — sample service list
- `POST /api/bookings` — save a booking request

## Before publishing
- Replace sample content/prices with your approved project details.
- Add screenshots of your own running application.
- Add your actual report and presentation if you want them public.
- Test the app on your computer.
- Never commit passwords, API keys, personal customer data or private files.

## Disclaimer
This is an academic starter template. It does not include production authentication, payment processing, identity verification or a deployed booking service. Do not claim those features are implemented unless you build and test them.
