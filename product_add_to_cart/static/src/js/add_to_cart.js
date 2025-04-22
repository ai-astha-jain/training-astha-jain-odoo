/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.AddToCartAjax = publicWidget.Widget.extend({
    selector: '.o_wsale_product_btn',
    events: {
        'click .custom_add_to_cart_btn': '_onClickAddToCart',
    },

    _onClickAddToCart: function(ev){
        let productID = ev.currentTarget.getElementsByTagName('button')[0].getAttribute('data-product-id');
        console.log(productID)
        rpc("/shop/cart/update_json", {'product_id': parseInt(productID), 'add_qty': 1}).then(function(order){
            console.log()
            $(".my_cart_quantity").text(order.cart_quantity)
        });
    }
});
