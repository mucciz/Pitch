from flask_script import Manager,Server
from app import create_app,db
from app.models import User
from  flask_migrate import Migrate, MigrateCommand

app = create_app('default')

manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ == '__main__':
    manager.run()
    
