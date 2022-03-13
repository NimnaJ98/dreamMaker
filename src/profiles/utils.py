import uuid

def get_randomCode():
    code = str(uuid.uuid4())[:8].replace('-','').lower()
    return code