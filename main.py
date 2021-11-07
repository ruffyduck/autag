import sys, getopt

from autag.tagging.auclean import AutoCleanup
from autag.tagging.aucrawl import AutoCrawler
from autag.tagging.audefault import AutoDefault
from autag.tagging.auimage import AutoImage
from autag.tagging.aumove import AutoMove
from autag.tagging.aunumber import AutoNumbers
from autag.tagging.auremove import AutoRemoval
from autag.tagging.aurename import AutoRename
from autag.tagging.autagger import AutoTagger
from autag.tagging.repltag import ReplaceTag
from autag.audict import build_auto_dicts
from autag.basetag import get_tag

def main(argv):
	try:
		opts, _ = getopt.getopt(argv, "hd:", ["-help","directory="])
	except getopt.GetoptError as e:
		print(e)
		sys.exit(2)

	dir = None
	for opt, arg in opts:
		if opt == '-h':
			print("Pass '-d' or 'directory=' to tag files in given directory")
			sys.exit()
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
	print("Done")


if __name__== "__main__":
	main(sys.argv[1:])
