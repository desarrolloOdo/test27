# -*- coding: utf-8 -*

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'Academy.course'
    _description = 'Datos de cita'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
   
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                      ('intermediate','Intermediate'),
                                      ('advanced','Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)