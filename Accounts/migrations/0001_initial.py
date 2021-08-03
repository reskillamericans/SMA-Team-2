# Generated by Django 3.2.5 on 2021-08-03 06:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, default=None, null=True)),
                ('verified', models.BooleanField(blank=True, default=False, null=True)),
                ('account_status', models.CharField(blank=True, choices=[('Locked', 'Locked'), ('Unlocked', 'Unlocked')], default='Unlocked', max_length=10, null=True)),
                ('followers_count', models.IntegerField(blank=True, default=0, null=True)),
                ('follows_count', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSocial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facebook_link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('instagram_link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('twitter_link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('linkedin_link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('github_link', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(blank=True, default=None, max_length=50, null=True, unique=True)),
                ('token_used', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('user_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Password Resets',
                'ordering': ['user_id'],
            },
        ),
    ]