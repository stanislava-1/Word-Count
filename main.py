import os
import jinja2
import webapp2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import count_words

template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
                               autoescape=True)



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("main_page.html")
            

    def post(self):
        text = self.request.get('text')
        dictionary = {}
        if text != '':
            dictionary = count_words.count_words(text)
        ordered_list = count_words.order(dictionary)
        total_words = count_words.count_all_words(dictionary)
        different_words = len(dictionary)
        most_common = len(count_words.most_common_words(dictionary, 80))
        percentage = 0
        if different_words:
            percentage = round(100.0*most_common/different_words, 2)
        self.render("main_page.html", text=text, dictionary=dictionary, 
                    ordered_list=ordered_list, total_words=total_words, 
                    different_words=different_words, most_common=most_common,
                    percentage=percentage)

       
        

app = webapp2.WSGIApplication([("/", MainPage),], debug=True)
