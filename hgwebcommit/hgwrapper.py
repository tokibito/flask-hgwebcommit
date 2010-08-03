import os

from mercurial import cmdutil
from mercurial import commands
from mercurial.util import datestr
from mercurial.hg import repository
from mercurial.ui import ui
from mercurial.match import match
from mercurial.node import short

class MercurialWrapper(object):
    def __init__(self, path, encoding='utf-8'):
        self.path = os.path.normpath(path)
        self.ui = ui()
        self.ui.readconfig(os.path.join(self.path, '.hg', 'hgrc'))
        self.repository = repository(self.ui, self.path)
        self.encoding = encoding

    @property
    def name(self):
        return os.path.basename(self.path)

    @property
    def parent_node(self):
        return self.repository['']

    def parent_date(self):
        return datestr(self.parent_node.date())

    def parent_branch(self):
        return self.parent_node.branch()

    def parent_revision(self):
        return short(self.parent_node.node())

    def parent_number(self):
        return self.parent_node.rev()

    def branch(self):
        return self.repository[None].branch()

    def status_modified(self):
        return self.repository.status()[0]

    def status_added(self):
        return self.repository.status()[1]

    def status_removed(self):
        return self.repository.status()[2]

    def status_deleted(self):
        return self.repository.status()[3]

    def status_unknown(self):
        return self.repository.status(unknown=True)[4]

    def add(self, files):
        self.repository[None].add(files)

    def commit(self, files, commit_message):
        self.repository.commit(
            text=commit_message.encode(self.encoding),
            match=match(self.repository.root, self.repository.root, None, include=files)
        )

    def revert(self, files, no_backup=True):
        opts = {
          'no_backup': no_backup,
          'date': '',
          'rev': '',
        }
        commands.revert(self.ui, self.repository, *[os.path.join(self.path, fn) for fn in files], **opts)

    def remove(self, files):
        self.repository[None].remove(files)
