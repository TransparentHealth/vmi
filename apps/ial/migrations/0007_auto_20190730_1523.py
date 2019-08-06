# Generated by Django 2.1.8 on 2019-07-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ial', '0006_identityassuranceleveldocumentation_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identityassuranceleveldocumentation',
            name='evidence',
            field=models.CharField(blank=True, choices=[('ONE-SUPERIOR-OR-STRONG+', "Driver's License"), ('TRUSTED-REFEREE-VOUCH', 'Medicare card presented in person.(Vouching)'), ('ONE-SUPERIOR-OR-STRONG+', "Driver's License"), ('', 'No Identity Assurance evidence'), ('ONE-SUPERIOR-OR-STRONG+', 'One Superior or Strong+ pieces of identity evidence'), ('ONE-STRONG-TWO-FAIR', 'One Strong and Two Fair pieces of identity evidence'), ('TWO-STRONG', 'Two Pieces of Strong identity evidence'), ('TRUSTED-REFEREE-VOUCH', 'I am a Trusted Referee Vouching for this person'), ('KBA', 'Knowledged-Based Identity Verification')], default='', max_length=24),
        ),
    ]