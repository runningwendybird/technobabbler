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
	author_id = Column(Integer, ForeignKey("authors.id"))
	topic_id = Column(Integer, ForeignKey("topics.id"))

	def __repr__(self):
		return "Title: %s" % self.topic_name

class Words(Base):

	__tablename__ = "words"

	id = Column(Integer, primary_key = True)
	word = Column(String(200), nullable = False)
	source_id = Column(Integer)

	def __repr__(self):
		return " word: %s" % self.word

class Linked_words(Base):

	__tablename__ = "linked_words"

	id = Column(Integer, primary_key = True)
	word1_id = Column(Integer, ForeignKey("words.id"))
	word2_id = Column(Integer, ForeignKey("words.id"))

	
	def __repr__(self):
		return "Word 1 ID: %d , Word 2 ID: %d" % (self.word1_id, self.word2_id)

class Next_words(Base):
	id = Column(Integer, primary_key = True)
	linked_word_id = Column(Integer, ForeignKey("linked_words.id"))
	word_id = Column(Integer, ForeignKey("words.id"))

	def __repr__(self):
		return "Next Word ID: %d" % self.word_id


# End of Classes


# Functions

def create_db():
	"""Recreates the database."""

	Base.metadata.create_all(ENGINE)


def find_author_by_name(first, last):

	author = sqla_session.query(Author).filter(author.first == first.lower() and author.last == last.lower()).all()
	return author



