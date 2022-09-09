from telegram.databases.sqlite import Category


class CategoryModel:

    @staticmethod
    def get_all(is_active=True):
        return Category.select().where(Category.is_active == is_active)

    @staticmethod
    def get(category_id):
        return Category.get(id=category_id)
