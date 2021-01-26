import os
import tempfile
import pytest


@pytest.fixture
def git_repository(tmpdir, scope='function'):  # scope: function, class, module, session
    path = tmpdir.mkdir('repo')
    os.system("""
    cd {d}
    git init
    touch A
    git config user.email 'user.exapmle.com'
    git configure user.name 'User Name'
    git add A
    git commit - 'A' A
    """.format(d=path.strpath))

    return path.strpath
