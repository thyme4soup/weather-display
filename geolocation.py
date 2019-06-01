
import requests, json

def get_geo():
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' + my_ip + '.json')
    geo_data = geo_request.json()
    lat = geo_data['latitude']
    lon = geo_data['longitude']

    return lat, lon