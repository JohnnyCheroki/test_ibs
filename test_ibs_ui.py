import pytest
import requests
from expected_response import *
from dt_json import *
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_u1():
    request = requests.get('https://reqres.in/api/users?page=2')
    assert request.status_code == 200
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get("https://reqres.in/api/users?page=2")
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u2():
    request = requests.get('https://reqres.in/api/users/2')
    assert request.status_code == 200
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/users/2')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u2():
    request = requests.get('https://reqres.in/api/users/2')
    assert request.status_code == 200
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/users/2')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u3():
    request = requests.get('https://reqres.in/api/users/23')
    assert request.status_code == 404
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/users/23')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u4():
    request = requests.get('https://reqres.in/api/users/23')
    assert request.status_code == 404
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/users/23')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u5():
    request = requests.get('https://reqres.in/api/unknown/2')
    assert request.status_code == 200
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/unknown/2')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u6():
    request = requests.get('https://reqres.in/api/unknown/23')
    assert request.status_code == 404
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/unknown/23')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request

def test_u7():
    request = requests.get('https://reqres.in/api/users?delay=3')
    assert request.status_code == 200
    received_data = request.json()
    received_request = json.dumps(received_data, indent=4)
    browser = webdriver.Chrome()
    browser.get('https://reqres.in/api/users?delay=3')
    jf = browser.find_element(By.TAG_NAME, "body").text
    formatted_text = json.dumps(json.loads(jf), indent=4)
    assert formatted_text == received_request
