from sqlalchemy import Column, Integer, String, Text
from .database import Base


class GroundsForUnpublishing(Base):
    __tablename__ = "grounds"
    id = Column(Integer, primary_key=True, index=True)
    reason = Column(String, nullable=False)
    description = Column(Text, nullable=False)
