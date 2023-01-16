# -*- coding: utf-8 -*

from odoo import models, fields, api

class medico(models.Model):
    
    _name = 'medicasis.medico'
    _description = 'medico Info'
    
    name = fields.Char(string='Nombre',required=True)
    description = fields.Text(string='Description')
    telefono = fields.Char(string='Numero de contacto',required=True)
    correo = fields.Char(string='Correo Electronico',required=True)
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                      ('intermediate','Intermediate'),
                                      ('advanced','Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)
