# -*- coding: utf-8 -*-
from odoo import http

# class EsqueletoModulo(http.Controller):
#     @http.route('/esqueleto_modulo/esqueleto_modulo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esqueleto_modulo/esqueleto_modulo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('esqueleto_modulo.listing', {
#             'root': '/esqueleto_modulo/esqueleto_modulo',
#             'objects': http.request.env['esqueleto_modulo.esqueleto_modulo'].search([]),
#         })

#     @http.route('/esqueleto_modulo/esqueleto_modulo/objects/<model("esqueleto_modulo.esqueleto_modulo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esqueleto_modulo.object', {
#             'object': obj
#         })