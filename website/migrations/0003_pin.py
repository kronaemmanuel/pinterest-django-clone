# Generated by Django 4.0.6 on 2022-07-26 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20220726_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('picture', models.ImageField(upload_to='images/')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.profile')),
            ],
        ),
    ]
