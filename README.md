# TV News

## Goal of this repo
This repo aim to give guidelines for API writed from scratch.
Which may contains :
- frameworks
- tests
- CI / CD
- dockerization


## Operation of this API
This API works with *fastapi* and *postgres* services.
Postgres is initialized with CSV from __/app folder__.
And then an app shell accessible from __localhost:8080/__ uses api routes to display tv news.


## Enhancement
Deployment could be automated with kubernetes or swarm.
Display of news should of course be improved.