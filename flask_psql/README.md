Flask app connected to host's PostgreSQL database<br /><br />
Usage:<br />
**docker run --network=host -p 5000:80 --mount type=bind,src=/srv/app/,dst=/srv/app 4f4952b4dd5b**