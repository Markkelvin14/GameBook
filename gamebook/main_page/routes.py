from flask import render_template, url_for, request, Blueprint
from gamebook.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/welcome")
def welcome():
	return render_template('index.html', title=welcome)

@main.route("/")
@main.route("/home")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=20)
	return render_template('home.html', posts=posts)


@main.route("/about")
def about():
	return render_template('about.html', title='About')