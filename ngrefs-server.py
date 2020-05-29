from app import app, db
from app.models import User, Post

# configure a "shell context", which is a list of other symbols to pre-import when using `flask shell`
# When the flask shell command runs, it will invoke this function and register the items returned by it in the shell session. 
# The reason the function returns a dictionary and not a list is that for each item you have to also provide a name under which it will be referenced in the shell, 
# which is given by the dictionary keys.
# registers the function as a shell context function. 
@app.shell_context_processor 
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
