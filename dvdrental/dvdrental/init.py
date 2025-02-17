def __init__(hub):
    # Remember not to start your app in the __init__ function
    # This function should just be used to set up the plugin subsystem
    # The run.py is where your app should usually start
    for dyne in []:
        hub.pop.sub.add(dyne_name=dyne)


def cli(hub):
    hub.pop.config.load(['dvdrental'], cli="dvdrental")
    # Your app's options can now be found under hub.OPT.dvdrental
    kwargs = dict(hub.OPT.dvdrental)

    # Initialize the asyncio event loop
    hub.pop.loop.create()

    # Start the web server and database
    hub.app.main.make_app(**kwargs)
    hub.pop.Loop.run_until_complete()