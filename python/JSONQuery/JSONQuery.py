import json, re, logging, sys

def json_format_compare(test_data, format_data, usedpath='', mismatches =[], matches = [],debugmode = 0, matchmode =0):
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
    if debugmode:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info("parsing test data"+ str(test_data))
    logging.info("parsing format data"+ str(format_data))
    for format_key in format_data.keys():
        logging.info("evaluating key:"+ format_key)
        if format_key not in test_data:
            logging.info("key not found")
            logging.info("usedpath" + usedpath + '/' + format_key)
            mismatches.append(usedpath + '/' + format_key)
            continue
        logging.info("format value for the key" +str(type(format_data[format_key]))
                     + str(len(format_data[format_key]))+ str(format_data[format_key]))
        logging.info("test value for the key"+ str(type(test_data[format_key]))
                     + str(len(test_data[format_key]))+ str(test_data[format_key]))
        if isinstance(format_data[format_key], dict):
            logging.info("recurse for " +str(format_data[format_key]))
            json_format_compare(test_data[format_key], format_data[format_key], usedpath + '/' + format_key, mismatches, matchmode=matchmode)
        else:
            logging.info("comparing "+ str(format_data[format_key])+ str(test_data[format_key]))
            findres = re.match(format_data[format_key], test_data[format_key])
            if findres:
                if matchmode:
                    logging.info("found")
                    logging.info("usedpath"+ usedpath+'/'+format_key)
                    matches.append([usedpath+'/'+format_key,test_data[format_key]])
            else:
                if not matchmode:
                    logging.info("not found")
                    logging.info("usedpath"+ usedpath+'/'+format_key)
                    mismatches.append(usedpath+'/'+format_key)
    if not matchmode:
        return mismatches
    return matches




test_json_str =         '{"hello": "1", "zap": {"h1": "one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}}'
test_json = json.loads(test_json_str)
json_query_format = json.loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
print("mismatches", json_format_compare(test_json, json_query_format, debugmode=1))

print("matches", json_format_compare(test_json, json_query_format, matchmode=1, debugmode=1))


