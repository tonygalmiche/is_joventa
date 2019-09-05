# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class IsSuiviCommande(models.Model):
    _name='is.suivi.commande'
    _description = u"Suivi Commande"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce code existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order"]

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()
        for obj in self:
            remise=0
            if obj.partner_id.parent_id:
                remise=obj.partner_id.parent_id.is_remise_base
            else:
                remise=obj.partner_id.is_remise_base
            obj.is_remise_base=remise


    is_commande_acceptee = fields.Boolean(u'Commande Acceptée')
    suivi_commande_id    = fields.Many2one('is.suivi.commande', u'Suivi commande', required=False)
    contact_livraison    = fields.Char(u"Contact Livraison", size=255)
    note_interne         = fields.Text(u"Note Interne")
    numero_commande      = fields.Char(u"N° commande", size=255)
    devis_origine        = fields.Many2one('sale.order', u'Devis Origine')
    is_remise_base       = fields.Integer(u'Remise de base (%)', required=False)
    #date_validite        = fields.Date(u"Date de validité")
    is_date_prevue       = fields.Date(u"Date prévue", help="Date de livraison prévue")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_uom_qty','qty_delivered')
    def _compute(self):
        for obj in self:
            obj.is_reste_a_livrer=obj.product_uom_qty-obj.qty_delivered

    is_reste_a_livrer = fields.Float(u"Reste à livrer", compute="_compute", store=True, readonly=True, digits=(12, 0))




