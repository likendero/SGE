# -*- coding: utf-8 -*-

from odoo import models, fields, api


class productos(models.Model):
    _name = 'productos.productos'

    nombre = fields.Char()
    stock = fields.Integer()
    precio = fields.Float(compute="_value_pc", store=True)
    descripcion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
