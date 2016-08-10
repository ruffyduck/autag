"""Entry point for 'auTag'"""

from model.auflac import AuFlac
from model.basetag import get_tag
from controller.repltag import ReplaceTag
from controller.auimage import AutoImage
from controller.filereader import list_files, count_files, get_directory
from controller.autagger import AutoTagger
from controller.auremove import AutoRemoval
from controller.aurename import AutoRename
from model.audict import build_auto_dicts


AUFIL = AuFlac("resources/test.flac")
AUTA = get_tag("GENRE")
AUTA2 = get_tag("TITLE")

AUDICTS = build_auto_dicts("resources/autodicts.json")

REPTAG = ReplaceTag(AUDICTS["GENRE"], AUTA)
REPTAG2 = ReplaceTag(AUDICTS["TITLE"], AUTA2)

REMTAG = AutoRemoval()
REMTAG.read_flags("resources/autoremove.json")

AUIMG = AutoImage()

TAGGER = AutoTagger()
#AGGER.add_auto_tags([REPTAG, REPTAG2, AUIMG, REMTAG])

TAGGER.auto_tag_file(AUFIL)

AURENAME = AutoRename()
AURENAME.set_auto_value(AUFIL)
