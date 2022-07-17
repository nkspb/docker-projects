Alpine-based image to download a file specified via $URL variable.<br/ ><br/ >
Usage:<br/ >
**docker run --mount type=volume,dst=/downloads/ -e URL="http://www.example.com" image_id**