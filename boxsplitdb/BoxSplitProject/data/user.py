import mongoengine
import datetime
from data.box import Box
from data.split import Split


class User(mongoengine.Document):
	user_id = mongoengine.ObjectIdField()
	name = mongoengine.StringField(required = True)
	email = mongoengine.StringField(required = True)
	creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)

	boxes = mongoengine.ListField(mongoengine.ReferenceField(Box))
	splits = mongoengine.ListField(mongoengine.ReferenceField(Split))

	# social media stuff

	meta = {
		'db_alias': 'core',
		'collection': 'users'
	}
