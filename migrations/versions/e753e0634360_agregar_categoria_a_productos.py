
"""agregar categoria a productos

Revision ID: e753e0634360
Revises: 9a88161e1950
"""

from alembic import op
import sqlalchemy as sa

revision = 'e753e0634360'
down_revision = '9a88161e1950'
branch_labels = None
depends_on = None


def upgrade():
    # No se realizan cambios en clientes.email,
    # productos.precio ni usuarios.email.
    # Esos cambios no corresponden a esta migración.
    pass


def downgrade():
    # No hay cambios que revertir.
    pass
