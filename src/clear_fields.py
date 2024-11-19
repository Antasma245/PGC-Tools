def clear_fields(main_window, add_logo:bool) -> None:
    """Clear the content of the fields widget"""
    fields_widget = main_window.central_widget.scroll_area.inner_widget.fields_widget

    while fields_widget.fields_widget_layout.count():
        # Get the first item of the fields widget layout
        item = fields_widget.fields_widget_layout.takeAt(0)
        
        widget = item.widget()

        # If the item has a widget, schedule its deletion
        if widget is not None:
            widget.deleteLater()
        
        sub_layout = item.layout()

        # If the item has its own layout, delete its content recursively
        if sub_layout is not None:
            clear_fields(sub_layout)

        del item
    
    # If specified, add the application logo to the fields widget as a placeholder
    if add_logo:
        fields_widget.add_logo()
    
    # Disable the create button of the buttons widget
    main_window.central_widget.scroll_area.inner_widget.buttons_widget.create_button.setDisabled(True)