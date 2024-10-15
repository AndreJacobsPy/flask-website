from flask import Flask, render_template
from github_scraper import get_pinned_repo_links

app = Flask(__name__)


@app.route('/')
def main_page():
    message = "Welcome to Data Works, where we solve your Data troubles!"
    return render_template(
        template_name_or_list="index.html", message=message,
        links=get_pinned_repo_links()
    )


if __name__ == '__main__':
    app.run(debug=True)
