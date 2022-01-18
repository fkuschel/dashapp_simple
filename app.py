


############# RUN APP
app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],title='DataTown',update_title='Cargando...')
server = app.server

# Create app layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Municipios")))))

# Main
if __name__ == "__main__":
    app.run_server(debug=False)