{
    'name': 'Advanced E-commerce Theme',
    'version': '16.0.1.0.0',
    'category': 'Theme/E-commerce',
    'summary': 'Advanced fully featured and functional industrial level modern and attractive e-commerce theme',
    'sequence': 1,
    'author': 'AI Developer',
    'website': 'https://www.yourwebsite.com',
    'description': """
Advanced E-commerce Theme
=========================
This module provides a fully featured and functional industrial level modern and attractive e-commerce theme for Odoo version 16 Community Edition.
""",
    'depends': ['website_sale', 'website_theme_install'],
    'data': [
        'views/theme_view.xml',
        'views/theme_templates.xml',
        'views/res_config_settings_views.xml',
        'data/theme_data.xml',
        'demo/theme_demo.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}