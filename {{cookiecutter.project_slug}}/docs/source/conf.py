#!/usr/bin/env python
# coding=utf-8
import sys
from os.path import abspath, relpath
import sphinx.environment


def _warn_node(func):
    def wrapper(self, msg, node, **kwargs):
        if msg.startswith('nonlocal image URI found:'):
            return

        return func(self, msg, node, **kwargs)

    return wrapper


sphinx.environment.BuildEnvironment.warn_node = _warn_node(sphinx.environment.BuildEnvironment.warn_node)

sys.path.insert(0, abspath(relpath('../', __file__)))

import {{ cookiecutter.project_slug }}

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.coverage', 'sphinx.ext.viewcode', ]

templates_path = ['_templates']

source_suffix = '.rst'

source_encoding = 'utf-8-sig'

master_doc = 'index'

# General information about the project.
project = '{{ cookiecutter.project_name }}'
copyright = '{{ cookiecutter.year }}, {{ cookiecutter.full_name }}'
author = {{ cookiecutter.project_slug }}.__author__
version = {{ cookiecutter.project_slug }}.__version__
release = {{ cookiecutter.project_slug }}.__version__

# language = None
# today = ''
# today_fmt = '%B %d, %Y'
exclude_patterns = ['build']
# default_role = None
# add_function_parentheses = True
# add_module_names = True
# show_authors = False
pygments_style = 'sphinx'
# modindex_common_prefix = []
# keep_warnings = False

viewcode_import = True
# -- Options for HTML output -------------------------------------------
html_theme = 'sphinx_rtd_theme'
# html_theme_options = {}
# html_theme_path = []
# html_title = None
# html_short_title = None
# html_logo = None
# html_favicon = None
html_static_path = ['_static']
# html_last_updated_fmt = '%b %d, %Y'
# html_use_smartypants = True
# html_sidebars = {}
# html_additional_pages = {}
# html_domain_indices = True
# html_use_index = True
# html_split_index = False
# html_show_sourcelink = True
# html_show_sphinx = True
# html_show_copyright = True
# html_use_opensearch = ''
# html_file_suffix = None
htmlhelp_basename = '{{ cookiecutter.project_slug }}doc'

# -- Options for LaTeX output ------------------------------------------

latex_elements = {}
# 'papersize': 'letterpaper',
# 'pointsize': '10pt',
# 'preamble': '',

latex_documents = [(
    'index',
    '{{ cookiecutter.project_slug }}.tex',
    '{{ cookiecutter.project_name }} Documentation',
    '{{ cookiecutter.full_name }}',
    'manual',
)]

# latex_logo = None
# latex_use_parts = False
# latex_show_pagerefs = False
# latex_show_urls = False
# latex_appendices = []
# latex_domain_indices = True

# -- Options for manual page output ------------------------------------

man_pages = [(
    'index',
    '{{ cookiecutter.project_slug }}',
    '{{ cookiecutter.project_name }} Documentation',
    ['{{ cookiecutter.full_name }}'],
    1
)]
# man_show_urls = False

# -- Options for Texinfo output ----------------------------------------

texinfo_documents = [(
    'index',
    '{{ cookiecutter.project_slug }}',
    '{{ cookiecutter.project_name }} Documentation',
    '{{ cookiecutter.full_name }}',
    '{{ cookiecutter.project_slug }}',
    'One line description of project.',
    'Miscellaneous'
)]

# texinfo_appendices = []
# texinfo_domain_indices = True
# texinfo_show_urls = 'footnote'
# texinfo_no_detailmenu = False
