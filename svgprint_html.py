import os
from os import listdir
from os.path import isfile, join

outSTR = """<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="183.85713"
   height="320"
   id="svg2"
   version="1.1"
   inkscape:version="0.48.4 r9939"
   sodipodi:docname="drawing.svg">
  <defs
     id="defs4" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.7"
     inkscape:cx="-285.59345"
     inkscape:cy="98.509114"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1920"
     inkscape:window-height="1056"
     inkscape:window-x="1920"
     inkscape:window-y="24"
     inkscape:window-maximized="1"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0" />
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-395.92857,-346.43361)">
    <path
       style="fill:none;stroke:#000000;stroke-width:1.00972736px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="m 396.43343,665.92875 182.84741,0 0,-318.99028 -182.84741,0 z"
       id="path2985"
       inkscape:connector-curvature="0"
       sodipodi:nodetypes="ccccc" />
    <path
       style="fill:#MYCOLORVALUE;fill-opacity:0.43378996;stroke:#000000;stroke-width:0.79987603px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       d="m 396.32893,666.03325 182.95714,0 0,-MYHEIGHTVALUE -182.95714,0 z"
       id="path2985-3"
       inkscape:connector-curvature="0" />
  </g>
</svg>
"""

d= {'Eggs' : 'FFFF66', 'Orange Juice' : 'FF6600', 'BLUE' : '0000c0', 'Milk' : 'FFF7D9'}

def im_output(value, color):
	files = [ f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(),f)) ]
	i = -1
	print outSTR.replace('MYHEIGHTVALUE', str(value * 320)).replace('MYCOLORVALUE', d.get(color))
