import json, re, logging, sys

def json_parse(test_data, format_data, usedpath='', mismatches =[], debugmode = 0):
    if debugmode == 1:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.info("parsing test data"+ str(test_data))
    logging.info("parsing format data"+ str(format_data))
    for i in format_data.keys():
        logging.info("evaluating key:"+ i)
        logging.info("format value for the key" +str(type(format_data[i]))+ str(len(format_data[i]))+ str(format_data[i]))
        logging.info("test value for the key"+ str(type(test_data[i]))+ str(len(test_data[i]))+ str(test_data[i]))
        if isinstance(format_data[i], dict) and len(format_data[i]) > 1:
            logging.info("recurse for " +str(format_data[i]))
            json_parse(test_data[i], format_data[i], usedpath +'/'+ i, mismatches)
        else:
            logging.info("comparing "+ str(format_data[i])+ str(test_data[i]))
            findres = re.match(format_data[i], test_data[i])
            if findres:
                logging.info("found")
            else:
                logging.info("not found")
                logging.info("usedpath"+ usedpath+'/'+i)
                mismatches.append(usedpath+'/'+i)
    return mismatches

test_json_str =         '{"hello":"1", "zarg": {"h1":"one", "h2":"2"}}'
json_query_format_str = '{"hello":"2", "zarg": {"h1":"one", "h2":"3"}}'
test_json = json.loads(test_json_str)
json_query_format = json.loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
print("mismatches", json_parse(test_json,json_query_format))
