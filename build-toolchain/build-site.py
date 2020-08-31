import os
import argparse
import configparser
import shutil
import markdown
import codecs
from distutils import dir_util

# Make our config global so we don't have to pass it to every function
config = {}

def main(args):
	global config
	parseConfig(args.settings)

	makeOutput()
	processFiles()


# Recusively processes all files in content_path. Markdown files are transformed
# into HTML. Other file types are copied as-is.
def processFiles():

	for root, dirs, files in os.walk(config['content_path']):

		# Map the source path to the destination path
		folder_path = os.path.relpath(root, start=config["content_path"])
		destination_path = os.path.join(config["output_path"], folder_path)
		os.makedirs(destination_path, exist_ok=True)

		# Process each file in the current path
		for file in files:
			source_file = os.path.join(root, file)
			dest_file = os.path.join(destination_path, file)

			if(file.endswith('md')):
				html_output = parse_markdown(source_file)

				# Change the extension to html and write the parsed stirng
				dest_file = os.path.splitext(dest_file)[0] + ".html"

				with codecs.open(dest_file, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
					output_file.write(html_output)
			else:
				shutil.copy(source_file, dest_file)


# Loads the contents of the specified file through the markdown processor, then inserts it
# into the appropriate template
def parse_markdown(markdown_file_path):
	md = markdown.Markdown(extensions = ['meta', 'footnotes', 'fenced_code', 'codehilite', 'toc', 'attr_list', 'tables', 'admonition'])
	
	# Load the markdown and convert it ot html
	html_content = ''
	with codecs.open(markdown_file_path, "r", encoding="utf-8") as f:
		markdown_text = f.read()
	
	html_content = md.convert(markdown_text)

	# If the markdown file specifies a template, use that. Otherwise, use the default template
	template_path = config['default_template']
	if 'template' in md.Meta:
		template_path = fixPath(md.Meta['template'])

	# Load the template, and replace any placeholder text with the appropriate content
	output_string = ''
	with codecs.open(template_path, mode="r", encoding="utf-8") as t:
		output_string = t.read()

	output_string = output_string.replace("{{CONTENT}}", html_content)
	output_string = output_string.replace("{{TOC}}", md.toc)

	if 'title' in md.Meta:
		output_string = output_string.replace("{{TITLE}}", md.Meta["title"][0])

	if 'body-class' in md.Meta:
		output_string = output_string.replace("{{BODYCLASS}}", md.Meta["body-class"][0])


	return output_string


# Clears the output path, then recreates it. This way, no
# old files are left behind between builds.
def makeOutput():
	output_path = config['output_path']
	shutil.rmtree(output_path, True)
	os.makedirs(output_path, 0o755)


# Normalizes the provided path relative to the path_root config variable.
# This variable is typically the location of the settings.cfg file.
def fixPath(path):
	return os.path.normpath(os.path.join(config['path_root'], path))


## Parses the config file specified using configparser and normalize the
## paths specified there, then stores those values in the global
## config dictionary.
def parseConfig(config_file_path):
	config_parser = configparser.RawConfigParser()	
	config_parser.read(config_file_path)

	# Determine where settings.cfg is located
	this_dir = os.getcwd()
	settings_path = os.path.dirname(config_file_path)
	config['path_root'] = os.path.join(this_dir, settings_path)

	# Get all the other paths, relative to the location of settings.cfg
	output_path = config_parser.get("Paths", "destination")
	content_path = config_parser.get("Paths", "source")
	template_path = config_parser.get("Templates", "default")

	# Normalize paths
	config['default_template'] = fixPath(template_path)
	config['output_path'] = fixPath(output_path)
	config['content_path'] = fixPath(content_path)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--settings', default="./settings.cfg")
	args = parser.parse_args()

	main(args)

