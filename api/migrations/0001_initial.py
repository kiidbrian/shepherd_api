# Generated by Django 2.0.8 on 2019-01-21 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('abstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Abstract')),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('address', models.TextField()),
            ],
            bases=('api.abstract',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('abstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Abstract')),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('role', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('password', models.TextField()),
            ],
            bases=('api.abstract',),
        ),
        migrations.AddField(
            model_name='attendance',
            name='member_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='api.Member'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
