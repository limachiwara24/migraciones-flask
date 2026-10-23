from alembic import op
import sqlalchemy as sa

revision = '9a88161e1950'
down_revision = '337c7160dd57'
branch_labels = None
depends_on = None


def upgrade():
    # Las tablas ventas y detalle_ventas ya existen.
    # No volver a crearlas.

    # Agregar apellido a clientes
    with op.batch_alter_table('clientes') as batch_op:
        batch_op.add_column(
            sa.Column('apellido', sa.String(100), nullable=True)
        )

    # Agregar campos a productos
    with op.batch_alter_table('productos') as batch_op:
        batch_op.add_column(
            sa.Column('nombre', sa.String(100), nullable=True)
        )
        batch_op.add_column(
            sa.Column('categoria', sa.String(50), nullable=True)
        )
        batch_op.alter_column(
            'descripcion',
            existing_type=sa.String(255),
            nullable=True
        )

    # Agregar campos a usuarios
    with op.batch_alter_table('usuarios') as batch_op:
        batch_op.add_column(
            sa.Column('nombre', sa.String(100), nullable=True)
        )
        batch_op.add_column(
            sa.Column('email', sa.String(120), nullable=True)
        )


def downgrade():
    # Revertir solamente los cambios realizados por esta migración.

    with op.batch_alter_table('usuarios') as batch_op:
        batch_op.drop_column('email')
        batch_op.drop_column('nombre')

    with op.batch_alter_table('productos') as batch_op:
        batch_op.alter_column(
            'descripcion',
            existing_type=sa.String(255),
            nullable=False
        )
        batch_op.drop_column('categoria')
        batch_op.drop_column('nombre')

    with op.batch_alter_table('clientes') as batch_op:
        batch_op.drop_column('apellido')
