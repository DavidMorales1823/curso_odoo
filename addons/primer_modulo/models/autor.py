from odoo import models,fields

class Autor(models.Model):
    _name= "autor"
    _rec_name="last_name"
    
    name = fields.Char(string='nombre del autor')
    last_name= fields.Char(string='apellido del autor')
    
     
    
    
