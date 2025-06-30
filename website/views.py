import os
from flask import Blueprint, render_template, request, jsonify
from flask_mail import Message
from website import mail
from website.config.skills import get_skills_with_links, SYSTEMS_INFRASTRUCTURE_SKILLS, LANGUAGES_APIS_TOOLING_SKILLS

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html.j2", 
                         systems_skills=get_skills_with_links(SYSTEMS_INFRASTRUCTURE_SKILLS),
                         languages_skills=get_skills_with_links(LANGUAGES_APIS_TOOLING_SKILLS))


@views.route("/send-email", methods=["POST"])
def send_email():
    try:
        data = request.get_json()
        
        # Extract form data
        sender_name = data.get('name')
        sender_email = data.get('email')
        subject = data.get('subject')
        message_body = data.get('message')
        
        # Validate required fields
        if not all([sender_name, sender_email, subject, message_body]):
            return jsonify({'success': False, 'error': 'All fields are required'}), 400
        
        # Create email message - Use MAIL_USERNAME as sender, not user's email
        msg = Message(
            subject=f"Portfolio Contact: {subject}",
            sender=os.environ.get('MAIL_USERNAME'),  # Use your Gmail as sender
            recipients=['josephrfoster@protonmail.com'],
            reply_to=sender_email,  # Set reply-to as the person contacting you
            body=f"""
New contact form submission:

Name: {sender_name}
Email: {sender_email}
Subject: {subject}

Message:
{message_body}

---
Sent from your portfolio website contact form
            """.strip()
        )
        
        # Send email
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Email sent successfully!'})
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({'success': False, 'error': 'Failed to send email. Please try again.'}), 500