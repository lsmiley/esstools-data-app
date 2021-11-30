# Generated by Django 2.2.10 on 2021-11-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acctcust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctname', models.CharField(blank=True, db_column='AcctName', max_length=75, null=True)),
                ('businesssec', models.CharField(blank=True, db_column='BusinessSec', max_length=75, null=True)),
                ('regulatory', models.CharField(blank=True, db_column='Regulatory', max_length=75, null=True)),
                ('created', models.CharField(db_column='Created', max_length=75)),
                ('address1', models.CharField(blank=True, db_column='Address1', max_length=75, null=True)),
                ('address2', models.CharField(blank=True, db_column='Address2', max_length=75, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=75, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=75, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=75, null=True)),
                ('contact1name', models.CharField(blank=True, db_column='Contact1Name', max_length=75, null=True)),
                ('contact1phone', models.CharField(blank=True, db_column='Contact1Phone', max_length=75, null=True)),
                ('contact1email', models.CharField(blank=True, db_column='Contact1Email', max_length=75, null=True)),
                ('contact2name', models.CharField(blank=True, db_column='Contact2Name', max_length=75, null=True)),
                ('contact2phone', models.CharField(blank=True, db_column='Contact2Phone', max_length=75, null=True)),
                ('contact2email', models.CharField(blank=True, db_column='Contact2Email', max_length=75, null=True)),
                ('wbsiteurl', models.CharField(blank=True, db_column='WbSiteURL', max_length=75, null=True)),
                ('createdby', models.CharField(blank=True, db_column='CreatedBy', max_length=75, null=True)),
                ('modifydate', models.CharField(blank=True, db_column='ModifyDate', max_length=75, null=True)),
            ],
            options={
                'ordering': ('acctname',),
            },
        ),
    ]
