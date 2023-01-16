# -*- coding: utf-8 -*

from odoo import models, fields, api

class medico(models.Model):
    
    _name = 'medicasis.medico'
    _description = 'medico Info'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                      ('intermediate','Intermediate'),
                                      ('advanced','Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)