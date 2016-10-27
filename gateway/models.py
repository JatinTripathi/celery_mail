
# from sqlalchemy.dialects.postgresql import JSON

from gateway import db


class Mails(db.Model):
    __tablename__ = 'mails'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100))
    sent_date = db.Column(db.DateTime)
    to = db.Column(db.Text)
    brief_description = db.Column(db.Text)
    rest_description = db.Column(db.Text)

    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, sub, brief_body, 
                rest_body, sent_date, to):
        self.subject = subject
        self.sent_date = sent_date
        self.to = to
        self.brief_body = brief_body
        self.rest_body = rest_body

    def __repr__(self):
        return '<Mail %r>' % self.subject