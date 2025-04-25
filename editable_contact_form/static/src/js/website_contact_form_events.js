/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";


publicWidget.registry.ContactForm = publicWidget.Widget.extend({
     selector: ".contact_detail_form",
     events: {
            'click #editBtn': '_onEditClickBtn',
            'click #saveBtn': '_onSaveClickBtn'
        },

     _onSaveClickBtn: function(event){
        var formData = {
            "name":$('#inputName').val(),
            "email": $('#InputEmail').val(),
            "phone": $('#inputPhone').val(),
            "contact_address_inline":$('#inputAddress').val(),
            "country_id":$('#inputCountry').val(),
            "state_id":$('#inputState').val(),
            "city":$('#inputCity').val(),
            "zip":$('#inputZip').val(),
            "website":$('#inputWebsite').val(),
            "function":$('#inputFunction').val(),
        }
        console.log(formData)
        var contactId = event.currentTarget.dataset.id
        console.log(contactId)
        formData['id'] = contactId

        let regexPhone = /\+[91][0-9]{10}/;
        let regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        let regexWebsite = /^(https?:\/\/)?([\da-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/?$/;

        if(!regexPhone.test(formData.phone)) {
            alert("Please enter the valid phone number.");
            return false;
        },
        if(!regexEmail.test(formData.email)) {
            alert("Please enter the valid email.");
            return false;
        },
        if(!regexWebsite.test(formData.website)) {
            alert("Please enter the valid website format.");
            return false;
        }

        rpc('/contacts/save',formData).then(
            function (data){
                $("#idForm input").attr("readonly", "readonly");
            });
     },

     _onEditClickBtn: function(ev){
        $("#idForm input").removeAttr("readonly")
     },
});
