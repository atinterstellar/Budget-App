# Budget App

A personal finance tracker I'm building from scratch — starting with plain Python and a JSON file, and eventually turning it into a real web app with Flask, HTML, and CSS.

## Why I'm building this

I started this right as I was heading into college. Suddenly budgeting isn't hypothetical anymore — it's tuition, stationaries, groceries, eating out, going out with friends, all of it adding up fast if you're not paying attention. I wanted something that could actually help me keep track of that, but instead of just downloading an app, I figured I'd build my own. Partly because I'd end up with something I actually understand and can tweak, and partly because I knew building it would force me to actually learn this stuff properly instead of just watching tutorials.

So this is equal parts "tool I use for my own money" and "project I'm using to learn Python, Git, and web dev." It's not finished, and it's not perfect — it's grown a lot through a bunch of rounds of bugs and rewrites, which honestly has been most of the learning.

## What it does right now

### The Main Python Code
  - You can create categories (Groceries, Rent, whatever) and each one keeps its own running balance and transaction history
  - Deposit and withdraw money from a category, with some basic checks so you can't withdraw more than you have or deposit a negative number
  - Transfer money between categories
  - Split one deposit across multiple categories by percentage (still rough around the edges, but functional)
  - Everything gets saved to a `budget.json` file so it's still there next time you open the app
  - You can pull up just the payments, just the credits, or the full ledger for any category
### Implementing Flask
  - Various fucntions to take input from users
  - Fucntions to perform each function defined in Main code
  - Implementing it along with html
### The HTML5 Files
  - Various files consisiting of HTML code to provide interface to web pages
  - Implementation with Flask
### Static Directory
  - Folder containing all my CSS code

## What's next

The Python/JSON side is in decent shape at this point. Next up is wrapping it in a Flask server so it can actually run in a browser instead of the terminal, then building out HTML/CSS so it looks like something a normal person would want to use. After that, I want to add a spending breakdown — probably a simple bar chart showing how much went where.

## Tech I'm using

- **Python** — all the core logic (categories, ledgers, balances)
- **JSON** — for saving data between sessions
- **Git/GitHub** — version control, and also where most of my "wait why did this break" moments have happened
- **Flask** — to serve this as a web app
- **HTML/CSS** — for the actual interface

## Project structure

```
Budget-App/
├── main_app.py        # core logic — categories, deposits, transfers, etc.
├── budget.json         # gets created automatically once you run it
├── app.py              # Flask app (not built yet)
├── templates/           # HTML pages (not built yet)
├── static/               # CSS/JS (not built yet)
└── README.md
```

## Running it

```bash
git clone https://github.com/atinterstellar/Budget-App.git
cd Budget-App
python main_app.py
```

Once the Flask side exists, you'll be able to run `python app.py` and open it at `localhost:5000` instead.

## A bit about me

I'm a first-year college student, still figuring a lot of this out. I'm joining Chemical Engineering at Indian Institue of Technology, Delhi [IIT Delhi], and I'm getting more into Competitive programming, Web development, Ai/ML etc. This project has been one of the more useful things I've built so far, less because of the end result and more because of everything I had to actually understand to get it working — reading files properly, keeping state in sync, not overwriting my own data, and using Git like an actual workflow instead of just `git add . && git commit -m "fix"` every five minutes.

If you want to reach me or see what else I'm working on:
- GitHub: [@atinterstellar](https://github.com/atinterstellar)
- Email: atinchakraborty9000@gmail.com
- Linkedin: [My linkedin](www.linkedin.com/in/atin-kumar-7185162a5)

## License

Feel free to look through this, fork it, or use it as a reference for your own project. It's a learning project first and foremost, so take it as that.
