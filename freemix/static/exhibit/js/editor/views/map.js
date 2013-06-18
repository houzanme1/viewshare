(function ($, Freemix, Exhibit) {
    "use strict";

    var View = Freemix.view.prototypes["map"];

    View.prototype.propertyTypes = ["location"];

    View.prototype.label = "Map";

    View.prototype.thumbnail = "/static/exhibit/img/map-icon.png";

    View.prototype.viewClass = Exhibit.OLMapView;

    View.prototype.template_name = "map-view-template";

    View.prototype.setupEditor = function (config, template) {

        this._setupViewForm(config, template);
        this._setupLabelEditor(config, template);

        var db = Freemix.exhibit.database;
        var latlng = template.find("#latlng_property");
        var points = db.getPropertiesWithTypes(["location"]);
        this._setupPropertySelect(config, template, latlng, "latlng", points);
        latlng.change();

        var color = template.find("#color_property");
        this._setupPropertySelect(config, template, color, "colorKey", Freemix.exhibit.database.getAllPropertyObjects(), true);
        color.change();

        var zoom = template.find("#zoom_level");
        this._setupSelectPropertyHandler(config, template, zoom, "zoom");
        zoom.change();

        this._setupLensEditor(config, template);
    };



})(window.Freemix.jQuery, window.Freemix, window.Exhibit);
