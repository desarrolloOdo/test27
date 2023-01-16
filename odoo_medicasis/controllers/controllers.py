# -*- coding: utf-8 -*-
# from odoo import http


# class OdooMedicasis(http.Controller):
#     @http.route('/odoo_medicasis/odoo_medicasis', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_medicasis/odoo_medicasis/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_medicasis.listing', {
#             'root': '/odoo_medicasis/odoo_medicasis',
#             'objects': http.request.env['odoo_medicasis.odoo_medicasis'].search([]),
#         })

#     @http.route('/odoo_medicasis/odoo_medicasis/objects/<model("odoo_medicasis.odoo_medicasis"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_medicasis.object', {
#             'object': obj
#         })
