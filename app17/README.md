# Job Application Django Project

This is a Django project for a job application form that allows users to submit their details. It sends a confirmation email upon form submission and stores the data in a MySQL database.

The only difference between this version and previous version(app16) is the use of MySQL for database integration.

## Features

- **Form Submission**: Users can submit their personal details through a form.
- **Database Integration**: Stores submitted form data in a MySQL database.
- **Email Notification**: Sends a confirmation email to the user upon form submission.

## Requirements

- Python 3.x
- Django
- django-crispy-forms
- MySQL
- Email service credentials (Gmail in this example)

## Configuration

### Email Configuration

Make sure to configure your email settings in the `settings.py` file:

```python
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

```

### Usage

- Fill out the job application form.
- Submit the form.
- Check your email for a confirmation message.
