import json, re, logging, sys

#TODO I will possibly make a marker for an AND match attempt and another marker for an OR match attempt
def json_format_compare(test_data, format_data, usedpath='', results =None,debugmode = 0, matchmode =0):
    '''json_parse
    accepts as input a test_data json variable
    and a format_data json variable
    and a debugmode variable
    usedpath and mismatches are for internal use only

    test_data is the json you want to compare against a particular format
    format_data is the json format with regex expressions for values

    return values are any paths to json keys which have a mismatch
    between the test_data value for those keys and the corresponding format_data
    or [] if no values are mismatched between test data and format

    If [] is returned then this is a JSON match with the search format
    which is used to specify variable criteria in a front end'''
    if results == None:
        print("clearing")
        results = []
    if debugmode:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info("parsing test data"+ str(test_data))
    logging.info("parsing format data"+ str(format_data))
    for format_key in format_data.keys():
        logging.info("evaluating key:"+ format_key)
        current_json_path = usedpath+'/'+format_key
        if format_key not in test_data:
            logging.info("key not found")
            logging.info("usedpath" + current_json_path)
            if not matchmode:
                results.append(current_json_path)
                continue
            else:
                raise ValueError
        format_value = format_data[format_key]
        test_value = test_data[format_key]
        logging.info("format value for the key " +str(type(format_value)) + " "
                     + str(len(format_value))+ " " + str(format_value))
        logging.info("test value for the key: "+ str(type(test_value)) + " "
                     + str(len(test_value))+ " " + str(test_value))
        ## if the format value which is being compared with the test value, recurse
        if isinstance(format_value, dict):
            logging.info("recurse for " +str(format_value))
            json_format_compare(test_value, format_value, usedpath=current_json_path,
                                results=results, matchmode=matchmode)
        else:
            logging.info("comparing "+ str(format_value) + " " + str(test_value))
            match_result = re.match(format_value, test_value)
            if match_result:
                logging.info(format_value + " matches " + test_value)
                if matchmode:
                    logging.info("adding current json path to results: "+ current_json_path)
                    results.append((current_json_path,test_value))
            else:
                logging.info(format_value + " does not match " + test_value)
                if not matchmode:
                    logging.info("adding current json path to results: "+ current_json_path)
                    results.append(current_json_path)
                else: ## partial matches are not okay
                    return []
    return results

test_json_str =         '{"hello": "1", "zap": {"h1": "one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}, "hello": ".*"}'
test_json = json.loads(test_json_str)
json_query_format = json.loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
print("mismatches", json_format_compare(test_json, json_query_format, debugmode=1))

print("matches", json_format_compare(test_json, json_query_format, matchmode=1, debugmode=1))
