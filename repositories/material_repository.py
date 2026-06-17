from models.material import Material

class MaterialRepository:

    def get_all(self, db):
        return db.query(Material).all()

    def get_by_id(self, db, material_id: int):
        return (
            db.query(Material)
            .filter(Material.id == material_id)
            .first()
        )

    # def create(self, db, data):
    #     material = Material(**data.dict())
    #     db.add(material)
    #     db.commit()
    #     db.refresh(material)
    #     return material
    
    def create_list(self, db, materials):
        rows = [Material(**m.dict()) for m in materials]

        db.add_all(rows)
        db.commit()


        # return None
        for row in rows:
            db.refresh(row)
        return rows