/*
A KBase module: sample_spreadsheet
*/

module sample_spreadsheet {
    typedef structure {
        string input_name;
    } InputParams;

    typedef structure {
        string output_name;
    } Results;

    funcdef run_sample_spreadsheet(InputParams) returns (Results output) authentication required;

};
