#snippet generator

import os

color_opts = ['light', 'stable', 'positive', 'calm', 'balanced', 'energized', 'assertive', 'royal', 'dark']
css_components = ['header', 'footer', 'button', 'list', 'card', 'form', 'toggle', 'checkbox', 'radio', 'range', 'select', 'tab', 'grid', 'utility']
bars = ['header', 'footer']
button_types = ['button', 'button-block', 'button-full']
bar_template = '<snippet>\n\
\t<content><![CDATA[\n\
<div class="bar bar-%s bar-%s">${1:<h1 class="title">Header</h1>}</div>\n\
]]></content>\n\
\t<tabTrigger>ion-%s:%s</tabTrigger>\n\
\t<source></source>\n\
\t<description></description>\n\
</snippet>'

button_template = '<snippet>\n\
\t<content><![CDATA[\n\
<button class="button%s button-%s">${1:Button}</button>\n\
]]></content>\n\
\t<tabTrigger>ion-%s:%s</tabTrigger>\n\
\t<source></source>\n\
\t<description></description>\n\
</snippet>'

button_template_1 = '<snippet>\n\
\t<content><![CDATA[\n\
<button class="button %s">${1:Button}</button>\n\
]]></content>\n\
\t<tabTrigger>ion-%s:%s</tabTrigger>\n\
\t<source></source>\n\
\t<description></description>\n\
</snippet>'

# template ='<snippet>\n\
# \t<content><![CDATA[\n\
# %s\n\
# ]]></content>\n\
# \t<tabTrigger>ion-%s:%s</tabTrigger>\n\
# \t<source></source>\n\
# \t<description>Snippet for %s %s</description>\n\
# </snippet>'
# button_template = '<button class="button%s">${1:Button}</button>'


for component in bars:

  if not os.path.exists(component):
      os.makedirs(component)

  for color in color_opts:
    # print color
    fname = '%s/ion-%s-%s.sublime-snippet' %(component,component,color)
    fo = open(fname, 'w')
    fo.write(bar_template %(component,color,component,color))
    fo.close()
    print fname+ ' generated.'

for component in button_types:

  if not os.path.exists(component):
      os.makedirs(component)

  for color in color_opts:
    fname = '%s/ion-%s-%s.sublime-snippet' %(component,component,color)
    fo  = open(fname, 'w')
    fo.write(button_template %([' '+component,''][component == 'button'], color, component, color))
    fo.close()
    print fname + ' generated.'

#TODO: add generator for README.md - Possibly add pictures

