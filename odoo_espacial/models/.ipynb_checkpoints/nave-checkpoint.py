# *-* coding: utf-8 *-*

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class nave(models.Model):
    
    _name = 'espacial.nave'
    _description = 'Nave info'
    
    descripcion = fields.Char('Descripcion', required = True)
    alto = fields.Integer('Alto', required = True)
    ancho = fields.Integer('Ancho', required = True)
    largo = fields.Integer('Largo', required = True)
    tipo_combustible = fields.Selection(string = 'Tipo de Combustible', 
                                        selection = [('hidrogeno', 'Hidrogeno'), ('queroseno', 'Queroseno')],
                                        copy = False, 
                                        required = True, 
                                        help = 'Seleccione el tipo de combustible...'
                                     )
    tipo = fields.Selection(string = 'Tipo de Nave', 
                           selection = [
                               ('vehiculos_lanzadera', 'Vehiculo Lanzadera'), 
                               ('nave_robotica', 'Nave Robotico'), 
                               ('nave_tripulada', 'Nave Tripulada')
                           ],
                            copy = False, 
                            required = True, 
                            help = 'Seleccione el tipo de nave...'
                           )
    numero_pasajero = fields.Integer('Numero de Pasajeros', required = True)
    activo = fields.Boolean('Nave Activa?', default = True)
    
    @api.onchange('ancho')
    def _onchange_ancho(self):
        if self.ancho > self.largo:
            raise UserError('El Ancho no puede ser mayor que el Largo de la nave.')
    
    @api.constrains('ancho')
    def _check_ancho(self):
        for record in self:
            if record.ancho > record.largo:
                raise ValidationError('El Ancho no puede ser mayor que el Largo de la nave, verifique.')