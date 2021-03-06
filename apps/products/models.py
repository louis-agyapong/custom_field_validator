from django.core import validators
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
    Product detail table
    """

    web_id = models.CharField(
        _("Product Website Id"),
        max_length=13,
        validators=[RegexValidator(r"^\d\d\d-\d\d-\d\d-\d\d\d$", _("Enter a valid web id."), "invalid")],
        unique=True,
        null=False,
        blank=False,
        help_text=_("format: xxx-xx-xx-xxx, required, unique"),
    )
    slug = models.SlugField(
        _("Product Safe URL"),
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        help_text=_("format:required, letters, numbers, hyphens or underscores"),
    )
    name = models.CharField(
        _("Product Name"),
        max_length=255,
        null=False,
        blank=False,
        help_text=_("format: required, max_length=255"),
    )
    description = models.TextField(
        _("Product Description"),
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name
