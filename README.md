gmuj-python-convert-urls-to-sitemap

This script will take an input text file containing a list of URLs to be converted into XML sitemap format. For more information on the format, please see https://www.google.com/sitemaps/protocol.html

This input text file should contain a list of URLs - one per line - which will be used to generate a corresponding sitemap. You can begin a line with a # symbol to mark it as a comment.

The filename of the input text file can be specified either interactively at runtime or by providing the filename using the -f (or --file) argument. 

An output file will be generated which represents the URLs in the input list in XML sitemap format. 

The output file will be named with a label and a timestamp and will be placed in the "\_sitemap-results" subfolder. 