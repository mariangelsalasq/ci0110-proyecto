{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red252\green99\blue94;\red173\green177\blue177;\red200\green147\blue255;
\red151\green205\blue255;\red190\green199\blue208;\red203\green203\blue202;\red183\green111\blue179;\red67\green192\blue160;
\red167\green197\blue151;\red252\green148\blue68;\red71\green138\blue206;\red205\green172\blue105;\red105\green179\blue255;
\red173\green176\blue178;}
{\*\expandedcolortbl;;\cssrgb\c100000\c48151\c44372;\cssrgb\c73503\c74682\c74891;\cssrgb\c82792\c66350\c100000;
\cssrgb\c65092\c84363\c100000;\cssrgb\c79043\c82190\c85130;\cssrgb\c83320\c83320\c83112;\cssrgb\c77407\c52698\c75307;\cssrgb\c30631\c78928\c69023;
\cssrgb\c71035\c80830\c65726;\cssrgb\c99757\c64750\c33519;\cssrgb\c34146\c61677\c84338;\cssrgb\c84195\c72766\c48633;\cssrgb\c47923\c75850\c100000;
\cssrgb\c73333\c74510\c74902;}
\margl1440\margr1440\vieww34000\viewh21460\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\strokec3  \strokec4 crearTableroVacio\strokec3 (): \
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn crearTableroVacio"\strokec3 )\
\
    \strokec6 matriz\strokec3  \strokec7 =\strokec3  [[\strokec5 "~"\strokec3  \strokec8 for\strokec3  \strokec6 i\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec10 8\strokec3 )] \strokec8 for\strokec3  \strokec6 j\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec10 8\strokec3 )]\
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn crearTableroVacio"\strokec3 )\
\
    \strokec8 return\strokec3  \strokec6 matriz\strokec3  \
\
\
\strokec2 def\strokec3  \strokec4 mostrarTablero\strokec3 (\strokec11 mat\strokec3 , \strokec11 ocultar\strokec7 =\strokec12 False\strokec3 ):    \
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn mostrarTablero"\strokec3 )\
\
    \strokec6 cadena\strokec3  \strokec7 =\strokec3  \strokec5 "  1 2 3 4 5 6 7 8\strokec13 \\n\strokec5 "\strokec3 \
\
    \strokec8 for\strokec3  \strokec6 i\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec10 8\strokec3 ):\
\
        \strokec6 cadena\strokec3  \strokec7 +=\strokec3  \strokec14 LETRAS\strokec3 [\strokec6 i\strokec3 ] \strokec7 +\strokec3  \strokec5 " "\strokec3 \
\
        \strokec8 for\strokec3  \strokec6 j\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec10 8\strokec3 ):\
            \
            \strokec6 valor\strokec3  \strokec7 =\strokec3  \strokec11 mat\strokec3 [\strokec6 i\strokec3 ][\strokec6 j\strokec3 ]\
\
            \strokec8 if\strokec3  \strokec11 ocultar\strokec3  \strokec12 and\strokec3  \strokec6 valor\strokec3  \strokec7 ==\strokec3  \strokec5 "B"\strokec3 :\
                \strokec6 valor\strokec3  \strokec7 =\strokec3  \strokec5 "~"\strokec3 \
\
            \strokec6 cadena\strokec3  \strokec7 +=\strokec3  \strokec6 valor\strokec3  \strokec7 +\strokec3  \strokec5 " "\strokec3 \
\
        \strokec6 cadena\strokec3  \strokec7 +=\strokec3  \strokec5 "\strokec13 \\n\strokec5 "\strokec3 \
\
    \strokec4 print\strokec3 (\strokec6 cadena\strokec3 )\
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn mostrarTablero"\strokec3 )\
\
\
\strokec2 def\strokec3  \strokec4 convertirCoordenada\strokec3 (\strokec11 coord\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn convertirCoordenada"\strokec3 )\
\
    \strokec6 fila\strokec3  \strokec7 =\strokec3  \strokec14 LETRAS\strokec3 .index(\strokec11 coord\strokec3 [\strokec10 0\strokec3 ].upper())\
    \strokec6 columna\strokec3  \strokec7 =\strokec3  \strokec9 int\strokec3 (\strokec11 coord\strokec3 [\strokec10 1\strokec3 ]) \strokec7 -\strokec3  \strokec10 1\strokec3 \
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn convertirCoordenada"\strokec3 )\
\
    \strokec8 return\strokec3  \strokec6 fila\strokec3 , \strokec6 columna\strokec3 \
\
\
\strokec2 def\strokec3  \strokec4 coordenadaValida\strokec3 (\strokec11 coord\strokec3 ):\
\
    \strokec8 if\strokec3  \strokec4 len\strokec3 (\strokec11 coord\strokec3 ) \strokec7 !=\strokec3  \strokec10 2\strokec3 :\
        \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
    \strokec6 letra\strokec3  \strokec7 =\strokec3  \strokec11 coord\strokec3 [\strokec10 0\strokec3 ].upper()\
    \strokec6 numero\strokec3  \strokec7 =\strokec3  \strokec11 coord\strokec3 [\strokec10 1\strokec3 ]\
\
    \strokec8 if\strokec3  \strokec6 letra\strokec3  \strokec12 not\strokec3  \strokec12 in\strokec3  \strokec14 LETRAS\strokec3 :\
        \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
    \strokec8 if\strokec3  \strokec6 numero\strokec3  \strokec12 not\strokec3  \strokec12 in\strokec3  \strokec5 "12345678"\strokec3 :\
        \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
    \strokec8 return\strokec3  \strokec12 True\strokec3 \
\
\
\strokec2 def\strokec3  \strokec4 validarPosicion\strokec3 (\strokec11 tablero\strokec3 , \strokec11 fila\strokec3 , \strokec11 columna\strokec3 , \strokec11 tama\'f1o\strokec3 , \strokec11 orientacion\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn validarPosicion"\strokec3 )\
\
    \strokec8 if\strokec3  \strokec11 orientacion\strokec3  \strokec7 ==\strokec3  \strokec5 "H"\strokec3 :\
\
        \strokec8 if\strokec3  \strokec11 columna\strokec3  \strokec7 +\strokec3  \strokec11 tama\'f1o\strokec3  \strokec7 >\strokec3  \strokec10 8\strokec3 :\
            \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
        \strokec8 for\strokec3  \strokec6 i\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec11 tama\'f1o\strokec3 ):\
\
            \strokec8 if\strokec3  \strokec11 tablero\strokec3 [\strokec11 fila\strokec3 ][\strokec11 columna\strokec3  \strokec7 +\strokec3  \strokec6 i\strokec3 ] \strokec7 !=\strokec3  \strokec5 "~"\strokec3 :\
                \strokec8 return\strokec3  \strokec12 False\strokec3  \
\
    \strokec8 elif\strokec3  \strokec11 orientacion\strokec3  \strokec7 ==\strokec3  \strokec5 "V"\strokec3 :\
\
        \strokec8 if\strokec3  \strokec11 fila\strokec3  \strokec7 +\strokec3  \strokec11 tama\'f1o\strokec3  \strokec7 >\strokec3  \strokec10 8\strokec3 :\
            \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
        \strokec8 for\strokec3  \strokec6 i\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec11 tama\'f1o\strokec3 ):\
\
            \strokec8 if\strokec3  \strokec11 tablero\strokec3 [\strokec11 fila\strokec3  \strokec7 +\strokec3  \strokec6 i\strokec3 ][\strokec11 columna\strokec3 ] \strokec7 !=\strokec3  \strokec5 "~"\strokec3 :\
                \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
    \strokec8 else\strokec3 :\
        \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn validarPosicion"\strokec3 )\
\
    \strokec8 return\strokec3  \strokec12 True\strokec3 \
\
\
\strokec2 def\strokec3  \strokec4 colocarBarco\strokec3 (\strokec11 tablero\strokec3 , \strokec11 fila\strokec3 , \strokec11 columna\strokec3 , \strokec11 tama\'f1o\strokec3 , \strokec11 orientacion\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn colocarBarco"\strokec3 )\
\
    \strokec8 if\strokec3  \strokec11 orientacion\strokec3  \strokec7 ==\strokec3  \strokec5 "H"\strokec3 :\
\
        \strokec8 for\strokec3  \strokec6 i\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec11 tama\'f1o\strokec3 ):\
\
            \strokec11 tablero\strokec3 [\strokec11 fila\strokec3 ][\strokec11 columna\strokec3  \strokec7 +\strokec3  \strokec6 i\strokec3 ] \strokec7 =\strokec3  \strokec5 "B"\strokec3 \
\
    \strokec8 else\strokec3 :\
\
        \strokec8 for\strokec3  \strokec6 i\strokec3  \strokec8 in\strokec3  \strokec9 range\strokec3 (\strokec11 tama\'f1o\strokec3 ):\
\
            \strokec11 tablero\strokec3 [\strokec11 fila\strokec3  \strokec7 +\strokec3  \strokec6 i\strokec3 ][\strokec11 columna\strokec3 ] \strokec7 =\strokec3  \strokec5 "B"\strokec3 \
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn colocarBarco"\strokec3 )\
\
\
\strokec2 def\strokec3  \strokec4 colocarBarcosJugador\strokec3 (\strokec11 tablero\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn colocarBarcosJugador"\strokec3 )\
\
    \strokec6 barcos\strokec3  \strokec7 =\strokec3  [\strokec10 2\strokec3 , \strokec10 3\strokec3 , \strokec10 3\strokec3 , \strokec10 4\strokec3 ]\
\
    \strokec8 for\strokec3  \strokec6 tama\'f1o\strokec3  \strokec8 in\strokec3  \strokec6 barcos\strokec3 :\
\
        \strokec6 colocado\strokec3  \strokec7 =\strokec3  \strokec12 False\strokec3 \
\
        \strokec8 while\strokec3  \strokec12 not\strokec3  \strokec6 colocado\strokec3 :\
\
            \strokec4 mostrarTablero\strokec3 (\strokec11 tablero\strokec3 )\
\
            \strokec4 print\strokec3 (\strokec5 "Barco de tama\'f1o"\strokec3 , \strokec6 tama\'f1o\strokec3 )\
\
            \strokec6 coord\strokec3  \strokec7 =\strokec3  \strokec4 input\strokec3 (\strokec5 "Digite coordenada inicial: "\strokec3 )\
            \strokec6 orientacion\strokec3  \strokec7 =\strokec3  \strokec4 input\strokec3 (\strokec5 "Digite orientaci\'f3n H/V: "\strokec3 ).\strokec4 upper\strokec3 ()\
\
            \strokec8 if\strokec3  \strokec12 not\strokec3  \strokec4 coordenadaValida\strokec3 (\strokec6 coord\strokec3 ):\
                \strokec4 print\strokec3 (\strokec5 "Coordenada inv\'e1lida"\strokec3 )\
                \strokec8 continue\strokec3 \
\
            \strokec6 fila\strokec3 , \strokec6 columna\strokec3  \strokec7 =\strokec3  \strokec4 convertirCoordenada\strokec3 (\strokec6 coord\strokec3 )\
\
            \strokec8 if\strokec3  \strokec4 validarPosicion\strokec3 (\strokec11 tablero\strokec3 , \strokec6 fila\strokec3 , \strokec6 columna\strokec3 , \strokec6 tama\'f1o\strokec3 , \strokec6 orientacion\strokec3 ):\
\
                \strokec4 colocarBarco\strokec3 (\strokec11 tablero\strokec3 , \strokec6 fila\strokec3 , \strokec6 columna\strokec3 , \strokec6 tama\'f1o\strokec3 , \strokec6 orientacion\strokec3 )\
\
                \strokec6 colocado\strokec3  \strokec7 =\strokec3  \strokec12 True\strokec3 \
\
            \strokec8 else\strokec3 :\
                \strokec4 print\strokec3 (\strokec5 "Posici\'f3n inv\'e1lida"\strokec3 )\
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn colocarBarcosJugador"\strokec3 )\
\
\
\strokec2 def\strokec3  \strokec4 colocarBarcosCPU\strokec3 (\strokec11 tablero\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn colocarBarcosCPU"\strokec3 )\
\
    \strokec6 barcos\strokec3  \strokec7 =\strokec3  [\strokec10 2\strokec3 , \strokec10 3\strokec3 , \strokec10 3\strokec3 , \strokec10 4\strokec3 ]\
\
    \strokec8 for\strokec3  \strokec6 tama\'f1o\strokec3  \strokec8 in\strokec3  \strokec6 barcos\strokec3 :\
\
        \strokec6 colocado\strokec3  \strokec7 =\strokec3  \strokec12 False\strokec3 \
\
        \strokec8 while\strokec3  \strokec12 not\strokec3  \strokec6 colocado\strokec3 :\
\
            \strokec6 fila\strokec3  \strokec7 =\strokec3  random.randint(\strokec10 0\strokec3 , \strokec10 7\strokec3 )\
            \strokec6 columna\strokec3  \strokec7 =\strokec3  random.randint(\strokec10 0\strokec3 , \strokec10 7\strokec3 )\
\
            \strokec6 orientacion\strokec3  \strokec7 =\strokec3  random.choice([\strokec5 "H"\strokec3 , \strokec5 "V"\strokec3 ])\
\
            \strokec8 if\strokec3  \strokec4 validarPosicion\strokec3 (\strokec11 tablero\strokec3 , \strokec6 fila\strokec3 , \strokec6 columna\strokec3 , \strokec6 tama\'f1o\strokec3 , \strokec6 orientacion\strokec3 ):\
\
                \strokec4 colocarBarco\strokec3 (\strokec11 tablero\strokec3 , \strokec6 fila\strokec3 , \strokec6 columna\strokec3 , \strokec6 tama\'f1o\strokec3 , \strokec6 orientacion\strokec3 )\
\
                \strokec6 colocado\strokec3  \strokec7 =\strokec3  \strokec12 True\strokec3 \
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn colocarBarcosCPU"\strokec3 )\
\
\
\strokec2 def\strokec3  \strokec4 procesarDisparo\strokec3 (\strokec11 tablero\strokec3 , \strokec11 fila\strokec3 , \strokec11 columna\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn procesarDisparo"\strokec3 )\
\
    \strokec8 if\strokec3  \strokec11 tablero\strokec3 [\strokec11 fila\strokec3 ][\strokec11 columna\strokec3 ] \strokec7 ==\strokec3  \strokec5 "B"\strokec3 :\
\
        \strokec11 tablero\strokec3 [\strokec11 fila\strokec3 ][\strokec11 columna\strokec3 ] \strokec7 =\strokec3  \strokec5 "X"\strokec3 \
\
        \strokec4 print\strokec3 (\strokec5 "Impacto"\strokec3 )\
\
        \strokec8 return\strokec3  \strokec12 True\strokec3 \
\
    \strokec8 elif\strokec3  \strokec11 tablero\strokec3 [\strokec11 fila\strokec3 ][\strokec11 columna\strokec3 ] \strokec7 ==\strokec3  \strokec5 "~"\strokec3 :\
\
        \strokec11 tablero\strokec3 [\strokec11 fila\strokec3 ][\strokec11 columna\strokec3 ] \strokec7 =\strokec3  \strokec5 "O"\strokec3 \
\
        \strokec4 print\strokec3 (\strokec5 "Agua"\strokec3 )\
\
        \strokec8 return\strokec3  \strokec12 True\strokec3 \
\
    \strokec8 else\strokec3 :\
\
        \strokec4 print\strokec3 (\strokec5 "Ya dispar\'f3 ah\'ed"\strokec3 )\
\
        \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
\
\strokec2 def\strokec3  \strokec4 quedanBarcos\strokec3 (\strokec11 tablero\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn quedanBarcos"\strokec3 )\
\
    \strokec8 for\strokec3  \strokec6 fila\strokec3  \strokec8 in\strokec3  \strokec11 tablero\strokec3 :\
\
        \strokec8 if\strokec3  \strokec5 "B"\strokec3  \strokec12 in\strokec3  \strokec6 fila\strokec3 :\
\
            \strokec8 return\strokec3  \strokec12 True\strokec3 \
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn quedanBarcos"\strokec3 )\
\
    \strokec8 return\strokec3  \strokec12 False\strokec3 \
\
\
\strokec2 def\strokec3  \strokec4 turnoJugador\strokec3 (\strokec11 tableroEnemigo\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn turnoJugador"\strokec3 )\
\
    \strokec6 valido\strokec3  \strokec7 =\strokec3  \strokec12 False\strokec3 \
\
    \strokec8 while\strokec3  \strokec12 not\strokec3  \strokec6 valido\strokec3 :\
\
        \strokec6 coord\strokec3  \strokec7 =\strokec3  \strokec4 input\strokec3 (\strokec5 "Digite coordenada de disparo: "\strokec3 )\
\
        \strokec8 if\strokec3  \strokec12 not\strokec3  \strokec4 coordenadaValida\strokec3 (\strokec6 coord\strokec3 ):\
\
            \strokec4 print\strokec3 (\strokec5 "Coordenada inv\'e1lida"\strokec3 )\
\
            \strokec8 continue\strokec3 \
\
        \strokec6 fila\strokec3 , \strokec6 columna\strokec3  \strokec7 =\strokec3  \strokec4 convertirCoordenada\strokec3 (\strokec6 coord\strokec3 )\
\
        \strokec6 valido\strokec3  \strokec7 =\strokec3  \strokec4 procesarDisparo\strokec3 (\strokec11 tableroEnemigo\strokec3 , \strokec6 fila\strokec3 , \strokec6 columna\strokec3 )\
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn turnoJugador"\strokec3 )\
\
\
\strokec2 def\strokec3  \strokec4 turnoCPU\strokec3 (\strokec11 tableroJugador\strokec3 ):\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn turnoCPU"\strokec3 )\
\
    \strokec6 valido\strokec3  \strokec7 =\strokec3  \strokec12 False\strokec3 \
\
    \strokec8 while\strokec3  \strokec12 not\strokec3  \strokec6 valido\strokec3 :\
\
        \strokec6 fila\strokec3  \strokec7 =\strokec3  random.randint(\strokec10 0\strokec3 , \strokec10 7\strokec3 )\
        \strokec6 columna\strokec3  \strokec7 =\strokec3  random.randint(\strokec10 0\strokec3 , \strokec10 7\strokec3 )\
\
        \strokec8 if\strokec3  \strokec11 tableroJugador\strokec3 [\strokec6 fila\strokec3 ][\strokec6 columna\strokec3 ] \strokec12 not\strokec3  \strokec12 in\strokec3  [\strokec5 "X"\strokec3 , \strokec5 "O"\strokec3 ]:\
\
            \strokec4 print\strokec3 (\strokec5 "La computadora dispar\'f3 en:"\strokec3 ,\
                  \strokec14 LETRAS\strokec3 [\strokec6 fila\strokec3 ] \strokec7 +\strokec3  \strokec9 str\strokec3 (\strokec6 columna\strokec3  \strokec7 +\strokec3  \strokec10 1\strokec3 ))\
\
            \strokec4 procesarDisparo\strokec3 (\strokec11 tableroJugador\strokec3 , \strokec6 fila\strokec3 , \strokec6 columna\strokec3 )\
\
            \strokec6 valido\strokec3  \strokec7 =\strokec3  \strokec12 True\strokec3 \
\
    \strokec4 print\strokec3 (\strokec5 "salio de la fn turnoCPU"\strokec3 )\
\
\
\strokec2 def\strokec3  \strokec4 jugarVsCPU\strokec3 ():\
\
    \strokec4 print\strokec3 (\strokec5 "entro a la fn jugarVsCPU"\strokec3 )\
\
    \strokec6 tableroJugador\strokec3  \strokec7 =\strokec3  \strokec4 crearTableroVacio\strokec3 ()\
    \strokec6 tableroCPU\strokec3  \strokec7 =\strokec3  \strokec4 crearTableroVacio\strokec3 ()\
\
    \strokec4 print\strokec3 (\strokec5 "Configure sus barcos"\strokec3 )\
\
    \strokec4 colocarBarcosJugador\strokec3 (\strokec6 tableroJugador\strokec3 )\
\
    \strokec4 colocarBarcosCPU\strokec3 (\strokec6 tableroCPU\strokec3 )\
\
    \strokec6 terminado\strokec3  \strokec7 =\strokec3  \strokec12 False\strokec3 \
\
    \strokec8 while\strokec3  \strokec12 not\strokec3  \strokec6 terminado\strokec3 :\
\
        \strokec4 print\strokec3 (\strokec5 "\strokec13 \\n\strokec5 ===== SU TURNO ====="\strokec3 )\
\
        \strokec4 mostrarTablero\strokec3 (\strokec6 tableroCPU\strokec3 , \strokec12 True\strokec3 )\
\
        \strokec4 turnoJugador\strokec3 (\strokec6 tableroCPU\strokec3 )\
\
        \strokec8 if\strokec3  \strokec12 not\strokec3  \strokec4 quedanBarcos\strokec3 (\strokec6 tableroCPU\strokec3 ):\
\
            \strokec4 print\strokec3 (\strokec5 "USTED GAN\'d3"\strokec3 )\
\
            \strokec6 terminado\strokec3  \strokec7 =\strokec3  \strokec12 True\strokec3 \
\
            \strokec8 break\strokec3 \
\
        \strokec4 print\strokec3 (\strokec5 "\strokec13 \\n\strokec5 ===== TURNO CPU ====="\strokec3 )\
\
        \strokec4 turnoCPU\strokec3 (\strokec6 tableroJugador\strokec3 )\
\
        \strokec4 print\strokec3 (\strokec5 "\strokec13 \\n\strokec5 Su tablero actual:"\strokec3 )\
\
        \strokec4 mostrarTablero\strokec3 (\strokec6 tableroJugador\strokec3 )\
\
        \strokec8 if\strokec3  \strokec12 not\strokec3  \strokec4 quedanBarcos\strokec3 (\strokec6 tableroJugador\strokec3 ):\
\
            \strokec4 print\strokec3 (\strokec5 "LA COMPUTADORA GAN\'d3"\strokec3 )\
\
            \strokec6 terminado\strokec3  \strokec7 =\strokec3  \strokec12 True\cf15 \strokec15 \
\
}