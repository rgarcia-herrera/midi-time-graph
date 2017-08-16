#!/bin/bash

SVG=$1

PREFIX=`basename $SVG .svg`

PNG=${PREFIX}.png

inkscape $SVG --export-png=$PNG --export-area-drawing
