# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JaiQuranAyat(models.Model):
    _name = 'jai_quran.ayat'
    _description = 'Data Ayat'

    surat_nomor = fields.Many2one("jai_quran.surat", string="Surat")
    ayat_nomor = fields.Integer(string="Nomor Ayat")
    ayat_teks_arab = fields.Html(string="Teks Arab")
    ayat_teks_indonesia = fields.Html(string="Teks Indonesia")
    tafsir_ids = fields.Many2many("jai_quran.tafsir", string="Tafsir")
    juz = fields.Integer(string="Juz")
    ayat_catatan = fields.Html(string="Keterangan")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
