

## python -m hgwebcommit.main /path/to/repository/
if __name__ == '__main__':
    from hgwebcommit import app
    import os
    import sys
    import random
    if len(sys.argv) < 2:
        sys.stdout.write('python -m hgwebcommit directory\n')
        sys.exit()
    repository_path = os.path.abspath(sys.argv[1])

    app.config.update(
        DEBUG=True,
        SECRET_KEY=''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$&():;') for i in range(30)]),
        HGWEBCOMMIT_REPOSITORY=repository_path,
        HGWEBCOMMIT_ENCODING='utf-8',
        HGWEBCOMMIT_ALLOW_COMMIT=True,
        HGWEBCOMMIT_ACTIONS=[],
    )
    app.run(host='127.0.0.1')
