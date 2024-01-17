# Generated by Django 5.0.1 on 2024-01-16 20:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.IntegerField(default=1, null=True)),
                ('Sample', models.CharField(default='Host', max_length=100, null=True)),
                ('Sample_type', models.CharField(default='Original', max_length=100, null=True, verbose_name='Sample Type')),
                ('Stratum', models.CharField(default='Urban Nairobi', max_length=100, null=True)),
                ('Status', models.CharField(default='Host', max_length=100, null=True)),
                ('HHID', models.CharField(max_length=100, verbose_name='HHID/HHRID')),
                ('Supervisor', models.CharField(max_length=100, verbose_name='Supervisor Name')),
                ('Enumerator', models.CharField(max_length=100, verbose_name='Enumerator Name')),
                ('HR_name', models.CharField(max_length=100, null=True, verbose_name='HR name')),
                ('RR_name', models.CharField(max_length=100, null=True, verbose_name='RR name')),
                ('WER_name', models.CharField(max_length=100, null=True, verbose_name='WER name')),
                ('CR_name', models.CharField(max_length=100, null=True, verbose_name='CR name')),
                ('RR_status', models.CharField(blank=True, choices=[('', ''), ('Available in Original Household', 'Available in Original Household'), ('Available in New Household', 'Available in New Household'), ('Not Available Relocated Locally', 'Not Available Relocated Locally'), ('Not Available Relocated Internationally', 'Not Available Relocated Internationally'), ('Deceased', 'Deceased'), ('Refused to participate', 'Refused to participate')], max_length=100, verbose_name='RR status')),
                ('attempt1_date', models.DateTimeField(blank=True, verbose_name='Date & Time of 1st attempt to surver RR')),
                ('attempt2_date', models.DateTimeField(blank=True, verbose_name='Date & Time of 2nd attempt to surver RR')),
                ('attempt3_date', models.DateTimeField(blank=True, verbose_name='Date & Time of 3rd attempt to surver RR')),
                ('if_rr_surveyed_date', models.DateField(blank=True, verbose_name='if RR was surveyed,record the date of interview')),
                ('if_rr_not_details', models.TextField(blank=True, verbose_name='If attempts to survey the RR in their original/current household were not successful, Please record in detail the outcome from the attempts made to interview RR1 ')),
                ('status_of_RR1', models.CharField(blank=True, choices=[('', ''), ('Approved', 'Approved '), ('Not Approved', 'Not Approved')], max_length=100, verbose_name='Status of RR1 Respondent Replacement approval [Based on feedback from column R]')),
                ('HR_module_completed', models.CharField(blank=True, choices=[('', ''), ('Completed', 'Completed'), ('Not Completed', 'Not Completed')], max_length=100, verbose_name='Has the HR module been completed or not completed?')),
                ('RR_module_completed', models.CharField(blank=True, choices=[('', ''), ('Completed', 'Completed'), ('Not Completed', 'Not Completed')], max_length=100, verbose_name='Has the RR module been completed or not completed?')),
                ('if_WER_eligible', models.CharField(blank=True, choices=[('', ''), ('Eligible', 'Eligible'), ('Not Eligible', 'Not Eligible')], max_length=100, verbose_name='If RR household was surveyed, was the household eligible for the WER module')),
                ('if_WER_eligible_coompleted', models.CharField(blank=True, choices=[('', ''), ('Completed', 'Completed'), ('Not Completed', 'Not Completed')], max_length=100, verbose_name='If eligible, has the WER module been completed or not completed?')),
                ('if_CR_eligible', models.CharField(blank=True, choices=[('', ''), ('Eligible', 'Eligible'), ('Not Eligible', 'Not Eligible')], max_length=100, verbose_name='If RR household was surveyed, was the household eligible for the CR module')),
                ('if_CR_eligible_completed', models.CharField(blank=True, choices=[('', ''), ('Completed', 'Completed'), ('Not Completed', 'Not Completed')], max_length=100, verbose_name='If eligible, has the CR module been completed or not completed?')),
                ('comments', models.TextField(blank=True, verbose_name='Record any other comment on the household/interview')),
                ('mark', models.BooleanField(default=False, verbose_name='completed the required fields')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
