# Generated by Django 4.1 on 2022-08-10 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qrgen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='action_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='input_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='scan_count',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='action_type',
            field=models.CharField(choices=[('web', 'Website URL'), ('tex', 'Text'), ('pdf', 'PDF'), ('biz', 'Business Card'), ('wap', 'Whatsapp'), ('img', 'Image'), ('eml', 'Email'), ('eve', 'Events')], max_length=3),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='img',
            field=models.ImageField(upload_to='media/qrcodes'),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='title',
            field=models.CharField(default='Untitled', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='qrtype',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='user_files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='qrcode',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qrgen.file'),
        ),
    ]
