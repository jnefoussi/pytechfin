import pandas

class CarolTechfin:
    """ Module to handle Carol's data.
        Needed add in Carol Module
    """

    def __init__(self, carol):
        self.carol = carol


    def get_staging_data(self, staging_name, connector_name='protheus_carol', merge_records=True, columns=None, callback=None, max_workers=30):
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

        df = self.carol.staging.fetch_parquet(staging_name=staging, 
                                connector_name=connector_name, 
                                max_workers=max_workers, 
                                columns=col, 
                                merge_records=merge_records, 
                                return_metadata=return_metadata, 
                                max_hits=max_hits,
                                callback=callback, file_pattern=file_pattern)
        return df

    def get_realtime_data(self, datamodel_name):
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
        realTime = pandas.DataFrame(result)
        # print(datamodel_name + ' ' + str(realTime.shape))
        return realTime