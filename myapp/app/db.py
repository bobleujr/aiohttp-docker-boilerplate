
class BaseModel():
    class Meta:
        pass
        # database = database_proxy  # Use proxy for our DB.


def get_objects(app):
    return app['objects']


def get_database(app):
    return app['database']


def setup(app):
    pass
    # we setup our db here
