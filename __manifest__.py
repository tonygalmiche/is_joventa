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


#        'views/is_type_evenement_client.xml',  # Table Type évènement
#        'views/is_evenement_client.xml',       # Evènement client
#        'views/is_selection_partenaire.xml',   # Selection Partenaire
#        'views/is_domaine_partenaire.xml',     # Domaine Partenaire
#        'views/suivi_commande.xml',            # Table de suivi des commandes
        'views/res_partner_view.xml',          # Surcharge fiche partner
#        'views/sale_view.xml',                 # Surcharge du bon de commande
#        'views/purchase_view.xml',


#        'report/sale_report_templates.xml',    # Surcharge PDF devis/commande
#        'report/report_stockpicking.xml',      # Surcharge PDF livraison
#        'report/report_invoice.xml',           # Surcharge PDF Facture
#        'report/purchase_order_templates.xml', # Surcharge PDF Commande achat
#        'wizard/is_analyse_stock_wizard_view.xml', 
        'views/menu.xml',                      # Menu
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

