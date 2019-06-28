# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class IsFamilleArticle(models.Model):
    _name='is.famille.article'
    _description = u"Famille article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Cette famille existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsDnArticle(models.Model):
    _name='is.dn.article'
    _description = u"DN article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce DN existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsTypeVanneArticle(models.Model):
    _name='is.type.vanne.article'
    _description = u"Type vanne article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce type de vanne existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsCoupleArticle(models.Model):
    _name='is.couple.article'
    _description = u"Couple article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce couple existe déjà')]

    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsMotorisationArticle(models.Model):
    _name='is.motorisation.article'
    _description = u"Motorisation article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Cette motorisation existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsSignalcommandeArticle(models.Model):
    _name='is.signalcommande.article'
    _description = u"Signal commande Article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce signal de commande existe déjà')]    
       
    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class IsTensionArticle(models.Model):
    _name='is.tension.article'
    _description = u"Tension Article"
    _order='name'
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Cette tension existe déjà')]    

    name        = fields.Char(u"Code",size=50,required=True, index=True)
    commentaire = fields.Text(u"Commentaire",size=200)


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = 'product.template'

    is_famille_article        = fields.Many2one('is.famille.article', u'Famille', required=False)
    is_dn_article             = fields.Many2one('is.dn.article', u'DN', required=False)
    is_type_vanne_article     = fields.Many2one('is.type.vanne.article', u'Type Vanne', required=False)
    is_couple_article         = fields.Many2one('is.couple.article', u'Couple', required=False)
    is_diaphragme             = fields.Boolean(u'Diaphragme', required=False)
    is_contacts_auxiliaires   = fields.Boolean(u'Contacts auxiliaires', required=False)
    is_code_douanier          = fields.Char(u'Code Douanier', required=False)
    is_motorisation_article   = fields.Many2one('is.motorisation.article', u'Motorisation', required=False)
    is_signalcommande_article = fields.Many2one('is.signalcommande.article', u'Commande', required=False)
    is_tension_article        = fields.Many2one('is.tension.article', u'Tension', required=False)
    is_origine_article        = fields.Many2one('res.country', u'Origine', required=False)
    is_stock_mini             = fields.Float(u'Stock mini', digits=(14,0))







