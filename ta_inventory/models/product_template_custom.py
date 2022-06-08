
from odoo import fields, models, api
from odoo.exceptions import ValidationError
import datetime

class ProductTemplate(models.Model):
    _inherit = "product.template"

    mc_ean = fields.Char(string="MC EAN")
    mc_quantity = fields.Float(string="MC Quantity")
    mc_weight = fields.Float(string="MC Weight in kg")
    mc_volume = fields.Float(string="MC Volume Cubic Meter")
    mc_uom = fields.Many2one("uom.uom", string="MC UOM")

    sc_ean = fields.Char(string="MC EAN")
    sc_quantity = fields.Float(string="MC Quantity")
    sc_weight = fields.Float(string="MC Weight in kg")
    sc_volume = fields.Float(string="MC Volume Cubic Meter")
    sc_uom = fields.Many2one("uom.uom", string="MC UOM")

    x_brand = fields.Many2one("ta.brand", string="Brand")
    x_hscode = fields.Char(string="HS CODE")
    type_filter = fields.Selection([('sale_invoice', 'Sale Invoice'),
                                    ('sales_tax_invoice', 'Sales Tax Invoice')],
                                   'Type Filter', default="", required=True)


