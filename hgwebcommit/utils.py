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
