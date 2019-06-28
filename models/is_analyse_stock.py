# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class IsAnalyseStock(models.Model):
    _name='is.analyse.stock'
    _description = u"Analyse Stock"
    _order='product_id'

    product_id   = fields.Many2one('product.product', u'Article', required=True)
    cde_cli_s1   = fields.Float(u'Cde Client S1'       , digits=(14,0))
    cde_cli_s2   = fields.Float(u'Cde Client S2'       , digits=(14,0))
    cde_cli_s3   = fields.Float(u'Cde Client S3'       , digits=(14,0))
    cde_cli_s4   = fields.Float(u'Cde Client S4'       , digits=(14,0))
    cde_cli_sx   = fields.Float(u'Cde Client S5-S9'    , digits=(14,0))
    cde_cli_sy   = fields.Float(u'Cde Client > S9'     , digits=(14,0))
    cde_fou      = fields.Float(u'Cde Fournisseur'     , digits=(14,0))
    stock_mini   = fields.Float(u'Stock mini'          , digits=(14,0))
    stock        = fields.Float(u'Stock'               , digits=(14,0))
    stock_7      = fields.Float(u'Stock à 7 jours'     , digits=(14,0))
    stock_28     = fields.Float(u'Stock à 28 jours'    , digits=(14,0))
    stock_terme  = fields.Float(u'Stock à terme'       , digits=(14,0))
    reapro_7     = fields.Float(u'Réappro à 7 jours'   , digits=(14,0))
    reapro_28    = fields.Float(u'Réappro à 28 jours'  , digits=(14,0))
    reapro_terme = fields.Float(u'Réappro à terme'     , digits=(14,0))
    livraison    = fields.Float(u'Livraisons à 12 mois', digits=(14,0))


    @api.multi
    def acces_cde_cli_action(self, data):
        for obj in self:
            return {
                'name': u'Commandes clients',
                'view_mode': 'tree,form',
                'view_type': 'form',
                'res_model': 'sale.order.line',
                'domain': [('product_id','=',obj.product_id.id)],
                'context':{},
                'type': 'ir.actions.act_window',
            }


    @api.multi
    def acces_cde_fou_action(self, data):
        for obj in self:
            return {
                'name': u'Commandes clients',
                'view_mode': 'tree,form',
                'view_type': 'form',
                'res_model': 'purchase.order.line',
                'domain': [('product_id','=',obj.product_id.id)],
                'context':{},
                'type': 'ir.actions.act_window',
            }



