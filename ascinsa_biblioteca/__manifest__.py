# -*- coding: utf-8 -*-

{
    'name' : 'Ascinsa Biblioteca', 
    
    'summary' : """Gestión y Administración de una Biblioteca""",
    
    'description' : """
    Modulo de Biblioteca que nos permitira:
        - Administrar libros.
        - Administrar clientes.
        - Organizar alquileres.
    """,
    
    'author' : 'ascinsa', 
    
    'website' : 'http://www.teleservicio.com', 
    
    'category' : 'administration', 
    
    'version' : '1.0.0.1', 
    
    'depends' : ['base'], 
    
    'data' : [
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_menuitems.xml',
    ], 
    
    'demo' : [
        'demo/biblioteca_demo.xml', 
    ]
}