# Django CV Website

A professional CV website built with Django, showcasing Luis Alberto Arboleda's professional experience, skills, and qualifications.

## Features

- Clean, professional CV layout
- Responsive design (mobile-friendly)
- Admin interface for easy content management
- Pre-populated with CV data
- Print-friendly styling
- Ready for PythonAnywhere deployment

## Project Structure

```
MyCV/
├── cv/                          # Main CV application
│   ├── management/
│   │   └── commands/
│   │       └── populate_cv.py   # Command to populate database
│   ├── migrations/              # Database migrations
│   ├── static/
│   │   └── cv/
│   │       └── style.css        # CV styling
│   ├── templates/
│   │   └── cv/
│   │       └── cv_template.html # CV template
│   ├── admin.py                 # Admin configuration
│   ├── models.py                # Data models
│   ├── urls.py                  # URL routing
│   └── views.py                 # View logic
├── mycv_project/                # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── DEPLOYMENT.md                # Deployment guide
└── README.md                    # Original CV content
```

## Data Models

The application includes the following models:

- **PersonalInfo**: Name, title, contact information, summary
- **Experience**: Work experience with company, position, dates, and description
- **Education**: Educational background
- **Skill**: Skills categorized by type (soft skills, methodologies, programming languages, databases, tools)
- **Certification**: Professional certifications

## Local Development

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/MyCV.git
   cd MyCV
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Populate the database with CV data**:
   ```bash
   python manage.py populate_cv
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - CV site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Managing Content

### Via Admin Panel

1. Access the admin panel at `/admin/`
2. Log in with your superuser credentials
3. Edit the following sections:
   - Personal Information
   - Skills
   - Experience
   - Education
   - Certifications

### Via Management Command

To reset and repopulate all CV data:

```bash
python manage.py populate_cv
```

**Note**: This will delete all existing CV data and recreate it from the script.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on deploying to PythonAnywhere.

### Quick Deployment Steps

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Clone this repository in a PythonAnywhere Bash console
3. Create a virtual environment and install dependencies
4. Configure the web app (see DEPLOYMENT.md for details)
5. Your CV will be live at `https://YOUR_USERNAME.pythonanywhere.com`

## Technologies Used

- **Django 5.2.8**: Web framework
- **SQLite**: Database (default, can be changed to PostgreSQL/MySQL)
- **HTML5 & CSS3**: Frontend
- **Python 3**: Backend language

## Customization

### Styling

Edit `cv/static/cv/style.css` to customize the appearance of your CV.

### Template

Edit `cv/templates/cv/cv_template.html` to modify the layout and structure.

### Data

You can modify `cv/management/commands/populate_cv.py` to change the default CV data, or use the admin panel to make updates.

## Production Considerations

Before deploying to production:

1. Set `DEBUG = False` in `mycv_project/settings.py`
2. Generate a new `SECRET_KEY`
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production-grade database (PostgreSQL recommended)
5. Set up proper static file serving
6. Enable HTTPS

## License

This project is open source and available for personal use.

## Contact

**Luis Alberto Arboleda**
- Email: arboledaluisalberto28@gmail.com
- Phone: +44 7386 182877
- LinkedIn: [linkedin.com/in/luis-arboleda-350316181](https://www.linkedin.com/in/luis-arboleda-350316181)

---

**Original CV content**: See [README.md](README.md)
