def gethostname():
    import socket
    return socket.gethostname()

def exec_command(command):
    from subprocess import Popen, PIPE
    p = Popen(command, stdout=PIPE)
    return p.stdout.read()

def get_repo():
    from hgwebcommit import app
    from hgwebcommit.repository import get_repository
    return get_repository(path=app.config['HGWEBCOMMIT_REPOSITORY'], encoding=app.config['HGWEBCOMMIT_ENCODING'])

def operation_repo(repo, operation, files, commit_message=None):
    from flaskext.babel import gettext as _
    from hgwebcommit import app
    if operation == 'commit':
        # commit
        repo.commit(files, commit_message)
        app.logger.info('commit - %s [%s]' % (commit_message, ', '.join(files)))
        return _('commited.')
    elif operation == 'revert':
        # revert
        repo.revert(files)
        app.logger.info('reverted - [%s]' % ', '.join(files))
        return _('reverted.')
    elif operation == 'remove':
        # remove
        repo.remove(files)
        app.logger.info('removed - [%s]' % ', '.join(files))
        return _('removed.')
    else:
        from flask import abort
        abort(400)
