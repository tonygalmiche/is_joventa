# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import datetime

class IsAnalyseStock(models.Model):
    _name='is.analyse.stock'
    _description = u"Analyse Stock"
    _order='product_id'

    product_id   = fields.Many2one('product.product', u'Article', required=True)
    order_id     = fields.Many2one('purchase.order' , u'Commande fournisseur')
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


    @api.multi
    def creer_devis_fournisseur_action(self):
        #for obj in self:
        #    print(obj)


        user = self.env['res.users'].search([('id','=',self._uid)],limit=1)[0]
        partner = user.partner_id
        vals={
            'partner_id'        : partner.id,
            'fiscal_position_id': partner.property_account_position_id.id,
        }
        order=self.env['purchase.order'].create(vals)
        if order:
            order_line_obj = self.env['purchase.order.line']
            for obj in self:
                obj.order_id = order.id
                qt = -obj.reapro_28
                if qt<0:
                    qt=0
                now = datetime.date.today()
                date_planned = now.strftime('%Y-%m-%d')
                vals={
                    'order_id'      : order.id,
                    'product_id'    : obj.product_id.id,
                    'name'          : obj.product_id.name,
                    'product_uom'   : obj.product_id.uom_id.id ,
                    'price_unit'    : 0,
                    'product_qty'   : qt,
                    'date_planned'  : date_planned,
                }
                line=order_line_obj.create(vals)













