"""Initial migration

Revision ID: c1dee4b2a666
Revises: 
Create Date: 2025-01-24 11:57:20.752994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c1dee4b2a666'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    op.drop_table('django_session')
    op.drop_index('books_book_bookshelves_0a4572cc', table_name='books_book_bookshelves')
    op.drop_index('books_book_bookshelves_40928700', table_name='books_book_bookshelves')
    op.drop_table('books_book_bookshelves')
    op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    op.drop_table('django_admin_log')
    op.drop_index('books_book_languages_0a4572cc', table_name='books_book_languages')
    op.drop_index('books_book_languages_468679bd', table_name='books_book_languages')
    op.drop_table('books_book_languages')
    op.drop_index('books_format_0a4572cc', table_name='books_format')
    op.drop_table('books_format')
    op.drop_table('django_migrations')
    op.drop_index('books_language_code_217c406c_like', table_name='books_language')
    op.drop_table('books_language')
    op.drop_table('books_subject')
    op.drop_table('django_content_type')
    op.drop_index('books_bookshelf_name_2642cad6_like', table_name='books_bookshelf')
    op.drop_table('books_bookshelf')
    op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c', table_name='auth_user_user_permissions')
    op.drop_index('auth_user_user_permissions_user_id_a95ead1b', table_name='auth_user_user_permissions')
    op.drop_table('auth_user_user_permissions')
    op.drop_index('books_book_subjects_0a4572cc', table_name='books_book_subjects')
    op.drop_index('books_book_subjects_ffaba1d1', table_name='books_book_subjects')
    op.drop_table('books_book_subjects')
    op.alter_column('auth_group', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    op.create_index(op.f('ix_auth_group_id'), 'auth_group', ['id'], unique=False)
    op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    op.drop_constraint('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'auth_group_permissions', type_='unique')
    op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    op.drop_constraint('auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', 'auth_group_permissions', type_='foreignkey')
    op.drop_constraint('auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', 'auth_group_permissions', type_='foreignkey')
    op.create_foreign_key(None, 'auth_group_permissions', 'auth_permission', ['permission_id'], ['id'])
    op.create_foreign_key(None, 'auth_group_permissions', 'auth_group', ['group_id'], ['id'])
    op.drop_column('auth_group_permissions', 'id')
    op.alter_column('auth_permission', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    op.drop_constraint('auth_permission_content_type_id_codename_01ab375a_uniq', 'auth_permission', type_='unique')
    op.create_index(op.f('ix_auth_permission_id'), 'auth_permission', ['id'], unique=False)
    op.create_unique_constraint(None, 'auth_permission', ['name'])
    op.drop_constraint('auth_permission_content_type_id_2f476e4b_fk_django_co', 'auth_permission', type_='foreignkey')
    op.drop_column('auth_permission', 'content_type_id')
    op.drop_column('auth_permission', 'codename')
    op.alter_column('auth_user', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.drop_index('auth_user_username_6821ab7c_like', table_name='auth_user')
    op.create_index(op.f('ix_auth_user_id'), 'auth_user', ['id'], unique=False)
    op.create_unique_constraint(None, 'auth_user', ['email'])
    op.drop_column('auth_user', 'is_superuser')
    op.drop_column('auth_user', 'first_name')
    op.drop_column('auth_user', 'last_login')
    op.drop_column('auth_user', 'last_name')
    op.drop_column('auth_user', 'is_staff')
    op.drop_column('auth_user', 'is_active')
    op.drop_column('auth_user', 'password')
    op.drop_column('auth_user', 'date_joined')
    op.drop_index('auth_user_groups_group_id_97559544', table_name='auth_user_groups')
    op.drop_index('auth_user_groups_user_id_6a12ed8b', table_name='auth_user_groups')
    op.drop_constraint('auth_user_groups_user_id_group_id_94350c0c_uniq', 'auth_user_groups', type_='unique')
    op.drop_constraint('auth_user_groups_group_id_97559544_fk_auth_group_id', 'auth_user_groups', type_='foreignkey')
    op.drop_constraint('auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', 'auth_user_groups', type_='foreignkey')
    op.create_foreign_key(None, 'auth_user_groups', 'auth_group', ['group_id'], ['id'])
    op.create_foreign_key(None, 'auth_user_groups', 'auth_user', ['user_id'], ['id'])
    op.drop_column('auth_user_groups', 'id')
    op.create_index(op.f('ix_books_author_id'), 'books_author', ['id'], unique=False)
    op.drop_column('books_author', 'death_year')
    op.drop_column('books_author', 'birth_year')
    op.alter_column('books_book', 'title',
               existing_type=sa.VARCHAR(length=1024),
               nullable=False)
    op.drop_constraint('books_book_gutenberg_id_key', 'books_book', type_='unique')
    op.create_index(op.f('ix_books_book_id'), 'books_book', ['id'], unique=False)
    op.drop_column('books_book', 'gutenberg_id')
    op.drop_column('books_book', 'media_type')
    op.drop_column('books_book', 'download_count')
    op.drop_index('books_book_authors_0a4572cc', table_name='books_book_authors')
    op.drop_index('books_book_authors_4f331e2f', table_name='books_book_authors')
    op.drop_constraint('books_book_authors_book_id_8714badb_uniq', 'books_book_authors', type_='unique')
    op.drop_constraint('books_book_authors_book_id_ed3433e7_fk_books_book_id', 'books_book_authors', type_='foreignkey')
    op.drop_constraint('books_book_authors_author_id_984f1ab8_fk_books_author_id', 'books_book_authors', type_='foreignkey')
    op.create_foreign_key(None, 'books_book_authors', 'books_author', ['author_id'], ['id'])
    op.create_foreign_key(None, 'books_book_authors', 'books_book', ['book_id'], ['id'])
    op.drop_column('books_book_authors', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books_book_authors', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'books_book_authors', type_='foreignkey')
    op.drop_constraint(None, 'books_book_authors', type_='foreignkey')
    op.create_foreign_key('books_book_authors_author_id_984f1ab8_fk_books_author_id', 'books_book_authors', 'books_author', ['author_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_foreign_key('books_book_authors_book_id_ed3433e7_fk_books_book_id', 'books_book_authors', 'books_book', ['book_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_unique_constraint('books_book_authors_book_id_8714badb_uniq', 'books_book_authors', ['book_id', 'author_id'])
    op.create_index('books_book_authors_4f331e2f', 'books_book_authors', ['author_id'], unique=False)
    op.create_index('books_book_authors_0a4572cc', 'books_book_authors', ['book_id'], unique=False)
    op.add_column('books_book', sa.Column('download_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('books_book', sa.Column('media_type', sa.VARCHAR(length=16), autoincrement=False, nullable=False))
    op.add_column('books_book', sa.Column('gutenberg_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_books_book_id'), table_name='books_book')
    op.create_unique_constraint('books_book_gutenberg_id_key', 'books_book', ['gutenberg_id'])
    op.alter_column('books_book', 'title',
               existing_type=sa.VARCHAR(length=1024),
               nullable=True)
    op.add_column('books_author', sa.Column('birth_year', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('books_author', sa.Column('death_year', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_books_author_id'), table_name='books_author')
    op.add_column('auth_user_groups', sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'auth_user_groups', type_='foreignkey')
    op.drop_constraint(None, 'auth_user_groups', type_='foreignkey')
    op.create_foreign_key('auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', 'auth_user_groups', 'auth_user', ['user_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_foreign_key('auth_user_groups_group_id_97559544_fk_auth_group_id', 'auth_user_groups', 'auth_group', ['group_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_unique_constraint('auth_user_groups_user_id_group_id_94350c0c_uniq', 'auth_user_groups', ['user_id', 'group_id'])
    op.create_index('auth_user_groups_user_id_6a12ed8b', 'auth_user_groups', ['user_id'], unique=False)
    op.create_index('auth_user_groups_group_id_97559544', 'auth_user_groups', ['group_id'], unique=False)
    op.add_column('auth_user', sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False))
    op.add_column('auth_user', sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.add_column('auth_user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('auth_user', sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('auth_user', sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.add_column('auth_user', sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('auth_user', sa.Column('first_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.add_column('auth_user', sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'auth_user', type_='unique')
    op.drop_index(op.f('ix_auth_user_id'), table_name='auth_user')
    op.create_index('auth_user_username_6821ab7c_like', 'auth_user', ['username'], unique=False)
    op.alter_column('auth_user', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.add_column('auth_permission', sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('auth_permission', sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('auth_permission_content_type_id_2f476e4b_fk_django_co', 'auth_permission', 'django_content_type', ['content_type_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.drop_constraint(None, 'auth_permission', type_='unique')
    op.drop_index(op.f('ix_auth_permission_id'), table_name='auth_permission')
    op.create_unique_constraint('auth_permission_content_type_id_codename_01ab375a_uniq', 'auth_permission', ['content_type_id', 'codename'])
    op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    op.alter_column('auth_permission', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.add_column('auth_group_permissions', sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'auth_group_permissions', type_='foreignkey')
    op.drop_constraint(None, 'auth_group_permissions', type_='foreignkey')
    op.create_foreign_key('auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', 'auth_group_permissions', 'auth_group', ['group_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_foreign_key('auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', 'auth_group_permissions', 'auth_permission', ['permission_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_unique_constraint('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'auth_group_permissions', ['group_id', 'permission_id'])
    op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    op.drop_index(op.f('ix_auth_group_id'), table_name='auth_group')
    op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    op.alter_column('auth_group', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    op.create_table('books_book_subjects',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books_book.id'], name='books_book_subjects_book_id_a578cff2_fk_books_book_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['books_subject.id'], name='books_book_subjects_subject_id_7445958f_fk_books_subject_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='books_book_subjects_pkey'),
    sa.UniqueConstraint('book_id', 'subject_id', name='books_book_subjects_book_id_74dcf64a_uniq')
    )
    op.create_index('books_book_subjects_ffaba1d1', 'books_book_subjects', ['subject_id'], unique=False)
    op.create_index('books_book_subjects_0a4572cc', 'books_book_subjects', ['book_id'], unique=False)
    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    )
    op.create_index('auth_user_user_permissions_user_id_a95ead1b', 'auth_user_user_permissions', ['user_id'], unique=False)
    op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', 'auth_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('books_bookshelf',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('books_bookshelf_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='books_bookshelf_pkey'),
    sa.UniqueConstraint('name', name='books_bookshelf_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('books_bookshelf_name_2642cad6_like', 'books_bookshelf', ['name'], unique=False)
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('books_subject',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='books_subject_pkey')
    )
    op.create_table('books_language',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('books_language_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('code', sa.VARCHAR(length=4), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='books_language_pkey'),
    sa.UniqueConstraint('code', name='books_language_code_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('books_language_code_217c406c_like', 'books_language', ['code'], unique=False)
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('books_format',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mime_type', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books_book.id'], name='books_format_book_id_b948fa34_fk_books_book_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='books_format_pkey')
    )
    op.create_index('books_format_0a4572cc', 'books_format', ['book_id'], unique=False)
    op.create_table('books_book_languages',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('language_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books_book.id'], name='books_book_languages_book_id_e833b1f4_fk_books_book_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['language_id'], ['books_language.id'], name='books_book_languages_language_id_e9f60572_fk_books_language_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='books_book_languages_pkey'),
    sa.UniqueConstraint('book_id', 'language_id', name='books_book_languages_book_id_554fdccb_uniq')
    )
    op.create_index('books_book_languages_468679bd', 'books_book_languages', ['language_id'], unique=False)
    op.create_index('books_book_languages_0a4572cc', 'books_book_languages', ['book_id'], unique=False)
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('books_book_bookshelves',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bookshelf_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books_book.id'], name='books_book_bookshelves_book_id_f820ff72_fk_books_book_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['bookshelf_id'], ['books_bookshelf.id'], name='books_book_bookshel_bookshelf_id_80cc77c5_fk_books_bookshelf_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='books_book_bookshelves_pkey'),
    sa.UniqueConstraint('book_id', 'bookshelf_id', name='books_book_bookshelves_book_id_6016a70a_uniq')
    )
    op.create_index('books_book_bookshelves_40928700', 'books_book_bookshelves', ['bookshelf_id'], unique=False)
    op.create_index('books_book_bookshelves_0a4572cc', 'books_book_bookshelves', ['book_id'], unique=False)
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    # ### end Alembic commands ###
