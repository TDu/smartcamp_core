{
    "name": "Point of Sale - New barcode rule for priced product with change rate",
    "version": "17.0.1.0.0",
    "category": "Sales/Point of Sale",
    "summary": """
        Add a barcode rule to be able to scan a barcode with price encoded (as the 
        standard "Priced Product" rule), and convert the price according to a given 
        change rate.
    """,
    "author": "Camptocamp",
    "depends": ["point_of_sale"],
    "data": ["views/res_config_settings_views.xml"],
    "assets": {
        "point_of_sale._assets_pos": [
            'pos_barcode_rule_priced_with_change_rate/static/src/**/*',
        ],
    },
    "installable": True,
    "license": "AGPL-3",
}
