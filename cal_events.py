import gdata.calendar.service

def getAllEvents(username, password, calendar_name=""):
    """
    Returns all events from now 'till the end of time.
    Fetches from the specified calendar, if provided, 
    else retrieves from the default.
    """
    client = gdata.calendar.service.CalendarService(username, password,
                                                    "Parallelevent")
    #Try to log in
    try:
        client.ProgrammaticLogin()
    except gdata.service.BadAuthentication, e:
        return "Authentication error logging in: %s" % e
    except Exception, e:
        return "Error Logging in: %s" % e

    #Get feeds
    feed = client.GetOwnCalendarsFeed()
    urls = dict((entry.title.text, entry) for entry in feed.entry)

    #Get events from the specified calendar
    cal = None
    if urls.get(calendar_name):
        cal = urls[calendar_name]
    else:
        #Use the default calendar
        cal = feed.entry[0]

    alternate_link = cal.GetAlternateLink()

    #No events
    if not alternate_link:
        return

    event_feed = client.GetCalendarEventFeed(alternate_link.href)

    all_events = []
    
    #Build up event data structure
    #[
    # (title, content, [] people, [] authors, [] when), ...
    #]

    for index, event in enumerate(event_feed.entry):
        title = event.title.text
        content = event.content.text

        people = []
        for person in event.who:
            people.append((person.name, person.email))
        
        authors = []
        for author in event.author:
            authors.append(author.name.text)

        when = []
        for e_index, e_time in enumerate(event.when):
            when.append((e_time.start_time, e_time.end_time))

        all_events.append((title, content, people, authors, when))

    return all_events
