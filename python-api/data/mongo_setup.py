import mongoengine


def global_init(secrets):
    mongoengine.connect(db=secrets["db"], username=secrets["username"], password=secrets["password"], host=secrets["host"], name="boxsplit")
    #mongoengine.connect(db=secrets["db"], name='boxsplitdb')