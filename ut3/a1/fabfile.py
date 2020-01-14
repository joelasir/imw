from fabric.api import env, cd, local, run


env.hosts = ['vm.alu5820.me']


def deploy():
    local('git push')
    with cd('~/webapps/vmweb'):
      run('git pull')
    run('supervisorctl restart vmweb')
