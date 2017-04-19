# peek-a-boo


## Prerequirements

We use:

- `python3.6`
- PostgreSQL 9.6.1

### Development

We use:

- `pycharm` (optional)
- `editorconfig` plugin (**required**)
- `pip-tools` (**required**)


## Development

### Configuration

You will need to copy file `config/config.template` to `config/config.secret`.
And set all the required values. Basically, it is just a database connection.
Or you can create file `murkosha/settings/environments/local.py`.
And specify any configuration you want. See template version.

### virtualenv

We are using `virtualenv` for development.

### Installing requirements

We are using `pip-tools` to specify dependencies.

Firstly, install `pip-tools` into your `virtualenv`:

```bash
pip install pip-tools
```

To install (or renew) existing dependencies run:

```bash
pip-sync
```

### Adding new dependencies

To add new dependency you will need to:

1. Add it to the `requirements.in`
2. Run `pip-compile requirements.in`
3. Install new dependencies with `pip-sync`

### Database setup

To create new development database run:

```bash
psql postgres -f sql/create_database.sql
```

Then migrate your database:

```bash
python manage.py migrate
```


## Running

### Creating superuser

To create a superuser run: `python manage.py createsuperuser`

### Running development server

To run the project: `python manage.py runserver`
