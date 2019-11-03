import mongoengine
import datetime
#from data.user import User


class Split(mongoengine.Document):
    split_id = mongoengine.ObjectIdField()
#   participant = mongoengine.ReferenceField(User)
    name = mongoengine.StringField(required = True)
    description = mongoengine.StringField(required = True)
    state = mongoengine.IntField(default = 0)
    price_cents = mongoengine.IntField(required = True)
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)


    meta = {
        'db_alias': 'core',
        'collection': 'splits'
}