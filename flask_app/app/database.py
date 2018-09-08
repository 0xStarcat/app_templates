class DbMixin(object):
    def __init__(self, *initial_data, **kwargs):
        pass

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.__dict__)
