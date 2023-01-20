# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JaiQuranTafsir(models.Model):
    _name = 'jai_quran.tafsir'
    _description = 'Data Tafsir'

    name = fields.Char(string="Nomor Tafsir")
    tafsir_isi = fields.Html("Isi Tafsir")
    tafsir_catatan = fields.Html("Catatan Tafsir")

#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
