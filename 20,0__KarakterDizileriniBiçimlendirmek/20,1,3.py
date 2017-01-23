sayfa="""<html>
    <head>
        <title> {{ sayfa başlığı }} </title>
    </head>

    <body>
        <h1> {{ birinci seviye başlık }} </h1>
        <p>Web sitemize hoşgeldiniz! Konumuz: {{ konu }}</p>
    </body>
</html>"""

print(sayfa % ("Python Programlama Dili",
               "Python Programlama Dili",
               "Python Programlama Dili"))
