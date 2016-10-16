import urllib2
import simplejson
import cStringIO

fetcher = urllib2.build_opener()
searchTerm = 'confused people faces'
startIndex = 0
searchUrl = "http://ajax.googleapis.com/ajax/services" \
            "/search/images?v=1.0&q=%s&start=%s", (searchTerm, startIndex)
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)

