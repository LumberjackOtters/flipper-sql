import re

def parse_table(create_statement):
    pattern = r'(?P<create>.*?)[\(](?P<fields_and_constraints>.*)[\)](?P<settings>.*)'
    result = re.match(pattern, create_statement, re.DOTALL)
    return result.groupdict()

def parse_fields_and_constraints(fields_and_constraints):
    # print (fields_and_constraints)
    # pattern = r'(?P<field>\`.*?)[,\n]|(?P<contraint>CONSTRAINT.*?)[,\n]|(?P<unique_key>UNIQUE KEY.*?)[,\n]|(?P<primary_key>PRIMARY KEY.*?)[,\n]|(?P<key>KEY.*?)[,\n]'
    # result = re.match(pattern, fields_and_constraints)
    # # result = result.groupdict()
    # print(result)
    regex = r"(?P<field>\`.*?)[\n]|(?P<contraint>CONSTRAINT.*?)[\n]|(?P<unique_key>UNIQUE KEY.*?)[\n]|(?P<primary_key>PRIMARY KEY.*?)[\n]|(?P<key>KEY.*?)[\n]"

    matches = re.finditer(regex, fields_and_constraints, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    # for chunk in splitted:
        # (\`.*?),?\\n?|(CONSTRAINT.*?),?\\n?|(UNIQUE KEY.*?),?\\n?|(PRIMARY KEY.*?),?\\n?|(KEY.*?),?\\n?
        # (?P<field>\`.*?),?\\n?|(?P<contraint>CONSTRAINT.*?),?\\n?|(?P<unique_key>UNIQUE KEY.*?),?\\n?|(?P<primary_key>PRIMARY KEY.*?),?\\n?|(?P<key>KEY.*?),?\\n?
        # (?P<field>\`.*?)[,\n]|(?P<contraint>CONSTRAINT.*?)[,\n]|(?P<unique_key>UNIQUE KEY.*?)[,\n]|(?P<primary_key>PRIMARY KEY.*?)[,\n]|(?P<key>KEY.*?)[,\n]
    return None
