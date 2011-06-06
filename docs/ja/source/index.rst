hgwebcommit ドキュメント
========================

hgwebcommit とは？
------------------

hgwebcommitはWebブラウザからmercurialリポジトリの操作するためのソフトウェアです。

FTPやSCPなどでファイルをサーバにアップロードしてコミットする際に、sshなどを使わなくてもブラウザ画面からコミットできます。

ソースリポジトリ
----------------

http://bitbucket.org/tokibito/flask-hgwebcommit

必要なライブラリのインストール
------------------------------

``requirements.txt`` がpip用のファイルです。

::

  $ sudo pip install -r requirements.txt

使い方
------

1. ソースリポジトリからcloneし、 ``main.py`` 設定ファイルを同じディレクトリに別名でコピーします。(ここでは ``myrepo.py`` とします)
2. ``myrepo.py`` の ``HGWEBCOMMIT_REPOSITORY`` にリポジトリのフルパスを設定します。
3. ``myrepo.py`` を実行するとHTTPサーバが起動します。

  ::

    $ python myrepo.py
     * Running on http://0.0.0.0:5000/
     * Restarting with reloader...

4. ブラウザで http://127.0.0.1:5000/ にアクセスします。

  .. image:: static/images/home.png

  正常に動作していれば、リポジトリの状態が表示されます。

設定ファイルの設定項目
----------------------

HGWEBCOMMIT_REPOSITORY
~~~~~~~~~~~~~~~~~~~~~~

操作対象のリポジトリのフルパスを指定します。

HGWEBCOMMIT_ENCODING
~~~~~~~~~~~~~~~~~~~~

コミットメッセージのエンコーディングを指定します。

HGWEBCOMMIT_ALLOW_COMMIT
~~~~~~~~~~~~~~~~~~~~~~~~

コミット操作の可否を指定します。デフォルトでは ``True`` です。

HGWEBCOMMIT_ACTIONS
~~~~~~~~~~~~~~~~~~~

サイドバーに表示するアクションを指定します。

アクション
----------

設定ファイルの ``HGWEBCOMMIT_ACTIONS`` にアクションを設定することで、hgwebcommitに機能を追加することができます。

追加したアクションはサイドバーに表示され、コンボボックスで選択して実行できます。

アクションの記述はシンプルです。helloアクションの内容を以下に示します。

.. code-block:: python

    from flask import flash
    from flaskext.babel import gettext, lazy_gettext

    from hgwebcommit.actions.decorators import action

    @action('hello', lazy_gettext('Hello'))
    def hello():
        flash(gettext('Hello!'))

このアクションを使うように設定ファイルを記述すると、コンボボックスには「こんにちは」と表示されます。

アクションを実行すると、フラッシュメッセージで「こんにちは！」と表示されます。

.. note::

  この例ではflask-babelを使用して国際化(i18n)を行っていますが、アクションを自作する場合、国際化が必ず必要というわけではありません。

権限
----

ファイルシステム上のリポジトリへ変更を行うため、hgwebcommitのサーバを実行するユーザでコミット操作が行われます。

