from invoke import task

@task
def start(ctx):
    ctx.run("python3 -m src.index", pty=True)

@task
def build(ctx):
    ctx.run("python3 -m src.build", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("PYTHONPATH=. pylint src")
