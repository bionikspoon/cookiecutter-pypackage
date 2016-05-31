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

- pytest_!  Uses ``pytest`` with a ``setup.py`` test command. See: ``python setup.py test`` and ``make test``
- git-flow_ friendly!  Subtle changes to improve git-flow workflow.
- coveralls_! Preconfigured integration with coveralls--coverage report monitoring.
- pip-tools_! Uses pip-tools for managing dependendencies.  See: ``make requirements``.
- Better requirements management. Project and dev requirements are seperated, and pip-tools_ makes it easier to update and pin requirements.
- PyPy_! Preconfigured to include PyPy.  This is usually free accessibility! Try it out! See if PyPy passes your tests.
- Better Tox_ + Travis-CI_ setup.
  Philosophy: Tox_ should do the maximum amount of work, and Travis-CI_ the minimum.  This creates a more consistent results when testing locally vs remotely on Travis-CI_.
- Inludes ``_compat`` module and ``logging`` boilerplate.

Massive overhaul to docs
~~~~~~~~~~~~~~~~~~~~~~~~

- Github readme is automatically generated from compiling doc sources, **reasoning:**

  1. Sphinx specific RST doesn't render on github (ugly) and outright breaks PyPI_.  For example, if you use Sphinx' python domain references, it looks like this: :class:`MyAwesomeClass` or :py:class:`MyAwesomeClass` instead of ``MyAwesomeClass``
  2. Usually you want to include extra sections on the github README.  For example, I like to include installation instructions and a quick start guide. But I also like how things look on ReadTheDocs_, and don't want to mess that up.  The answer is they need to be combined using a different process.  This fork delivers a DRY and intuitive process to have both.

  See: ``make github`` and ``docs/github_docs.py``.  I wrote a minimalistic, text processing framework--it should be intuitive to extend and customize for your needs.

- Doc sources follow the nested format, adding clarity.
- Includes a doc linter to avoid PyPI_'s RST parser from breaking.
- A million times more badges, badges for everything! You get a badge, you get badge, and YOU get badge!!


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
- Auto-release to PyPI_ when you push a new tag to master (optional)



Quickstart
----------

Generate a Python package project::

    cookiecutter https://github.com/bionikspoon/cookiecutter-pypackage

Then:

- Create a repo and put it there.
- Add the repo to your Travis CI account.
- Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
- Run the script `travis_pypi_setup.py` to encrypt your PyPI_ password in Travis config
  and activate automated deployment on PyPI_ when you push a new tag to master branch.
- Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
- Release your package by pushing a new tag to master.
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


.. _PyPI: https://pypi.python.org/pypi
.. _PyPy: https://pypy.org/
.. _Travis-CI: https://travis-ci.org/
.. _Tox: https://testrun.org/tox/
.. _Sphinx: https://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
