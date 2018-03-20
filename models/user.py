from google.appengine.ext import ndb
import hmac



class User(ndb.Model):
    first_name = ndb.StringProperty()
    value = ndb.IntegerProperty()
    email = ndb.StringProperty()
    admin = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_or_create(cls, email,nickname):
        hash = hmac.new(email).hexdigest()


        user = User.query(User.email == hash).get()  # check if user already exists in the database

        if not user:
            # if user does not exist yet, create a new one

            user = User(email=hash,first_name=nickname,value=100)
            user.put()

        return user




