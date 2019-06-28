# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class IsTypeEvenementClient(models.Model):
    _name='is.type.evenement.client'
    _description = u"Type évènement client"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Cette famille existe deja')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsEvenementClient(models.Model):
    _name='is.evenement.client'
    _description = u"Evènement client"
    _order='name'
    
    client_id      = fields.Many2one('res.partner', u'Partenaire', required=False)
    name           = fields.Date(u"Date", index=True, required=True)
    type_evenement = fields.Many2one('is.type.evenement.client', u'Type évènement', required=True, ondelete='set null', help="Sélectionnez un type évènement")
    commentaire    = fields.Text(u"Commentaire",size=200)


class IsSelectionPartenaire(models.Model):
    _name='is.selection.partenaire'
    _description = u"Sélection partenaire"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Cette sélection existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsDomainePartenaire(models.Model):
    _name='is.domaine.partenaire'
    _description = u"Domaine partenaire"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Cette famille existe deja')]    
       
    name        = fields.Char("Code",size=50,required=True, index=True)
    commentaire = fields.Text("Commentaire",size=200)


class ResPartner(models.Model):
    _name = "res.partner"
    _description = "Type de production"
    _inherit = 'res.partner'
    
    is_evenement_ids             = fields.One2many('is.evenement.client', 'client_id', u'Évènements')
    is_siret                     = fields.Char(u'N°Siret', required=False)
    is_source                    = fields.Char(u'Source', required=False, help="Origine du prospect/client")
    is_prospect                  = fields.Boolean(u'Prospect', required=False)
    is_remise_base               = fields.Integer(u'Remise de base (%)', required=False)
    is_selection_partenaire      = fields.Many2one('is.selection.partenaire', u'Selection', required=False)
    is_domaine_partenaire        = fields.Many2one('is.domaine.partenaire', u'Domaine', required=False)
    is_code_partenaire           = fields.Char(u'Code Partenaire', required=False)
    is_numfournisseur_partenaire = fields.Char(u'N° Fournisseur', required=False)
    is_street3                   = fields.Char(u'Rue 3', required=False)


