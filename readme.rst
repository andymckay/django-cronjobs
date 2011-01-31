django-cronjobs
------------------

Provides a @cron decorator to mark cronjob methods in your site and
a namespace for manage so they can be executed.

Installation
=================

1. Install from pypi::

    pip install cronjobs

2. Add 'cronjobs' to your INSTALLED_APPS in settings.py.

Usage
=================

Methods can be added to anywhere, but if you put them in a file called cron.py
inside an app, they will be automatically imported.

Register your method by decorating it with @register, for example::

    from cronjobs import register
    @register
    def some_function():
        pass

You can then run::

    manage.py cron some_function


License: BSD

Authors: Jeff Balogh then packaged and broken by Andy McKay
