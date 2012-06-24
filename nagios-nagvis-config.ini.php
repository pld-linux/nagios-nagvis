; <?php return 1; ?>
; the line above is to prevent viewing this file from web. DON'T REMOVE IT!

; ----------------------------
; Default NagVis Configuration File
; At delivery everything here is commented out. The default values are set in
; the NagVis code. You can make your changes here, it'll overwrite the default
; settings.
; ----------------------------

; global options
[global]
; select language (english,german,...)
language="english"
; rotate maps (0/1)
rotatemaps=1
; maps to rotate
maps="localhost,demo,demo2"
; show header (0/1)
displayheader=1
; options per line in header
headercount=4
; use gdlibs (if set to 0 lines will not work, all other types should work fine)
usegdlibs=1
; refresh time of pages
refreshtime=60

; default values for the maps
[defaults]
; default backend (id of the default backend)
backend="ndomy_1"
; default icons
icons="std_medium"
; recognize service states in host/hostgroup objects
recognizeservices=1
; recognize only hard states (not soft)
onlyhardstates=0
; background color of maps
backgroundcolor="#fff"

; options for the wui
[wui]
; auto update frequency
autoupdatefreq=25

; path options
[paths]
; absolute physical NagVis path
base="/usr/share/nagios/nagvis/"
; absolute html NagVis path
htmlbase="/nagios/nagvis"
; absolute html NagVis cgi path
htmlcgi="/nagios/cgi-bin"

; options for the NDO-Backend
; in this example the ID of the Backend is "ndomy_1" you can define another ID.
[backend_ndomy_1]
; type of backend - MUST be set
backendtype="ndomy"
; hostname for NDO-db
dbhost="localhost"
; portname for NDO-db
dbport=3306
; database-name for NDO-db
dbname="nagios"
; username for NDO-db
dbuser="nagios"
; password for NDO-db
dbpass="nagios"
; prefix for tables in NDO-db
dbprefix="nagios_"
; instace-name for tables in NDO-db
dbinstancename="default"
; maximum delay of the NDO Database in Seconds
maxtimewithoutupdate=180

; include options
[includes]
; header include
header="header.nagvis.inc"

; EOF
