from django.db import connection, models
from django.forms import ValidationError
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
        
    def clean(self):
        super().clean()
        if not self.validate_dni(self.dni):
            raise ValidationError('La cédula proporcionada no es válida.')
        if not self.validate_phone_number(self.phone_number):
            raise ValidationError('El número de teléfono no es válido.')
        if self.pk:
            if Client.objects.filter(dni=self.dni).exclude(pk=self.pk).exists():
                raise ValidationError({'dni': 'Esta cédula ya está registrada'})
        else:
            if Client.objects.filter(dni=self.dni).exists():
                raise ValidationError({'dni': 'Esta cédula ya está registrada'})
        if self.pk:
            if Client.objects.filter(email=self.email).exclude(pk=self.pk).exists():
                raise ValidationError({'email': 'Este correo electrónico ya está registrado'})
        else:
            if Client.objects.filter(email=self.email).exists():
                raise ValidationError({'email': 'Este correo electrónico ya está registrado'})
        if self.pk:
            if Client.objects.filter(phone_number=self.phone_number).exclude(pk=self.pk).exists():
                raise ValidationError({'phone_number': 'Este número telefónico ya está registrado'})
        else:
            if Client.objects.filter(phone_number=self.phone_number).exists():
                raise ValidationError({'phone_number': 'Este número telefónico ya está registrado'})

    def validate_dni(self, dni):
        with connection.cursor() as cursor:
            cursor.execute("SELECT validate_dni(%s)", [dni])
            is_valid = cursor.fetchone()[0]
        return is_valid

    def validate_phone_number(self, phone_number):
        with connection.cursor() as cursor:
            cursor.execute("SELECT validate_phone_number(%s)", [phone_number])
            is_valid = cursor.fetchone()[0]
        return is_valid

    def save(self, *args, **kwargs):
        self.clean()  # Validar antes de guardar
        super().save(*args, **kwargs)

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
        ('J', 'Jamón'),
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
        ('J', 'Jamón'),
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
        ('J', 'Jamón'),
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
        ('J', 'Jamón'),
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
    stock = models.IntegerField()
    picture_products = models.ImageField(upload_to='picture_products')

    def __str__(self) -> str:
        return f'{self.product_name}'
class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    def __str__(self) -> str:
        return f"{self.id} - {self.date} - {self.client}"
    

class Purchase_Detail(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='detail')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    amount_pizza = models.PositiveIntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    amount_product = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.id} en Venta {self.purchase.id}"

#sonido ambiental

class AudioFile(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio')

    def __str__(self):
        return self.title