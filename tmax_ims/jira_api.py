import requests
from requests.auth import HTTPBasicAuth
import json

# API Documentation
# https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
# API KEY: https://id.atlassian.com/manage-profile/security/api-tokens
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
class Jira:
    def __init__(self, domain, email, api_key):
        self.url = domain + "/rest/api/3/issue"
        self.auth = HTTPBasicAuth(email, api_key)

    def create_issue(self, data):
        payload = json.dumps( data )
        response = requests.request(
            "POST",
            self.url,
            data=payload,
            headers=headers,
            auth=self.auth
        )
        return response
