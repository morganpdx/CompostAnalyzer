import {Component, ViewEncapsulation} from '@angular/core';

import {LineChartService} from './lineChart.service';

@Component({
  selector: 'line-chart',
  encapsulation: ViewEncapsulation.None,
  styles: [require('./lineChart.scss')],
  template: require('./lineChart.html')
})
export class LineChart {

  chartData:Object;

  constructor(private _lineChartService:LineChartService) {
    this.chartData = this._lineChartService.getData();
  }

  initChart(chart:any) {
    let zoomChart = () => {
      chart.zoomToDates(new Date(2016, 11, 1), new Date(2017, 12, 31));
    };

    chart.addListener('rendered', zoomChart);
    zoomChart();

    if (chart.zoomChart) {
      chart.zoomChart();
    }
  }
}
