# This needs to be set to true to enable analytics.
default persistent.analytics = None

# Initialize this to a unique cid.
default persistent.analytics_cid = None

init -10 python in analytics:

    # The google analytics tracking ID.  If not set, no tracking will occur.
    tracking_id = None

    from store import persistent, config
    import uuid
    import threading
    import requests
    import urllib

    # Create a cid if needed.
    if persistent.analytics_cid is None:
        persistent.analytics_cid = str(uuid.uuid4())

    # The queue of events that are going to be called. This should not
    # change, as we don't want this to be saved.
    queue = [ ]

    def enqueue(**kwargs):
        if not persistent.analytics:
            return

        if not tracking_id:
            return

        kwargs["v"] = 1
        kwargs["tid"] = tracking_id
        kwargs["cid"] = persistent.analytics_cid

        queue.append(urllib.urlencode(kwargs))

    def event(category, action, label=None, value=None):
        """
        `category`
            The category of the event. A string.

        `action`
            The action that occurred. A string.

        `label`
            An optional label associated with the event. A string.

        `value`
            If given, a numeric value associated with the ending. A number.

        """

        kwargs = dict(
            t="event",
            ec=category,
            ea=action)

        if label is not None:
            kwargs["el"] = label
        if value is not None:
            kwargs["ev"] = value

        enqueue(**kwargs)

    def post_events(queue):
        """
        This is called in a thread from the interact callback, and is responsible for
        actually posting events to Google Analytics.
        """

        for i in queue:

            try:
                res = requests.post("https://www.google-analytics.com/collect", i, timeout=10)
                print(res)
            except:
                if config.developer:
                    import traceback
                    traceback.print_exc()


    def interact_callback():
        """
        This is called once per interaction, and then
        """

        q = queue[:]
        queue[:] = [ ]

        if not persistent.analytics:
            return

        if not q:
            return

        t = threading.Thread(target=post_events, args=(q,))
        t.daemon = True
        t.start()


    config.interact_callbacks.append(interact_callback)
