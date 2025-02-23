/* eslint no-magic-numbers: 0 */
import React, { useState, Component } from 'react';
//import React from 'react-dom/client';
import { DashFlows } from '../lib';

class App extends Component {
    constructor() {
        super();
        const initial_nodes = [
            {
                id: "1",
                type: "resizable",
                data: {
                    label: "something"
                },
                position: { x: 250, y: 25 },
                style: {
                    width: 300,
                    height: 300,
                }
            }
        ];

        const initial_edges = [
        ];

        this.state = {
            id: "dash-flows-example",
            nodes: initial_nodes,
            edges: [],
            layoutOptions: null,
            style: { height: "600px" },
            showDevTools: true,
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps = (newProps) => {
        this.setState(newProps);
    };

    //const[state, setState] = useState({
    //    value:'',
    //    label:'Type Here',
    //    nodes: initial_nodes,
    //});

    render = () => {
        return (
            <div>
                <DashFlows
                    setProps={this.setProps}
                    {...this.state}
                />
            </div >
        );
    }
};


export default App;
