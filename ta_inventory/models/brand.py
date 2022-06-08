from odoo import fields, models

class TaBrand(models.Model):
    _name = "ta.brand"
    _description = "Brands"
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
