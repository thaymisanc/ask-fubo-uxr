"""Builds ../ask-fubo-web.html (one self-contained file) from src.html + assets/.
Run from this folder:  python3 build.py   (needs Pillow: pip install pillow)"""
import re,os,io,base64,json
from PIL import Image
A="assets/"
src=open("src.html").read()
b64=lambda b:base64.b64encode(b).decode()
imgs={}
for k in sorted(set(re.findall(r"img:'([ms]\d\d)'",src))):
    folder="movies" if k[0]=="m" else "shows"
    im=Image.open(A+"%s/%s.png"%(folder,k[1:])).convert("RGB");buf=io.BytesIO();im.save(buf,"JPEG",quality=84,optimize=True)
    imgs[k]="data:image/jpeg;base64,"+b64(buf.getvalue())
NAMED={'n-kimmel':'shows/jimmy kimmel.jpeg','n-greys':'shows/greys.jpg','n-doc':'shows/p24472079_b_v12_ah.jpg','n-ncis':'shows/p184930_b_v12_ay.jpg','n-snl':'shows/p183890_b_v12_ax.jpg','n-ncisorig':'shows/p26467713_b_v12_aq.jpg','n-ncisny':'shows/p32898230_b_v12_ab.jpg','n-cupertino':'shows/p32898304_b_v12_ab.jpg','n-chifire':'shows/p9257455_b_v12_bi.jpg','n-survivor':'shows/p187348_b_v12_by.jpg','n-dwts':'shows/p187511_b_v12_ax (1).jpg','n-animal':'shows/p23199865_b_v12_ac.jpg','n-assisted':'shows/p18537710_b_v12_aj.jpg','n-bbt':'shows/p185554_b_v11_az.jpg','n-rhonyc':'shows/p186003_b_v12_ah.jpg',
'n-otto':'movies/a man called otto.jpeg','n-castaway':'movies/castaway.jpeg','n-forrest':'movies/forrest gump.jpg','n-song':'movies/a song for christmas.png','n-merry':'movies/p34270030_v_v12_aa.jpg','n-grownups':'movies/p7937506_v_v8_ac.jpg','n-grownups2':'movies/p9670463_v_v8_ab.jpg','n-xlove':'movies/christmas love story.png','n-mylove':'movies/my christmas love.png','n-unplugged':'movies/p34255683_v_v12_aa.jpg','n-danish':'movies/p34255496_v_v12_aa.jpg','n-promises':'movies/p34270021_v_v12_aa.jpg',
'ff-nwsl':'featured on fubo/3b5aa4f8-3b88-4715-abaf-419482caacff.png','ff-fav':'featured on fubo/4fb8b9d8-867a-406b-8bc6-9a77b51d6af5.png','ff-xmas':'featured on fubo/56d7f7f5-1d65-430c-93c4-1656cf13971e.png','ff-nbacup':'featured on fubo/90bb6f1c-a76c-47fc-877e-22f711bcaf6e.png'}
NAMED.update({'n-indis':'news/p19991910_b_h8_aa.jpg','n-wxcmd':'news/p23801375_b_h8_ah.jpg','n-cbsm':'news/p31819629_b_h8_ab.jpg','n-natrep':'news/p949199_b_h10_ae.jpg'})
for i in range(1,11):
    imgs['num%d'%i]='data:image/svg+xml;base64,'+b64(open(A+'numbers/top10_rank%d.svg'%i,'rb').read())
NAMED.update({'n-tonight':'shows/tonightshow.jpeg','n-lateshow':'shows/lateshow.jpeg','n-meyers':'shows/latenight.jpeg','n-kep1':'shows/p34150509_e_h10_aa.jpg','n-kep2':'shows/p34208542_e_h10_aa.jpg','n-scrubs':'shows/p31616310_b_v12_ae.jpg','n-scrubsh':'shows/p31616310_b_h8_ae.jpg','n-abbott':'shows/p20001974_b_v12_as.jpg','n-voice':'shows/p8449661_b_v12_ax.jpg','n-bluey':'shows/p16030422_b_v12_ak (1).jpg','n-paw':'shows/p10077400_b_v12_cd.jpg','n-tj':'shows/p19292277_b_v12_ac.jpg','n-bugs':'shows/p19292303_b_v12_ab.jpg','n-peppa':'shows/p274928_b_v12_aa.jpg','n-kitties':'shows/p23652268_b_v12_ba.jpg','n-rubble':'shows/p23455586_b_v12_ao.jpg','n-chimed':'shows/p11770123_b_h8_bh.jpg','n-bestmed':'shows/p30194083_b_h8_af.jpg',
'n-desc2':'movies/p13805148_v_v8_ab.jpg','n-fgm':'movies/p14773322_b_v11_aa.jpg','n-adastra':'movies/p15724355_v_v12_ad.jpg','n-addams':'movies/p16762657_v_v12_ad.jpg','n-seven':'movies/p17198_v_v12_ay.jpg','n-deadman':'movies/p17487_v_v8_aa.jpg','n-camprock':'movies/p180548_v_v8_an.jpg','n-copland':'movies/p19678_v_v8_ad.jpg','n-spider':'movies/p20130736_v_v12_ao.jpg','n-monsters':'movies/p27462_v_v12_am.jpg','n-holstory':'movies/p28473495_v_v12_aa.jpg','n-makebreak':'movies/p31622213_v_v12_aa.jpg','n-tis':'movies/p12101353_v_v8_ab.jpg','n-gamble':'movies/p28532105_v_v11_ab.jpg','n-gangster':'movies/p472_v_v11_aa.jpg','n-prom':'movies/p8815605_v_v11_al.jpg','n-hoodlum':'movies/p19852_v_v12_af.jpg','n-heist':'movies/p25533804_v_v12_aa.jpg'})
NAMED.update({'n-theholiday':'movies/christmas1.webp','n-forgotten':'movies/christmas4.jpeg','n-grinch':'movies/christmas5.jpeg','n-pitch':'movies/p31319995_v_v12_ac.jpg'})
NAMED['profile']='profile-avatar.png'
for i in range(1,7):NAMED['rc%d'%i]='recaps/recap %d.png'%i
for k,f in NAMED.items():
    if "'%s'"%k not in src:continue
    im=Image.open(A+f).convert("RGB")
    if im.width>1100:im=im.resize((1100,round(im.height*1100/im.width)))
    buf=io.BytesIO();im.save(buf,"JPEG",quality=84,optimize=True)
    imgs[k]="data:image/jpeg;base64,"+b64(buf.getvalue())
for t in sorted(set(re.findall(r"\bl[ab]:'(\w+)'",src))):
    imgs["team-"+t]="data:image/png;base64,"+b64(open(A+"teams/%s.png"%t,"rb").read())
for c in sorted(set(re.findall(r"img:'([a-z0-9-]+)',k:",src))):
    imgs["ch-"+c]="data:image/png;base64,"+b64(open(A+"channels/%s.png"%c,"rb").read())
ff=lambda w,f:"@font-face{font-family:'FT Regola Neue';font-weight:%d;font-style:normal;font-display:swap;src:url(data:font/otf;base64,%s) format('opentype')}"%(w,b64(open(A+"font/FTRegolaNeue-%s.otf"%f,"rb").read()))
fonts="\n".join(ff(w,f) for w,f in [(400,"Regular"),(500,"Medium"),(600,"Semibold"),(700,"Bold")])
logo="data:image/png;base64,"+b64(open(A+"ask-fubo-logo.png","rb").read())
bg="data:image/jpeg;base64,"+b64(open(A+"ask-bg.jpg","rb").read())
h=src.replace("__ASKBG__",bg).replace("__ASKLOGO__",logo).replace("/*FONTS*/",fonts).replace("/*FWCSS*/",open(A+"components.css").read()).replace("<!--ICONS-->",open(A+"icons.svg").read())
old="function imgSrc(k){return k.startsWith('team-')||k.startsWith('ch-')?'img/'+k+'.png':'img/'+k+'.jpg';}"
assert old in h
h=h.replace(old,"const IMGDATA="+json.dumps(imgs)+";function imgSrc(k){return IMGDATA[k]||'';}")
o="try{const d=await window.claude.use('downloads');if(!d)throw 0;"
assert o in h
h=h.replace(o,"try{const d=(window.claude&&window.claude.use)?await window.claude.use('downloads'):null;if(!d){const u=URL.createObjectURL(new Blob([toCsv(rows)],{type:'text/csv'}));const a=document.createElement('a');a.href=u;a.download='ask-fubo-queries.csv';document.body.appendChild(a);a.click();a.remove();toast('CSV downloaded');return;}")
i=h.index('</style>')+8
out='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+h[:i]+'</head><body>'+h[i:]+'</body></html>'
open("../ask-fubo-web.html","w").write(out)
print(len(out)//1024,"KB written to ../ask-fubo-web.html")
