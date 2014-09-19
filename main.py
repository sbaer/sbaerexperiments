import os
from google.appengine.ext import webapp
from google.appengine.api.urlfetch import fetch
from google.appengine.ext.webapp import template
import mistune
from google.appengine.api import users

class MainHandler(webapp.RequestHandler):
    def get(self):
        """
        user = users.get_current_user()

        allowed_ids = {'112266133891816514376':('Localhost Steve', 'sbaer'),
                       '104684131424750918512':('Steve Baer', 'sbaer'),
                       '115053547347074595578':('Brian Gillespie', 'golsby')}
        if not user or not allowed_ids.has_key(user.user_id()):
            self.response.out.write("Not Authorized - " + user.user_id() )
            return
        """
        if "favicon" in self.request.path:
            return
        markdown_file = self.request.path[1:] + ".md"
        folder = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(folder, 'docs', markdown_file)
        f = open(file_path, 'r')
        markdown = f.read()
        f.close()
        #self.response.out.write(template.render(path, template_values))

        html = mistune.markdown(markdown)
        self.response.out.write(html)


app = webapp.WSGIApplication([('/.*', MainHandler)],
                             debug=True)

