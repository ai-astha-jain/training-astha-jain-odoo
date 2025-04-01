/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.ContactsCard = publicWidget.Widget.extend({
    selector: '.contact_page',
    events: {
    'click .contacts_card': '_onContactCardClick',
    },

    _onContactCardClick: function(events){
        let contactSlug = $(events.currentTarget).data('contacts-slug');
        window['location']['href'] = '/contacts/' + contactSlug;
    }
    });
