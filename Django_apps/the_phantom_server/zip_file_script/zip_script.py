import os
import shutil
import json
from django.conf import settings
import geopandas as gpd
import pandas as pd
import json
from shapely.geometry import mapping
from django.contrib import messages
from dbfread import DBF
import zipfile
from django.conf import settings


class StoreData:
    def __init__(self, cursor, zip_file_path) -> None:
        self.cursor = cursor
        self.zip_file_path = zip_file_path

    def create_dbf_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mft_rrc_texas_gov_dbf_table (
                id SERIAL PRIMARY KEY, 
                TPMS_ID VARCHAR(255),
                OPER_LINK VARCHAR(255),
                OPS_ID VARCHAR(255),
                P5_NUM VARCHAR(255),
                OPER_NM VARCHAR(255),
                SYS_NM VARCHAR(255),
                SUBSYS_NM VARCHAR(255),
                T4PERMIT VARCHAR(255),
                DIAMETER VARCHAR(255),
                COMMODITY1 VARCHAR(255),
                COMMODITY2 VARCHAR(255),
                COMMODITY3 VARCHAR(255),
                CMDTY_DESC VARCHAR(255),
                INTERSTATE VARCHAR(255),
                STATUS_CD VARCHAR(255),
                QUALITY_CD VARCHAR(255),
                SYSTYPE VARCHAR(255),
                COUNTY VARCHAR(255),
                COM_CARRIE VARCHAR(255),
                PLINE_ID VARCHAR(255),
                SYS_ID VARCHAR(255),
                NPMS_SYS_I VARCHAR(255),
                ALBERS_MIL VARCHAR(255),
                LENGTH VARCHAR(255)
            )
        """
        )
        
    def create_shp_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mft_rrc_texas_gov_shp_table (
                id SERIAL PRIMARY KEY,
                TPMS_ID VARCHAR(255),
                OPER_LINK VARCHAR(255),
                OPS_ID VARCHAR(255),
                P5_NUM VARCHAR(255),
                OPER_NM VARCHAR(255),
                SYS_NM VARCHAR(255),
                SUBSYS_NM VARCHAR(255),
                T4PERMIT VARCHAR(255),
                DIAMETER VARCHAR(255),
                COMMODITY1 VARCHAR(255),
                COMMODITY2 VARCHAR(255),
                COMMODITY3 VARCHAR(255),
                CMDTY_DESC VARCHAR(255),
                INTERSTATE VARCHAR(255),
                STATUS_CD VARCHAR(255),
                QUALITY_CD VARCHAR(255),
                SYSTYPE VARCHAR(255),
                COUNTY VARCHAR(255),
                COM_CARRIE VARCHAR(255),
                PLINE_ID VARCHAR(255),
                SYS_ID VARCHAR(255),
                NPMS_SYS_I VARCHAR(255),
                ALBERS_MIL VARCHAR(255),
                LENGTH VARCHAR(255),
                geometry JSON
            )
        """
        )

    def store_data_dbf_data(self, data):
        self.cursor.execute(
            """
            INSERT INTO mft_rrc_texas_gov_dbf_table (
                TPMS_ID,
                OPER_LINK,
                OPS_ID,
                P5_NUM,
                OPER_NM,
                SYS_NM,
                SUBSYS_NM,
                T4PERMIT,
                DIAMETER,
                COMMODITY1,
                COMMODITY2,
                COMMODITY3,
                CMDTY_DESC,
                INTERSTATE,
                STATUS_CD,
                QUALITY_CD,
                SYSTYPE,
                COUNTY,
                COM_CARRIE,
                PLINE_ID ,
                SYS_ID,
                NPMS_SYS_I,
                ALBERS_MIL,
                LENGTH
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            data,
        )
        
    def store_data_shp_data(self, data):
        self.cursor.execute(
            """
            INSERT INTO mft_rrc_texas_gov_shp_table (
                TPMS_ID,
                OPER_LINK,
                OPS_ID,
                P5_NUM,
                OPER_NM,
                SYS_NM,
                SUBSYS_NM,
                T4PERMIT,
                DIAMETER,
                COMMODITY1,
                COMMODITY2,
                COMMODITY3,
                CMDTY_DESC,
                INTERSTATE,
                STATUS_CD,
                QUALITY_CD,
                SYSTYPE,
                COUNTY,
                COM_CARRIE,
                PLINE_ID ,
                SYS_ID,
                NPMS_SYS_I,
                ALBERS_MIL,
                LENGTH, 
                geometry
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            data,
        )

    def extract_data(self):
        file_name = os.path.basename(self.zip_file_path).split(".")[0]
        extract_dir = settings.BASE_DIR + f"/downloads/{file_name}/"
        with zipfile.ZipFile(self.zip_file_path, "r") as zip_ref:
            file_names = zip_ref.namelist()
            zip_ref.extractall(extract_dir)

        files = os.listdir(extract_dir)
        for file in files:
            if file.endswith(".zip"):
                zip_file = os.path.splitext(file)[0]
                file_path = extract_dir + f"{zip_file}.zip"
                file_extract_path = extract_dir + f"{zip_file}/"
                with zipfile.ZipFile(file_path, "r") as zip_ref:
                    file_names = zip_ref.namelist()
                    zip_ref.extractall(file_extract_path)
                extracted_files = os.listdir(file_extract_path)
                for file in extracted_files:
                    if file.endswith(".dbf"):
                        dbf_file_name = os.path.splitext(file)[0]
                        dbf_file_path = file_extract_path + f"{dbf_file_name}.dbf"
                        dbf = DBF(dbf_file_path, encoding="utf-8")
                        for record in dbf:
                            value = []
                            for i in record.keys():
                                value.append(record.get(i))
                            self.store_data_dbf_data(value)
                            print('inserted dbf data successfully')
                            
                    elif file.endswith(".shp"):
                        shp_file_name = os.path.splitext(file)[0]
                        shp_file_path = file_extract_path + f"{shp_file_name}.shp"
                        shp = gpd.read_file(shp_file_path)
                        data_dict = shp.to_dict(orient='records')
                        for record in data_dict:
                            value = []
                            for i in record.keys():
                                if i == 'geometry':
                                    continue
                                value.append(record.get(i))
                            value.append(json.dumps(mapping(record.get('geometry'))))
                            self.store_data_shp_data(value)
                            print('inserted shp data successfully')

        return True
    
    def remove_exist_folder(self):
        file_path = self.zip_file_path
        file_name = os.path.basename(self.zip_file_path).split(".")[0]
        folder_path = settings.BASE_DIR + f"/downloads/{file_name}"
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder {folder_path} deleted successfully.")
        else:
            print(f"Folder {folder_path} not found.")
            
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print(f"File {file_path} not found.")


class SHP_DATA:
    def __init__(self, cursor, zip_file_path) -> None:
        self.cursor = cursor
        self.zip_file_path = zip_file_path
        
    def get_shp_data(self):
        query = """
        SELECT * FROM mft_rrc_texas_gov_shp_table
        """
        with self.cursor as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        
    def extract_shp_data(self):

        dfs = []
        file_name = os.path.basename(self.zip_file_path).split(".")[0]
        extract_dir = settings.BASE_DIR + f"/downloads/{file_name}/"
        # with zipfile.ZipFile(self.zip_file_path, "r") as zip_ref:
        #     file_names = zip_ref.namelist()
        #     zip_ref.extractall(extract_dir)

        files = os.listdir(extract_dir)
        for file in files:
            if file.endswith(".zip"):
                zip_file = os.path.splitext(file)[0]
                # file_path = extract_dir + f"{zip_file}.zip"
                file_extract_path = extract_dir + f"{zip_file}/"
                # with zipfile.ZipFile(file_path, "r") as zip_ref:
                #     file_names = zip_ref.namelist()
                #     zip_ref.extractall(file_extract_path)
                extracted_files = os.listdir(file_extract_path)
                for file in extracted_files:
                    if file.endswith(".shp"):
                        shp_file_name = os.path.splitext(file)[0]
                        shp_file_path = file_extract_path + f"{shp_file_name}.shp"
                        
                        # shp = gpd.read_file(shp_file_path)
                        # dfs.extend(shp.to_dict(orient='records'))
            else:
                zip_file = os.path.splitext(file)[0]
                file_extract_path = extract_dir + f"{zip_file}/"
                extracted_files = os.listdir(file_extract_path)
                for file in extracted_files:
                    if file.endswith(".shp"):
                        shp_file_name = os.path.splitext(file)[0]
                        shp_file_path = file_extract_path + f"{shp_file_name}.shp"
                            
                    
                        
                        shp = gpd.read_file(shp_file_path)
                        dfs.extend(shp.to_dict(orient='records'))
        return dfs


class ReadSHP:
    
    def __init__(self, folder):
        self.folder = folder
        
    def read_shp(self):
        items = os.listdir(self.folder)[:3]
        dfs = []
        for item in items:
            file_extract_path = self.folder + f"/{item}/"
            extracted_files = os.listdir(file_extract_path)
            for file in extracted_files:
                if file.endswith(".shp"):
                    shp_file_name = os.path.splitext(file)[0]
                    shp_file_path = file_extract_path + f"{shp_file_name}.shp"
                    shp = gpd.read_file(shp_file_path)
                    dfs.extend(shp.to_dict(orient='records'))
        return dfs