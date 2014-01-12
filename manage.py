from flask.ext.script import Manager
from flask.ext.assets import ManageAssets
from app import app, assets, db

from peewee import *
from app.models.Frame import Frame, populate_frames_dummy_data
from app.models.Speech import Speech
from app.models.Topic import Topic
from app.models.SpeechTopic import SpeechTopic
from app.models.User import User

manager = Manager(app)

manager.add_command("assets", ManageAssets(assets))

@manager.command
def hello():
    print "hello"

@manager.command
def createdb():
	Frame.create_table(fail_silently=True)
	Speech.create_table(fail_silently=True)
	Topic.create_table(fail_silently=True)
	SpeechTopic.create_table(fail_silently=True)
	User.create_table(fail_silently=True)
	db.database.execute_sql("ALTER TABLE speech_topic ADD CONSTRAINT speech_topic_unique UNIQUE(speech_id,topic_id);")
	populate_frames_dummy_data()

@manager.command
def deletedb():
	db.database.execute_sql("DROP TABLE frames, speeches, topics, speech_topic, users;")

if __name__ == "__main__":
    manager.run()


### SEEEEEEED DATA
# import os 

# #Delete the database
# try:
# 	os.remove('database.db')
# 	print "Database Deleted"
# except:
# 	pass

# #Create new DB
# execfile('createdb.py')
# print "new database created"

# #Populate Frames
# from app.models.Frame import populate_frames_dummy_data
# populate_frames_dummy_data()

# #Populate Speeches
# from app.database_views import download_speeches_for_topic
# download_speeches_for_topic('gay')
# download_speeches_for_topic('tomato')
# download_speeches_for_topic('potato')
