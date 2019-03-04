# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libros(models.Model):
	_name = 'biblioteca.libros'

	Nombre = fields.Char(string='Nombre')
	Autor = fields.Char(string='Autor')
	Editorial = fields.Char(string='Editorial')


	
	
