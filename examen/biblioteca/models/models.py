# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libros(models.Model):
	_name = 'biblioteca.libros'

	Nombre = fields.Char(string='Nombre')
	Autor = fields.Char(string='Autor')
	Editorial = fields.Char(string='Editorial')

class autores():
	_name = 'biblioteca.autores'

	Nombre = fields.Char(string='Nombre')
	Apellidos = fields.Char(string='Apellidos')
	Nacionalidad= fields.Char(string='Nacionalidad')
