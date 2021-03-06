/*global define */
define([
    'handlebars',
    'jquery',
    'text!templates/modal.html',
    'views/view-interface',
    'bootstrap'
], function (
    Handlebars,
    $,
    modalTemplate,
    ViewInterface
) {
    'use strict';
    /**
     * View to display modals.
     * @constructor
     * @param {string} options.header - string to use modal header
     * @param {string} options.body - string to use for modal body
     * @param {string} options.buttonText - (optional) string to use for button
     * text in footer
     * @param {string} options.toggleEventName - name of event to toggle
     * modal's visibility
     * @param {function} options.buttonFunction - (optional) function to run
     * when button in footer is clicked
     */
    var ModalView = function(options) {
        this.initialize.apply(this, [options]);
    };

    $.extend(ModalView.prototype, {
        initialize: function(options) {
            this.$el = $(this.template({
                header: new Handlebars.SafeString(options.header),
                body: new Handlebars.SafeString(options.body),
                buttonText: options.buttonText
            }));
            if (typeof(options.buttonFunction) === 'function') {
                this.$el.find('#modalButton').on(
                    'click', this, options.buttonFunction);
            }
            this.toggleEventName = options.toggleEventName;
            // events
            ViewInterface.Observer(this.toggleEventName).subscribe(
                this.handleShowModal.bind(this));
        },
        /** Compile the template we will use to render the View */
        template: Handlebars.compile(modalTemplate),

        /** Add view to the DOM */
        render: function() { $('body').append(this.$el); },

        /** Make the modal visible */
        handleShowModal: function() {
            this.$el.modal('show');
        },

        /** Remove event bindings, child views, and DOM elements */
        destroy: function() {
            ViewInterface.Observer(this.toggleEventName).unsubscribe(
                this.handleShowModal.bind(this));
            this.$el.remove();
        }
    });

    return ModalView;
});
