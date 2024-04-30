import os
import shutil
import subprocess
import zipfile
from models import Artifact
from database import db

def clean_up_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def save_artifact_to_db(zip_file_path, commit_hash):
    artifact_name = f'{commit_hash}/output_binary'
    new_artifact = Artifact(name=artifact_name, zip_path=zip_file_path)
    db.session.add(new_artifact)
    db.session.commit()
    return new_artifact.id

def build_program(program):
    repo_path = f'repos/{program.id}'
    clean_up_directory(repo_path)
    clone_result = subprocess.run(['git', 'clone', program.repo_url, repo_path], capture_output=True, text=True)
    
    if clone_result.returncode != 0:
        return {"message": f"Failed to clone repository: {clone_result.stderr}"}, 500
    
    latest_commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=repo_path, capture_output=True, text=True).stdout.strip()
    
    build_result = subprocess.run(['make', 'all'], cwd=f'{repo_path}/{program.build_directory}', capture_output=True, text=True)
    
    if build_result.returncode != 0:
        program.status = 'Failed'
        db.session.commit()
        return {"message": f"Build failed: {build_result.stderr}"}, 500
    
    zip_file_path = f'artifacts/{program.id}/{latest_commit}.zip'
    os.makedirs(os.path.dirname(zip_file_path), exist_ok=True)
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        zip_file.write(f'{repo_path}/{program.build_directory}/output_binary', arcname='output_binary')
        
    artifact_id = save_artifact_to_db(zip_file_path, latest_commit)
    
    program.status = 'Success'
    program.latest_commit = latest_commit
    program.latest_artifact_id = artifact_id
    db.session.commit()
    
    return {"message": "Build successful"}, 200

def check_for_new_commits():
    programs = Program.query.all()
    for program in programs:
        repo_path = f'repos/{program.id}'
        
        fetch_result = subprocess.run(['git', 'fetch'], cwd=repo_path, capture_output=True, text=True)
        
        if fetch_result.returncode != 0:
            continue
        
        status_result = subprocess.run(['git', 'status', '-sb'], cwd=repo_path, capture_output=True, text=True)
        
        if 'behind' in status_result.stdout:
            build_program(program)