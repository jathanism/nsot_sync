import json
import click
from nsot_sync.drivers import facter


@click.command()
@click.pass_context
def cli(ctx):
    '''The facter driver can add attributes to created resources from facter'''
    driver = facter.FacterDriver(cli_params=ctx.obj)
    if ctx.obj['NOOP']:
        click.echo(json.dumps(driver.get_resources()))
        return

    driver.ensure_attrs()
    driver.handle_resources()