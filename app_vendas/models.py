from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    APP vendas User class
    Email and password are required. Other fields are optional.
    """

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s ' % (self.first_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True, blank=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    email = models.EmailField(default=None)
    whats = models.BooleanField(default=None)
    telefone = models.CharField(max_length=15)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    cod_produto = models.IntegerField(primary_key=True, blank=True)
    titulo = models.CharField(max_length=20, default='Titulo')
    descricao_produto = models.TextField(default='Descreva o Produto')
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, unique=True)

    def __str__(self):
        return self.titulo


class Venda(models.Model):
    cod_venda = models.IntegerField(primary_key=True , blank=True, auto_created=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produto, default=0, blank=True, on_delete=models.CASCADE)
    observacao = models.TextField(default=None, blank=True)

    class TipoPagamento(models.TextChoices):
        visa = 'Visa'
        boleto = 'Boleto'
        master = 'Mastercard'

    tipo_pagamento = models.CharField(max_length=10, choices=TipoPagamento.choices, default='Visa',
                                      verbose_name='Meio de Pagamento')

    def __str__(self):
        return self.cod_venda.__str__()