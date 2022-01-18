import dash
import dash_html_components as html


############# RUN APP
app = dash.Dash(__name__,title='DataTown',update_title='Cargando...')
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
                                    "Municipios")])])])])

# Main
if __name__ == "__main__":
    app.run_server(debug=True)