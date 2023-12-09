# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vinayvasantham-jira-project.atlassian.net//rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0LGuJ-6Ixn6Nh0tTnNrMqq_U2LFEd8vD6zDLIaBHvf17sbgUziYu-Dl1zkDm9E6uRdLFzfL1fDX38aACBy6n3AdALWUuep79HF3Dvv2fyNgszgl1KGmGA4lFt4LvrbKDIUb_S9ZUTiSjAihZS3o5eOIG4W3TgUgowf8wWJDrmgCo=ED18DDD6"

auth = HTTPBasicAuth("nagavinay.vasantham_mel2020@svce.edu.in", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "SCRUM"
    },
    "issuetype": {
      "id": "10003"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))