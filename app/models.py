from sqlalchemy.ext.automap import automap_base
from .database import engine, metadata

# Automap Base
AutomapBase = automap_base(metadata=metadata)

# Reflect tables
AutomapBase.prepare(engine, reflect=True)

# Access mapped classes for existing tables
AuthUser = AutomapBase.classes.auth_user
AuthGroup = AutomapBase.classes.auth_group
AuthPermission = AutomapBase.classes.auth_permission
BooksSubject = AutomapBase.classes.books_subject
BooksBookSubjects = AutomapBase.classes.books_book_subjects
BooksBook = AutomapBase.classes.books_book
BooksAuthor = AutomapBase.classes.books_author
BooksBookshelf = AutomapBase.classes.books_bookshelf
BooksFormat = AutomapBase.classes.books_format
BooksLanguage = AutomapBase.classes.books_language
BooksSubject = AutomapBase.classes.books_subject
DjangoAdminLog = AutomapBase.classes.django_admin_log
DjangoContentType = AutomapBase.classes.django_content_type
DjangoMigrations = AutomapBase.classes.django_migrations
DjangoSession = AutomapBase.classes.django_session
