from sqlalchemy.orm import  Session
from . import models, schemas


def get_courses(db: Session):
    return db.query(models.Course).all()


def create_Course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


