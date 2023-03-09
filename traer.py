import json
import datetime
import boto3
import requests

def traer(cantidad):
  url = 'https://api.fincaraiz.com.co/document/api/1.0/listing/search'
  data = {"filter":{"offer":{"slug":["sell"]},"path":"zona-chapinero bogota"},"fields":{"exclude":[],"facets":[],"include":["area","baths.id","baths.name","baths.slug","client.client_type","client.company_name","client.first_name","client.fr_client_id","client.last_name","client.logo.full_size","garages.name","is_new","locations.cities.fr_place_id","locations.cities.name","locations.cities.slug","locations.countries.fr_place_id","locations.countries.name","locations.countries.slug","locations.groups.name","locations.groups.slug","locations.groups.subgroups.name","locations.groups.subgroups.slug","locations.neighbourhoods.fr_place_id","locations.neighbourhoods.name","locations.neighbourhoods.slug","locations.states.fr_place_id","locations.states.name","locations.states.slug","locations.location_point","max_area","max_price","media.photos.list.image.full_size","media.photos.list.is_main","media.videos.list.is_main","media.videos.list.video","media.logo.full_size","min_area","min_price","offer.name","price","products.configuration.tag_id","products.configuration.tag_name","products.label","products.name","products.slug","property_id","property_type.name","fr_property_id","fr_parent_property_id","rooms.id","rooms.name","rooms.slug","stratum.name","title"],"limit":25,"offset":0,"ordering":[],"platform":41,"with_algorithm":True}}
  headers = {
      'Content-Type': 'application/json',
      'Connection': 'keep-alive',
  }
  response = requests.post(url, json=data, headers=headers)
  return response.text
    
    
    
def lambda1(event, context):
    print('--------------------------------------------VOY  A LLAMAR-------------------------------------------------------------------')
    datos = traer(30)
    print(f"------------------- datos es {datos} ---------------------------")
    client = boto3.client('s3')
    actual = datetime.datetime.now()
    nombre = f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}.txt"
    client.put_object(Body=datos, Bucket='landingxx', Key=nombre)
    return {
        'statusCode': 200,
        'body': json.dumps('Guarde los datos')
    }
  
 
