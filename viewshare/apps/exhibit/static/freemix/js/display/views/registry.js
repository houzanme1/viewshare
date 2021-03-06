define(["jquery", "display/views/base"],
    function ($, BaseView) {
    "use strict";

    var Registry = function() {

    };


    Registry.prototype.type_order = [];

    Registry.prototype.prototypes = {};

    Registry.prototype.construct = function (type, config) {
        var Type = this.prototypes[type];
        return new Type(config);
    };

    Registry.prototype.register = function (config, render_function) {
        var View = function (config) {
            BaseView.call(this, config);
        };
        View.prototype = new BaseView();
        View.prototype.config = config;
        View.prototype.generateExhibitHTML = render_function;
        var type = config.type;
        this.prototypes[type] = View;
        this.type_order.push(type);
        return View;
    };

    return new Registry();

});
