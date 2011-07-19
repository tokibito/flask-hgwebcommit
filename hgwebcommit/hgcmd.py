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

    port = 5000
    if opts['port']:
        try:
            port = int(opts['port'])
        except ValueError:
            pass

    host = opts['host'] or '0.0.0.0'

    app.run(host=host, port=port)

cmdtable = {
    "^webcommit|wc": (webcommit,
                     [('p', 'port', None, 'port number'),
                      ('h', 'host', None, 'bind host')],
                     "[options] REV")
}
