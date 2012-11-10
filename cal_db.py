import sqlite3
import cal_events

def create_db(events):
    """
    Create an sqlite db from the user's calendar events
    """
    conn = sqlite3.connect('gcal.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE events
                         (title text, content text, people text, authors text, date text)''')

    for event in events:
        title, content, people, authors, when = event
        c.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?)",
                   (title, content, "\n".join(people[0]), "\n".join(authors), "\n".join(when[0])))
    
    conn.commit()
    conn.close()

def check_new_events(events):
    """
    Check against the db for new events
    """
    conn = sqlite3.connect('gcal.db')
    c = conn.cursor()

    c.execute("SELECT title from events")
    data = c.fetchall()

    new_events = []

    #Flatten titles
    data = [title for item in data for title in item]

    for event in events:
        title, content, people, authors, when = event
        
        if title not in data:
            c.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?)",
                       (title, content, "\n".join(people[0]), "\n".join(authors), "\n".join(when[0])))

            new_events.append(event)

    conn.commit()
    conn.close()

    return new_events
