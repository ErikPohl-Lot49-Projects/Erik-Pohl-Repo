# this is almost deliberately bad
# I wanted to prove to myself I could do this in list comprehensions and dict comprehensions
# AND I DID BWAH HA HA HA HA
# you want readable code?  I could do that, too.  Easier.
def list_of_xs_converter(*,
                         list_of_xs=None,
                         to_list_of=None,
                         output_as_string_delimiter=' '):
    '''
    list of xs converter converts a list of [lists, dicts, string lists] to another type within the same set
    :param list_of_xs: List of xs where x is in types [lists, dicts, string lists]
    :param to_list_of: Output type in [str, dict, list]
    :param output_as_string_delimiter:  Delimiter for string list output, or string list input
    :return: Converted type of list of xs
    '''
    if type(list_of_xs[0])== to_list_of:
        return list_of_xs
    if type(list_of_xs[0]) == dict:
        decision_dict = {
            list:   [
                        [
                            [key for key in list_of_xs[0]]
                        ] +
                        [
                            [dictval for dictval in dict.values()] for dict in list_of_xs
                        ]
                    ][0],
            dict: list_of_xs,
            str:    [
                        output_as_string_delimiter.join(x) for x in
                            [
                                [
                                    [str(key) for key in list_of_xs[0]]
                                ] +
                                [
                                    [str(dictval) for dictval in dict.values()]
                                    for dict in list_of_xs
                                ]
                            ][0]
                    ]
        }
        return decision_dict[to_list_of]
    if type(list_of_xs[0]) == list:
        decision_dict = {
            dict:   [
                        {list_of_xs[0][lcount]: litem for lcount, litem in enumerate(list)}
                        for list in list_of_xs[1:]
                    ],
            list: list_of_xs,
            str:    [
                        output_as_string_delimiter.join([str(item) for item in listx]) for listx in list_of_xs
                    ]
            }
        return decision_dict[to_list_of]
    if type(list_of_xs[0]) == str:
        decision_dict = {
            dict: list_of_xs_converter(list_of_xs=[x.split(output_as_string_delimiter) for x in list_of_xs],
                                       to_list_of=dict,
                                       output_as_string_delimiter=' '),
            list: [x.split(output_as_string_delimiter) for x in list_of_xs],
            str: list_of_xs
        }
        return decision_dict[to_list_of]
