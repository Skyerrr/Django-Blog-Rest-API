from django.core.mail import EmailMessage

# import os


# def sending_email(pk):
#     EMAIL = os.environ["EMAIL"]
#     PASSWORD = os.environ["PASSWORD"]

#     all_users = models.User.objects.all()
#     post = models.News.objects.get(pk=pk)

#     try:
#         smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#         smtp_server.ehlo()
#         smtp_server.login(EMAIL, PASSWORD)

#     except Exception as ex:
#         print("Something went wrong….", ex)

#     for user in all_users:

#         subject = f"Hello {user.username} we have a new post!"
#         message = f"Hey come check this out! {post.name} --- The best {post.category_id.name} News of all time!"
#         user_email = user.email

#         try:

#             smtp_server.sendmail(
#                 EMAIL, user_email, msg=f"Subject:{subject}\n\n{message}"
#             )
#             print(f"email sent to {user.email}")
#         except Exception as ex:

#             print("Something went wrong….", ex)


def sending_email(pk: str, all_users, post) -> None:
    """Function to send email to all users when a new post is made"""

    for user in all_users:
        if user.is_superuser:
            subject = f"Hello {user.username} we have a new post!"
            message = f"Hey come check this out! {post.name} --- The best {post.category_id.name} News of all time!"
            user_email = user.email
            email = EmailMessage(subject, message, to=[user_email])
            email.send()
