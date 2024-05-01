class Gis_Router:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'land_app':
            return 'third_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'land_app':
            return 'third_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if at least one of the models is in 'yourapp'
        if obj1._meta.app_label == 'land_app' or obj2._meta.app_label == 'land_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(f'Allowing migration for {app_label} on {db}')  # add this line
        if app_label == 'land_app':
            return db == 'third_db'
        else:
            return None
