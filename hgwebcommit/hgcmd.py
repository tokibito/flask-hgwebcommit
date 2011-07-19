# mercurial command extension

DEFAULT_CONFIG = {
    'SECRET_KEY': '(secret key)',
    'HGWEBCOMMIT_ENCODING': 'utf-8',
    'HGWEBCOMMIT_ALLOW_COMMIT': True,
    'HGWEBCOMMIT_ACTIONS': (),
}

def webcommit(ui, repo, **opts):
    """start hgwebcommit webserver"""
    from hgwebcommit import app
    app.config.update(DEFAULT_CONFIG)
    app.config['HGWEBCOMMIT_REPOSITORY'] = repo.root
    app.run(host=opts['address'], port=opts['port'])

cmdtable = {
    "^webcommit|wc": (webcommit,
                     [('p', 'port', 5000, 'port number'),
                      ('a', 'address', '127.0.0.1', 'bind address')],
                     "[options]")
}
