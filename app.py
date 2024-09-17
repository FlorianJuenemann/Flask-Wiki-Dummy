from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory storage for articles (you can switch this to a database later)
wiki = {
    "Home": "Welcome to the Flask Wiki! This is the home page.",
    "About": "This is a simple wiki built using Flask!"
}

@app.route('/')
def home():
    return render_template('index.html', pages=wiki)

@app.route('/<page_name>')
def view_page(page_name):
    content = wiki.get(page_name, "This page does not exist.")
    return render_template('page.html', page_name=page_name, content=content)

@app.route('/edit/<page_name>', methods=['GET', 'POST'])
def edit_page(page_name):
    if request.method == 'POST':
        # Save the page content
        wiki[page_name] = request.form['content']
        return redirect(url_for('view_page', page_name=page_name))
    
    content = wiki.get(page_name, "")
    return render_template('edit.html', page_name=page_name, content=content)

if __name__ == '__main__':
    app.run(debug=True)