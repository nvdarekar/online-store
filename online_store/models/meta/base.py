from app import db


class Base:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def _asdict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
