from flask import abort
from flock.app import db_wrapper as db
from flock.services.notification import notify

def add(role, company_id):
    db.role_add(role, company_id)
    notify(u'{} added a new Role - <strong>%s</strong>' % role['name'], action='add', target='person')

def delete(role_id):
    people = db.person_get(role_id=role_id)
    role = get(role_id=role_id)
    if people:
        abort(400, u'There are {} {}(s) registered. Remove those People first.'.format(len(people), role.name))
    db.role_delete(role_id)
    notify(u'{} deleted a Role - <strong>%s</strong>' % role.name, action='delete', target='person')

def update(role):
    db.role_update(role)
    db.person_role_update(role)
    notify(u'{} edited a Role - <strong>%s</strong>' % role['name'], action='edit', target='person')

def get(role_id=None, company_id=None, user_id=None):
    rank = None if user_id is None else db.person_get(user_id=user_id).role.rank
    return db.role_get(role_id=role_id, company_id=company_id, rank=rank)