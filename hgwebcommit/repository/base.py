class BaseRepository(object):
    def __init__(self, **kwargs):
        pass

    def get_name(self):
        raise NotImplementedError

    @property
    def name(self):
        return self.get_name()

    def get_path(self):
        raise NotImplementedError

    @property
    def path(self):
        return self.get_path()

    def parent_date(self):
        raise NotImplementedError

    def parent_revision(self):
        raise NotImplementedError

    def parent_number(self):
        raise NotImplementedError

    def branch(self):
        raise NotImplementedError

    def status_modified(self):
        raise NotImplementedError

    def status_added(self):
        raise NotImplementedError

    def status_removed(self):
        raise NotImplementedError

    def status_deleted(self):
        raise NotImplementedError

    def status_unknown(self):
        raise NotImplementedError

    def add(self, files):
        raise NotImplementedError

    def commit(self, files, commit_message):
        raise NotImplementedError

    def revert(self, files, no_backup=True):
        raise NotImplementedError

    def remove(self, files):
        raise NotImplementedError
