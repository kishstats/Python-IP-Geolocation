In order to get the free [GeoLite2 Free Geolocation Data](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data), you must sign up and create an account. After filling in the signup form and logging in you should be able to access the downloads page. The URL should look something like the following (with `<account id>` being your actual account id):

```
https://www.maxmind.com/en/accounts/<account id>/geoip/downloads
```

Scroll down to the section that says "GeoLite2 City", then click "Download GZIP" in the right column.

Move the file to the `db` folder and unzip the file. Note: the name of file will vary depending on when you downloaded it. The database file is the file with the `mmdb` extension.

Extract the files
```bash
tar -xvzf GeoLite2-City_20230929.tar.gz
```