from fabric import task

@task
def render_build(c):
    # bundle install
    c.run('pip install -r requirements.txt')

    # bundle exec rake assets:precompile
    c.run('python manage.py collectstatic')

    # bundle exec rake assets:clean
    # 何もする必要がない場合はスキップしても構いません

    # bundle exec rake db:migrate
    c.run('python manage.py migrate')