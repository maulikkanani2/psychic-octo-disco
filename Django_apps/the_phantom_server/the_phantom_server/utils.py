"""_summary_

Returns:
    _type_: this is a catch all utils
"""
from datetime import datetime, timedelta, date
import numpy as np

import geopandas as gpd
import holoviews as hv
import pandas as pd
from django.db.models import Avg, F
from django.core.exceptions import FieldError

from bokeh.plotting import figure
from bokeh.models import (HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource,TableColumn, CustomJS,NumberFormatter,Range1d,LinearAxis,Legend, LegendItem,DatetimeTicker,
DatetimeTickFormatter,DateFormatter,DateRangeSlider,Spacer,BoxAnnotation,AjaxDataSource,BuiltinIcon, Dropdown, Select, FuncTickFormatter
)
from bokeh.models.widgets import Button, Div, Select , DataTable
from bokeh.layouts import column, layout,row
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from land_app.models import *

hv.extension("bokeh")


def calculate_average(queryset, field_name):
    """
    Calculate the average of a numeric field for a given queryset.
    Args:
        queryset: A Django queryset.
        field_name: The name of the numeric field for which to calculate the average.
    Returns:
        The average value.
    """
    try:
        average_result = queryset.aggregate(Avg(field_name))
        return average_result[field_name + "__avg"]
    except FieldError:
        return "FieldError: The field name provided is non-numeric or does not exist."


def create_alias_queryset(queryset, alias_names, original_fields):
    """
    Annotate a queryset with alias names for specified original fields.

    Parameters:
    - queryset: The initial queryset to be annotated.
    - alias_names: List of alias names for the fields.
    - original_fields: List of original field names in the model.

    Returns:
    - An annotated queryset with alias fields.
    """
    # Create a dictionary to map original field names to alias names
    alias_mapping = {
        original_field: alias_names[i]
        for i, original_field in enumerate(original_fields)
    }

    # Use annotate with the dictionary
    for original_field, alias_field in alias_mapping.items():
        queryset = queryset.annotate(**{alias_field: F(original_field)})

    return queryset


# @cache_page(60 * 15)
def double_line_regular_chart(data):
    df = pd.DataFrame(data)

    p = figure(
        title="Line Chart",
        x_axis_label="X-axis",
        y_axis_label="Y-axis",
        min_width=150,
        min_height=200,
    )
    p.line(
        df["x_values"],
        df["y_values"],
        line_width=2,
        legend_label="Line 1",
        line_color="blue",
    )
    p.line(
        df["x_values"],
        df["y2_values"],
        line_width=2,
        legend_label="Line 2",
        line_color="red",
    )

    # p.toolbar.logo = None
    # p.add_tools(BoxSelectTool(icon='/home/ts/Documents/Projects/Jon/psychic-octo-disco/Django_apps/the_phantom_server/static/images/logo_1.png'))
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    p.sizing_mode = "stretch_both"
    return p


def double_Line_date_chart(
    data, x_column, y1_column, y2_column, y_axis_label, x_axis_label
):
    df = pd.DataFrame(data)
    df[x_column] = pd.to_datetime(df[x_column])
    p = figure(
        title="Line Chart",
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        x_axis_type="datetime",
        min_width=150,
        min_height=200,
    )
    p.line(
        df[x_column],
        df[y1_column],
        line_width=2,
        legend_label=y1_column,
        line_color="blue",
    )
    p.line(
        df[x_column],
        df[y2_column],
        line_width=2,
        legend_label=y2_column,
        line_color="red",
    )
    p.xaxis.formatter = DatetimeTickFormatter(
        days="%m/%d", months="%m/%d", years="%Y-%m-%d"
    )
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    p.sizing_mode = "stretch_both"
    return p


def single_line_date_chart(data, x_column, y_column, x_axis_label, y_axis_label):
    df = pd.DataFrame(data)
    df[x_column] = pd.to_datetime(df[x_column])
    p = figure(
        title="Line Chart",
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        x_axis_type="datetime",
        min_width=150,
        min_height=200,
    )
    p.line(
        df[x_column],
        df[y_column],
        line_width=2,
        legend_label=y_column,
        line_color="blue",
    )
    p.xaxis.formatter = DatetimeTickFormatter(
        days="%m/%d", months="%m/%d", years="%Y-%m-%d"
    )
    p.yaxis.formatter = y_axis_formatter(df[y_column])
    p.sizing_mode = "stretch_both"
    # Add hover tool
    hover = HoverTool(
        tooltips=[('Timestamp', '@timestamp{%F %H:%M:%S}'), (legend_label, f'@{y_column}{{0.00}}')],
        formatters={'@timestamp': 'datetime'}, mode='vline')
    p.add_tools(hover)
    ###################################
    #slider components
    # create rt gas chart
    plot_width = 150
    # Get the current date and time
    enddate = df[x_column].max()
    print(f'Plotting {enddate}')

    # Calculate startdate as the current date minus one day
    startdate = df[x_column].min() #enddate - timedelta(days=180)
    print(f'Plotting {startdate}')
    # Convert startdate to a NumPy datetime64 object
    startdate = np.datetime64(startdate)

    # Subtract one day from startdate using NumPy timedelta64
    startdate -= np.timedelta64(1, 'D')

    slider_edit_width = int(plot_width * 2)

    slider_p = figure(height=60, min_width=150, x_axis_type='datetime', toolbar_location=None,
                  x_range=(startdate, enddate))
    slider_p.yaxis.major_label_text_color = None
    slider_p.yaxis.major_tick_line_color = None
    slider_p.yaxis.minor_tick_line_color = None
    slider_p.grid.grid_line_color = None
    #slider_p.visible = False
    slider_line = slider_p.line(df[x_column],df[y_column],line_width=1, color="red")
    slider_box = BoxAnnotation(fill_alpha=0.5, line_alpha=0.5, level='underlay', left=startdate, right=enddate)
    #slider_box.visible = False
    slider_p.add_layout(slider_box)
    chart_slider = DateRangeSlider(start=startdate, end=enddate, value=(startdate, enddate), title=None,
                                   sizing_mode='stretch_both', min_width=slider_edit_width )
    chart_slider.visible = True
    callback = create_date_range_slider_callback(plot=p,slider_box =slider_box )
    chart_slider.js_on_change('value', callback)
    # spacer_edit = Spacer(min_width=400)
    slider_space_1 = Div(text='', min_width=60,sizing_mode='scale_width')
    slider_space_2 = Div(text=' ', min_height=5,sizing_mode='scale_width')
    # Create empty spacers to add margins around the DateRangeSlider
    margin_spacer_left = Spacer(min_width=60)
    margin_spacer_right = Spacer(min_width=1)
    ###################################################################################################################
    #drop down components
    columns_to_resample = [y_axis_label]
    dropdown_options = ["1 day", "1 week", "1 month"]
    dropdown = Dropdown(label="Period:", menu=dropdown_options)
    #dropdown.js_on_change('value', callback)

    layout =column([dropdown,p, slider_p,row([margin_spacer_left, chart_slider, margin_spacer_right]),slider_space_2],sizing_mode='stretch_both')
    return layout



def create_date_range_slider_callback(plot,slider_box):
    #this slider takes in the plot and box annotation and adusts tem to the slider that the callback
    #it is is attached to
    callback = CustomJS(args=dict(plot=plot,box=slider_box), code="""
    var new_start = cb_obj.value[0];
    var new_end = cb_obj.value[1];

    // Check if the new_start is greater than or equal to new_end
    if (new_start >= new_end) {
        // If new_start is greater than or equal to new_end, swap the values
        var temp = new_start;
        new_start = new_end;
        new_end = temp;
        
        // Update the DateRangeSlider values to reflect the swap
        rslider.setv({ start: new_start, end: new_end });
    }
    box.left = new_start;
    box.right = new_end;
        // Update the x-axis range of the plot
    plot.x_range.setv({start: new_start, end: new_end});    

    """)
    return callback


def single_line_date_chart_day(data, x_column, y_column, x_axis_label, y_axis_label, legend_label):
    #data is the dataframe, x_column is the date colum, y is the column graph we need, label legend is the single
    #chart legend
    df = pd.DataFrame(data)
    df[x_column] = pd.to_datetime(df[x_column])
    df['timestamp'] = df[x_column]
    df = df.filter(['timestamp', y_column])
    # Inspect the data to identify the issue
    print("Data:", df)

    # Create the ColumnDataSource from the DataFrame
    #conversion to source works better and is faster
    source = ColumnDataSource(df)
    source2 = ColumnDataSource(df)

    # Create the main line chart
    p = figure(
        title=legend_label,
        #x_axis_label=x_axis_label,  #hide lable for vertical space
        y_axis_label=y_axis_label,
        x_axis_type="datetime",
        min_width=150,
        min_height=200,
        tools="pan,box_zoom,wheel_zoom,reset"
    )
    p.toolbar.autohide = True
    p.line(
        x='timestamp',
        y=y_column,
        source=source,
        line_width=2,
        legend_label=legend_label,
        line_color="blue",
    )
    p.xaxis.formatter = DatetimeTickFormatter(
        days="%m/%d", months="%m/%d", years="%Y-%m-%d"
    )
    p.sizing_mode = "stretch_both"

    # Add hover tool
    hover = HoverTool(
        tooltips=[('Period', '@timestamp{%c}'), (legend_label, f'@{y_column}{{0.00}}')],
        formatters={'@timestamp': 'datetime'},
        mode='vline')
    #https://docs.bokeh.org/en/0.10.0/docs/reference/models/formatters.html
    p.add_tools(hover)
    ###################################
    #slider components
    # create rt gas chart
    #slider_edit_width = int(plot_width * 2)
    plot_width = 150
    # Get the current date and time for the date range slider
    enddate = source.data['timestamp'].max()
    print(enddate)
    startdate = source.data['timestamp'].min()
    print(startdate)

    # Create the slider figure
    slider_p = figure(height=60, min_width=150, max_width=846, width_policy="max", x_axis_type='datetime', toolbar_location=None,
                      x_range=(startdate, enddate))

    slider_p.yaxis.major_label_text_color = None
    slider_p.yaxis.major_tick_line_color = None
    slider_p.yaxis.minor_tick_line_color = None
    slider_p.grid.grid_line_color = None
    slider_line = slider_p.line(x='timestamp', y=y_column, source=source, line_width=1, color="red")
    slider_box = BoxAnnotation(fill_alpha=0.5, line_alpha=0.5, level='underlay', left=startdate, right=enddate)
    slider_p.add_layout(slider_box)

    # Create the date range slider

    chart_slider = DateRangeSlider(start=startdate, end=enddate, value=(startdate, enddate), title=None,
                                   sizing_mode='stretch_both',height=50, min_width=150 )

    # Create the callback function for the date range slider
    callback = create_date_range_slider_callback(plot=p, slider_box=slider_box)
    chart_slider.js_on_change('value', callback)

    # Create empty spacers for layout
    margin_spacer_left = Spacer(min_width=60)
    margin_spacer_right = Spacer(min_width=15)
    slider_space_2 = Div(text='', min_height=25,sizing_mode='scale_width')

    ###################################################################################################################
    #drop down components
    columns_to_resample = [y_column]
    columns_to_ave = [y_column]
    dropdown_options = ["1 day", "1 week", "1 month"]
    select = Select( value="1 day", options=dropdown_options)
    callback = create_resample_min_callback(source,source2,columns_to_resample, columns_to_ave,p,p.y_range)
    #this resamples the data
    select.js_on_change('value', callback)

    #dropdown = Dropdown(label="Period:", menu=dropdown_options)

    # Create the layout
    #both row and column need a sizing mode
    layout = column([select,p, slider_p, row([margin_spacer_left, chart_slider, margin_spacer_right],sizing_mode='stretch_both'), slider_space_2],
                    sizing_mode='stretch_both')
    return layout



def create_resample_min_callback(source,source2, columns_to_resample, columns_to_ave,p,yr):
    #by default if the column is not in cols to ave then it is for agg
    #source2 maintains original data
    #need a high def data flag
    callback_code = """
        //get the value of the drop down
        const selectedInterval = cb_obj.value;
        console.log("Selected Interval:", selectedInterval);

        // Print the source object and its data attribute
        console.log("Source Object:", source2);
        console.log("Source Data:", source2.data);
        //split the the string into two parts 
        const selectedIntervalParts = selectedInterval.split(" ");
        //1st part is the numeric portion ie 10 min = 10
        const selectedIntervalValue = parseInt(selectedIntervalParts[0]);
        //2nd part is the string portion 
        const selectedIntervalUnit = selectedIntervalParts[1];

        // Define the time unit in milliseconds
        const timeUnits = {
            //Multiplying 1000 (milliseconds in a second) by 60 gives the number of milliseconds in a minute
            //ie 60000 milliseconds in a minute  
            'minutes': 1000 * 60,
            //milliseconds. It multiplies the conversion factor for hours (1000 * 60 * 60) by 24, giving the number of milliseconds in a day.
            'hours': 1000 * 60 * 60,
            //: This line approximates the conversion factor for months to milliseconds. It multiplies the conversion factor for days (1000 * 60 * 60 * 24) by 30, assuming that there are approximately 30 days in a month. 
            'day': 1000 * 60 * 60 * 24,
            'week': 1000 * 60 * 60 * 24 * 7,
            'month': 1000 * 60 * 60 * 24 * 30  // Approximation for a month
        };

        // Calculate the time interval in milliseconds
        //calculate the time interval in milliseconds based on the selected interval value
        //ie 5 Min = 5 * (1000 * 60)
        const selectedIntervalMillis = selectedIntervalValue * timeUnits[selectedIntervalUnit];
        // Clear all values in the source
        Object.keys(source.data).forEach(key => {
        source.data[key] = [];
        });

 

        // Resample data based on selected interval
        //initialize an empty array
        const resampledData = {};
        // initialize array for timestamps
        resampledData['timestamp'] = [];
        //loop through each column
        columnsToResample.forEach(column => {
            resampledData[column] = [];
        });
        // set start equal to 1st item in series 
        //console.log(source2.data['docdatedate'][0]);
        //let startTime = Array.prototype.slice.call(source2.data['docdatedate'])[1];

        let startTime = source2.data['timestamp'][0];
        //loop through each colum

            columnsToResample.forEach(column => {    //source2.data['timestamp'].forEach((timestamp, index) =>
               ///   console.log(timestamp);
                //assign a value
                let sum = 0;
                //console.log("sum:",sum);            
                let count = 0;
                  source2.data['timestamp'].forEach((timestamp, index) => {    //columnsToResample.forEach(column =>
                    //console.log("sum:",sum);            
                    //assign a value
                    const value = source2.data[column][index];
                    // Convert float64 timestamp to milliseconds
                    const timestampMillis = timestamp;
                    console.log(value);
                    //if the miliseconds are less than the specified but sum the values 
                    if (timestamp - startTime < selectedIntervalMillis) {
                        console.log("current time:", timestamp);
                        console.log("start time:", startTime);
                        console.log("time-delta:", timestamp-startTime);
                        console.log("calc interval:",selectedIntervalMillis);
                
                        sum += value;
                        console.log("value:",value);
                        count++;  //short hand for count +1
                        console.log("count:",count);
                        // define action when the number aer larger than the unit    
                    } else {
                        if (columns_to_ave.includes(column)) {
                            let average;
                            if (count > 1) {
                                average = parseFloat((sum / count).toFixed(2));
                                console.log("ave:",average);
                            } else if (count > 0 && count <= 1) {
                                average = parseFloat(sum.toFixed(2));   
                                console.log("total:",average); 
                            } else {
                                average = 0;
                            }
                            // Push to resampledData regardless of count
                            resampledData['timestamp'].push(startTime);
                            resampledData[column].push(average);
                           } 
                        else {
                           const total = count > 0 ? parseFloat(sum.toFixed(2))  : null;
                           console.log("else total:",total);
                           resampledData['timestamp'].push(startTime);
                           resampledData[column].push(total);
                           }
                        //start the next row 
                        startTime = timestamp   //new Date(timestampMillis + selectedIntervalMillis);
                        sum = value;
                        count = 1;                                    
                }
            });
        });

        // Update the data source of the plot with the resampled data
        console.log(resampledData);
        source.data = resampledData;
            // Calculate the minimum and maximum y values
        const yMin = Math.min(...source.data['total_volume']);
        console.log("yr.start:",yr.start)
        const yMax = Math.max(...source.data['total_volume']);
        
        // Update the y-axis range
        yr.start = yMin - 1;
        console.log("yr.start:",yr.start)
        yr.end = yMax + 1;

        yr.setv({ start: yMin - 1, end: yMax + 1 });
        
     

        // Trigger a redraw of the plot
        source.change.emit();

        // Update display div with resampled data
        //const resampledDataText = JSON.stringify(resampledData);
        //display_div.text = "Resampled Data:\\n" + resampledDataText;
    """

    return CustomJS(args=dict(source=source, source2=source2,columnsToResample=columns_to_resample,columns_to_ave=columns_to_ave,p=p,yr=yr), code=callback_code)

def create_resample_min_callbackv1(data, columns_to_resample, display_div):
    callback_code = """
        const selectedInterval = cb_obj.item;
        const selectedIntervalMinutes = parseInt(selectedInterval.split(" ")[0]);

        // Resample data based on selected interval
        const resampledData = [];
        let startTime = data[0].timestamp;

        columnsToResample.forEach(column => {
            let sum = 0;
            let count = 0;

            data.forEach(entry => {
                const timestamp = new Date(entry.timestamp);
                const value = entry[column];

                if (timestamp - startTime < selectedIntervalMinutes * 60 * 1000) {
                    sum += value;
                    count++;
                } else {
                    const average = count > 0 ? sum / count : null;
                    resampledData.push({ timestamp: startTime, [column]: average });

                    startTime = new Date(startTime.getTime() + selectedIntervalMinutes * 60 * 1000);
                    sum = value;
                    count = 1;
                }
            });
        });

    // Update the data source of the plot with the resampled data
    source.data = resampledData;


    // Update display div with resampled data
    const resampledDataText = JSON.stringify(resampledData);
    display_div.text = "Resampled Data:\n" + resampledDataText;
    """

    return CustomJS(args=dict(data=data, columnsToResample=columns_to_resample, display_div=display_div), code=callback_code)


def y_axis_formatter(y_range):
    max_value = y_range.values.max()
    if max_value >= 18000:
        return FuncTickFormatter(code="""
            return (tick / 1000).toFixed(0);
        """)
    else:
        return FuncTickFormatter(code="""
            return tick;
        """)

def y_axis_lables(y_range):
    max_value = y_range.values.max()
    if max_value >= 18000:
        return "MBbls"
    else:
        return "Bbls"

def read_queryset_to_geopandas(queryset):
    # Transform LeaseholdUnit objects to a list of dictionaries
    values = list(queryset.values())

    # Transforms geometries into shapely objects
    geometry = gpd.GeoSeries.from_wkb([x["geom"] for x in values])

    # Creates dataframe
    df = gpd.GeoDataFrame(values, geometry=geometry)

    # Add separate columns for latitude and longitude
    df["centroid"] = df["geometry"].centroid
    df["longitude"] = pd.to_numeric(df["centroid"].x, errors="coerce")
    df["latitude"] = pd.to_numeric(df["centroid"].y, errors="coerce")

    return df.dropna(subset=["longitude", "latitude"])


class financial_Data_Processor:
    # this class pulls in the json query and then run analysis on it for visualizations.
    # this will reduce db queries
    def __init__(self, queryset):
        self.queryset = queryset
        self.df = self._to_dataframe()

    def _to_dataframe(self):
        df = pd.DataFrame(self.queryset)

        return df

    def base_calcs(self):
        """Private method to convert JSON to DataFrame."""

        if "Amount" in self.df.columns and "Qty" in self.df.columns:
            self.df["unitcost"] = self.df["Amount"].div(self.df["Qty"]).round(0)
            return self._update_df()

    def pivot_trans_data(self):
        pivot_df = self.df.pivot_table(
            index="acct__name",
            columns="acctg_period",
            values="amt",
            # aggfunc='sum'
        )
        return self._update_df(pivot_df)

    def date_columns(self):
        # Convert 'Period' to datetime
        self.df["Period"] = pd.to_datetime(self.df["Period"])

        # Get unique dates as strings
        date_column_names = self.df["Period"].dt.date.unique().astype(str).tolist()

        # Convert list to JSON string
        # date_column_names_json = json.dumps(date_column_names)

        return date_column_names

    def aggregate_account(self, groupby_list):
        """Aggregate account by gen_account and return result as JSON."""
        # Group and sum
        self.df = self.df.groupby(groupby_list).sum()

        # Convert DataFrame to JSON
        # result_json = self.df.reset_index().to_json(orient='records')

        return self._update_df()  # result_json

    def filter_column(self, column, items):
        """
        Filters the DataFrame to only include rows where 'column' is in 'items'.
        :param column: Column to filter
        :param items: List of items to filter by
        :return: Filtered DataFrame
        """
        self.df = self.df[self.df[column].isin(items)]
        return self._update_df()

    def pivot_dataframe(self, index, columns, values):
        """
        Pivot the DataFrame organized by given index / columns values.
        :param index: Keys to group by on the pivot table index.
        :param columns: Keys to group by on the pivot table column.
        :param values: Column to aggregate.
        :return: self
        """
        self.df = self.df.pivot(index=index, columns=columns, values=values)
        return self

    def to_list_of_dicts(self):
        """Convert the DataFrame to a list of dictionaries."""
        list_of_dicts = self.df.reset_index().to_dict(orient="records")
        return list_of_dicts

    def combine_gen_acc(self, new_value):
        """Replaces the specified values in 'gen_acc' column with the new value."""
        self.df["gen_acc"] = np.where(
            self.df["gen_acc"].isin(self.gen_account), new_value, self.df["gen_acc"]
        )
        return self._update_df()
        """# Usage
            fdp = financial_Data_Processor(queryset, ['Gen1', 'Gen2'])
            fdp.combine_gen_acc('Gen3')
            """
        # You can add more methods here for specific types of data processing

    def net_revenue(self):
        # this creates a new amount based on the LOS_aggregation field
        # and aggregate
        self.df["Net_Revenue"] = self.df["Amount"] * self.df["LOS_aggregation"]
        return self._update_df()

    def to_dataframe(self):
        """Convert the FinancialDataProcessor instance to a DataFrame."""
        return self.df.copy()

    def drop_columns(self, columns):
        """
        Drops specified columns from the DataFrame.
        :param columns: Columns to drop
        """
        self.df = self.df.drop(columns, axis=1)
        return self._update_df()

    def _update_df(self, new_df=None):
        if new_df is not None:
            self.df = new_df
        return self


class DataProcessor:
    def __init__(self, queryset):
        self.queryset = queryset
        self.df = self._to_dataframe()

    def _to_dataframe(self):
        """Private method to convert queryset to DataFrame."""
        return pd.DataFrame(list(self.queryset))

    def pivot_trans_data(self):
        pivot_df = self.df.pivot_table(
            index="acct__name",
            columns="acctg_period",
            values="amt",
            # aggfunc='sum'
        )
        return pivot_df


def df_calcs(dataframe, revenue, units):
    # this runs calcs broadly accross the dataset.
    # It's a good practice so that the original dataframe isn't modified when we don't want it to.
    df = dataframe.copy()
    df["unitcost"] = df[revenue].div(df[units])
    df = df.round(0)
    # add additional calcs as necessary
    return df


def oil_data(df):

    oil_data = df.loc[(df["Gen_account"] == 410) | (df["Gen_account"] == 415)].copy()
    oil_data.loc[:, "General_account"] = "Oil"
    oil_data_amount_pivot = oil_data.pivot_table(
        index="General_account", columns="Period", values=["Amount"], aggfunc="sum"
    )
    oil_data_qty_pivot = oil_data.pivot_table(
        index="General_account", columns="Period", values=["Qty"], aggfunc="sum"
    )
    oil_data_bbl_pivot = oil_data.pivot_table(
        index="General_account", columns="Period", values=["unitcost"], aggfunc="sum"
    )

    # convert to dictionary
    oil_data_amount_pivot = oil_data_amount_pivot.to_dict("records")
    oil_data_qty_pivot = oil_data_qty_pivot.to_dict("records")
    oil_data_bbl_pivot = oil_data_bbl_pivot.to_dict("records")
    # print(oil_data_bbl_pivot)
    return oil_data_amount_pivot, oil_data_qty_pivot, oil_data_bbl_pivot


def gas_data(df):

    gas_data = df.loc[df["Gen_account"] == 420].copy()
    gas_data.loc[:, "General_account"] = "Gas"
    gas_data_amount_pivot = gas_data.pivot_table(
        index="General_account", columns="Period", values=["Amount"], aggfunc="sum"
    )
    gas_data_qty_pivot = gas_data.pivot_table(
        index="General_account", columns="Period", values=["Qty"], aggfunc="sum"
    )
    gas_data_mcf_pivot = gas_data.pivot_table(
        index="General_account", columns="Period", values=["unitcost"], aggfunc="sum"
    )

    # convert to dictionary
    gas_data_amount_pivot = gas_data_amount_pivot.to_dict("records")
    gas_data_qty_pivot = gas_data_qty_pivot.to_dict("records")
    gas_data_mcf_pivot = gas_data_mcf_pivot.to_dict("records")
    # print(gas_data_mcf_pivot)
    return gas_data_amount_pivot, gas_data_qty_pivot, gas_data_mcf_pivot


def ngl_data(df):

    ngl_data = df.loc[df["Gen_account"] == 430].copy()
    ngl_data.loc[:, "General_account"] = "NGL"
    ngl_data_amount_pivot = ngl_data.pivot_table(
        index="General_account", columns="Period", values=["Amount"], aggfunc="sum"
    )
    ngl_data_qty_pivot = ngl_data.pivot_table(
        index="General_account", columns="Period", values=["Qty"], aggfunc="sum"
    )
    ngl_data_bbl_pivot = ngl_data.pivot_table(
        index="General_account", columns="Period", values=["unitcost"], aggfunc="sum"
    )

    # convert to dictionary
    ngl_data_amount_pivot = ngl_data_amount_pivot.to_dict("records")
    ngl_data_qty_pivot = ngl_data_qty_pivot.to_dict("records")
    ngl_data_bbl_pivot = ngl_data_bbl_pivot.to_dict("records")
    # print(ngl_data_bbl_pivot)
    return ngl_data_amount_pivot, ngl_data_qty_pivot, ngl_data_bbl_pivot


def total_rev_data(df):

    total_revenue = df.loc[
        (df["Gen_account"] >= 400) | (df["Gen_account"] <= 430)
    ].copy()
    total_revenue.loc[:, "General_account"] = "Total Revenue"

    total_revenue_amount_pivot = total_revenue.pivot_table(
        index="General_account", columns="Period", values=["Amount"], aggfunc="sum"
    )
    total_revenue_qty_pivot = total_revenue.pivot_table(
        index="General_account", columns="Period", values=["Qty"], aggfunc="sum"
    )
    total_revenue_bbl_pivot = total_revenue.pivot_table(
        index="General_account", columns="Period", values=["unitcost"], aggfunc="sum"
    )

    # convert to dictionary
    total_revenue_amount_pivot = total_revenue_amount_pivot.to_dict("records")
    total_revenue_qty_pivot = total_revenue_qty_pivot.to_dict("records")
    total_revenue_bbl_pivot = total_revenue_bbl_pivot.to_dict("records")
    # print(total_revenue_bbl_pivot)
    return total_revenue_amount_pivot, total_revenue_qty_pivot, total_revenue_bbl_pivot


def gathering_and_Processing_data(df):

    G_AND_P_data = df.loc[df["Gen_account"] == 515].copy()
    print(G_AND_P_data)
    total_G_and_P_amount_pivot = G_AND_P_data.pivot_table(
        index="Gen_account", columns="Period", values=["Amount"], aggfunc="sum"
    )
    total_G_and_P_amount_pivot = total_G_and_P_amount_pivot.to_dict("records")
    print(total_G_and_P_amount_pivot)
    return total_G_and_P_amount_pivot


def loe_data(df):
    # you can have functions in a utils folder for data cleaning

    G_AND_P_data = df.loc[df["Gen_account"] == 515].copy()
    G_AND_P_data = G_AND_P_data.groupby(["Period", "Account_name"]).agg(
        {"Amount": "sum"}
    )

    print(G_AND_P_data)
    G_AND_P_data.to_csv("/Users/jongrottis/Documents/g_and_p.csv", index=False)

    # consolidate data
    # total_revenue['General_account'] = 'Gathering & Processing'  #want the agg account
    # total_G_and_P_amount_pivot = G_AND_P_data.pivot_table(index='Gen_account', columns='Period', values=['Amount'], aggfunc='sum')

    # convert to dictionary
    total_G_and_P_amount_pivot = total_G_and_P_amount_pivot.to_dict("records")

    print(total_G_and_P_amount_pivot)
    return total_G_and_P_amount_pivot


def LOS_columns(df):
    """_summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    date_column_names = df["Period"].unique().tolist()

    # Convert Timestamp to date
    date_column_names = [date.date() for date in date_column_names]
    return date_column_names
