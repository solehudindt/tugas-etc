odoo.define('gratis_antar.component', function (require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const models = require('point_of_sale.models');
    const _super_Order = models.Order.prototype;

    // const gratis = models.load_fields('pos.order', 'gratis_antar');
    // console.log("gratis", typeof(gratis));

    models.Order = models.Order.extend({
        export_as_JSON: function () {
            var json = _super_Order.export_as_JSON.apply(this, arguments);
            console.log("json1", json.gratis_antar);
        }
    });

    class PosDiscountButton extends PosComponent {
        async onClick() {
            const order = this.env.pos.get_order();
            console.log("total order", order.get_total_with_tax());
            console.log("order", order);
            // if (oder.get_total_with_tax() >= 750000) {
            //     order.gratis_antar = true;
            // } 
       
        }
    }
    PosDiscountButton.template = 'PosDiscountButton';
    ProductScreen.addControlButton({
        component: PosDiscountButton,
        condition: function () {
            return true;
        },
    });
    Registries.Component.add(PosDiscountButton);

    return PosDiscountButton;

});