from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root@localhost/material_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# CREATE TABLE `materials` (
#   `id` int NOT NULL AUTO_INCREMENT,
#   `name` varchar(100) NOT NULL,
#   `quantity` int NOT NULL,
#   `location` varchar(100) NOT NULL,
#   PRIMARY KEY (`id`)
# );