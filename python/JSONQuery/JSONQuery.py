import json, re, logging, sys
from collections import namedtuple

#TODO refactor
json_query_finding = namedtuple('json_query_finding', 'current_json_path, queried_json_clause')

def json_format_compare(test_data, format_data, usedpath='', results =None,debugmode = 0, matchmode =0):
    '''json_format_compare
    accepts as input a test_data json variable
    and a format_data json variable
    and a debugmode variable
    usedpath and mismatches are for internal use only

    test_data is the json you want to compare against a particular format
    format_data is the json format with regex expressions for values

    results are either full matches in the test_data to the format_data if match mode is set to find matches
    or a list of mismatches if match mode is set to find mismatches
    '''

    if results == None:
        results = []
    if debugmode:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info("parsing test data"+ str(test_data))
    logging.info("parsing format data"+ str(format_data))
    for format_key in format_data.keys():
        logging.info("evaluating key:"+ format_key)
        current_json_path = usedpath+'/'+format_key
        try:
            test_value = test_data[format_key]
        except:
            logging.info("key not found at usedpath" + current_json_path)
            if not matchmode:
                results.append(json_query_finding(current_json_path,'key_not_found'))
                continue
            else:
                raise ValueError
        format_value = format_data[format_key]
        logging.info("format value for the key " +str(type(format_value)) + " "
                     + str(len(format_value))+ " " + str(format_value))
        logging.info("test value for the key: "+ str(type(test_value)) + " "
                     + str(len(test_value))+ " " + str(test_value))
        ## if the format value which is being compared with the test value, recurse
        if isinstance(format_value, dict):
            logging.info("recurse for " +str(format_value))
            json_format_compare(test_value, format_value, usedpath=current_json_path,
                                results=results, matchmode=matchmode,debugmode=debugmode)
        else:
            logging.info("comparing "+ str(format_value) + " " + str(test_value))
            match_result = re.match(format_value, test_value)
            if match_result:
                logging.info(format_value + " matches " + test_value)
                if matchmode:
                    logging.info("adding current json path to results: "+ current_json_path)
                    results.append(json_query_finding(current_json_path,test_value))
            else:
                logging.info(format_value + " does not match " + test_value)
                if not matchmode:
                    logging.info("adding current json path to results: "+ current_json_path)
                    results.append(json_query_finding(current_json_path,'mismatch'))
                else: ## partial matches are not okay
                    if matchmode == 2: # or mode
                        # this is a mismatch, but don't short circuit and exit because we're in or mode
                        pass
                    else: # and mode
                        return []
    return results
