======================
cookiecutter-pypackage
======================

.. image:: https://img.shields.io/travis/bionikspoon/cookiecutter-pypackage.svg
   :target: https://travis-ci.org/bionikspoon/cookiecutter-pypackage

Cookiecutter_ template for a Python package.

- GitHub repo: https://github.com/bionikspoon/cookiecutter-pypackage/

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Notable Deviations from Upstream
--------------------------------

- pytest_!  Uses ``pytest`` with a ``setup.py`` test command.
- git-flow_ friendly!  Subtle changes to improve git-flow workflow.
- coveralls_! Preconfigured integration with coveralls, coverage report monitoring.
- pip-tools_! Uses pip-tools for managing dependendencies.  See ``make requirements``.
- Better requirements management. Project and dev requirements are seperated, and pip tools makes it easier to update and pin requirements.
- PyPy_! Preconfigured to include PyPy.  This is usually free accessibility! It's easier to remove PyPy support then to add it. Try it out, see if PyPy passes your tests.
- Better Tox_ + Travis-CI_ config. Tox should do the maximum amount of work, and travis the minimum.  This creates a more consistent environment for testing locally and remotely on Travis.
- Inludes ``_compat`` module and logging boilerplate.



..

- **Massive overhaul to docs.**

  - Github readme is auto generated from compiling doc sources, reasoning:

    1. Sphinx specific RST doesn't render on github (ugly) and outright breaks PyPI.  For example, if you use Sphinx' python domain references, it looks like this: :class:`MyAwesomeClass` or :py:class:`MyAwesomeClass` instead of ``MyAwesomeClass``
    2. Usually you want to include extra sections on the github README, like installation instructions and a quick start guide, but don't want to mess up the output on ReadTheDocs.  DRY demands a single source, this fork delivers.

    See ``make github`` and ``docs/github_docs.py``.  I wrote a minimalistic, text processing framework--it should be intuitive to extend and customize for your needs.

  - Doc sources follow the nested format, adding clarity.
  - Includes a doc linter to avoid PyPI's rst parser from breaking.
  - A million times more badges.  Badges for everything! You get a badge, you get badge, and YOU get badge!!


.. _pytest: http://pytest.org/latest/
.. _git-flow: https://github.com/nvie/gitflow
.. _coveralls: https://coveralls.io/
.. _pip-tools: https://github.com/nvie/pip-tools

Features
--------

- Open source MIT license
- Travis-CI_: Ready for Travis Continuous Integration testing
- Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4, 3.5, and PyPy_
- Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
- Bumpversion: Pre-configured version bumping with a single command
- Auto-release to PyPI when you push a new tag to master (optional)

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _PyPy: http://pypy.org/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/


Quickstart
----------

Generate a Python package project::

    cookiecutter https://github.com/bionikspoon/cookiecutter-pypackage

Then:

- Create a repo and put it there.
- Add the repo to your Travis CI account.
- Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
- Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
- Release your package the standard Python way. Here's a release checklist:
  https://gist.github.com/audreyr/5990987
- (Optional) If you feel like pinning the requirements for your package, you can
  add a `requirements.txt` that specifies packages and version numbers.

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: http://cookiecutter-pypackage.readthedocs.org/en/latest/tutorial.html

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

- `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions.
  See ``README.rst`` or the `github comparison view`_ for exhaustive list of
  additions and modifications.

- `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements files rather than a requirements list in the ``setup.py`` file.

- Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members


Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

- Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

- It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.
