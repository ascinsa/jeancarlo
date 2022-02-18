# *-* coding: utf-8 *-*

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class libro(models.Model):
    
    _name = 'biblioteca.libro'
    _description = 'Información de Libro'
    
    titulo = fields.Char('Titulo', required=True)
    autor = fields.Char('Autor', required = True)
    editores = fields.Text('Editor(es)', required = True)
    editorial = fields.Char('Editorial', required = True)
    anno = fields.Integer('Año', required = True)
    isbn = fields.Char('ISBN', required = True)
    genero = fields.Char('Genero', required = True)
    activo = fields.Boolean('Activo?', default = True)
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if len(self.isbn) > 13:
            raise UserError('El ISBN no puede tener mas de 13 caracteres.')
            
    @api.constrains('isbn')
    def check_isbn(self):
        for record in self:
            if len(record.isbn) > 13:
                raise ValidationError('El ISBN no puede tener mas de 13 caracteres.')