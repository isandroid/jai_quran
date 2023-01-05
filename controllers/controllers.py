# -*- coding: utf-8 -*-
# from odoo import http


# class JaiQuran(http.Controller):
#     @http.route('/jai_quran/jai_quran', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jai_quran/jai_quran/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jai_quran.listing', {
#             'root': '/jai_quran/jai_quran',
#             'objects': http.request.env['jai_quran.jai_quran'].search([]),
#         })

#     @http.route('/jai_quran/jai_quran/objects/<model("jai_quran.jai_quran"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jai_quran.object', {
#             'object': obj
#         })
