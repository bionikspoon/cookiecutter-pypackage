.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal::

    $ pip install {{ cookiecutter.project_slug }}

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository::

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball`_::

    $ curl  -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with::

    $ python setup.py install


.. _Github repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master

Uninstall
---------

::

    $ pip uninstall {{ cookiecutter.project_slug }}

