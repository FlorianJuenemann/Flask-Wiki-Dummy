from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory storage for articles (you can switch this to a database later)
wiki = {
    "Home": """
        <h2>Welcome to the Hafenmuseum Hamburg Wiki!</h2>
        <p>This wiki provides information about the Hafenmuseum in Hamburg, a place where you can explore the 
        rich maritime history of the Port of Hamburg. Learn about the museum's collections, events, and the 
        historic ships that form a crucial part of the museum's exhibits.</p>
        <p>Feel free to explore the various sections of this wiki to discover more about Hamburg's maritime legacy.</p>
    """,
    
    "About": """
        <h2>About this Wiki</h2>
        <p>This is a simple wiki built using Flask to provide information about the Hafenmuseum in Hamburg.</p>
    """,

    "Historic Ships": """
        <h2>Historic Ships at the Hafenmuseum</h2>
        <ul>
            <li><strong>MS Bleichen</strong>: Built in 1958, the MS Bleichen is a general cargo vessel that played an important role in transporting goods to and from Hamburg. Visitors can explore the ship to understand the life of sailors in the mid-20th century.</li>
            <li><strong>SS Stettin</strong>: The SS Stettin is a historic icebreaker, originally built in 1933. It was designed to keep the shipping routes ice-free during the harsh winters.</li>
            <li><strong>Rickmer Rickmers</strong>: A restored 19th-century full-rigged ship, now a museum ship at the Hamburg harbor.</li>
        </ul>
    """,

    "Cranes and Harbor Machinery": """
        <h2>Harbor Cranes and Machinery</h2>
        <p>The Hafenmuseum features several historical cranes that were once used for loading and unloading ships at the Port of Hamburg. These include:</p>
        <ul>
            <li><strong>Hansa Crane:</strong> A historical crane that was once an iconic feature of the Hamburg skyline, used to load heavy cargo from ships.</li>
            <li><strong>Steam Crane:</strong> Dating back to the early 20th century, this crane was powered by steam and used for lifting heavy machinery.</li>
        </ul>
    """,

    "Opening Hours": """
        <h2>Opening Hours of Hafenmuseum Hamburg</h2>
        <p>The Hafenmuseum is open at the following times:</p>
        <ul>
            <li>Monday - Friday: 10:00 AM to 6:00 PM</li>
            <li>Saturday - Sunday: 10:00 AM to 8:00 PM</li>
            <li>Closed on public holidays</li>
        </ul>
    """,

    "Tickets & Prices": """
        <h2>Ticket Prices</h2>
        <ul>
            <li>Adults: €10</li>
            <li>Children (6-12): €5</li>
            <li>Family Ticket (2 Adults + 2 Children): €25</li>
            <li>Students/Seniors: €8</li>
        </ul>
        <p>Guided tours are available for an additional €3 per person.</p>
    """
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