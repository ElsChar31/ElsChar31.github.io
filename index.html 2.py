<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Belly Button Biodiversity</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>

<body>

  <div class="container">
    <div class="row">
      <div class="col-md-12 jumbotron text-center">
        <h1>Belly Button Biodiversity Dashboard</h1>
        <p>Use the interactive charts below to explore the dataset</p>
      </div>
    </div>
    <div class="row">
      <div class="col-md-2">
        <div class="well">
          <h5>Test Subject ID No.:</h5>
          <select id="selDataset" onchange="optionChanged(this.value)"></select>
        </div>
        <div class="panel panel-primary">
          <div class="panel-heading">
            <h3 class="panel-title">Demographic Info</h3>
          </div>
          <div id="sample-metadata" class="panel-body"></div>
        </div>
      </div>
      <div class="col-md-5">
        <div id="bar"></div>
      </div>
      <div class="col-md-5">
        <div id="gauge"></div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div id="bubble"></div>
      </div>
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/5.5.0/d3.js"></script>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="./static/js/app.js"></script>

<html>
<h1>Welcome to my website!</h
</html>
function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("samples.json").then((data) => {
      var sampleNames = data.names;
  
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      var firstSample = sampleNames[0];
      buildCharts(firstSample);
      buildMetadata(firstSample);
    });
  }
  
  // Initialize the dashboard
  init();
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildMetadata(newSample);
    buildCharts(newSample);
    
  }
  
  // Demographics Panel 
  function buildMetadata(sample) {
    d3.json("samples.json").then((data) => {
      var metadata = data.metadata;
      // Filter the data for the object with the desired sample number
      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
      var result = resultArray[0];
      // Use d3 to select the panel with id of `#sample-metadata`
      var PANEL = d3.select("#sample-metadata");
  
      // Use `.html("") to clear any existing metadata
      PANEL.html("");
  
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      Object.entries(result).forEach(([key, value]) => {
        PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
      });
  
    });
  }
  
  // 1. Create the buildCharts function.
  function buildCharts(sample) {
    // 2. Use d3.json to load and retrieve the samples.json file 
    d3.json("samples.json").then((data) => {
      // 3. Create a variable that holds the samples array. 
        let samples = data.samples;
      // 4. Create a variable that filters the samples for the object with the desired sample number.
        let resultArray = samples.filter(sampleObj => sampleObj.id ==sample);
      //  5. Create a variable that holds the first sample in the array.
        let result = resultArray[0];
        console.log(result);  
  
      // 6. Create variables that hold the otu_ids, otu_labels, and sample_values.
        let otu_ids = result.otu_ids;
        console.log(otu_ids)

        let otu_labels = result.otu_labels;
        console.log(otu_labels)
        let sample_values = result.sample_values;
        console.log(sample_values);
      // 7. Create the yticks for the bar chart.
      // Hint: Get the the top 10 otu_ids and map them in descending order  
      //  so the otu_ids with the most bacteria are last. 
  
      var yticks = otu_ids.slice(0,10).map(otuID => 'OTU ${otuID}')
      // console.log(yticks)
  
      // 8. Create the trace for the bar chart. 
      var barData = [
        {
            y: yticks,
            x: sample_values,
            text: otu_labels,
            type: "bar",
            orientation: "h",
        }

      ];
      // 9. Create the layout for the bar chart. 
      var barLayout = {
       title: 'Top Ten Bacteria Cultures Found in Sample $(sample)'
      };
      // 10. Use Plotly to plot the data with the layout. 
      Plotly.newPlot("bar", barData, barLayout)
    });
  }













</body>

</html>