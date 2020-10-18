# SCT Website

The official
[website for Senior Computer Team (SCT)](https://activities.tjhsst.edu/sct/) at 
[Thomas Jefferson High School for Science and Technology](https://tjhsst.fcps.edu/)
(TJHSST).

## Setup

This project uses [Flask](http://flask.pocoo.org/) as a Python backend.
[Gunicorn](https://gunicorn.org/) and [gevent](http://www.gevent.org/) are
installed with Director 4's native Docker packages (see `packages.txt`),
and the rest of the packages can be installed with
```bash
pip install -r requirements.txt
```
For JavaScript and CSS/SCSS styling, [npm](https://www.npmjs.com/) is used.
Install node packages by going to `/static` and running
```bash
npm install package.json
```

## File Structure

- `files/config.json`: Configuration file which defines variables given to each
template. Parameters:
    - `url`, which is the URL of the site.
        - "https://activities.tjhsst.edu/sct" on the Director site
        - "http://127.0.0.1:5000" when locally testing
    - `static`, which gives the static URL.
        - "/sct/static" on Director
        - "/static" locally
- `templates/helper`: Defines a global header, footer, and base template.

