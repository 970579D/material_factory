from fastapi import FastAPI
from database import Base, engine
from controllers.material_controller import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

# CREATE TABLE materials (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     quantity INT NOT NULL,
#     location VARCHAR(100) NOT NULL
# );