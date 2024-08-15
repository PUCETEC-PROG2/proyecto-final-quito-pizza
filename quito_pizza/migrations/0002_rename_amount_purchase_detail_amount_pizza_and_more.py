# Generated by Django 4.2 on 2024-08-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quito_pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_detail',
            old_name='amount',
            new_name='amount_pizza',
        ),
        migrations.RenameField(
            model_name='purchase_detail',
            old_name='unit_price',
            new_name='unit_price_pizza',
        ),
        migrations.AddField(
            model_name='purchase_detail',
            name='amount_product',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase_detail',
            name='unit_price_product',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient_1',
            field=models.CharField(blank=True, choices=[('QM', 'Queso Mozzarela'), ('PO', 'Pollo'), ('CA', 'Carne'), ('QP', 'Queso Parmesano'), ('SA', 'Salchicha Alemana'), ('J', 'Jamon'), ('CH', 'Chorizo'), ('SI', 'Salchica Italiana'), ('-', '---'), ('QF', 'Queso Fontina'), ('C', 'Choclo'), ('P', 'Pepperoni')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient_2',
            field=models.CharField(blank=True, choices=[('QM', 'Queso Mozzarela'), ('PO', 'Pollo'), ('CA', 'Carne'), ('QP', 'Queso Parmesano'), ('SA', 'Salchicha Alemana'), ('J', 'Jamon'), ('CH', 'Chorizo'), ('SI', 'Salchica Italiana'), ('-', '---'), ('QF', 'Queso Fontina'), ('C', 'Choclo'), ('P', 'Pepperoni')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient_3',
            field=models.CharField(blank=True, choices=[('QM', 'Queso Mozzarela'), ('PO', 'Pollo'), ('CA', 'Carne'), ('QP', 'Queso Parmesano'), ('SA', 'Salchicha Alemana'), ('J', 'Jamon'), ('CH', 'Chorizo'), ('SI', 'Salchica Italiana'), ('-', '---'), ('QF', 'Queso Fontina'), ('C', 'Choclo'), ('P', 'Pepperoni')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient_4',
            field=models.CharField(blank=True, choices=[('QM', 'Queso Mozzarela'), ('PO', 'Pollo'), ('CA', 'Carne'), ('QP', 'Queso Parmesano'), ('SA', 'Salchicha Alemana'), ('J', 'Jamon'), ('CH', 'Chorizo'), ('SI', 'Salchica Italiana'), ('-', '---'), ('QF', 'Queso Fontina'), ('C', 'Choclo'), ('P', 'Pepperoni')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizza_size',
            field=models.CharField(choices=[('P', 'Personal'), ('F', 'Familiar'), ('M', 'Mediana'), ('X', 'XXL')], max_length=10),
        ),
    ]
