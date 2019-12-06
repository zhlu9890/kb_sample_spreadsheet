# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import quote_sheetname
#END_HEADER


class sample_spreadsheet:
    '''
    Module Name:
    sample_spreadsheet

    Module Description:
    A KBase module: sample_spreadsheet
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_sample_spreadsheet(self, ctx, InputParams):
        """
        :param InputParams: instance of type "InputParams" -> structure:
           parameter "input_name" of String
        :returns: instance of type "Results" -> structure: parameter
           "output_name" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_sample_spreadsheet
        output = {
            'output_name': 'test'
        }
        #END run_sample_spreadsheet

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_sample_spreadsheet return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
