odoo.define('theme_module.theme_script', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    var qweb = core.qweb;
    var _t = core._t;

    publicWidget.registry.themeScript = publicWidget.Widget.extend({
        selector: '.o_website_sale',
        events: {
            'click .product-card': '_onProductCardClick',
            'click .add-to-cart': '_onAddToCartClick',
        },

        start: function () {
            return this._super.apply(this, arguments);
        },

        _onProductCardClick: function (ev) {
            ev.preventDefault();
            var $card = $(ev.currentTarget);
            var productId = $card.data('product-id');
            this._rpc({
                route: '/shop/product/' + productId,
                params: {
                    product_id: productId,
                },
            }).then(function (data) {
                if (data) {
                    window.location = '/shop/product/' + productId;
                }
            });
        },

        _onAddToCartClick: function (ev) {
            ev.preventDefault();
            var $btn = $(ev.currentTarget);
            var productId = $btn.data('product-id');
            this._rpc({
                route: '/shop/cart/update',
                params: {
                    product_id: productId,
                    add_qty: 1,
                },
            }).then(function (data) {
                if (data) {
                    window.location = '/shop/cart';
                }
            });
        },
    });

    return publicWidget.registry.themeScript;
});