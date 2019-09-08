import os
from unittest.mock import Mock, patch

import pytest
import requests

from ns import NSAPI

key = os.environ.get('PRIMARY_KEY')

@pytest.fixture()
def ns():
    return NSAPI(key)

@patch('ns.NSAPI._request')
def test_all_stations(mock_response, ns):
    mock_response.return_value = {"links": {},"payload": [{"sporen": [],"synoniemen": [],"heeftFaciliteiten": "true","heeftVertrektijden": "true","heeftReisassistentie": "false","code": "STP","namen": {"lang": "London St. Pancras Int.","kort": "London StP","middel": "London St. P Int"},"stationType": "MEGA_STATION","land": "GB","UICCode": "7015400","lat": 51.531437,"lng": -0.126136,"radius": 1,"naderenRadius": 1,"EVACode": "7004428"}], "meta": {}}
    response = ns.get_all_stations()
    assert len(response) == 1
    assert response[0].code == 'STP'


@patch('ns.NSAPI._request')
def test_trip_price(mock_response, ns):
    mock_response.return_value = {"priceOptions": [{"type": "FIXED_PRICE","tariefEenheden": 0,"prices": [{"classType": "NONE","discountType": "NONE","productType": "RAILRUNNER","price": 250.0,"supplements": {}}, {"classType": "NONE","discountType": "NONE","productType": "SUPPLEMENT_ICE_INTERNATIONAL","price": 260.0,"supplements": {}}, {"classType": "NONE","discountType": "NONE","productType": "SUPPLEMENT_SINGLE_USE_OV_CHIPKAART","price": 100.0,"supplements": {}}]}]}
    response = ns.get_trip_price('UT', 'ASD')
    assert len(response) == 1
    assert response[0].type == 'FIXED_PRICE'
    assert len(response[0].prices) == 3


def test_invalid_key():
    ns = NSAPI('invalidkey')
    with pytest.raises(requests.exceptions.HTTPError):
        ns.get_all_stations()
