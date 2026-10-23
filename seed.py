
from decimal import Decimal

from app import create_app
from app.extensions import db
from app.models import Usuario, Cliente, Producto, Venta, DetalleVenta

app = create_app()

with app.app_context():
    if Usuario.query.first():
        print("La base ya tiene datos. Nada que hacer.")
        raise SystemExit

    # Usuarios
    admin = Usuario(
        username="admin",
        nombre="Administrador",
        email="admin@ventas.com",
        password="admin123",
        rol="admin"
    )

    vendedor = Usuario(
        username="maria",
        nombre="Maria",
        email="maria@ventas.com",
        password="maria123",
        rol="usuario"
    )

    # Clientes
    ana = Cliente(
        nombre="Ana",
        apellido="Pérez",
        email="ana@mail.com",
        telefono="70000001"
    )

    luis = Cliente(
        nombre="Luis",
        apellido="Gómez",
        email="luis@mail.com",
        telefono="70000002"
    )

    # Productos
    teclado = Producto(
        nombre="Teclado mecánico",
        descripcion="Teclado mecánico",
        precio=float(Decimal("45.50")),
        stock=20,
        categoria="Accesorios"
    )

    mouse = Producto(
        nombre="Mouse inalámbrico",
        descripcion="Mouse inalámbrico",
        precio=float(Decimal("18.00")),
        stock=35,
        categoria="Accesorios"
    )

    monitor = Producto(
        nombre="Monitor 24 pulgadas",
        descripcion="Monitor 24 pulgadas",
        precio=float(Decimal("120.00")),
        stock=8,
        categoria="Monitores"
    )

    db.session.add_all([
        admin,
        vendedor,
        ana,
        luis,
        teclado,
        mouse,
        monitor
    ])

    db.session.flush()

    # Primera venta
    v1 = Venta(cliente=ana)

    v1.detalles = [
        DetalleVenta(
            producto=teclado,
            cantidad=1,
            precio_unitario=teclado.precio,
            subtotal=teclado.precio
        ),
        DetalleVenta(
            producto=mouse,
            cantidad=2,
            precio_unitario=mouse.precio,
            subtotal=mouse.precio * 2
        )
    ]

    v1.total = sum(detalle.subtotal for detalle in v1.detalles)

    # Segunda venta
    v2 = Venta(cliente=luis)

    v2.detalles = [
        DetalleVenta(
            producto=monitor,
            cantidad=1,
            precio_unitario=monitor.precio,
            subtotal=monitor.precio
        )
    ]

    v2.total = sum(detalle.subtotal for detalle in v2.detalles)

    db.session.add_all([v1, v2])

    try:
        db.session.commit()
        print("Datos de prueba insertados correctamente.")
    except Exception:
        db.session.rollback()
        raise
