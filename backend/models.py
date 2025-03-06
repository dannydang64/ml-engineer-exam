from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class TextChunk(Base):
    """Stores text chunks extracted from uploaded PDFs."""
    __tablename__ = "text_chunks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    is_annotated = Column(Boolean, default=False)
    annotation_json = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class MolecularTarget(Base):
    """Stores molecular targets extracted by NLP."""
    __tablename__ = "molecular_targets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    my = Column(Float, nullable=False)  # Membership Degree
    mn = Column(Float, nullable=False)  # Non-Membership Degree
    hesitancy = Column(Float, nullable=False)  # Hesitancy
    confidence = Column(Float, nullable=False)  # NLP confidence score
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Therapy(Base):
    """Stores extracted therapy entities."""
    __tablename__ = "therapies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    my = Column(Float, nullable=False)
    mn = Column(Float, nullable=False)
    hesitancy = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
