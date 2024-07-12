from result_output import *
import sys
import json
import importlib.util
import urllib.request
from google.oauth2 import service_account
from pprint import pprint
from google.cloud import bigquery

class Activity():

    def testcase_check_BigQuery_Dataset_Name(self,test_object,credentials,project_id):
        testcase_description="Check BigQuery dataset name"
        expected_result="demo_bq"
        
        try:
            is_present = False
            actual = 'BigQuery dataset name is not '+ expected_result
            error =None
            try:
                client = bigquery.Client(credentials= credentials,project=project_id)
                datasets = list(client.list_datasets())
                if datasets:
                    for dataset in datasets:
                        if (dataset.dataset_id == expected_result):
                            is_present=True
                            actual=expected_result
                            break
            except Exception as e:
                is_present = False
                error=str(e)
                
            
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                if error != None:
                    test_object.update_eval_message({"testcase_check_BigQuery_Dataset_Name":error})
                return test_object.update_result(0,expected_result,actual,"Check BigQuery Dataset name","https://cloud.google.com/bigquery/docs/datasets-intro")   
                
        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.update_eval_message({"testcase_check_BigQuery_Dataset_Name":error})             

    def testcase_check_BigQuery_Table_Name(self,test_object,credentials,project_id):
        testcase_description="Check Bigquery Table name"
        dataset_id = 'demo_bq'
        expected_result="demo_table"

        try:
            is_present = False
            actual = 'BigQuery table is not '+ expected_result
            client = bigquery.Client(credentials= credentials,project=project_id)
            dataset_ref = client.dataset(dataset_id)
            tables = client.list_tables(dataset_ref)
            try:
                for table in tables:
                    if expected_result == table.table_id:
                        is_present=True
                        actual=expected_result
                        break
            except Exception as e1:
                pass
            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                return test_object.update_result(0,expected_result,actual,"Check BigQuery table Name","https://cloud.google.com/bigquery/docs/tables-intro")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_cloud_run_service_name"]=str(e)                

    def testcase_check_BigQuery_View_Name(self,test_object,credentials,project_id):
        testcase_description="Check Bigquery View name"
        dataset_id = 'demo_bq'
        expected_result="top_10_technologies"

        try:
            is_present = False
            actual = 'BigQuery View name is not '+ expected_result
            client = bigquery.Client(credentials= credentials,project=project_id)
            dataset_ref = client.dataset(dataset_id)
            tables = client.list_tables(dataset_ref)
            try:
                for table in tables:
                    if expected_result == table.table_id:
                        is_present=True
                        actual=expected_result
                        break
            except Exception as e1:
                pass

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                return test_object.update_result(0,expected_result,actual,"Check BigQuery View Name","https://cloud.google.com/bigquery/docs/views-intro")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_cloud_run_service_name"]=str(e)                

def start_tests(credentials, project_id, args):

    if "result_output" not in sys.modules:
        importlib.import_module("result_output")
    else:
        importlib.reload(sys.modules[ "result_output"])
    
    test_object=ResultOutput(args,Activity)
    challenge_test=Activity()
    challenge_test.testcase_check_BigQuery_Dataset_Name(test_object,credentials,project_id)
    challenge_test.testcase_check_BigQuery_Table_Name(test_object,credentials,project_id)
    challenge_test.testcase_check_BigQuery_View_Name(test_object,credentials,project_id)

    json.dumps(test_object.result_final(),indent=4)
    return test_object.result_final()

