# using Redis for data science and data engineering

* Install Docker and Docker Compose https://docs.docker.com/compose/install/
* Clone this repo
* Create Github token via https://github.com/settings/tokens.  
* In `~/.bash_profile` set `export GITHUB_TOKEN="token-here"`.  Need it to deal with Github rate limiting https://developer.github.com/v3/#rate-limiting
* `docker-compose up --build -d --scale worker=2`
* Browse to http://localhost:5000/github to start data process
* Browse to http://localhost:5000/rq/ to view jobs running
* Browse to http://localhost:8888/ to use Jupyter Notebooks