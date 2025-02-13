# Generated by Django 2.1 on 2019-10-13 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.Cart')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
    ]
