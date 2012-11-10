import sqlite3
import cal_events

def check_new_events(events):
    """
    Check against the db for new events
    """
    conn = sqlite3.connect('gcal.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS events
                         (title text, content text, people text, authors text, date text)''')

    c.execute("SELECT title from events")
    data = c.fetchall()

    new_events = []

    #Flatten titles
    data = [title for item in data for title in item]

    for event in events:
        title, content, people, authors, when = event
        
        if title not in data:
            #Flatten people, when
            people = [person for person_list in people for person in person_list]
            when = [time for time_list in when for time in time_list]

            c.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?)",
                       (title, content, "\n".join(people), "\n".join(authors), "\n".join(when)))

            new_events.append(event)

    conn.commit()
    conn.close()

    return new_events
