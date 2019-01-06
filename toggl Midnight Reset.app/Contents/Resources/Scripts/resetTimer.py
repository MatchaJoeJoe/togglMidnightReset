from toggl.TogglPy import Toggl
import sys

USAGE_TXT = "Usage: python [path to script] [api token]"

def resetTimer(apiKey):
	# create a Toggl object and set our API key 
	toggl = Toggl()
	toggl.setAPIKey(apiKey)

	# get current timer info
	currentTimer = toggl.currentRunningTimeEntry()
	thePID = currentTimer['data']['pid']
	theDesc = currentTimer['data']['description']
	
	# create duplicate timer
	toggl.startTimeEntry(theDesc, thePID)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		apiKey = sys.argv[1]
		resetTimer(apiKey)
	else:
		raise USAGE_TXT
