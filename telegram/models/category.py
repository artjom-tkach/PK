from telegram.databases.sqlite import Category


class CategoryModel:

    @staticmethod
    async def get_parents(is_active=True):
        return Category.select().where(Category.parent.is_null(), Category.is_active == is_active)

    @staticmethod
    async def get_children(category_id, is_active=True):
        return Category.select().where(Category.parent == category_id, Category.is_active == is_active)

    @staticmethod
    async def get(category_id):
        return Category.get(id=category_id)
