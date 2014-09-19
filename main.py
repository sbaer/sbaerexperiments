import os
from google.appengine.ext import webapp
import mistune


class MainHandler(webapp.RequestHandler):
    def get(self):
        if "favicon" in self.request.path:
            return
        markdown_file = self.request.path[1:] + ".md"
        folder = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(folder, 'docs', markdown_file)
        f = open(file_path, 'r')
        markdown = f.read()
        f.close()

        html = mistune.markdown(markdown)
        self.response.out.write(html)


app = webapp.WSGIApplication([('/.*', MainHandler)],
                             debug=True)

