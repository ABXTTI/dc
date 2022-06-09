
from odoo import fields, models, api
from odoo.exceptions import ValidationError
import datetime

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # overriding existing field
    weight = fields.Float(string="Weight", digits=(16,6))
    volume =  fields.Float(string="Volume", digits=(16,6))

    mc_ean = fields.Char(string="MC EAN")
    mc_quantity = fields.Float(string="MC Quantity")
    mc_weight = fields.Float(string="MC Weight in kg", digits=(16,6))
    mc_volume = fields.Float(string="MC Volume Cubic Meter", digits=(16,6))
    mc_uom = fields.Many2one("uom.uom", string="MC UOM")

    sc_ean = fields.Char(string="SC EAN")
    sc_quantity = fields.Float(string="SC Quantity")
    sc_weight = fields.Float(string="SC Weight in kg", digits=(16,6))
    sc_volume = fields.Float(string="SC Volume Cubic Meter", digits=(16,6))
    sc_uom = fields.Many2one("uom.uom", string="SC UOM")

    x_brand = fields.Many2one("ta.brand", string="Brand")
    x_hscode = fields.Char(string="HS CODE")
    type_filter = fields.Selection([('sale_invoice', 'Sale Invoice'),
                                    ('sales_tax_invoice', 'Sales Tax Invoice')],
                                   'Type Filter', default="", required=True)


