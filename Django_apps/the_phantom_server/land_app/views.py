from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import LeaseholdUnit
import matplotlib as mpl  # add this line
mpl.use('Agg')  # add this line
from bokeh.models import HoverTool
import matplotlib.pyplot as plt
import contextily as ctx
from io import BytesIO
import base64
import urllib
import geopandas as gpd
import pandas as pd
from shapely import wkb
import base64
from holoviews import opts
import holoviews as hv
import geoviews as gv
from bokeh.embed import components
import os
from psycopg2 import connect
from sqlalchemy import create_engine, text
from cartopy import crs as ccrs
import io

import os
from google.google_drive import GoogleDriveService, GoogleDriveAPI
from django.http import HttpResponseBadRequest
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import Flow
#from googleapiclient.discovery import build
import geopandas as gpd
from datetime import datetime
# from .tasks import store_zip_file_data
from django_descope.models import DescopeUser
import shutil
import logging


logger = logging.getLogger(__name__)




hv.extension('bokeh')


def hover_feature(columns):
    tooltips = [(col, f"@{col}") for col in columns]
    hover_tool = HoverTool(tooltips=tooltips)
    return hover_tool

def color_feature(col_name):
    return col_name

def get_non_geom_columns(df):
    non_geom_columns = [col for col in df.columns if col != 'geometry']
    return non_geom_columns



def map_sqlview(request):
    # Retrieve the database URL from environment variables
    DEV_DATABASE_URL = os.getenv('DEV_DATABASE_URL')

    # Ensure the URL is not None before proceeding
    if DEV_DATABASE_URL is None:
        raise ValueError("DEV_DATABASE_URL environment variable is not set")

    # Append the database name to the URL
    DEV_DATABASE_URL += 'gis_db'

    # Create the SQLAlchemy engine
    engine_db = create_engine(DEV_DATABASE_URL)

    # Establish a connection to the PostgreSQL database
    connection = engine_db.connect()

    # Print the engine details
    print(engine_db)

    # Specify your SQL query
    sql_query = "SELECT * FROM leasehold_unit"

    # Execute the query and retrieve the results into a DataFrame
    dataframe = pd.read_sql_query(sql_query, connection)

    #queryset = LeaseholdUnit.objects.values()
    dataframe =pd.read_sql_query(sql_query,engine_db)

    # Convert 'gid' column to numeric (assuming it's a numerical column)
    """
    dataframe['gid'] = pd.to_numeric(dataframe['gid'], errors='coerce')
    dataframe = dataframe[dataframe['gid'].notna()]
    # replace 'col_name_1', 'col_name_2', etc. with your column names"""
    #numeric_columns = ['unit_no', 'un_gma', 'nma_hbp']
    #for col in numeric_columns:
    #    dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')
    #converts its hexadecimal representation back to the original geom object using wkb.loads(geom.hex). If the geom object is None, it returns None.

    geometry = gpd.GeoSeries(dataframe['geometry'].apply(lambda geom: wkb.loads(geom, hex=True) if geom else None))
    dataframe = dataframe.fillna(0)  # Fills all NaN with 0
    #(print(dataframe.dtypes))
    dataframe = dataframe.drop(['geometry','nma_term','comment'], axis=1)
    (print(dataframe.dtypes))
    #create a geopandas dataframe dynamic or static
    #geometries = gpd.read_file('../../assets/boundaries/boundaries.shp')
    #referendum = pd.read_csv('../../assets/referendum.csv')
    #gdf = gpd.GeoDataFrame(pd.merge(geometries, referendum))
    # You can set your data to the NAD 27 system using its EPSG code.
    # The common EPSG code for NAD 27 is 'EPSG:4267'. NAD 83 = 4269For example:
    # gdf = gpd.GeoDataFrame(dataframe, geometry=geometry, crs='EPSG:4267')

    gdf = gpd.GeoDataFrame(dataframe, geometry=geometry)
    #gdf = gdf.to_crs('EPSG:3857')
    print(gdf.crs)
    bounds = gdf.geometry.bounds
    print("min lon:", bounds.minx.min(), "max lon:", bounds.maxx.max())
    print("min lat:", bounds.miny.min(), "max lat:", bounds.maxy.max())
    gdf.to_csv('/Users/jongrottis/Documents/gdf.csv', index=False)
    hover_columns = get_non_geom_columns(dataframe)

    #color_column = color_feature('gid')
    # Under the hood, HoloViews uses a system of composing graphical components with * and + operators,
    # which allows you to quickly and easily combine various elements.
    # The * operator in this context is used to overlay the geo_data on top of the CartoLight tileset.
    # The result would be a map using CartoLight base tiles with geo_data overlaid on top.
    gdf.crs = ccrs.PlateCarree()
    #gdf = gdf.to_crs(ccrs.PlateCarree())
    gv_data = gv.Dataset(gdf, vdims=hover_columns)

    # Create the CartoLight tiles
    tiles = gv.tile_sources.CartoLight()

    # Create Polygons element
    polygons = gv.Polygons(gv_data).opts(
        tools=['hover'], width=800, height=600, color='yellow', toolbar='above'
    )

    # Combine tiles and polygons
    gv_obj = tiles * polygons

    # Use Bokeh to get the script and HTML div components for embedding
    script, div = components(hv.render(gv_obj))


    return render(request, 'map_view.html', {'script': script, 'div': div})

def map_view(request):
    queryset = LeaseholdUnit.objects.values()
    dataframe = pd.DataFrame.from_records(queryset)

    # Convert 'gid' column to numeric (assuming it's a numerical column)
    """
    dataframe['gid'] = pd.to_numeric(dataframe['gid'], errors='coerce')
    dataframe = dataframe[dataframe['gid'].notna()]
    # replace 'col_name_1', 'col_name_2', etc. with your column names"""
    numeric_columns = ['unit_no', 'un_gma', 'nma_hbp']
    for col in numeric_columns:
        dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')
    #converts its hexadecimal representation back to the original geom object using wkb.loads(geom.hex). If the geom object is None, it returns None.
    geometry = gpd.GeoSeries(dataframe['geometry'].apply(lambda geom: wkb.loads(geom.hex) if geom else None))
    dataframe = dataframe.fillna(0)  # Fills all NaN with 0
    #(print(dataframe.dtypes))
    dataframe = dataframe.drop(['geometry','nma_term','comment'], axis=1)
    (print(dataframe.dtypes))
    #create a geopandas dataframe dynamic or static
    #geometries = gpd.read_file('../../assets/boundaries/boundaries.shp')
    #referendum = pd.read_csv('../../assets/referendum.csv')
    #gdf = gpd.GeoDataFrame(pd.merge(geometries, referendum))
    # You can set your data to the NAD 27 system using its EPSG code.
    # The common EPSG code for NAD 27 is 'EPSG:4267'. NAD 83 = 4269For example:
    # gdf = gpd.GeoDataFrame(dataframe, geometry=geometry, crs='EPSG:4267')

    gdf = gpd.GeoDataFrame(dataframe, geometry=geometry)
    #gdf = gdf.to_crs('EPSG:3857')
    print(gdf.crs)
    bounds = gdf.geometry.bounds
    print("min lon:", bounds.minx.min(), "max lon:", bounds.maxx.max())
    print("min lat:", bounds.miny.min(), "max lat:", bounds.maxy.max())
    gdf.to_csv('/Users/jongrottis/Documents/gdf.csv', index=False)
    hover_columns = get_non_geom_columns(dataframe)

    #color_column = color_feature('gid')
    # Under the hood, HoloViews uses a system of composing graphical components with * and + operators,
    # which allows you to quickly and easily combine various elements.
    # The * operator in this context is used to overlay the geo_data on top of the CartoLight tileset.
    # The result would be a map using CartoLight base tiles with geo_data overlaid on top.
    gv_obj = gv.tile_sources.CartoLight()*gv.Polygons(gdf, vdims=hover_columns).opts(
        tools=['hover'], width=800, height=600, color='yellow',
        toolbar='above'
    )
    # Use Bokeh to get the script and HTML div components for embedding
    script, div = components(hv.render(gv_obj))


    return render(request, 'map_view.html', {'script': script, 'div': div})


"""
def map_view(request):
    queryset = LeaseholdUnit.objects.values()
    dataframe = pd.DataFrame.from_records(queryset)
    geometry = gpd.GeoSeries(dataframe['geom'].apply(lambda geom: wkb.loads(geom.hex) if geom else None))
    dataframe = dataframe.drop('geom', axis=1)
    gdf = gpd.GeoDataFrame(dataframe, geometry=geometry, crs='EPSG:3857')

    ax = gdf.plot(figsize=(10, 10))
    ctx.add_basemap(ax, url=ctx.providers.Stamen.TonerLite)
    fig = ax.get_figure()

    buf = BytesIO()
    plt.savefig(buf, format='PNG')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string.decode('utf-8'))

    return render(request, 'map_view.html', {'data': uri})
    
    """
    

# @login_required
# def download_request(request):
#     context = {}
#     if f"{settings.DESCOPE_IS_STORE_DATA_ROLE}" not in request.user.session_token.get('roles'):
#         context[f"{settings.DESCOPE_IS_STORE_DATA_ROLE}"] = False
#     else:
        
#         if 'credentials' not in request.session:
#             authorization = GoogleDriveAPI().authenticate()
#             if authorization.get('authorization_url'):  
#                 return redirect(authorization.get('authorization_url'))        
        
#         credentials = Credentials( **request.session['credentials'])
#         service = build("drive", "v3", credentials=credentials)
#         folder_name = settings.GOOGLE_DRIVE_FOLDER
#         folder_ids = get_folder_id_by_name(service, folder_name)
#         files = []
#         for folder_id in folder_ids:
#             results = service.files().list(q=f"'{folder_id['id']}' in parents", fields="files(id, name)").execute()
#             files.extend(results.get('files'))
#         request.session['credentials'] = GoogleDriveAPI().credentials_to_dict(credentials)
#         auth_user = DescopeUser.objects.using('default').get(username = request.user.username)
        
#         store_zip = store_zip_file.objects.filter(user=auth_user)
        
#         processed_ids = set()
#         for file in files:
#             for data in store_zip:
#                 if file['id'] == data.file_id:
#                     if data.is_process or data.is_complete:
#                         processed_ids.add(file['id'])
#         context = {}
#         context['files']= files
#         context['is_store_data'] = True
#         context['store_zip'] = store_zip
#         context['processed_ids'] = processed_ids
#         if request.method == "POST":
#             id = request.POST.get("id", None)
#             file_details = service.files().get(fileId=id).execute()
#             files_data = service.files().get_media(fileId=id)
#             file_path = settings.BASE_DIR + f'/downloads/{file_details['name']}'
#             try:
#                 fh = io.FileIO(file_path, 'wb')
#                 downloader = io.BytesIO()
#                 downloader.write(files_data.execute())
#                 fh.write(downloader.getvalue())
#                 fh.close()
#             except Exception as e:
#                 print(str(e))
            
#             try:
#                 store_zip_file.objects.using('third_db').create(
#                     user=auth_user,
#                     file_id = id,
#                     file_name = file_details['name'],
#                     is_process=True,
#                     process_at = datetime.now()
#                 )
#                 store_zip_file_data.delay(auth_user.username, id, file_path)
#             except Exception as e:
#                 print(str(e))
#             return render(request, "demo.html", context)  
#     return render(request, "demo.html", context)


# def google_callback(request):
#     code = request.GET.get("code")
#     if not code:
#         return HttpResponseBadRequest("Missing code parameter")
    
#     flow = Flow.from_client_secrets_file(
#         "client_secret_217617410571-ghl2fdushp3fl79nqe57frhkn08kmhqe.apps.googleusercontent.com.json",
#         scopes=["https://www.googleapis.com/auth/drive"],
#         redirect_uri="http://localhost:8000/auth/google/callback",
#     )
#     flow.fetch_token(code=code)
#     credentials = flow.credentials
#     google_cred = GoogleDriveAPI().credentials_to_dict(credentials)
#     request.session['credentials'] = google_cred
#     return redirect("download_request")

# def get_folder_id_by_name(service, folder_name):
#     results = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'",
#                                     fields="files(id)").execute()
#     items = results.get('files', [])
#     if not items:
#         return None
#     else:
#         return items

