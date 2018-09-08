from app.database import DbMixin


class User(DbMixin):
    __tablename__ = 'users'
