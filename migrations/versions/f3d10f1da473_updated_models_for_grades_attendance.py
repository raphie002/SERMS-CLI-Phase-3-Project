# migrations/versions/f3d10f1da473_updated_models_for_grades_attendance.py
"""updated models for grades + attendance

Revision ID: f3d10f1da473
Revises: 
Create Date: 2025-12-03 15:38:05.468113
"""

from typing import Sequence, Union

from alembic import op  # type: ignore
import sqlalchemy as sa  # type: ignore


# revision identifiers, used by Alembic.
revision: str = 'f3d10f1da473'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- COURSES ---
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('code', sa.String(length=20), nullable=False),
        sa.Column('description', sa.String(length=255)),
        sa.UniqueConstraint('code')
    )

    # --- INSTRUCTORS ---
    op.create_table(
        'instructors',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('department', sa.String(length=100))
    )

    # --- STUDENTS ---
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('age', sa.Integer),
        sa.Column('department', sa.String(length=100))
    )

    # --- ATTENDANCE ---
    op.create_table(
        'attendance',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False)  # Present, Absent, Late
    )

    # --- GRADES ---
    op.create_table(
        'grades',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
        sa.Column('score', sa.Float, nullable=True),
        sa.Column('letter', sa.String(length=5), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('grades')
    op.drop_table('attendance')
    op.drop_table('students')
    op.drop_table('instructors')
    op.drop_table('courses')
