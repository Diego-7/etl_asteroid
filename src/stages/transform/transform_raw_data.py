# pylint: disable=multi-statements

from typing import List, Dict
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract
from src.errors.transform_error import TrasformError


class TransformRawData:
    
    def transform(self, extract_contract: ExtractContract) -> TransformContract:
       try: 
        transformed_information = self.__filter_and_transform_data(extract_contract)
        transformed_data_contract = TransformContract(
            load_content = transformed_information
        )
        return transformed_data_contract
       except Exception as exception: 
           raise TrasformError(str(exception)) from exception
       
    def __filter_and_transform_data(self, extract_contract: ExtractContract) -> List[Dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content
        transformed_information = []
        
        for data in data_content:
          pass
        #return transformed_data