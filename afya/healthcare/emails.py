from django.core.mail import EmailMessage
from django.conf import settings

# Send email for appointments
def sendEmail(user_email, email_header, doctor_data, symptoms, date):
    my_email = user_email
    print(my_email)
    first_name = doctor_data['first_name']
    last_name = doctor_data['last_name']
    specialization = doctor_data['specialization']
    email = EmailMessage(
        f'{email_header}',
        f'Appointment Information \n\n Doctor Name: {first_name} {last_name} \n Specialization: {specialization} \n Appointment Date: {date} \n Symptoms:\n {symptoms}',
        settings.EMAIL_HOST_USER,
        ['gasaji8612@sopulit.com']
    )

    email.fail_silently = True
    email.send()

# Send email for the doctor application
def applicationEmail(user_email, email_header, email_body):
    my_email = user_email
    print(my_email)
    email = EmailMessage(
        f'{email_header}',
        f'{email_body}',
        settings.EMAIL_HOST_USER,
        ['gasaji8612@sopulit.com']
    )

    email.fail_silently = True
    email.send()