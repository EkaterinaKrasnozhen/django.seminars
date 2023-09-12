# Generated by Django 4.2.4 on 2023-09-12 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('chanched_at', models.DateField(default=None, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp4.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp4.post')),
            ],
        ),
    ]