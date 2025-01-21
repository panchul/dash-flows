# AUTO GENERATED FILE - DO NOT EDIT

export resizablenode

"""
    resizablenode(;kwargs...)

A ResizableNode component.

Keyword arguments:
- `data` (required): . data has the following type: lists containing elements 'label'.
Those elements have the following types:
  - `label` (Bool | Real | String | Dict | Array; optional)
- `selected` (Bool; optional)
"""
function resizablenode(; kwargs...)
        available_props = Symbol[:data, :selected]
        wild_props = Symbol[]
        return Component("resizablenode", "ResizableNode", "dash_flows", available_props, wild_props; kwargs...)
end

