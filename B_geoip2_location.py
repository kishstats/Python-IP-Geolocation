import geoip2.database

reader = geoip2.database.Reader("./db/GeoLite2-City_20230929/GeoLite2-City.mmdb")

response = reader.city("98.155.130.10")

# response.country.iso_code: US
print("response.country.iso_code: {}".format(response.country.iso_code))

# response.subdivisions.most_specific.name: Hawaii
print(
    "response.subdivisions.most_specific.name: {}".format(
        response.subdivisions.most_specific.name
    )
)

# response.subdivisions.most_specific.iso_code: HI
print(
    "response.subdivisions.most_specific.iso_code: {}".format(
        response.subdivisions.most_specific.iso_code
    )
)

# response.city.name: Kailua
print("response.city.name: {}".format(response.city.name))

# response.postal.code: 96734
print("response.postal.code: {}".format(response.postal.code))

reader.close()
