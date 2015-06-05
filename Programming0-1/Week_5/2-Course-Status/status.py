def status_count(students):
    result = {
        'finalized': [],
        'not_finalized': []
    }
    for s in students:
        if s['status'] == 'finalized':
            result['finalized'].append(s['name'])
        else:
            result['not_finalized'].append(s['name'])
    return result

print(status_count([{
    "name": "RadoRado",
    "status": "not_finalized"
}, {
    "name": "Ivo",
    "status": "finalized"
}, {
    "name": "Genadi",
    "status": "finalized"
}]))
