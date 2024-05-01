from django.apps import apps
from django.core.management.base import BaseCommand
from django.core.serializers import serialize

class Command(BaseCommand):
    help = 'Dump data with row limit'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--model',
            dest='model',
            help='Specify a model to dump',
        )

        # Named (required) arguments
        parser.add_argument(
            '--filename',
            dest='filename',
            required=True,
            help='Specify a filename to save the output',
        )

    def handle(self, *args, **options):
        model_to_dump = options['model']
        filename = options['filename']

        # Ensure filename ends with .json
        if not filename.endswith('.json'):
            filename += '.json'

        with open(filename, 'w') as f:
            if model_to_dump:
                # User has requested to dump a specific model
                ModelClass = apps.get_model('finance_app', model_to_dump)
                data = serialize('json', ModelClass.objects.all()[:100000])
                f.write(data)
            else:
                # Dump all models
                for model in apps.get_app_config('finance_app').get_models():
                    data = serialize('json', model.objects.all()[:100000])
                    f.write(data)

        self.stdout.write(f'Data has been successfully written to {filename}')