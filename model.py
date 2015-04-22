from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

ENGINE = create_engine("sqlite:///technobabble.db", echo=False)
sqla_session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = sqla_session.query_property()


#
# Classes
#

class Topic(Base):

	__tablename__ = "topics"

	id = Column(Integer, primary_key = True)
	topic_name = Column(String(64), unique = True, nullable = False)

	source_texts = relationship("Source_texts", backref=backref("topics"))
	

	def __repr__(self):
		return "Topic: %s" % self.topic_name

class Author(Base):

	__tablename__ = "authors"

	id = Column(Integer, primary_key = True)
	first = Column(String(64))
	last = Column(String(64), nullable = False)

	texts = relationship("Source_texts", backref("author"))

	def __repr__(self):
		return "%s %s" % (self.first.capitalize(), self.last.capitalize())

class Source_texts(Base):

	__tablename__ = "source_texts"
	id = Column(Integer, primary_key = True)
	title = Column(String(200), unique = True, nullable = False)
	author = Column(String(200))
	topic_id = Column(Integer, ForeignKey("topics.id"))

	def __repr__(self):
		return "Title: %s, By: " % self.topic_name

class Words(Base):

	__tablename__ = "words"
