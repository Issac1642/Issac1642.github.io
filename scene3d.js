(function(){
var el=document.getElementById('scene');if(!el||!window.THREE)return;
var r;try{r=new THREE.WebGLRenderer({antialias:true,alpha:true})}catch(x){return}
var W=function(){return el.clientWidth},H=function(){return el.clientHeight};
r.setPixelRatio(Math.min(window.devicePixelRatio,2));r.setSize(W(),H(),false);
el.innerHTML='';el.appendChild(r.domElement);
var s=new THREE.Scene(),cam=new THREE.PerspectiveCamera(40,W()/H(),.1,100);
cam.position.set(-2.5,3.2,12);cam.lookAt(0,0,0);
var g=new THREE.Group(),w=new THREE.Group();s.add(g);g.add(w);w.position.x=1.6;function place(){g.position.x=W()>760?2.4:0}place();
var i,grid=new THREE.GridHelper(16,16,0x2a4a6a,0x16283a);grid.position.y=-3;w.add(grid);
var pg=new THREE.PlaneGeometry(7,7,14,14),pq=pg.attributes.position;
for(i=0;i<pq.count;i++){var u=pq.getX(i),v=pq.getY(i);pq.setZ(i,-.012*(u*u+v*v))}
var sh=new THREE.Group();
sh.add(new THREE.Mesh(pg,new THREE.MeshBasicMaterial({color:0xffb52e,wireframe:true,transparent:true,opacity:.4})));
sh.add(new THREE.Mesh(pg,new THREE.MeshBasicMaterial({color:0xffb52e,transparent:true,opacity:.09,side:THREE.DoubleSide,depthWrite:false})));
sh.rotation.y=Math.PI/2;w.add(sh);
var th=.87,ct=Math.cos(th),st=Math.sin(th),rr=2.5,dn=Math.sqrt(ct*ct+rr*rr*st*st),
 u1=[ct,0,st],u2=[ct/dn,0,rr*st/dn],e2=[-st,0,ct],NU=120,ND=50,L=[];
function mk(y0,z0){var n=NU+ND+1,pos=new Float32Array(n*3),col=new Float32Array(n*3),k;
 for(k=0;k<n;k++){var up=k<=NU;col[k*3]=up?.37:.62;col[k*3+1]=up?.78:.7;col[k*3+2]=1}
 var geo=new THREE.BufferGeometry();
 geo.setAttribute('position',new THREE.BufferAttribute(pos,3));geo.setAttribute('color',new THREE.BufferAttribute(col,3));
 w.add(new THREE.Line(geo,new THREE.LineBasicMaterial({vertexColors:true,transparent:true,opacity:.9})));
 L.push({y:y0,z:z0,xs:-.012*(y0*y0+z0*z0),pos:pos,geo:geo,n:n})}
for(var a=-2;a<=2;a++)for(var b=-1;b<=1;b++)mk(a*.8,b*1.5);
function upd(t){for(var i=0;i<L.length;i++){var l=L[i],p=l.pos;
 for(var k=0;k<l.n;k++){var x,y,z;
  if(k<=NU){var d=7*(1-k/NU),A=.3*Math.exp(-d/3)*(1-Math.exp(-d/.25)),ph=5*d+t*2.2;
   x=l.xs-u1[0]*d+A*Math.sin(ph)*e2[0];y=l.y+A*Math.cos(ph);z=l.z-u1[2]*d+A*Math.sin(ph)*e2[2]}
  else{var d2=4*(k-NU)/ND,B=.14*(1-Math.exp(-d2/.6)),q=B*Math.sin(3.3*d2+l.z*2-t*1.1);
   x=l.xs+u2[0]*d2+q*e2[0];y=l.y+B*Math.sin(2.1*d2+l.y*3+t*1.5);z=l.z+u2[2]*d2+q*e2[2]}
  p[k*3]=x;p[k*3+1]=y;p[k*3+2]=z}
 l.geo.attributes.position.needsUpdate=true}}
var N=650,pa=new Float32Array(N*3),PX=[],PY=[],PZ=[];
for(i=0;i<N;i++){PX[i]=-4.5+Math.random()*7;PY[i]=(Math.random()-.5)*5.2;PZ[i]=(Math.random()-.5)*5.2}
var pgm=new THREE.BufferGeometry();pgm.setAttribute('position',new THREE.BufferAttribute(pa,3));
w.add(new THREE.Points(pgm,new THREE.PointsMaterial({color:0xdfeaff,size:.06,transparent:true,opacity:.8})));
var px=0,py=0,t=0,still=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
el.addEventListener('pointermove',function(ev){var bb=el.getBoundingClientRect();px=(ev.clientX-bb.left)/bb.width-.5;py=(ev.clientY-bb.top)/bb.height-.5;if(still)frame()});
window.addEventListener('resize',function(){r.setSize(W(),H(),false);cam.aspect=W()/H();cam.updateProjectionMatrix();place();if(still)frame()});
function frame(){
 if(!still){t+=.016;for(var k=0;k<N;k++){PX[k]+=PX[k]<0?.035:.012;if(PX[k]>2.2)PX[k]=-4.5}}
 for(var m=0;m<N;m++){pa[m*3]=PX[m];pa[m*3+1]=PY[m];pa[m*3+2]=PZ[m]}
 pgm.attributes.position.needsUpdate=true;upd(t);
 g.rotation.y=.4*Math.sin(t*.15)+px*.7;g.rotation.x=.12+py*.3;
 r.render(s,cam);if(!still)requestAnimationFrame(frame)}
frame();
})();
