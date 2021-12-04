# easyid
This is a Flask page and API for generating id strings.
This code is intended to be hosted on Heroku.  It is, in fact, at http://easyid.herokuapp.com/

An easyid is a short, memorable adjective-noun pair that can be created from any arbitrary string.  The app provides a numeric suffix with the pair in order to expand the id space.
I thought this might be a good way to help match labels for shipments of materials that have complex numeric ids.

TODO: Review word lists and take out any words that might result in an offensive id.
