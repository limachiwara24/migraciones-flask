
from datetime import datetime, timezone
from .extensions import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), default="usuario", nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username}>"


class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))

    ventas = db.relationship(
        "Venta",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Cliente {self.nombre} {self.apellido or ''}>"


class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=True)
    descripcion = db.Column(db.String(255), nullable=True)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)
    categoria = db.Column(db.String(50))

    detalles = db.relationship(
        "DetalleVenta",
        back_populates="producto"
    )

    def __repr__(self):
        return f"<Producto {self.nombre or self.descripcion}>"


class Venta(db.Model):
    __tablename__ = "ventas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    total = db.Column(db.Float, default=0.0, nullable=False)
    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False
    )

    cliente = db.relationship(
        "Cliente",
        back_populates="ventas"
    )

    detalles = db.relationship(
        "DetalleVenta",
        back_populates="venta",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Venta {self.id}>"


class DetalleVenta(db.Model):
    __tablename__ = "detalle_ventas"

    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(
        db.Integer,
        db.ForeignKey("ventas.id"),
        nullable=False
    )
    producto_id = db.Column(
        db.Integer,
        db.ForeignKey("productos.id"),
        nullable=False
    )
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    venta = db.relationship(
        "Venta",
        back_populates="detalles"
    )

    producto = db.relationship(
        "Producto",
        back_populates="detalles"
    )

    def __repr__(self):
        return f"<DetalleVenta {self.id}>"
