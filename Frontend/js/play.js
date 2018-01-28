let baseURL = "http://10.5.61.44:8000/api";
let validateURL = baseURL + "/validate-news/";
let fakeURL = baseURL + "/fake-news/";
let reportURL = baseURL + "/report-news/";

const getFakeNews = () => {
	$.get(fakeURL, data => {
		document.querySelector(".list-group").innerHTML = "";
		console.log(data[0]);
		for(var i=0; i < data.length;i++){
			document.querySelector(".list-group").innerHTML += `
				<div class="list-group-item">
		            <h4 class="list-group-item-heading">${data[i].sourceName}</h4>
		            <p class="list-group-item-text"><a href="${data[i].sourceURL}">${data[i].title}</a></p>
				</div>
			`;
		}
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

const clearAll = () => {
	document.querySelector("#news-title").value = "";
	document.querySelector("#news-desc").value = "";
	document.querySelector("#news-source").value = "";
	document.querySelector("#news-url").value = "";
}

getFakeNews();