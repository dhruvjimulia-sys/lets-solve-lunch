# Generated by Django 4.2.1 on 2023-06-12 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_restaurant_name_restaurant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('is_student', models.BooleanField(default=True, null=True)),
                ('loyalty_points', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='qr',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
    ]
