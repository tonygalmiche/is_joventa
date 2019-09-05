# -*- coding: utf-8 -*-

from odoo import api, fields, models
import time
import datetime

#TODO : 
# - Ne pas prendre en compte les devis
# - Bug si quantitée livrée > qt commandée


class IsAnalyseStockWizard(models.TransientModel):
    _name = 'is.analyse.stock.wizard'
    _description = u"Analyse Stock Wizard"

    date_fin = fields.Date('Date de fin')


    @api.multi
    def get_cde_cli(self, product_id, date_debut=False, date_fin=False):
        cr=self._cr
        sql="""
            select sum(sol.product_uom_qty-sol.qty_delivered)
            from sale_order so inner join sale_order_line sol on sol.order_id=so.id
            where 
                sol.product_id="""+str(product_id)+""" and
                so.is_commande_acceptee='t' and
                so.state not in ('cancel')
        """
        if date_debut:
            sql=sql+" and so.is_date_prevue>='"+str(date_debut)+"'"
        if date_fin:
            sql=sql+" and so.is_date_prevue<'"+str(date_fin)+"'"
        cr.execute(sql)
        qty=0
        for row in cr.fetchall():
            if row[0]:
                qty=row[0]
        return qty


    @api.multi
    def get_cde_fou(self, product_id, date_debut=False, date_fin=False):
        cr=self._cr
        sql="""
            select sum(pol.product_qty-pol.qty_received)
            from purchase_order po inner join purchase_order_line pol on pol.order_id=po.id
            where 
                pol.product_id="""+str(product_id)+"""
        """
        if date_debut:
            sql=sql+" and pol.is_date_confirmee>='"+str(date_debut)+"'"
        if date_fin:
            sql=sql+" and pol.is_date_confirmee<'"+str(date_fin)+"'"
        cr.execute(sql)
        qty=0
        for row in cr.fetchall():
            if row[0]:
                qty=row[0]
        return qty



    @api.multi
    def get_livraison(self, product_id, date_debut=False, date_fin=False):
        cr=self._cr
        sql="""
            select sum(sm.product_uom_qty)
            from stock_move sm inner join stock_picking sp on sm.picking_id=sp.id
            where 
                sp.picking_type_id=4 and 
                sm.product_id="""+str(product_id)+"""
        """
        if date_debut:
            sql=sql+" and sm.date>='"+str(date_debut)+"'"
        if date_fin:
            sql=sql+" and sm.date<'"+str(date_fin)+"'"
        cr.execute(sql)
        qty=0
        for row in cr.fetchall():
            if row[0]:
                qty=row[0]
        return qty



    @api.multi
    def is_analyse_stock_wizard_action(self, data):
        cr=self._cr
        for obj in self:
            date_jour = time.strftime('%Y-%m-%d')
            date_jour = datetime.datetime.strptime(date_jour, '%Y-%m-%d')

            date_s1_debut = False
            date_s1_fin   = (date_jour + datetime.timedelta(days=7)).strftime('%Y-%m-%d')

            date_s2_debut =  date_s1_fin
            date_s2_fin   = (date_jour + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

            date_s3_debut =  date_s2_fin
            date_s3_fin   = (date_jour + datetime.timedelta(days=21)).strftime('%Y-%m-%d')

            date_s4_debut =  date_s3_fin
            date_s4_fin   = (date_jour + datetime.timedelta(days=28)).strftime('%Y-%m-%d')

            date_sx_debut =  date_s4_fin
            date_sx_fin   = (date_jour + datetime.timedelta(days=8*7)).strftime('%Y-%m-%d')

            date_sy_debut =  date_sx_fin
            date_sy_fin   =  False



            self.env['is.analyse.stock'].search([]).unlink()
            #products = self.env['product.product'].search([('purchase_ok','=',True),('qty_available','>',0)])
            products = self.env['product.product'].search([('purchase_ok','=',True),('name','not like','+')])


            for product in products:
                cde_cli      = self.get_cde_cli(product.id)
                cde_cli_s1   = self.get_cde_cli(product.id, date_s1_debut, date_s1_fin)
                cde_cli_s2   = self.get_cde_cli(product.id, date_s2_debut, date_s2_fin)
                cde_cli_s3   = self.get_cde_cli(product.id, date_s3_debut, date_s3_fin)
                cde_cli_s4   = self.get_cde_cli(product.id, date_s4_debut, date_s4_fin)
                cde_cli_sx   = self.get_cde_cli(product.id, date_sx_debut, date_sx_fin)
                cde_cli_sy   = self.get_cde_cli(product.id, date_sy_debut, date_sy_fin)
                cde_fou      = self.get_cde_fou(product.id)
                cde_fou_s1   = self.get_cde_fou(product.id, date_s1_debut, date_s1_fin)
                cde_fou_s4   = self.get_cde_fou(product.id, date_s1_debut, date_s4_fin)
                stock_mini   = product.is_stock_mini
                stock        = product.qty_available
                stock_7      = stock-cde_cli_s1+cde_fou_s1
                stock_28     = stock-cde_cli_s1-cde_cli_s2-cde_cli_s3-cde_cli_s4+cde_fou_s4
                stock_terme  = stock-cde_cli+cde_fou
                reapro_7     = stock_7     - stock_mini
                reapro_28    = stock_28    - stock_mini
                reapro_terme = stock_terme - stock_mini
                livraison    = self.get_livraison(product.id)

                vals = {
                    'product_id'   : product.id,
                    'cde_cli_s1'   : cde_cli_s1,
                    'cde_cli_s2'   : cde_cli_s2,
                    'cde_cli_s3'   : cde_cli_s3,
                    'cde_cli_s4'   : cde_cli_s4,
                    'cde_cli_sx'   : cde_cli_sx,
                    'cde_cli_sy'   : cde_cli_sy,
                    'cde_fou'      : cde_fou,
                    'stock_mini'   : stock_mini,
                    'stock'        : stock,
                    'stock_7'      : stock_7,
                    'stock_28'     : stock_28,
                    'stock_terme'  : stock_terme,
                    'reapro_7'     : reapro_7,
                    'reapro_28'    : reapro_28,
                    'reapro_terme' : reapro_terme,
                    'livraison'    : livraison,
                }
                res = self.env['is.analyse.stock'].create(vals)

        return {
            'name': u'Analyse des stocks',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'res_model': 'is.analyse.stock',
            'domain': [],
            'context':{},
            'type': 'ir.actions.act_window',
        }



