///** @odoo-module **/
//
//import publicWidget from "@web/legacy/js/public/public_widget";
//import { rpc } from "@web/core/network/rpc";
//
//publicWidget.registry.InputEmailData = publicWidget.Widget.extend({
//    selector: '.customer_page',
//    events: {
//    'change #email_input': '_onEmailChange',
//    },
//
//    _onEmailChange function(events){
//        var email = $(#email_input).val();
//        console.log(email)
//        rpc('/customers/email',{'email': email}).then(
//            function (data){
//                $(#name_input).val(data.name),
//                $(#website_input).val(data.website),
//                $(#phone_input).val(data.phone)
//      });
//    }
