console.log("app.js is running!")

function userAnalysis() {
    console.log("Running user analysis in app.py")
    var userText = d3.select("#user-text-input").property("value")
    console.log(`User text: ${userText}`)

    fetch(`${window.origin}/interactive/user-sentiment`, {
		method: "POST",
		credentials: "include",
		body: JSON.stringify(userText),
		cache: "no-cache",
		headers: new Headers({
			"content-type": "application/json"
		})
	})
	.then(function (response) {
		if (response.status !== 200) {
			console.log(`Looks like there was a problem. Status code: ${response.status}`);
			return;
		}
		response.json().then(function (responseJson) {
            console.log(responseJson)
            
			Plotly.newPlot("user-analysis-gauge", responseJson.gauge_data)
			Plotly.newPlot("user-analysis-emotions", responseJson.emotion_plot_data, responseJson.emotion_plot_layout)



			// let clear_results = d3.select("#dice-table")
            //     if (clear_results._groups[0][0].hasChildNodes()) {
			// 		clear_results.selectAll("table").remove()
			// 		}

			// var table = d3.select('#dice-table')
			// 	.append('table')
			// 	.classed("center", true)
			// var thead = table.append('thead')
			// var	tbody = table.append('tbody');

			// // append the header row
			// thead.append('tr')
			// .selectAll('th')
			// .data(Object.keys(tableData))
			// .enter()
			// .append('th')
			// .text(d => d);

			// for (i = 0; i < _.size(tableData["Roll Total"]); i++) {
			// 	var row = tbody.append('tr')
			// 	Object.keys(tableData).forEach(column => {
			// 		row.append('td')
			// 		.text(tableData[column][i])
			// 	}) 				
			// }

			// // create a row for each object in the data
			// var rows = tbody.selectAll('tr')
			// .data(tableData["Roll #"])
			// .enter()
			// .append('tr')
			
			// rows.selectAll('td')
			// .data(tableData)
			// .enter()
			// .append('td')
			// .text(d => d)

			
			
		})
	})
	.catch(function (error) {
		console.log("Fetch error: " + error)
	})
}

