import React, { Component } from 'react';
import c3 from 'c3';
import "c3/c3.min.css"; 


class Chart extends Component {
    componentDidMount() {
      this._updateChart();
    }

    _updateChart() {
        c3.generate({
            bindto: '#chart',
            data: {
                json: this.props.json,
                keys: {
                        value: ['Close', 'Open'],
                    }
            },axis: {
                x: {
                //    type: 'category',
                }
            }
      });
    }
    render() {
      return <div id="chart"></div>;    
    }
  }

export default Chart;
