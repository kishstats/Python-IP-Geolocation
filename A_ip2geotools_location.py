from ip2geotools.databases.noncommercial import DbIpCity

ip_location = DbIpCity.get("98.155.130.10", api_key="free")

# ip_location.country: US
print(f"ip_location.country: {ip_location.country}")

# ip_location.region: Hawaii
print(f"ip_location.region: {ip_location.region}")

# ip_location.city: Kaneohe
print(f"ip_location.city: {ip_location.city}")

# ip_location.latitude: 21.418555
print(f"ip_location.latitude: {ip_location.latitude}")

# ip_location.longitude: -157.804184
print(f"ip_location.longitude: {ip_location.longitude}")
