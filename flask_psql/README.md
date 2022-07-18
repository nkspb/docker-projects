Flask app connected to host's PostgreSQL database<br /><br />
Usage:<br />
**docker run --network=host -p 5000:80 image_id**<br />
**docker run --network=host -p 5000:80 --mount type=bind,src=/srv/app/,dst=/srv/app/ image_id**<br />