import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/thecocktaildb/api/the-cocktail-db'

mcp = FastMCP('the-cocktail-db')

@mcp.tool()
def search_cocktail_by_name(s: Annotated[Union[str, None], Field(description='Search Cocktail Ingredient by Name')] = None) -> dict: 
    '''Search cocktails by name'''
    url = 'https://the-cocktail-db.p.rapidapi.com/search.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        's': s,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_by_ingredient(i: Annotated[Union[str, None], Field(description='Ingredient')] = None) -> dict: 
    '''Search by ingredient'''
    url = 'https://the-cocktail-db.p.rapidapi.com/filter.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'i': i,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_ingredient_by_name(i: Annotated[Union[str, None], Field(description='Ingredient Search Query')] = None) -> dict: 
    '''Search ingredient by name'''
    url = 'https://the-cocktail-db.p.rapidapi.com/search.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'i': i,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lookup_arandom_cocktail() -> dict: 
    '''Lookup a random cocktail'''
    url = 'https://the-cocktail-db.p.rapidapi.com/random.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lookup_full_cocktail_details_by_id(i: Annotated[Union[str, None], Field(description='Cocktail ID')] = None) -> dict: 
    '''Lookup full cocktail details by ID'''
    url = 'https://the-cocktail-db.p.rapidapi.com/lookup.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'i': i,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lookup_ingredient_by_id(iid: Annotated[Union[str, None], Field(description='Ingredient ID')] = None) -> dict: 
    '''Lookup ingredient by ID'''
    url = 'https://the-cocktail-db.p.rapidapi.com/lookup.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'iid': iid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lookup_aselection_of10_random_cocktails() -> dict: 
    '''Lookup a selection of 10 random cocktails'''
    url = 'https://the-cocktail-db.p.rapidapi.com/randomselection.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filter_by_category(c: Annotated[Union[str, None], Field(description='Values: (Cocktail, Ordinary_Drink)')] = None) -> dict: 
    '''Filter by Cocktail Category'''
    url = 'https://the-cocktail-db.p.rapidapi.com/filter.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'c': c,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filter_by_alcoholic(a: Annotated[Union[str, None], Field(description='Values: (Alcoholic, Non-Alcoholic)')] = None) -> dict: 
    '''Filter by alcoholic or non-alcoholic cocktail'''
    url = 'https://the-cocktail-db.p.rapidapi.com/filter.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'a': a,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filter_by_glass(c: Annotated[Union[str, None], Field(description='Values: (Cocktail_glass, Champagne_flute)')] = None) -> dict: 
    '''Filter by Cocktail Glass'''
    url = 'https://the-cocktail-db.p.rapidapi.com/filter.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'c': c,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filter_by_multi_ingredient(i: Annotated[str, Field(description='Values: list delimited ingredients')]) -> dict: 
    '''Filter by multi-ingredient'''
    url = 'https://the-cocktail-db.p.rapidapi.com/filter.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'i': i,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_the_ingredients() -> dict: 
    '''Get a list of the ingredients'''
    url = 'https://the-cocktail-db.p.rapidapi.com/list.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_the_alcoholic_filters() -> dict: 
    '''Get a list of all the alcoholic filters'''
    url = 'https://the-cocktail-db.p.rapidapi.com/list.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_the_glasses() -> dict: 
    '''Get a list of the glasses'''
    url = 'https://the-cocktail-db.p.rapidapi.com/list.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_the_categories() -> dict: 
    '''Get a list of all the categories'''
    url = 'https://the-cocktail-db.p.rapidapi.com/list.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_popular_cocktails() -> dict: 
    '''List Popular cocktails'''
    url = 'https://the-cocktail-db.p.rapidapi.com/popular.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_most_latest_cocktails() -> dict: 
    '''List most latest cocktails'''
    url = 'https://the-cocktail-db.p.rapidapi.com/latest.php'
    headers = {'x-rapidapi-host': 'the-cocktail-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
