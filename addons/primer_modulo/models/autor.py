from odoo import models,fields

class Autor(models.Model):
    _name= "autor"
    
    name = fields.Char(string='nombre del autor')
    
    
