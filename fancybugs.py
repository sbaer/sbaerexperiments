from google.appengine.ext import webapp
from google.appengine.api.urlfetch import fetch
from google.appengine.ext.webapp import template
import os
import json
from google.appengine.api import users

class FancyBugHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        allowed_ids = {'112266133891816514376':('Localhost Steve', 'sbaer'),
                       '104684131424750918512':('Steve Baer', 'sbaer'),
                       '115053547347074595578':('Brian Gillespie', 'golsby')}
        if not user or not allowed_ids.has_key(user.user_id()):
            self.response.out.write("Not Authorized - " + user.user_id() )
            return

        projects = {'rhino5':'Rhino 5',
                    'rhino6':'Rhino 6',
                    'flamingonxt':'Flamingo nXt',
                    'accurendernxt':'AccuRender nXt',
                    'bongo2':'Bongo 2',
                    'brazil2':'Brazil 2'}

        active_project = "rhino5"
        path_components = self.request.path.split('/')
        path_components = filter( lambda a: a!='' and a!='/', path_components)
        if path_components: active_project = path_components[0].lower()

        # make sure the active project is one that we know about
        if not projects.has_key(active_project):
            self.error(404)
            return

        product = projects[active_project]

        user_filter = 'user_anyone'
        if len(path_components)>1:
            if path_components[1].lower()=='owner': user_filter = 'user_owner'
            elif path_components[1].lower()=='created_by': user_filter = 'user_creator'

        api_base_url = "https://api.github.com"
        all_tags_url = api_base_url + "/repos/mcneel/rhinocommon/labels"
        api_response = fetch(all_tags_url)
        json_tags = json.loads(api_response.content)
        for tag in json_tags:
            issues_url = api_base_url + "/repos/mcneel/rhinocommon/issues?state=closed&labels=" + tag["name"].replace(' ','+')
            api_response = fetch(issues_url)
            if api_response.content:
                json_issues = json.loads(api_response.content)
                tag["issuecount"] = len(json_issues)
            else:
                tag["issuecount"] = 0
        json_tags = sorted(json_tags, key=lambda tag: tag["name"])

        collaborators_url = api_base_url + "/repos/mcneel/rhinocommon/collaborators"
        api_response = fetch(collaborators_url)
        json_collaborators = json.loads(api_response.content)
        for collaborator in json_collaborators:
            user_url = api_base_url + "/users/" + collaborator["login"]
            api_response = fetch(user_url)
            json_user = json.loads(api_response.content)
            if json_user.has_key("name"):
                collaborator["name"] = json_user["name"]
            else:
                collaborator["name"] = ""

        issues_url = api_base_url + "/repos/mcneel/rhinocommon/issues?state=closed&page=1"
        issues_response = fetch(issues_url)
        json_issues = json.loads(issues_response.content)

        project_keys = sorted(projects.iterkeys())
        json_projects = []
        for key in project_keys:
            json_projects.append({'name':key, 'friendly_name':projects[key]})

        template_values = {
            'product': product,
            'active_project': active_project,
            'projects': json_projects,
            'user': allowed_ids[user.user_id()][0],
            'userlogin': allowed_ids[user.user_id()][1],
            'tags': json_tags,
            'collaborators': json_collaborators,
            'issues': json_issues,
            user_filter: 1,
            'root_url': self.request.host_url
            }

        path = os.path.join(os.path.dirname(__file__), 'issues.html')
        html = template.render(path, template_values)
        self.response.out.write(html)


app = webapp.WSGIApplication([('/fancybugs/.*', FancyBugHandler)],
                             debug=True)

