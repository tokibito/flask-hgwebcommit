from werkzeug import import_string

from hgwebcommit import app

def get_repository(repository_backend=None, **opt):
    """
    return repository instance.
    """
    if not repository_backend:
        repository_backend = app.config.get('HGWEBCOMMIT_REPOSITORY_BACKEND', 'hgwebcommit.repository.hg.MercurialRepository')

    names = repository_backend.split('.')
    module_name = '.'.join(names[:-1])
    class_name = names[-1]
    mod = import_string(module_name)
    return getattr(mod, class_name)(**opt)
