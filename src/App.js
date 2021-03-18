import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';
import TickerList from './components/tickerlist.component';


class App extends Component {
 
	render() {
		return (
      <div className="app-wrap">
        <TickerList />  
      </div>
    );
  }
}
export default App;
