import {Injectable} from '@angular/core';
import {BaThemeConfigProvider, colorHelper, layoutPaths} from '../../../theme';

@Injectable()
export class LineChartService {

  constructor(private _baConfig:BaThemeConfigProvider) {
  }

  getData() {

    var layoutColors = this._baConfig.get().colors;
    var graphColor = this._baConfig.get().colors.custom.dashboardLineChart;

    return {
      type: 'serial',
      theme: 'blur',
      marginTop: 15,
      marginRight: 15,
      responsive: {
        'enabled': true
      },
      dataProvider: [

        { date: new Date(2016, 11, 3), value: 100},
        { date: new Date(2016, 11, 4), value: 155},
        { date: new Date(2016, 11, 5), value: 140},
        { date: new Date(2016, 11, 6), value: 150},
        { date: new Date(2016, 11, 7), value: 165},
        { date: new Date(2016, 12, 3), value: 140},
        { date: new Date(2016, 12, 10), value: 145},
        { date: new Date(2016, 12, 15), value: 142},
        { date: new Date(2017, 1, 4), value: 155},
        { date: new Date(2017, 3, 4), value: 155},
        { date: new Date(2017, 3, 5), value: 140},
        { date: new Date(2017, 3, 6), value: 150},
        { date: new Date(2017, 3, 7), value: 165},
      ],
      categoryField: 'date',
      categoryAxis: {
        parseDates: true,
        gridAlpha: 0,
        color: layoutColors.defaultText,
        axisColor: layoutColors.defaultText
      },
      valueAxes: [
        {
          minVerticalGap: 20,
          gridAlpha: 0,
          color: layoutColors.defaultText,
          axisColor: layoutColors.defaultText
        }
      ],
      graphs: [
        {
          id: 'g1',
          bullet: 'none',
          useLineColorForBulletBorder: true,
          lineColor: colorHelper.hexToRgbA(graphColor, 0.15),
          lineThickness: 1,
          negativeLineColor: layoutColors.danger,
          type: 'smoothedLine',
          valueField: 'value',
          fillAlphas: 1,
          fillColorsField: 'lineColor'
        }
      ],
      chartCursor: {
        categoryBalloonDateFormat: 'MM DD YYYY',
        categoryBalloonColor: '#4285F4',
        categoryBalloonAlpha: 0.7,
        cursorAlpha: 0,
        valueLineEnabled: true,
        valueLineBalloonEnabled: true,
        valueLineAlpha: 0.5
      },
      dataDateFormat: 'MM DD YYYY',
      export: {
        enabled: true
      },
      creditsPosition: 'bottom-right',
      zoomOutButton: {
        backgroundColor: '#fff',
        backgroundAlpha: 0
      },
      zoomOutText: '',
      pathToImages: layoutPaths.images.amChart
    };
  }
}
