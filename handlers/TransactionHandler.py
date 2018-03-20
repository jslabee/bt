
from google.appengine.api import users

from handlers.base import BaseHandler
from models.user import User
from untils.decorator import validate_csrf
import hmac


class TransactionHandler(BaseHandler):

    def get(self):
        return self.render_template("transaction.html")
    @validate_csrf
    def post(self):
        #get values
        user = users.get_current_user()
        recepient = self.request.get("recipient")

        hash = hmac.new(str(recepient)).hexdigest()
        recepient_email = User.query(hash == User.email).get()

        amount = self.request.get('amount')
        # add money to recepient
        if  recepient_email :
            recepient_id = recepient_email.key.id()
            trans = User.get_by_id(recepient_id)
            trans.value = int(amount) + recepient_email.value
            trans.put()
        else:
            return self.write("no user with this name")

        # get money from sender
        sender_hash = hmac.new(user.email()).hexdigest()

        sender_email = User.query(str(sender_hash) == User.email).get()
        sender_id = sender_email.key.id()
        send = User.get_by_id(sender_id)
        send.value = sender_email.value - int(amount)
        send.put()



        return self.render_template("main.html")

