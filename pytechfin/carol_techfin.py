from collections import defaultdict
import pandas as pd

# TODO: Add custom pipeline function from 
# https://github.com/rafarui/techfin-reprocess/blob/master/functions/custom_pipeline.py

# TODO: Add track_tasks function from
# https://github.com/rafarui/techfin-reprocess/blob/master/functions/carol_task.py

class CarolTechfin:
    """ Module to handle Carol's data.
        Needed add in Carol Module
    """

    def __init__(self, carol):
        self.carol = carol


    def get_staging_data(self, staging_name, 
            connector_name='protheus_carol', merge_records=True, columns=None, callback=None, max_workers=30):
        """ Get records from a staging table.

        Args:
            staging_name: `str`,
                Staging name to fetch parquet of
            merge_records: `bool`, default `True`
                This will keep only the most recent record exported. Sometimes there are updates and/or deletions and
                one should keep only the last records.
            columns: `list`, default `None`
                List of columns to fetch.
            callback: `callable`, default `None`
                Function to be called each downloaded file.
            max_workers: `int` default `30`
                Number of workers to use when downloading parquet files with pandas back-end.

        Returns: `pandas.DataFrame`
            DataFrame with the staging data.

        """

        # number of workers to download in parallel
        max_workers=max_workers

        # if you want to download a few columns, ["COLUMNS", "TO", "FETCH"]
        col=columns

        # maximum records to fetch. P.S.: only works if `max_workers=None`
        max_hits=None 

        # if metadata should be returned (mdmId, mdmLastUpdated, etc)
        return_metadata = True

        # if records with duplicated ids should be consolidated by pyCarol
        merge_records = merge_records

        #connector + staging table
        connector_name=connector_name
        staging = staging_name

        # file_pattern = '2021-02'
        file_pattern = None

        df = self.carol.staging.fetch_parquet(
                staging_name=staging, 
                connector_name=connector_name, 
                max_workers=max_workers, 
                columns=col, 
                merge_records=merge_records, 
                return_metadata=return_metadata, 
                max_hits=max_hits,
                callback=callback, file_pattern=file_pattern)

        return df


    def get_realtime_data(self, datamodel_name):
        """ Get records from a realtime datamodel

        Args:
            datamodel_name: ``str`
                Carol datamodel name

        Returns: `pandas.DataFrame`
            DataFrame with the realtime data.
        """

        filter = {
            "mustList": [
                {
                "mdmFilterType": "TYPE_FILTER",
                "mdmValue": datamodel_name+"Golden"      
                }
                ,
                {
                "mdmFilterType": "TERM_FILTER",
                "mdmKey":"mdmMergePending",
                "mdmValue": "false"
            },
            {
                "mdmFilterType": "RANGE_FILTER",
                "mdmKey": "mdmCounterForEntity",
                "mdmValue": [0,'null'],
                "mdmValuesQuery": {}
            }
            ]
        }

        result = self.carol.query(only_hits=True, page_size=1000, print_status=True).query(filter).go().results
        realtime = pd.DataFrame(result)

        return realtime

    def get_cds_data(self, datamodel_name, merge_records=True, columns = None, return_metadata = False, callback=None,  max_workers=30):
        """[summary]

        Args:
            datamodel_name: `str` optional
                Carol datamodel name
            merge_records: `bool` optional
                Merge cds data. Defaults to True.
            columns: `list of string`  optional
                Datamodel's columns. Defaults to None (return all columns).
            return_metadata: `bool`  optional 
                Return Carol metadata columns. Defaults to False.
            callback: `function` optional
                Callback function to handle data. Defaults to None.
            max_workers: `int` optional
                Number of worker used to process. Defaults to 30.

        Returns: `pandas.DataFrame`
            DataFrame with the staging data.
        """

        df = self.carol.datamodel.fetch_parquet(
            dm_name=datamodel_name, max_workers=max_workers,
            backend='pandas', return_dask_graph=False, columns=columns, merge_records=merge_records, 
            return_metadata=return_metadata, max_hits=None, callback=callback , cds=True,
            file_pattern=None)

        return df

    def get_datamodel_relationship_constraints(self, dm_list=None):
        """
        Create relationship between data models based on their  relationship constraints
        Args:
            carol: `pycarol.Carol`
                CarolAPI() object.
            prefix: 'str` default `DM_`
                prefix to add to the data model name. e.g., 
                if dm_name='mydatamoldel', the result will be "DM_mydatamoldel`
        Returns: `defaultdict(set)`
            dictionary { "dm1" : {"dm2": "field_dm_1" : "field_dm_2"}}
        """
        
        # find Relationship Constraints
        if dm_list is None:
            dms = self.carol.datamodel.get_all().template_dict.keys()
        else:
            dms = dm_list
        relationship_constraints = defaultdict(list)
        for i in dms:
            snap = self.carol.datamodel.get_by_name(i)['mdmRelationshipConstraints']
            if snap:
                relationship_constraints[i].append({i["mdmTargetEntityName"]:i["mdmSourceTargetFieldName"] for i in snap})
        return relationship_constraints

    def process_staging(self, stagings_list):
        """ Process a list of staging tables

        Args:
            stagings_list `list str`: List of stagings name
        """

        for staging_name in stagings_list:
            print(f'adding process staging task to staging: {staging_name} ')
            self.carol.cds_staging.process_data(staging_name, connector_name='protheus_carol', recursive_processing=False)
        print(f'see more in https://{self.carol.organization}.{self.carol.environment}/{self.carol.domain}/carol-ui/tasks')

    
    def get_carol_record_count(self):
        """ Get carol record count from tenant explore stats

        Returns:
            `dict`
                Dict with datamodels stats
        """
        response = self.carol.call_api(path=f'v1/dashboard/exploreStatistics?days=3', method='GET')

        return response["exploreStats"]
