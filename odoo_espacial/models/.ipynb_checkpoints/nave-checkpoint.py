# *-* coding: utf-8 *-*

from odoo import models, fields, api

class nave(models.Model):
    
    _name = 'espacial.nave'
    _description = 'Nave info'
    
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
