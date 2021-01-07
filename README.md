# TMAX ims alert

## Download

`pip install tmax-ims`

## Example

### IMS example
```
from tmax_ims import IMS

ims = IMS('your_id', 'your_password')

# Get my team's assigned issues
# return type pandas.DataFrame with default headers
print( ims.fetch() )

# set custom header
ims.set_header(['Issue Number', 'Subject', 'Handler', 'Version', 'Status'])

# set custom fetch url (default: Issues assigned to me)
ims.set_issue_list_url('http://~')

```
## Feature
 - IMS List fetch
 - (TODO) new ims alert bot
