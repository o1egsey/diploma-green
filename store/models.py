from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(verbose_name='Category Name', help_text='Required and unique', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Category slug', max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MTTPMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(
        verbose_name="title",
        help_text="Required",
        max_length=255,
    )
    description = models.TextField(verbose_name="description", help_text="Not Required", blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(verbose_name="Regular price", max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(verbose_name="Discount price", max_digits=7, decimal_places=2)
    is_active = models.BooleanField(
        verbose_name="Product visibility",
        help_text="Change product visibility",
        default=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name="image",
        help_text="Upload a product image",
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name="Alternative text",
        help_text="Please add alternative text",
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
