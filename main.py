import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

image_style = {
    'width': '100%',
    'height': 'auto',
    'maxHeight': '300px',
    'objectFit': 'contain'
}

app.layout = dbc.Container([
    html.H1("Movie Dashboard", className="text-center mb-4 mt-4"),

    dbc.Row([
        dbc.Col(html.Img(src="/assets/insight1_movies_per_year.png", style=image_style), md=6),
        dbc.Col(html.Img(src="/assets/insight3_top_actors.png", style=image_style), md=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(html.Img(src="/assets/insight4_top_genres.png", style=image_style), md=6),
        dbc.Col(html.Img(src="/assets/insight5_rating_vs_gross.png", style=image_style), md=6),
    ]),
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
