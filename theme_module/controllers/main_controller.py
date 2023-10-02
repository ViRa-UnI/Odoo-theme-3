```python
from odoo import http
from odoo.http import request

class ThemeController(http.Controller):

    @http.route('/shop', type='http', auth='public', website=True)
    def shop(self, **kwargs):
        products = request.env['product.template'].sudo().search([])
        return request.render('theme_module.shop_page', {
            'products': products
        })

    @http.route('/product/<model("product.template"):product>', type='http', auth='public', website=True)
    def product(self, product, **kwargs):
        return request.render('theme_module.product_page', {
            'product': product
        })

    @http.route('/cart', type='http', auth='public', website=True)
    def cart(self, **kwargs):
        order = request.website.sale_get_order()
        return request.render('theme_module.cart_page', {
            'order': order
        })

    @http.route('/checkout', type='http', auth='public', website=True)
    def checkout(self, **kwargs):
        order = request.website.sale_get_order()
        return request.render('theme_module.checkout_page', {
            'order': order
        })

    @http.route('/confirmation', type='http', auth='public', website=True)
    def confirmation(self, **kwargs):
        order = request.website.sale_get_order()
        return request.render('theme_module.confirmation_page', {
            'order': order
        })
```