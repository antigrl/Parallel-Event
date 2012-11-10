import gdata.calendar.service
import gdata.calendar.client
import datetime

from pe_errors import error_codes

def getAllEvents(username, password, calendar_name="", 
                 start_date=None, end_date = None):
    """
    Returns all events from now 'till the end of time.
    Fetches from the specified calendar, if provided, 
    else retrieves from the default.
    """
    query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full')
    if not start_date:
        start_date = str(datetime.date.today())
    query.start_min = start_date

    client = gdata.calendar.service.CalendarService(username, password,
                                                    "Parallelevent")
    #Try to log in
    try:
        client.ProgrammaticLogin()
    except gdata.service.BadAuthentication, e:
        return [], (error_codes["ERR_AUTH"], "Authentication error logging in: %s" % e)
    except Exception, e:
        return [], (error_codes["ERR_LOGIN"], "Error Logging in: %s" % e)

    #Specify query converter (to get queries in the date range)
    feed = client.CalendarQuery(query)
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

    all_events = []
    
    #Build up event data structure
    #[
    # (id, title, content, [] people, [] authors, [] when), ...
    #]

    for index, event in enumerate(feed.entry):
        uid = event.id.text
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

        all_events.append((uid, title, content, people, authors, when))

    return all_events, ()
