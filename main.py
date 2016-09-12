"""Entry point for AuTag"""

from controller.auclean import AutoCleanup
from controller.aucrawl import AutoCrawler
from controller.audefault import AutoDefault
from controller.auimage import AutoImage
from controller.aumove import AutoMove
from controller.aunumber import AutoNumbers
from controller.auremove import AutoRemoval
from controller.aurename import AutoRename
from controller.autagger import AutoTagger
from controller.repltag import ReplaceTag
from model.audict import build_auto_dicts
from model.basetag import get_tag
from view.augui import AuGUI


AUDICTS = build_auto_dicts("resources/autodicts.json")

AUTO_TAG = AutoTagger()
AUTO_TAG.add_auto_tags([AutoImage(), AutoCleanup(), AutoNumbers(),
                        AutoCrawler("UVtLSggkngYRiFHyFSdnjrgaFufcXmWIjrhiPkiN",
                                    [get_tag("GENRE"),
                                     get_tag("ORGANIZATION")],
                                    AUDICTS),
                        ReplaceTag(AUDICTS["GENRE"], get_tag("GENRE")),
                        ReplaceTag(AUDICTS["TITLE"], get_tag("TITLE")),
                        AutoRemoval("resources/autoremove.json"),
                        AutoDefault("resources/defaultvalues.json")])

AUTO_FILE = AutoTagger()
AUTO_FILE.add_auto_tags([AutoRename()])  #, AutoMove("D:/Musik/")])

gui = AuGUI(AUTO_TAG, AUTO_FILE)
gui.draw()
