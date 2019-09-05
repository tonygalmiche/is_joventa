# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 12 pour Joventa',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 12 pour Joventa
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'mail',
        'crm',
        'sale',
        'sale_management',
        'stock',
        'mrp',
        'purchase',
        'account',
        'document',
    ],
    'data' : [
        'security/ir.model.access.csv',        # Droits d'accès aux tables
        'views/assets.xml',                    # Permet d'ajouter des css et des js
        'views/is_analyse_stock_view.xml',     # Analyse des stocks
        'views/product_template_view.xml',     # Surcharge fiche article
        'views/res_partner_view.xml',          # Surcharge fiche partner
        'views/purchase_view.xml',
        'views/sale_view.xml',                 # Surcharge du bon de commande
        'wizard/is_analyse_stock_wizard_view.xml', 
        'report/report_templates.xml',
        'report/report_invoice.xml',           # Surcharge PDF Facture
        'report/purchase_order_templates.xml', # Surcharge PDF Commande achat
        'report/report_stockpicking.xml',      # Surcharge PDF livraison
        'report/sale_report_templates.xml',    # Surcharge PDF devis/commande
        'views/menu.xml',                      # Menu
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

