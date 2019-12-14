import click
from flask.cli import AppGroup
from . import APP, jobs


AGD = AppGroup('demo')
APP.cli.add_command(AGD)


@AGD.command()
def github():
    ''' queue github jobs '''
    job = jobs.github_users.queue()
    click.echo(click.style(job.id, bold=True, fg='blue'))
