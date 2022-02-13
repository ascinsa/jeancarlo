# *-* coding: utf-8 *-*

from odoo import models, fields, api

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
    