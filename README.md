# Python stoppable app

This is an example of an app that executes an action repeatedly
and can be gracefully stopped.

If you stop it when the action is running, the app will wait for it to complete, and then exit.

    $ python3 app.py
    ->
    (Ctrl + C PRESSED NOW) ^COK, exiting.
    -<

If the action is currently not running, the app will exit immediately.

    $ python3 app.py
    ->
    -<
    (Ctrl + C PRESSED NOW) ^COK, exiting.
