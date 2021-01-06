# TMAX ims alert

## Download

`pip install tmax-ims`

## Example

### basic fetch example
```
from tmax_ims import IMS

ims = IMS('your_id', 'your_password')

# return type pandas.DataFrame
print( ims.fetch() )

```

### extra settings
```
from tmax_ims import IMS

ims = IMS('your_id', 'your_password')

# set custom header
ims.set_header(['Issue Number', 'Subject'])

# set custom fetch url
ims.set_issue_list_url('http://~')

```

## Feature
 - IMS List fetch
 - (TODO) new ims alert bot
