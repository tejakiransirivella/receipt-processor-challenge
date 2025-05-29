import uuid
from app.storage.user import User
from app.models.receipt import Receipt

class Cache:

    info = {}

    @staticmethod
    def get_user_cache(session_id = None):
        if session_id is None:
            session_id = Cache.generate_session_id()
            Cache.info[session_id] = User(session_id)

        if session_id not in Cache.info:
            return None
        return Cache.info[session_id]
        

    @staticmethod
    def generate_session_id():
        session_id = str(uuid.uuid4())
        return session_id
    
def main():
    pass


if __name__ == "__main__":
    main()
