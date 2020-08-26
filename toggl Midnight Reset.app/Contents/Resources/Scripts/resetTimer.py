from toggl.TogglPy import Toggl
import sys

USAGE_TXT = "Usage: python [path to script] [api token] [-getTimer (optional)]"

def resetTimer(apiKey):
	# create a Toggl object and set our API key
	toggl = Toggl()
	toggl.setAPIKey(apiKey)

	# get current timer info
	currentTimer = toggl.currentRunningTimeEntry()
	if currentTimer['data'] != None:
		thePID = currentTimer['data']['pid']
		theDesc = currentTimer['data']['description']

		# create duplicate timer
		toggl.startTimeEntry(theDesc, thePID)


def returnCurrentTimer(apiKey):
	# create a Toggl object and set our API key
	toggl = Toggl()
	toggl.setAPIKey(apiKey)

	# get current timer info
	currentTimer = toggl.currentRunningTimeEntry()
	if currentTimer['data'] != None:
		print currentTimer['data']['description']


if __name__ == "__main__":
	if len(sys.argv) > 0:
		apiKey = sys.argv[1]
	if len(sys.argv) == 2:
		resetTimer(apiKey)
	elif len(sys.argv) == 3 and sys.argv[2] == "-getTimer":
		returnCurrentTimer(apiKey)
	else:
		raise USAGE_TXT
