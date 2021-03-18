import React, {Component} from 'react';
import Select from 'react-select'
import axios from 'axios';
import Chart from './stockprices.component';

const API_URL = 'http://127.0.0.1:5000/'; 

class TickerList extends Component {
    constructor(props){
        super(props);
  
        this.state = {
            selectOptions : [],
            id: "",
            name: "",
            chartData: []
        }
    }
   // Make an API call to get the list of companies with tickers
    async getOptions(){
        const res = await axios.get(API_URL + 'api/tickerlist');
        const data = res.data.data;
    
        const options = data.map(d => ({
          "value" : d.Quandl_Code,
          "label" : d.Name
        }));
        this.setState({selectOptions: options});
      }
      
    // Handle company change value.Make API call to get the EoD Stock prices by company
     async handleChange(e){
        this.setState({id:e.value, name:e.label})
        const res = await axios.post(API_URL + 'api/eodstock', {"quandl_code":e.value});
        const data = res.data.data;
        this.setState({chartData: data});
       }
  
    componentDidMount() {
        this.getOptions();
    }
    render(){
        return (
        <div>
            <Select options={this.state.selectOptions} onChange={this.handleChange.bind(this)} />
            <p>You have selected <strong>{this.state.name}</strong> whose ticker is <strong>{this.state.id}</strong></p>
            <Chart 
            json={this.state.chartData} />
        </div>
        )
    }
  }
  

export default TickerList;