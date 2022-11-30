import nox


@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest", "-s", "test")


@nox.session
def lint(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", "--show-diff-on-failure")
