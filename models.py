from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, Table, MetaData
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from static.data import for_beginner_columns, for_advanced, step_course_beginner, step_course_advance



engine = create_engine('sqlite:///RifatDataBase.db')
metadata = MetaData()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tg_id = Column(Integer)
    tg_full_name = Column(String)
    tg_username = Column(String)
    results = relationship("Result", back_populates="student")


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship("Student", back_populates="results")
    course_id = Column(Integer)
    score = Column(Float)
    update_date = Column(Date)
    
class StepNameForBeginners(Base):
    __tablename__ = 'stepnamebeginner'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class StepNameForAdvances(Base):
    __tablename__ = 'stepnameadvances'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Stepname(Base):
    __tablename__ = 'stepname'
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer)
    lesson_name = Column(String)  


Base.metadata.create_all(engine)


python_for_beginner = Table('for_beginner', metadata,
              Column('student_id', Integer, primary_key=True),
              Column('update_date', Date),
              *[Column(name, Date) for name in for_beginner_columns])


python_for_advanced = Table('for_advanc', metadata,                                            
              Column('student_id', Integer, primary_key=True),
              Column('update_date', Date),
              *[Column(name, Date) for name in for_advanced])



metadata.create_all(engine)
