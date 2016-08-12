"""Entry point for 'auTag'"""

from model.auflac import AuFlac
from model.basetag import get_tag
from controller.repltag import ReplaceTag
from controller.auimage import AutoImage
from controller.filereader import list_files, count_files, get_directory, delete_empty_directories, get_aufile
from controller.autagger import AutoTagger
from controller.auremove import AutoRemoval
from controller.aurename import AutoRename
from controller.aumove import AutoMove
from controller.auclean import AutoCleanup
from controller.audefault import AutoDefault
from model.audict import build_auto_dicts

from view.augui import AuGUI


AUFIL = get_aufile("resources/music/test.flac")
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

AUMOVE = AutoMove()
#AUMOVE.set_auto_value(AUFIL)

AUCLEAN = AutoCleanup()
AUCLEAN.set_auto_value(AUFIL)

AUDEF = AutoDefault("resources/defaultvalues.json")
AUDEF.set_auto_value(AUFIL)

AUFIL.save_changes()


gui = AuGUI()
gui.draw()
