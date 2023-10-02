from odoo import models, fields

class ThemeProduct(models.Model):
    _name = 'theme_module.product'
    _description = 'Theme Product'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', digits=(6, 2))
    image = fields.Binary(string='Image')

class ThemeCategory(models.Model):
    _name = 'theme_module.category'
    _description = 'Theme Category'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')

class ThemeCustomer(models.Model):
    _name = 'theme_module.customer'
    _description = 'Theme Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')

class ThemeOrder(models.Model):
    _name = 'theme_module.order'
    _description = 'Theme Order'

    customer_id = fields.Many2one('theme_module.customer', string='Customer')
    product_ids = fields.Many2many('theme_module.product', string='Products')
    total = fields.Float(string='Total', compute='_compute_total')

    def _compute_total(self):
        for order in self:
            order.total = sum(product.price for product in order.product_ids)