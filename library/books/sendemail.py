from django.core.mail import EmailMessage


def sending_email(all_users, post) -> None:
    """
    Function to send email to all users with superadmin when a new post is made.
    params:
    all_users -> all users from User table.
    post -> Blog post from News that has just be created.
    """
    print(type(all_users))
    print(type(post))

    for user in all_users:
        if user.is_superuser:
            subject = f"Hello {user.username} we have a new post!"
            message = f"Hey come check this out! {post.name} --- The best {post.category_id.name} News of all time!"
            user_email = user.email
            email = EmailMessage(subject, message, to=[user_email])
            email.send()
