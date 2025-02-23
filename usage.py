import dash
from dash import html, Input, Output, State, clientside_callback, _dash_renderer, dcc
import dash_flows
import dash_mantine_components as dmc

_dash_renderer._set_react_version("18.2.0")

app = dash.Dash(__name__, assets_folder='assets',
                 external_stylesheets=dmc.styles.ALL)

initial_nodes = [
    {
        'id': '1',
        'type': 'resizable',
        'data': {
            'label': html.Div([
                html.Img(src="tbd",
                         style={'width': '100%', 'height': '100%'}),
            ], style={
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                'gap': '10px',
                'padding': '10px'
            })
        },
        'position': {'x': 250, 'y': 25},
        'style': {
            'width': 300,
            'height': 300,
        }
    },
    {
        'id': '2',
        'type': 'resizable',
        'data': {'label': html.Div([
            html.Img(src="tbd",
                     style={'width': '100%', 'height': '100%'}),
        ], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'gap': '10px',
            'padding': '10px'
        })},
        'position': {'x': 250, 'y': 150},
        'style': {
            'width': 300,
            'height': 300,
        }
    },
    {
        'id': 'animated1',
        'type': 'circle',
        'data': {'label': '🔄'},
        'position': {'x': 250, 'y': 150},
        'style': {
            'width': 60,
            'height': 60,
        }
    },
    {
        'id': '3',
        'type': 'resizable',
        'data': {
            'label': html.Div([
                html.Button(id='btn_example', children='button')], style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'gap': '10px',
            'padding': '10px'
        })
        },
        'position': {'x': 250, 'y': 250},
        'style': {
            'width': 300,
            'height': 300,
            'minHeight': 200
        }
    },
    {
        'id': '4',
        'type': 'banana',
        'data': {'label': 'banana' },
        'position': {'x': 250, 'y': 250},
        'style': {
            'width': 300,
            'height': 300,
            'minHeight': 200
        }
    }
]

initial_edges = [
    {
        'id': 'e1-2',
        'source': '1',
        'target': '2',
        'type': 'animated',
        'data': {
            'animatedNode': 'animated1'  # Reference the dedicated animated node
        },
        'style': {
            'strokeWidth': 2,
            'stroke': '#555'
        }
    },
    {
        'id': 'e2-3',
        'source': '2',
        'target': '3',
        'type': 'default',  # Changed to default type
        'style': {
            'strokeWidth': 2,
            'stroke': '#555'
        }
    }
]


# Add layout buttons above the DashFlow component
layout_buttons = dmc.Group([
    dmc.Button("Vertical Layout", id="btn-vertical", variant="outline"),
    dmc.Button("Horizontal Layout", id="btn-horizontal", variant="outline"),
    dmc.Button("Radial Layout", id="btn-radial", variant="outline"),
    dmc.Button("Force Layout", id="btn-force", variant="outline"),
], mt="md", mb="md")

app.layout = dmc.MantineProvider([
    dmc.Text("Here's the component:", size="sm"),
    dmc.JsonInput(
        label="Here's the initial input (json):",
        placeholder="Textarea will autosize to fit the content",
        validationError="Invalid JSON",
        formatOnBlur=True,
        autosize=True,
        minRows=4,
        maxRows=8,
        w = 800,
        value = '{"something":1, "another":{"something":1, "another":2}}'
    ),

    dcc.Upload(id='upload-data',
               children=html.Button('Upload',
            id='upload-button'),
            multiple=False),
    html.Button("download", id='btn-download-txt'),
    dcc.Download(id="download-txt"),
    html.Hr(),

    layout_buttons,
    dash_flows.DashFlows(
        id='react-flow-example',
        nodes=initial_nodes,
        edges=initial_edges,
        showDevTools=True,
        style={'height': '600px'},
        layoutOptions=None  # Add this prop
    ),
    # Hidden div for storing layout options
    html.Div(id='layout-options', style={'display': 'none'})
])

# Create a clientside callback to handle layout changes
app.clientside_callback(
    """
    function(n_vertical, n_horizontal, n_radial, n_force) {
        const triggered = dash_clientside.callback_context.triggered[0];
        if (!triggered) return window.dash_clientside.no_update;

        const btnId = triggered.prop_id.split('.')[0];
        let options = {};

        switch(btnId) {
            case 'btn-vertical':
                options = {
                    'elk.algorithm': 'layered',
                    'elk.direction': 'DOWN',
                    'elk.spacing.nodeNode': 80,
                    'elk.layered.spacing.nodeNodeBetweenLayers': 100
                };
                break;
            case 'btn-horizontal':
                options = {
                    'elk.algorithm': 'layered',
                    'elk.direction': 'RIGHT',
                    'elk.spacing.nodeNode': 80,
                    'elk.layered.spacing.nodeNodeBetweenLayers': 100
                };
                break;
            case 'btn-radial':
                options = {
                    'elk.algorithm': 'org.eclipse.elk.radial',
                    'elk.radial.radius': 200
                };
                break;
            case 'btn-force':
                options = {
                    'elk.algorithm': 'org.eclipse.elk.force',
                    'elk.force.iterations': 300,
                    'elk.spacing.nodeNode': 80
                };
                break;
            default:
                return window.dash_clientside.no_update;
        }
        return JSON.stringify(options);
    }
    """,
    Output('react-flow-example', 'layoutOptions'),  # Change output target to DashFlow's layoutOptions
    Input('btn-vertical', 'n_clicks'),
    Input('btn-horizontal', 'n_clicks'),
    Input('btn-radial', 'n_clicks'),
    Input('btn-force', 'n_clicks'),
    prevent_initial_call=True
)

# TODO: callbacks for upload and download, use State

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)