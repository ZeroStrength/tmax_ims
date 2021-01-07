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

### Bot example
```
from tmax_ims import Bot

bot = Bot('your_id', 'your_password')

# custom refresh interval seconds (unit: seconds)
# default 5 min ( 5 * 60 )
bot = Bot('your_id', 'your_password', 60)

# allow alert type (input type: list)
# default ['new']
bot = Bot('your_id', 'your_password', ['new', 'delete'])

# start running
bot.start()

# stop running
bot.stop()

# set custom callback function when something new or changed
# default callback is sending desktop notification
bot.set_callback(your_function)

# reset callback to default desktop notification
bot.reset_callback()

# example callback function
def print_new(item):
    print(item)
bot.set_callback(print_new)
```
## Feature
 - IMS list fetch
 - New/Delete issue alert bot
