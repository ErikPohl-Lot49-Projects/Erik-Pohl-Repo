import json, re, logging, sys
from collections import namedtuple

#TODO make it a class with a compare method
#TODO should a mismatch which is actually mismatched return an 'actual_finding_value' of the input json
json_query_finding = namedtuple('json_query_finding', 'current_json_path, actual_finding_value')
json_query_final_results = namedtuple('json_query_results', 'json_query_finding, overall_result')
JSON_KEY_MISSING = 'JSON_key_not_found'
JSON_VALUE_MISMATCH = 'JSON_value_mismatch'
MATCHMODES = {'AND': 1, 'OR': 2, 'MISMATCH':0}

def compare_json_to_query_clause(JSON_to_query, JSON_query_clause, *,
                                 match_mode=MATCHMODES["MISMATCH"],
                                 debug_mode=False, current_JSON_path='', JSON_query_results=None):
    '''
    compare_json_to_query_clause
    :param JSON_to_query: This is an input JSON which you want to query
    :param JSON_query_clause: This is a clause in JSON format for the keys you want to query with values in regex
    :param match_mode: This is the match mode to apply making the comparison [AND,OR,MISMATCH]
    :param debug_mode: Debug mode can be on or off, deprecated
    :param current_JSON_path: This is an internal only variable which tracks the current JSON path for reporting findings
    :param JSON_query_results: This stores results of the comparison throughout the query
    :return: This returns findings based on the JSON_to_query, the JSON_query_clause, and the match_mode
    '''
    if JSON_query_results == None:
        JSON_query_results = []
    if debug_mode:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    for format_key in JSON_query_clause.keys():
        current_json_path = current_JSON_path + '/' + format_key
        try:
            JSON_to_query_key_value = JSON_to_query[format_key]
        except:
            if not match_mode:
                JSON_query_results.append(json_query_finding(current_json_path, JSON_KEY_MISSING))
                continue
            else:
                raise ValueError
        JSON_query_key_value = JSON_query_clause[format_key]
        ## if the format value which is being compared with the test value is itself a clause, recurse
        if isinstance(JSON_query_key_value, dict):
            compare_json_to_query_clause(JSON_to_query_key_value, JSON_query_key_value,
                                         current_JSON_path=current_json_path,
                                         JSON_query_results=JSON_query_results,
                                         match_mode=match_mode, debug_mode=debug_mode)
        else:
            if re.match(JSON_query_key_value, JSON_to_query_key_value):
                if match_mode:
                    JSON_query_results.append(json_query_finding(current_json_path, JSON_to_query_key_value))
            else:
                if not match_mode: #mismach is being tracked
                    JSON_query_results.append(json_query_finding(current_json_path, JSON_VALUE_MISMATCH))
                else:  ## partial matches are not okay for ANDs but are okay for ORs
                    if match_mode == MATCHMODES["AND"]:
                        return json_query_final_results([],None)
                        # otherwise, this is a mismatch, but don't short circuit and exit because we're in or mode
    if (match_mode) and (JSON_query_results):
        return json_query_final_results(JSON_query_results, JSON_to_query)
    return json_query_final_results(JSON_query_results, None)
