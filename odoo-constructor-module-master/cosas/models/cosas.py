# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class cosas(models.Model): 
    _name = 'ej.cosas' 
    cosa1 = fields.text(string='cosa1', required=True) 
 
    cosa2 = fields.integer(string='cosa2', required=True) 
 
    cosa3 = fields.text(string='cosa3', required=True) 
 
    cosa4 = fields.text(string='cosa4', required=True) 
 
    cosa5 = fields.text(string='cosa5', required=True) 
 
