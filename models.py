from database import db

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_url = db.Column(db.String(150), unique=True, nullable=False)
    build_command = db.Column(db.String(200), nullable=False, default='make all')
    build_directory = db.Column(db.String(200), nullable=False, default='hello')
    status = db.Column(db.String(50), nullable=False, default='Not Built')
    latest_commit = db.Column(db.String(40))
    latest_artifact_id = db.Column(db.Integer, db.ForeignKey('artifact.id'))
    latest_artifact = db.relationship('Artifact', backref='program', lazy=True)

    def __repr__(self):
        return f'<Program {self.repo_url}>'

class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    zip_path = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Artifact {self.name}>'