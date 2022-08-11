# import standard python packages
import requests

def verify_source(app_id, github_url):
    # defining response object as empty dictionary
    response = {}

    # defining payloads for various requests
    algoexplorer_url = 'https://node.algoexplorerapi.io/v2/applications/' + app_id
    raw_github_url = github_url.replace('blob', 'raw')

    # get on-chain compiled bytecode
    algoexplorer_response = requests.get(algoexplorer_url)
    algoexplorer_response_json = algoexplorer_response.json()

    # try to get response if request succeeded
    try:
        onchain_base64_bytecode_string = algoexplorer_response_json['params']['approval-program']
    except:
        # set empty string if request fails
        onchain_base64_bytecode_string = ""

    # get github compiled bytecode
    github_contract_response = requests.get(raw_github_url)

    # try to get compliled contract if transaction succeeded
    try:
        github_contract_string = github_contract_response.text

        # compile source code in plain text, return base64 encoded program bytes
        github_contract_compile = requests.post('https://node.algoexplorerapi.io/v2/teal/compile', data=github_contract_string)
        github_contract_base64_string = github_contract_compile.json()['result']
    except:
        # set empty string if request fails
        github_contract_base64_string = ""

    # populating response dict
    response['onchain_status_code'] = algoexplorer_response.status_code
    response['github_status_code'] = github_contract_response.status_code

    # checking if claimed contract bytecode matched on-chain bytecode
    if onchain_base64_bytecode_string == github_contract_base64_string:
        response['isMatch'] = True
    else:
        response['isMatch'] = False

    return response
