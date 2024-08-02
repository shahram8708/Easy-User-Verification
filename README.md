# User Registration and Email Verification

This project is a simple Flask web application that allows users to register, receive an email verification link, and access a dashboard once their email is verified. It uses Flask for the web framework and Flask-Mail for sending verification emails.

## Features

- **User Registration**: Users can register with a username, email, and password.
- **Email Verification**: After registration, users receive an email with a verification link.
- **Dashboard Access**: Once verified, users can access a personalized dashboard.
- **Logout**: Users can log out and end their session.

## Installation

### Prerequisites

- Python 3.7 or higher
- A Gmail account for sending emails

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shahram8708//Easy-User-Verification.git
   cd your-repository
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Email Settings**

   Update the following configuration in `app.py` with your Gmail credentials:

   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-email-password'
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

   The application will start and be accessible at `http://localhost:5000`.

## Usage

1. **Register**: Navigate to the home page (`/`) and fill out the registration form. After submitting, check your email for a verification link.
2. **Verify Email**: Click the link in the email to verify your account. This will log you in and redirect you to the dashboard.
3. **Access Dashboard**: Once verified, you can access the dashboard at `/dashboard`.
4. **Logout**: Click the "Logout" button on the dashboard to end your session.

## File Structure

- `app.py`: The main Flask application file with routing and logic.
- `templates/`: Contains HTML templates for registration, email verification, and dashboard.
  - `register.html`: Registration form.
  - `dashboard.html`: User dashboard.
  - `email_verification.html`: Email verification message.
- `requirements.txt`: List of Python package dependencies.

## Troubleshooting

- **Email Not Received**: Check your spam/junk folder. Ensure your email settings are correctly configured in `app.py`.
- **Application Errors**: Check the Flask development server output for error messages. Make sure all dependencies are installed.
