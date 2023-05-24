# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'NCSA System Documentation'
copyright = '2023, University of Illinois'
author = 'Trustees of the University of Illinois'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# added to make the width parameters work
html_css_files = [
    'css/custom.css',
]

# added this section for logo-ing
html_static_path = ['_static']
#html_logo = 'logo.svg'
html_logo = 'NCSA_OrangeI_RGB.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
