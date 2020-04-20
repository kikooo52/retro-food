# Generated by Django 2.2.11 on 2020-04-14 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Име и Фамилия')),
                ('phone', models.CharField(max_length=150, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Създадено на')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Променено на')),
                ('paid', models.BooleanField(default=False, verbose_name='Платено')),
            ],
            options={
                'verbose_name': 'Поръчка',
                'verbose_name_plural': 'Поръчки',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_foods', to='foods.Food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
            ],
        ),
    ]
