from flock.app import db_wrapper as db
from notification import notify

def get(company_id, start=None, end=None, show_expired=True, limit=None, offset=None, sort_by=None,
        sort_dir=None, user_id=None):
    return db.event_get(company_id=company_id, start=start, end=end, show_expired=show_expired, limit=limit,
                             offset=offset, sort_by=sort_by, sort_dir=sort_dir, user_id=user_id)

def add(new_event):
    db.event_add(new_event)
    notify(u'{} added a new Event - <b>%s</b>' % new_event['title'], action='add', target='event')
