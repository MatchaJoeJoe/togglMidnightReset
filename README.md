# togglMidnightReset
Simple applescript droplet that uses [TogglPY](https://github.com/matthewdowney/TogglPy) to reset currently running timer at midnight.   
## Instructions
* Download the latest release [here](https://github.com/MatchaJoeJoe/togglMidnightReset/releases).
* Unzip and run the app.
* A dialog will be displayed asking for your toggl API key, this can be found at the bottom of your [toggl Profile](https://toggl.com/app/profile).  
  * If you press the **Cancel button**, the app will quit.
  * If you press the **OK** button, the app will ask for your API key again the next time you run it.
  * If you press the **Save in Keychain button**, the app will save the API key in your keychain. If your API key ever changes, you will need to manually update the **togglMidnightReset** entry using [Keychain Access](https://support.apple.com/guide/keychain-access/what-is-keychain-access-kyca1083/mac). 
* Once the API key is put in, a progress bar will display counting down the time until the app runs the [python script](https://github.com/MatchaJoeJoe/togglMidnightReset/blob/master/toggl%20Midnight%20Reset.app/Contents/Resources/Scripts/resetTimer.py) that resets the currently running timer.
* Once the script has been run, the progress bar will reset.
* At any time you can press the **Stop** button to quit the app.
