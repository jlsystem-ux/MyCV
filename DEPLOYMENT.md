# Deployment Guide for PythonAnywhere

This guide will help you deploy your Django CV website to PythonAnywhere.

## Prerequisites

1. Create a free account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Have your GitHub repository ready with this project

## Step-by-Step Deployment

### 1. Clone Your Repository

Once logged into PythonAnywhere, open a Bash console and clone your repository:

```bash
git clone https://github.com/YOUR_USERNAME/MyCV.git
cd MyCV
```

### 2. Create a Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 mycv_env
```

If the environment is created successfully, you should see `(mycv_env)` in your prompt.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Settings for Production

Edit `mycv_project/settings.py`:

```bash
nano mycv_project/settings.py
```

Update the following:

```python
# Set DEBUG to False for production
DEBUG = False

# Add your PythonAnywhere domain
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']

# Update secret key (generate a new one for production)
SECRET_KEY = 'your-new-secret-key-here'
```

To generate a new secret key, you can use:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run Migrations and Populate Data

```bash
python manage.py migrate
python manage.py populate_cv
```

### 6. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 7. Collect Static Files

```bash
python manage.py collectstatic
```

Type 'yes' when prompted.

### 8. Configure the Web App

1. Go to the **Web** tab in your PythonAnywhere dashboard
2. Click **Add a new web app**
3. Choose **Manual configuration** (not Django wizard)
4. Select **Python 3.10**

### 9. Set Up the WSGI File

1. In the **Web** tab, find the **Code** section
2. Click on the WSGI configuration file link
3. Delete all content and replace with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/MyCV'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable to tell Django where settings are
os.environ['DJANGO_SETTINGS_MODULE'] = 'mycv_project.settings'

# Activate virtual environment
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

### 10. Configure Virtual Environment Path

In the **Web** tab:

1. Find the **Virtualenv** section
2. Enter the path to your virtual environment:
   ```
   /home/YOUR_USERNAME/.virtualenvs/mycv_env
   ```

### 11. Configure Static Files

In the **Web** tab, find the **Static files** section and add:

| URL          | Directory                                      |
|--------------|------------------------------------------------|
| /static/     | /home/YOUR_USERNAME/MyCV/staticfiles          |

Replace `YOUR_USERNAME` with your PythonAnywhere username.

### 12. Reload Your Web App

Click the green **Reload** button at the top of the Web tab.

### 13. Visit Your Site

Your CV site should now be live at:
```
https://YOUR_USERNAME.pythonanywhere.com
```

## Managing Your CV

To update your CV content:

1. Visit `https://YOUR_USERNAME.pythonanywhere.com/admin/`
2. Log in with your superuser credentials
3. Edit the Personal Info, Skills, Experience, Education, and Certifications

## Updating Your Site

When you make changes to your code:

```bash
cd ~/MyCV
git pull
python manage.py migrate  # If you added new migrations
python manage.py collectstatic  # If you changed static files
```

Then reload your web app from the Web tab.

## Troubleshooting

### Site Not Loading
- Check the error log in the Web tab
- Ensure all paths in WSGI config are correct
- Verify virtual environment path is correct

### Static Files Not Loading
- Make sure you ran `collectstatic`
- Verify static files path in Web tab is correct
- Check STATIC_ROOT in settings.py

### Database Issues
- Make sure migrations were run: `python manage.py migrate`
- Check that db.sqlite3 file exists in project root

## Production Security Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Generate new `SECRET_KEY` for production
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Use environment variables for sensitive data (optional)
- [ ] Regularly backup your database
- [ ] Keep Django and dependencies updated

## Need Help?

- PythonAnywhere Help: https://help.pythonanywhere.com/
- Django Documentation: https://docs.djangoproject.com/
- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/

## Local Development

To run the site locally for testing:

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

**Note**: Free PythonAnywhere accounts have some limitations. For custom domains and more resources, consider upgrading to a paid plan.
