import os
color_opts = ['light', 'stable', 'positive', 'calm', 'balanced', 'energized', 'assertive', 'royal', 'dark']
css_components = ['header', 'footer', 'button', 'list', 'card', 'form', 'toggle', 'checkbox', 'radio', 'range', 'select', 'tab', 'grid', 'utility']
bars = ['header', 'footer']

bar_template = '<snippet>\n\
\t<content><![CDATA[\n\
<${1:div} class="bar bar-%s bar-%s">${2:<h1 class="title">Header</h1>}</${1:div}>\n\
]]></content>\n\
\t<tabTrigger>ion-%s:%s</tabTrigger>\n\
</snippet>'


for component in bars:

  if not os.path.exists(component):
      os.makedirs(component)
    
  for color in color_opts:
    # print color
    fname = "%s/ion-header-%s.sublime-snippet" %(component,color)
    fo = open(fname, "w")
    fo.write(bar_template %(component,color,component,color))
    fo.close()
    print fname+ " generated."

