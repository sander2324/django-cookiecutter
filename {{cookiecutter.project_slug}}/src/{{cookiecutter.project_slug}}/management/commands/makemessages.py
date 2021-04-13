import glob
import os
import re

from django.conf import settings
from django.core.management.commands import makemessages


def flatten(list_of_lists):
    return [val for sublist in list_of_lists for val in sublist]


def undo_pot_creation_date_change():
    """
    Each time makemessages OR compilemessages is executed, the `POT-Creation-Date` header in the PO file is updated.
    This leads to both unnecessary merge conflicts AND not clean checkouts.
    Here we make sure the POT-Creation-Date does not change.
    """

    for translation_file in glob.glob("locales/*/LC_MESSAGES/django.po"):
        file_path = os.path.join(settings.BASE_DIR, translation_file)
        with open(file_path, "r") as f:
            file_str = f.read()
        file_str = re.sub(
            r"\"POT-Creation-Date: \d{4}-\d{2}-\d{2} \d{2}:\d{2}\+\d{4}\\n\"",
            '"POT-Creation-Date: 2019-01-01 00:00+0200\\n"'.encode(
                "unicode_escape"
            ).decode("utf-8"),
            file_str,
        )
        with open(file_path, "w") as f:
            f.write(file_str)


class Command(makemessages.Command):
    msgmerge_options = makemessages.Command.msgmerge_options + ["--no-fuzzy-matching"]

    def handle(self, *args, **options):
        super().handle(*args, **options)
        undo_pot_creation_date_change()
