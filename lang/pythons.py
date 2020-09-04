from pygments import formatters , styles


style = styles.get_style_by_name('murphy')
formatter = formatters.HtmlFormatter(style=style)
outfile = open('pygment.css' , 'w')
outfile.write(formatter.get_style_defs())
outfile.close()
