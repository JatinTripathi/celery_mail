
from sqlalchemy.dialects.postgresql import JSON

from goals import db


class LifeGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    end_date = db.Column(db.DateTime)
    brief_description = db.Column(db.Text)
    rest_description = db.Column(db.Text)
    completed = db.Column(default=False)

    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, name, brief_description, rest_description,
                 end_date, completed=False):
        self.name = name
        self.brief_description = brief_description
        self.rest_description = rest_description

    def __repr__(self):
        return '<Goal %r>' % self.title