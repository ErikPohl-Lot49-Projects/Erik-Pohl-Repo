# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import re
import sys
from collections import namedtuple


# todo : handle parameters which are attributes better
# todo : address complicated clauses
# (this clause AND this clause) OR (This clause AND this clause) OR (this clause)
# Ultimately a json query grammar
# With findings in json format

class JnesaisQ:
    '''
    JnesaisQ 
    Allows you to create a search term in JSON, and then apply that search term
    to JSON inputs to see if and where matches or mismatches occur.
    '''

    def __init__(self, JSON_query_clause):
        self.json_query_finding = namedtuple('json_query_finding', 'current_json_path, actual_finding_value')
        self.json_query_final_results = namedtuple('json_query_results', 'json_query_mismatches, json_query_matches')
        self.JSON_KEY_MISSING = 'JSON_key_not_found'
        self.JSON_VALUE_MISMATCH = 'JSON_value_mismatch'
        self.JSON_query_clause = JSON_query_clause

    def compare(self, JSON_to_query, JSON_query_clause=None,
                *,
                debug_mode=False,
                current_JSON_path='',
                JnesaisQ_matches=None,
                JnesaisQ_mismatches=None):
        '''
        compare_json_to_query_clause
        :param JSON_to_query: This is an input JSON which you want to query
        :param JSON_query_clause: This is a clause in JSON format for the keys you want to query with values in regex
        :param debug_mode: Debug mode can be on or off, deprecated
        :param current_JSON_path: This is an internal only variable which tracks the current JSON path for reporting findings
        :param JnesaisQ_matches: This stores results of the matches identified by the query
        :param JnesaisQ_mismatches: This stores results of the mismatches identified by the query
        :return: This returns findings based on the JSON_to_query, the JSON_query_clause, and the match_mode
        '''
        if not JSON_query_clause:
            JSON_query_clause = self.JSON_query_clause
        if JnesaisQ_matches == None:
            JnesaisQ_matches = []
        if JnesaisQ_mismatches == None:
            JnesaisQ_mismatches = []
        if debug_mode:
            logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        for format_key in JSON_query_clause.keys():
            current_json_path = current_JSON_path + '/' + format_key
            try:
                JSON_to_query_key_value = JSON_to_query[format_key]
            except:
                # key not found in JSON to query, so it is a mismatch
                JnesaisQ_mismatches.append(self.json_query_finding(current_json_path, self.JSON_KEY_MISSING))
                continue
            JSON_query_key_value = JSON_query_clause[format_key]
            ## if the format value which is being compared with the test value is itself a clause, recurse
            if isinstance(JSON_query_key_value, dict):
                x = self.compare(JSON_to_query_key_value,
                                 JSON_query_clause=JSON_query_key_value,
                                 current_JSON_path=current_json_path,
                                 JnesaisQ_matches=JnesaisQ_matches,
                                 JnesaisQ_mismatches=JnesaisQ_mismatches,
                                 debug_mode=debug_mode)
            else:
                if re.match(JSON_query_key_value, JSON_to_query_key_value):
                    JnesaisQ_matches.append(self.json_query_finding(current_json_path, JSON_to_query_key_value))
                else:
                    JnesaisQ_mismatches.append(self.json_query_finding(current_json_path, self.JSON_VALUE_MISMATCH))
        return self.json_query_final_results(JnesaisQ_mismatches, JnesaisQ_matches)

    def overall_result(self, match_tuple):
        '''
        overall_result
        Returns a diagnosis of the JSON format match attempt:
        AND_match, OR_match_mismatch, AND_mismatch
        :param match_tuple: this is the output of JnesaisQ.compare
        :return: an overall result
        '''
        retval = []
        if match_tuple.json_query_mismatches == [] and match_tuple.json_query_matches == []:
            return None
        if not match_tuple.json_query_mismatches and match_tuple.json_query_matches:
            retval.append("AND_match")
        if match_tuple.json_query_mismatches and match_tuple.json_query_matches:
            retval.append("OR_match_mismatch")
        if match_tuple.json_query_mismatches and not match_tuple.json_query_matches:
            retval.append("AND_mismatch")
        return retval

    def list_of_compares(self, list_of_JSON_to_query):
        '''
        list of compares
        outputs comparisons using the current search setup for a list of JSON 
        :param list_of_JSON_to_query: this is the list of JSON to apply the query to
        :return: list of matching JSON
        '''
        output_list_of_dicts = []
        for JSON_to_query in list_of_JSON_to_query:
            if self.overall_result(self.compare(JSON_to_query=JSON_to_query)) in ("OR_match_mismatch", "AND_match"):
                output_list_of_dicts.append(JSON_to_query)
        return output_list_of_dicts
