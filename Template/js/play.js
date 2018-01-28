let baseURL = "http://127.0.0.1:8000/api";
let validateURL = baseURL + "/validate-news/";
let fakeURL = baseURL + "/fake-news/";
let reportURL = baseURL + "/report-news/";

const getFakeNews = () => {
	$.get(fakeURL, data => {
		console.log(data);
	})
}

const validateNews = () => {

	let snip = document.querySelector("#snip").value;
	let links = "";

	if(snip !== ""){
		$.post(validateURL, {"newsText": snip}, data => {
			console.log(data);

			data.sources.map(source => {
				links += `
				<li>${source.name} - <a href="${source.url}">${source.title}</a></li>
				`;
			});

			document.querySelector(".vresult").innerHTML = `
				<h1>Score: ${data.aScore}%</h1>
				<h1>This phrase was used ${data.no_of_sources} times in the past 3 months</h1>
				<h1>Links:</h1>
				<ul>${links}</ul>
			`;
		})
	}
}