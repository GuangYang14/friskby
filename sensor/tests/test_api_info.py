import random
import json

from django.utils import timezone
from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from rest_framework import status

from sensor.models import *
from .context import TestContext


class SensorInfoTest(TestCase):
    def setUp(self):
        self.context = TestContext()

    def test_get_list(self):
        client = Client( )

        # Missing data
        response = client.get("/sensor/api/sensorinfo/")
        self.assertEqual( response.status_code , status.HTTP_200_OK , response.data)
        sensor_list = response.data
        sensor0 = sensor_list[0]
        self.assertEqual( sensor0["data_type"] , "TEST" )
        loc = sensor0["location"]
        self.assertEqual( loc , {"id" : 1 , "name" : "Ulriken" , "latitude" : 200 , "longitude" : 120 , "altitude" : 600})

        dev = sensor0["parent_device"]
        #self.assertEqual( dev , {"id" : 1 , "name" : "HP-X123" , "company" : {"id" : 1 , "name" : "Hewlett Packard"} } )

        sensor_type = sensor0["sensor_type"]
        self.assertEqual( sensor_type["product_name"] , "XX12762 Turbo" ) 
        
        self.assertEqual( sensor_type["min_value"] , 0 )
        self.assertEqual( sensor_type["max_value"] , 100 )


    def test_get(self):
        client = Client( )

        response = client.get("/sensor/api/sensorinfo/XYZ/")
        self.assertEqual( response.status_code , status.HTTP_404_NOT_FOUND )

        response = client.get("/sensor/api/sensorinfo/TEMP:XX/")
        self.assertEqual( response.status_code , status.HTTP_200_OK )

        sensor0 = response.data
        loc = sensor0["location"]
        self.assertEqual( loc , {"id" : 1 , "name" : "Ulriken" , "latitude" : 200 , "longitude" : 120 , "altitude" : 600})

        dev = sensor0["parent_device"]
        #self.assertEqual( dev , {"id" : 1 , "name" : "HP-X123" , "company" : {"id" : 1 , "name" : "Hewlett Packard"} } )

        sensor_type = sensor0["sensor_type"]
        self.assertEqual( sensor_type["measurement_type"] , {"id" : 1 , "name" : "Temperature"} ) 
        self.assertEqual( sensor_type["min_value"] , 0 )
        self.assertEqual( sensor_type["max_value"] , 100 )

        
        response = client.get("/sensor/api/sensorinfo/HUM:XX/")
        self.assertEqual( response.status_code , status.HTTP_200_OK )
        sensor0 = response.data
        self.assertEqual( sensor0["data_type"] , "RAWDATA" )