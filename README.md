
### Project summary:
  
      फrji, is a RESTful service aimed at reducing the circulation of fake news. We decided to make a RESTful service instead of a regular application because, fake news is being spread on platforms which are already being used by consumers. Creating another such platform will not have as big an impact. But, on the other hand, a RESTful service can be used by existing as well as future social platforms. Also, since this is a developer tool, the fake news will be filtered before reaching the end-users.

We have devised our own algorithm which assigns a score (percentage) to any given snippet of news. The criteria used in this scoring involves ‘number of occurrences of the snippet’, ‘time of publication’, ‘quality of the websites it occurs on’ and ‘manually flagging fake news’.  This ‘score’ along with remarks and other data are sent as response in json format. The developers who use this service can modify their views based on the score or the remarks. 

We have also created a portal where people can voluntarily upload the fake news snippets that they might have encountered. Along with other details like source, url etc. This is a part of the manual flagging of fake news.

### End-points

Validate-news : Takes a “news snippet” and Returns a percentage score with remarks and other details.
Report-fake-news: Takes a “news snippet”, “sourceName”, “sourceURL” and Stores it in out database.
Get-fake-news: Returns a list of recently reported fake news.


### User flow
Users can copy paste the news which they want to validate on our API
The copy pasted news will be validated and a legitimacy score will be shown based on an algorithm
Also, all the occurrences over the web and on some of the known media sites will be displayed.
User can manually report fake news if they have the surety of it.
The fake news reported will be shown on a news feed in the API.

 ### Future Enhancements

Automatically alerting concerned authorities if a certain fake news is gaining a lot of outrage.
Memefying the fake news and publishing it on social media to spread awareness.

