from flask import Blueprint, request, jsonify, send_file, render_template
from models import Program, Artifact 
from utils import build_program, check_for_new_commits
from database import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "Build Server is running"

@routes.route('/register', methods=['POST'])
def register_program():
    data = request.json
    new_program = Program(repo_url=data['repo_url'], build_command=data.get('build_command', 'make all'), build_directory=data.get('build_directory', 'hello'))
    db.session.add(new_program)
    db.session.commit()
    return jsonify({"message": "Program registered"}), 201

@routes.route('/build/<int:program_id>', methods=['POST'])
def build(program_id):
    program = Program.query.get(program_id)
    if program:
        build_result = build_program(program)
        return jsonify(build_result)
    else:
        return jsonify({"message": "Program not found"}), 404

@routes.route('/artifacts/<int:program_id>/latest')
def get_latest_artifact(program_id):
    program = Program.query.get(program_id)
    if program and program.latest_artifact:
        return send_file(program.latest_artifact.zip_path, as_attachment=True)
    else:
        return jsonify({"message": "No artifact found"}), 404
        
@routes.route('/status')
def status():
    programs = Program.query.all()
    return render_template('status.html', programs=programs)