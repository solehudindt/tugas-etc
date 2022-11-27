# -*- coding: utf-8 -*-
{
    'name': "tb cahaya",
    'summary': "Point of sale tb cahaya bulakan",
    'description': """Long description""",
    'author': "Solehudindt",
    'website': "http://www.example.com",
    'category': 'Point of Sale',
    'version': '14.0.1',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_assets.xml',
        'views/gratis_antar.xml'
    ],
    'qweb': [
        'static/src/xml/pos_demo.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}