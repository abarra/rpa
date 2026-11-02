# Genera figuras/comparativa_algoritmos.pdf a partir de los resultados del notebook
# Uso: python comparativa_algoritmos.py comparativa_algoritmos.pdf
import sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch
import glob
for f in glob.glob('/usr/share/fonts/truetype/crosextra/Carlito-*.ttf'): fm.fontManager.addfont(f)
fams={f.name for f in fm.fontManager.ttflist}
plt.rcParams['font.family']='Carlito' if 'Carlito' in fams else 'DejaVu Sans'
plt.rcParams['font.size']=9
plt.rcParams['pdf.fonttype']=42
TEXT='#0b0b0b'; TEXT2='#52514e'; GRID='#e4e3df'; BLUE='#2a78d6'
# datos de la ejecución del notebook (mapa original)
labels=['Amplitud (casos 1 y 2)','Profundidad (caso 1)','Coste uniforme (casos 2 y 3)','A* H1 Manhattan (casos 2 y 3)','A* H2 Chebyshev (caso 3)','A* H3 2·Manhattan (caso 3)']
optimal=[True,False,True,True,True,False]  # caso 1: amplitud y profundidad con costes 1; resto con left=4
expanded=[26,19,33,26,30,13]
fringe=[7,12,8,10,8,5]
labels=[l+('' if o else '  ·  no óptima') for l,o in zip(labels,optimal)]
labels[0]='Amplitud (casos 1 y 2)  ·  no óptima en caso 2'
fig,axes=plt.subplots(1,2,figsize=(6.3,2.35),sharey=True,gridspec_kw=dict(wspace=0.08))
y=list(range(len(labels)))[::-1]
for ax,vals,title in [(axes[0],expanded,'Nodos expandidos'),(axes[1],fringe,'Tamaño máximo de la lista abierta')]:
    h=0.55
    for yi,v in zip(y,vals):
        ax.barh(yi,v,height=h,color=BLUE,edgecolor='none')
        ax.text(v+max(vals)*0.02,yi,str(v),va='center',ha='left',color=TEXT,fontsize=8.5)
    ax.set_title(title,loc='left',color=TEXT,fontsize=9.5,fontweight='bold')
    ax.set_xlim(0,max(vals)*1.15)
    ax.xaxis.grid(True,color=GRID,linewidth=0.6); ax.set_axisbelow(True)
    for s in ('top','right','left'): ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(GRID)
    ax.tick_params(axis='x',colors=TEXT2,labelsize=8,length=0)
    ax.tick_params(axis='y',length=0)
axes[0].set_yticks(y); axes[0].set_yticklabels(labels,color=TEXT,fontsize=8.5)
fig.savefig(sys.argv[1],bbox_inches='tight',pad_inches=0.02)

