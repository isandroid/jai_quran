# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JaiQuranSurat(models.Model):
    _name = 'jai_quran.surat'
    _description = 'Data Surat'
    _order = 'surat_nomor asc'

    name = fields.Char(
	    	string="Nama Surat",
	    	required=True
    	)
    surat_arti = fields.Char(string="Arti Surat")
    surat_nomor = fields.Integer(string="Nomor Surat")
    surat_pengantar = fields.Html(string="Pengantar Surat")

    # value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
