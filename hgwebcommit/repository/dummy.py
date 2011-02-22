from hgwebcommit.repository.base import BaseRepository

class DummyRepository(BaseRepository):
    def get_name(self):
        return 'dummy'

    def get_path(self):
        return '/path/to/dummy'

    def parent_date(self):
        return '2020-02-01 10:00:00 +0900'

    def parent_revision(self):
        return 'abcd1234'

    def parent_number(self):
        return 12345

    def branch(self):
        return 'dummy_branch'

    def status_modified(self):
        return [
            'modified.txt',
        ]

    def status_added(self):
        return [
            'added.txt',
        ]

    def status_removed(self):
        return [
            'removed.txt',
        ]

    def status_deleted(self):
        return [
            'deleted.txt',
        ]

    def status_unknown(self):
        return [
            'unknown.txt',
        ]

    def add(self, files):
        pass

    def commit(self, files, commit_message):
        pass

    def revert(self, files, no_backup=True):
        pass

    def remove(self, files):
        pass
