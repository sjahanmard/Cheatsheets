import React from "react";
import GaugeChart from 'react-gauge-chart'



export default class Displaying extends React.Component{
  constructor(props) {
    super(props);
    };
    

    render(){
      return (
        <tr>
        <th scope="row">{this.props.sensor.sensorid}</th>
        <td>{this.props.sensor.sensorname}</td>
        <td>
        <div className="progress">
          <div className="progress-bar" role="progressbar" aria-valuenow={this.props.sensor.sensordata}
              aria-valuemin="0" aria-valuemax="100" style={{width:`${this.props.sensor.sensordata}%`}}>
              {this.props.sensor.sensordata} %
          </div>
        </div>        
        </td>
        <td>
        <GaugeChart id="gauge-chart2" 
  nrOfLevels={20} 
  percent={0.86} 
/>
        </td>

      </tr>
      );
}
}
















