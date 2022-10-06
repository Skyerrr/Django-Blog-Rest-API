# Generated by Django 4.1.2 on 2022-10-05 22:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_alter_books_id_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="books",
            name="id_book",
        ),
        migrations.AddField(
            model_name="books",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
