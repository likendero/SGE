# -*- coding: utf-8 -*-

from odoo import models, fields, api


class productos(models.Model):
    _name = 'productos.productos'

    Nombre = fields.Char()
    Stock = fields.Integer()
    Precio = fields.Float(compute="_value_pc", store=True)
    Descripcion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
