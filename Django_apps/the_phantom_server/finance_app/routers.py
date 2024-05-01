class FinanceRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'finance_app':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'finance_app':
            return 'secondary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Optional: Define if relations between objects are allowed
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'finance_app':
            return db == 'secondary'
        return None  #None
