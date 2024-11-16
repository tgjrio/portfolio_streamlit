from st_aggrid import AgGrid, GridOptionsBuilder


def display_aggrid_table(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(
        selection_mode='multiple',
        use_checkbox=True,
        rowMultiSelectWithClick=True,
        suppressRowDeselection=False,
        suppressRowClickSelection=False,
        groupSelectsChildren=True,
        groupSelectsFiltered=True
    )
    gb.configure_pagination(
        enabled=True,
        paginationAutoPageSize=False,
        paginationPageSize=10
    )
    gb.configure_default_column(
        resizable=True,
        filter=True,
        sortable=True,
        editable=False,
        groupable=True,
    )
    gb.configure_side_bar(
        filters_panel=True,
        columns_panel=True,
    )
    grid_options = gb.build()
    AgGrid(
        df,
        gridOptions=grid_options,
        height=350,
        theme='alpine',
    )