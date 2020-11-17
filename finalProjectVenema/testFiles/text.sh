# Here's how to use image magick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: 
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
	-size $SIZE \
	label:'ImageMagick\nExamples\nby Anthony' \
	-draw "text 0,200 'Bottom of Display'" \
	$TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE
