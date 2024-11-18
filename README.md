# PersonalSite

This is the application that generates my personal portfolio website
which can be found at [josephfoster.me](http://josephfoster.me).

It is a flask application that:

- Displays information about different coding projects that I have completed
- Generates pages about different countries I have visited
- Dynamically generates a page about a country of the user's choice using
  a Wikipedia API and the open weather API

This project is open source, use it as a template to build your own application
if you wish. Or check out this [free tutorial](https://youtu.be/mqhxxeeTbu0?si=OicLhr4NVffZhQWZ)
with techwithtim to start at the same place I did.

## Installation

The application can be viewed at the website mentioned above.

Alternatively the app can be run locally by following these steps:

1. clone the repo
2. add .api_keys.yaml to the project root
3. create api key at [open weather](https://openweathermap.org/api)
4. add open weather api key to .api_keys.yaml with the format:
   `open_weather: "your-key"`
5. build the docker image: `docker build -t flask-website .`
6. run the image: `docker run flask-website`
