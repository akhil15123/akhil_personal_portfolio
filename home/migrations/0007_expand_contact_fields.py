from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('home', '0006_rename_category_project_categories')]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=2000),
        ),
    ]
