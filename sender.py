import requests
import time
import os
from requests.auth import HTTPBasicAuth
import json

token = os.environ['SC_TOKEN']
project = os.environ['PROJECT_KEY']

while True:
    for p in range(1, 10000):
        requests.get(f'https://dev.sc-dev.io/api/measures/component_tree?component={project}&p={p}&ps=500&metricKeys=sqale_index,sqale_debt_ratio,alert_status,bugs,reliability_rating,reliability_remediation_effort,vulnerabilities,security_rating,security_remediation_effort,security_hotspots,security_review_rating,classes,comment_lines,comment_lines_density',
                      auth=HTTPBasicAuth(token, ''))
        requests.get(f'https://dev.sc-dev.io/api/measures/component_tree?component={project}&p={p}&ps=500&metricKeys=complexity,cognitive_complexity,duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,violations,blocker_violations,critical_violations,major_violations,minor_violations,info_violations,open_issues,code_smells,sqale_rating',
                      auth=HTTPBasicAuth(token, ''))
        x = requests.get(f'https://dev.sc-dev.io/api/measures/component_tree?component={project}&p={p}&ps=500&metricKeys=directories,files,lines,ncloc,functions,statements,branch_coverage,coverage,line_coverage,lines_to_cover,uncovered_conditions,uncovered_lines,skipped_tests,tests',
            auth=HTTPBasicAuth(token, ''))

        print(f'another cycle {p}')
        if len(json.loads(x.text)['components']) == 0:
            print(f'full cycle {p}')
            break





