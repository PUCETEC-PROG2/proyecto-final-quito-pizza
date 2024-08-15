from django.db import models
#pizza, bebidas, complemento, postre
class Category(models.Model):
    name_category = models.CharField(max_length=16, null=False)

    def __str__(self) -> str:
        return f'{self.name_category}'
class Client(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=50, null=False)
    dni = models.CharField(max_length=10, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=150, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=30, null=False)
    PIZZA_SIZE = {
        ('P', 'Personal'),
        ('M', 'Mediana'),
        ('F', 'Familiar'),
        ('X', 'XXL')
    }
    pizza_size = models.CharField(max_length=10, choices=PIZZA_SIZE, null=False)
    PIZZA_DOUGH = {
        ('T', 'Tradicional'),
        ('D', 'Delgada'),
        ('A', 'Artesanal')
    }
    pizza_dough = models.CharField(max_length=14, choices=PIZZA_DOUGH, null=False)
    INGREDIENT_1 = {
        ('P', 'Pepperoni'),
        ('J', 'Jamon'),
        ('C', 'Choclo'),
        ('SI', 'Salchica Italiana'),
        ('SA', 'Salchicha Alemana'),
        ('CH', 'Chorizo'),
        ('CA', 'Carne'),
        ('PO', 'Pollo'),
        ('QP', 'Queso Parmesano'),
        ('QM', 'Queso Mozzarela'),
        ('QF', 'Queso Fontina'),
        ('-', '---')
    }
    ingredient_1 = models.CharField(max_length=20, choices=INGREDIENT_1, blank=True)
    INGREDIENT_2 = {
        ('P', 'Pepperoni'),
        ('J', 'Jamon'),
        ('C', 'Choclo'),
        ('SI', 'Salchica Italiana'),
        ('SA', 'Salchicha Alemana'),
        ('CH', 'Chorizo'),
        ('CA', 'Carne'),
        ('PO', 'Pollo'),
        ('QP', 'Queso Parmesano'),
        ('QM', 'Queso Mozzarela'),
        ('QF', 'Queso Fontina'),
        ('-', '---')
    }
    ingredient_2 = models.CharField(max_length=20, choices=INGREDIENT_2, blank=True)
    INGREDIENT_3 = {
        ('P', 'Pepperoni'),
        ('J', 'Jamon'),
        ('C', 'Choclo'),
        ('SI', 'Salchica Italiana'),
        ('SA', 'Salchicha Alemana'),
        ('CH', 'Chorizo'),
        ('CA', 'Carne'),
        ('PO', 'Pollo'),
        ('QP', 'Queso Parmesano'),
        ('QM', 'Queso Mozzarela'),
        ('QF', 'Queso Fontina'),
        ('-', '---')
    }
    ingredient_3 = models.CharField(max_length=20, choices=INGREDIENT_3, blank=True)
    INGREDIENT_4 = {
        ('P', 'Pepperoni'),
        ('J', 'Jamon'),
        ('C', 'Choclo'),
        ('SI', 'Salchica Italiana'),
        ('SA', 'Salchicha Alemana'),
        ('CH', 'Chorizo'),
        ('CA', 'Carne'),
        ('PO', 'Pollo'),
        ('QP', 'Queso Parmesano'),
        ('QM', 'Queso Mozzarela'),
        ('QF', 'Queso Fontina'),
        ('-', '---')
    }
    ingredient_4 = models.CharField(max_length=20, choices=INGREDIENT_4, blank=True)
    description = models.CharField(max_length=150, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_pizza = models.DecimalField(max_digits=10, decimal_places=2, null = False)
    picture_pizza = models.ImageField(upload_to='picture_pizzas')

    def __str__(self) -> str:
        return f'{self.pizza_name}'

class Product(models.Model):
    product_name = models.CharField(max_length=30, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_product = models.DecimalField(max_digits=10, decimal_places=2, null = False)
    picture_products = models.ImageField(upload_to='picture_products')

    def __str__(self) -> str:
        return f'{self.product_name}'
class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    def __str__(self) -> str:
        return f"Venta {self.id} - {self.date} - {self.client}"
    
    def update_total(self):
        self.total = sum(detail.subtotal() for detail in self.detail.all())
        self.save()


class Purchase_Detail(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='detail')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    amount_pizza = models.PositiveIntegerField()
    unit_price_pizza = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount_product = models.PositiveIntegerField()
    unit_price_product = models.DecimalField(max_digits=10, decimal_places=2)
    
    def subtotal(self):
        return self.amount_pizza * self.unit_price_pizza + self.amount_product * self.unit_price_product
    
    def __str__(self) -> str:
        return f"{self.amount_product} x {self.product.product_name} y {self.amount_pizza} x {self.pizza.pizza_name} en Venta {self.purchase.id}"