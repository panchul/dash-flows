# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class BananaNode(Component):
    """A BananaNode component.
ddd

Keyword arguments:

- data (dict; default {    label: "undef",    depends_on: [],    node_id: "undef"}):
    ddd.

    `data` is a dict with keys:

    - label (boolean | number | string | dict | list; optional)

    - depends_on (list; optional)

    - node_id (string; optional)

    - onChange (optional)

    - onDelete (optional)

    - dependsOnOptions (boolean | number | string | dict | list; optional)

- selected (boolean; default False):
    ddd."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flows'
    _type = 'BananaNode'
    @_explicitize_args
    def __init__(self, data=Component.UNDEFINED, selected=Component.UNDEFINED, **kwargs):
        self._prop_names = ['data', 'selected']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['data', 'selected']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(BananaNode, self).__init__(**args)
