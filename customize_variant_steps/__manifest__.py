# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Variant process bar',
    'version' : '1.1',
    'summary': 'Variant process bar',
    'sequence': 10,
    'description': """ Select multiple products variant for product. """,
    'category': 'Ecommerce',
    'author': 'Shaikh Huzaifa',
    'maintainer': 'Zeeshan',
    'license': 'LGPL-3',
    'images' : [],
    'depends' : ['website','website_sale'],
    'data': [
        
        'views/variant_selection_bar.xml',
        
    ],

    'assets': {
        'web.assets_frontend': [
            # 'customize_variant_steps/static/src/css/style_variants.css',
            # 'customize_variant_steps/static/src/js/main_mixin.js',
        ],
        #'web.assets_qweb': ['customize_variant_steps/static/src/xml/variant_selection_bar.xml'],
        },           
    'demo': [],
    'images': ['images/1.jpg', 'images/2.jpg', 'images/3.jpg','images/4.jpg','images/5.jpg','images/6.jpg','images/7.jpg','images/8.jpg','static/description/icon.png','static/description/background.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
