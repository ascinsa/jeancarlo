# -*- coding: utf-8 -*-

{
    'name' : 'Odoo Academy',
    
    'summary' : """Academy app to manage Trainning""",
    
    'description' : """
        Academy Module to manage Trainning:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author' : 'Odoo', 
    
    'website' : 'https://www.odoo.com', 
    
    'category' : 'Trainning', 
    
    'version' : '0.1', 
    
    'depends' : ['base'], 
    
    'data' : [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    
    'demo' : [
        'demo/academy_demo.xml', 
    ],
}