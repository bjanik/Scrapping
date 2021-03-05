# WEB Scrapping

Project made during Simplon course

This program scraps the hendonmob.com poker All Time Money list and saves in a database the top 100 winning players.

## How to run it

You need to have Docker installed on your system. To do so, please refer to Docker documentation https://docs.docker.com/get-docker/

1. Clone the project `https://github.com/bjanik/Scrapping`
2. Move to the clone directory `cd Scrapping`
3. Run locally with `docker-compose up`
4. Access to the API on `localhost:3000`

## API endpoints

/players: endpoint returns the top 100 winning players. It accept several arguments:
1. ranking: Returns players with a ranking equal or higher to the specified one
2. country: Returns players from specified country
3. money_won: Returns players than won more money than specified value
4. highest_win: Returns players who won more in a single tournament than specified value


## Example
Daniel Negreanu is the only Canadian player in the top 10 winning players.
![Scrapper_endpoint](https://user-images.githubusercontent.com/25487297/110122194-9495c180-7dbf-11eb-837a-f7d831c3892b.png)

