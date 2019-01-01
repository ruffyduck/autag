"""Entry point for AuTag"""

import sys, getopt
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


def main(argv):

	try:
		opts, args = getopt.getopt(argv, "hd:", ["-help","directory="])
	except getopt.GetoptError as e:
		print(e)
		sys.exit(2)

	dir = None
	for opt, arg in opts:
		if opt == '-h':
			print("Pass '-d' or 'directory=' to tag files in given directory")
			sys.exit();
		elif opt in ('-d', '-directory'):
			dir = arg

	audicts = build_auto_dicts("resources/autodicts.json")
	auto_tag = AutoTagger()
	auto_tag.add_auto_tags([AutoImage(), AutoCleanup(), AutoNumbers(),
	                        AutoCrawler("UVtLSggkngYRiFHyFSdnjrgaFufcXmWIjrhiPkiN",
	                                    [get_tag("GENRE"),
	                                     get_tag("ORGANIZATION")],
	                                    audicts),
	                        ReplaceTag(audicts["GENRE"], get_tag("GENRE")),
	                        ReplaceTag(audicts["TITLE"], get_tag("TITLE")),
	                        AutoRemoval("resources/autoremove.json"),
	                        AutoDefault("resources/defaultvalues.json")])

	auto_file = AutoTagger()
	auto_file.add_auto_tags([AutoRename()])  #, AutoMove("D:/Musik/")])

	gui = AuGUI(auto_tag, auto_file, dir)
	gui.draw()


if __name__== "__main__":
	main(sys.argv[1:]);
