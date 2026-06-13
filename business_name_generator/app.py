from flask import Flask, render_template, request, redirect, url_for, flash
from generator import generate_names

app = Flask(__name__)
app.secret_key = "change-me-for-prod"


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    # form defaults
    form = {
        "keywords": [],
        "other_keyword": "",
        "industry": "",
        "other_industry": "",
        "description": "",
        "style": "modern",
        "count": 8,
    }

    if request.method == "POST":
        # collect multiple selected keywords from a single multi-select dropdown
        selected_keywords = request.form.getlist("keywords") or []
        other_keyword = request.form.get("other_keyword", "").strip()
        form["keywords"] = selected_keywords
        form["other_keyword"] = other_keyword

        # industry (allow Other)
        industry = request.form.get("industry", "").strip()
        other_ind = request.form.get("other_industry", "").strip()
        form["industry"] = industry
        form["other_industry"] = other_ind

        form["description"] = request.form.get("description", "").strip()
        form["style"] = request.form.get("style", "modern")
        try:
            form["count"] = int(request.form.get("count", 8))
        except ValueError:
            form["count"] = 8

        # determine final keyword list (use custom when 'Other' selected)
        final_keywords = []
        for sel in selected_keywords:
            if sel.lower() == "other":
                if other_keyword:
                    final_keywords.extend([kw.strip() for kw in other_keyword.split(",") if kw.strip()])
            elif sel:
                final_keywords.append(sel)

        # build input text from keywords + description
        if final_keywords:
            text_input = " ".join(final_keywords) + (" " + form["description"] if form["description"] else "")
        else:
            text_input = form["description"]

        # determine industry string (use custom if 'Other' selected)
        industry_value = other_ind if industry.lower() == "other" and other_ind else industry

        # validation
        if not text_input or not text_input.strip():
            flash("Please enter keywords or a short description.", "error")
        else:
            try:
                results = generate_names(text_input, industry=industry_value, style=form["style"], count=form["count"])
            except Exception as e:
                flash(str(e), "error")

    return render_template("index.html", form=form, results=results)


if __name__ == "__main__":
    app.run(debug=True)
