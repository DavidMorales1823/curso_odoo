from odoo import models,fields
 #crea una tabla en la base de datos 
class Libros(models.Model):
    _name= 'libros'# nombre de la tabla que se va a generar
    _inherit =['mail.thread', 'mail.activity.mixin']
    
    name= fields.Char(string='nombre del libro', required=True, tracking=True)# tracking me muestra las modificaciones que se realizaron 
    editorial = fields.Char(string='Editorial',required=True ) 
    isbn = fields.Char(string='Isbn')
    autor_id = fields.Many2one(string='Autor', comodel_name='autor', required=True, ondelete='restrict') 
    image = fields.Binary( string="Imagen")
    
    _sql_constraints =[("name_uniq", "unique(name)","El nombre del libro ya se encuentra dentro de la base de datos")]
    # nombre del sql constraints
    #unique (nombre variable/campo que no quiero que se repita)
    #mensaje de error que sale cuando se repita