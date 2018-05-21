from flask import Flask, request, render_template_string, render_template
app = Flask(__name__)



@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.errorhandler(404)
def page_not_found(e):
    template = '''{%% extends "base.html" %%}
		{%% block body %%}
		    <div class="center-content error">
		        <h1>Oops! That page doesn't exist.</h1>
		        <h3>%s</h3>
		    </div>
		{%% endblock %%}
		''' % (request.url)
    return render_template_string(template), 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
