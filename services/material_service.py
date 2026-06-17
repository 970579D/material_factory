from repositories.material_repository import MaterialRepository

repo = MaterialRepository()

class MaterialService:

    def get_all(self, db):
        return repo.get_all(db)

    def get_by_id(self, db, material_id: int):
        return repo.get_by_id(db, material_id)

    # def create(self, db, data):
    #     return repo.create(db, data)
    
    def create_list(self, db, materials):
        return repo.create_list(db, materials)