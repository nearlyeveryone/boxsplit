import mongoengine

def global_init(secrets):
	mongoengine.connect(db=secrets.db, username='admin', password='yeetersqweeter', host='mongodb://boxsplit.nearlyevery.one')