from app import db
from app import Program

def test_build_program(client):
    program = Program(repo_url='https://github.com/example/hello.git')
    db.session.add(program)
    db.session.commit()
    
    response = client.post(f'/build/{program.id}')
    assert response.status_code == 200
    assert 'Build successful' in response.json['message']
    
    program = Program.query.get(program.id)
    assert program.status == 'Success'  
    assert program.latest_commit is not None
    assert program.latest_artifact is not None