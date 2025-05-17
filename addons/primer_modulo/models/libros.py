from odoo import models,fields, api
 #crea una tabla en la base de datos 
class Libros(models.Model):
    _name= 'libros'# nombre de la tabla que se va a generar
    _inherit =['mail.thread', 'mail.activity.mixin']
    
    supervisor_id= fields.Many2one( comodel_name='hr.employee',string="supervisor")# --> como sacar los comodel
    
    name= fields.Char(string='nombre del libro', required=True, tracking=True)# tracking me muestra las modificaciones que se realizaron 
    editorial = fields.Char(string='Editorial',required=True ) 
    isbn = fields.Char(string='Isbn')
    autor_id = fields.Many2one(string='Autor', comodel_name='autor', required=True, ondelete='restrict')# impide que un autor ea eliminado de la db si tiene un libro registrado
    lastname_autor = fields.Char(related='autor_id.last_name',string="apellido del autor")# relacion de dato gracias al any two one del campo nombre del autor
    image = fields.Binary( string="Imagen")
    categoria_id= fields.Many2one(comodel_name='categoria.libro')
    state = fields.Selection([('draft', 'Borrador'),('published','publicado')],
    default='draft', string="estado del libro")
    #campo calculado --> si quiere que se guarde en db debe incluirse store,= Tru
    description = fields.Char(string="descripcion", compute="_compute_description")
    
    _sql_constraints =[("name_uniq", "unique(name)","El nombre del libro ya se encuentra dentro de la base de datos")]
    # nombre del sql constraints
    #unique (nombre variable/campo que no quiero que se repita)
    #mensaje de error que sale cuando se repita
   
    # def _compute_description(self):
    #     self.description= self.name + ' | ' + self.isbn + ' | ' + self.autor_id.name + ' | ' + self.categoria_id.name 
    
    @api.depends('name', 'isbn', 'autor_id.name', 'categoria_id.name')# --> calculo en tiempo real
    def _compute_description(self):
        for record in self:
            record.description = f"{record.name or ''} | {record.isbn or ''} | {record.autor_id.name or ''} | {record.categoria_id.name or ''}"

        
    def boton_publicar(self):
        self.state= 'published'
        print("prueba click boton")
    
    def boton_borrador(self):
        self.state= 'draft'
        print("prueba click boton")
    
class CategoriaLibro(models.Model):
    _name='categoria.libro'
    
    name= fields.Char(string="nombre de la categoria")