(this["webpackJsonpfungataua-crm-frontend"]=this["webpackJsonpfungataua-crm-frontend"]||[]).push([[12],{116:function(e,t,r){"use strict";var a=r(2),o=r.n(a),c=r(8),n=r(43),s=r(5),i=r(12),l=r(10);t.a=function(e){var t=e.url,r=e.method,a=e.data,d=e.headers,j=e.nextSuccess,b=e.nextError,h=e.initialValue,u=void 0===h?"":h,m=Object(s.useState)(u),O=Object(n.a)(m,2),p=O[0],x=O[1],f=Object(s.useState)(!1),g=Object(n.a)(f,2),v=g[0],w=g[1],C=Object(s.useState)(""),y=Object(n.a)(C,2),N=y[0],_=y[1];return[function(){var e=Object(c.a)(o.a.mark((function e(){var c;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,_(null),w(!0),e.next=5,Object(i.a)({url:t,method:r,headers:d,data:a});case 5:(c=e.sent).data.success?(x(c.data.data),j&&j(c.data.data,x),w(!1)):(b&&b(c.data.error),w(!1),_(c.data.error)),e.next=14;break;case 9:e.prev=9,e.t0=e.catch(0),Object(l.j)(e.t0),w(!1),_(e.t0);case 14:case"end":return e.stop()}}),e,null,[[0,9]])})));return function(){return e.apply(this,arguments)}}(),v,N,p]}},120:function(e,t,r){"use strict";r(5);var a=r(274),o=r(275),c=r(105),n=r(114),s=r(6),i=r(14),l=function(e){return"/".concat(e)===s.d?Object(i.jsx)(n.a,{id:"menu.home"}):Object(i.jsx)(n.a,{id:"menu.".concat(e)})},d=function(e,t){return e.split(t)[0]+t},j=function(e){var t=e.match.path.substr(1),r=t.split("/");return r[r.length-1].indexOf(":")>-1&&(r=r.filter((function(e){return-1===e.indexOf(":")}))),Object(i.jsx)(i.Fragment,{children:Object(i.jsx)(a.a,{className:"pt-0 breadcrumb-container d-none d-sm-block d-lg-inline-block",children:r.map((function(e,a){return Object(i.jsx)(o.a,{active:r.length===a+1,children:r.length!==a+1?Object(i.jsx)(c.b,{to:"/".concat(d(t,e)),children:l(e)}):l(e)},a)}))})})};t.a=function(e){var t=e.heading,r=e.match;return Object(i.jsxs)(i.Fragment,{children:[t&&Object(i.jsx)("h1",{children:Object(i.jsx)(n.a,{id:t})}),Object(i.jsx)(j,{match:r})]})}},367:function(e,t,r){"use strict";r.r(t);var a=r(0),o=r(43),c=r(5),n=r.n(c),s=r(206),i=r(162),l=r(276),d=r(163),j=r(44),b=r(207),h=function(){var e=getComputedStyle(document.body);return{themeColor1:e.getPropertyValue("--theme-color-1").trim(),themeColor2:e.getPropertyValue("--theme-color-2").trim(),themeColor3:e.getPropertyValue("--theme-color-3").trim(),themeColor4:e.getPropertyValue("--theme-color-4").trim(),themeColor5:e.getPropertyValue("--theme-color-5").trim(),themeColor6:e.getPropertyValue("--theme-color-6").trim(),themeColor1_10:e.getPropertyValue("--theme-color-1-10").trim(),themeColor2_10:e.getPropertyValue("--theme-color-2-10").trim(),themeColor3_10:e.getPropertyValue("--theme-color-3-10").trim(),themeColor4_10:e.getPropertyValue("--theme-color-3-10").trim(),themeColor5_10:e.getPropertyValue("--theme-color-3-10").trim(),themeColor6_10:e.getPropertyValue("--theme-color-3-10").trim(),primaryColor:e.getPropertyValue("--primary-color").trim(),foregroundColor:e.getPropertyValue("--foreground-color").trim(),separatorColor:e.getPropertyValue("--separator-color").trim()}},u={backgroundColor:h().foregroundColor,titleFontColor:h().primaryColor,borderColor:h().separatorColor,borderWidth:.5,bodyFontColor:h().primaryColor,bodySpacing:10,xPadding:15,yPadding:15,cornerRadius:.15},m={legend:{display:!1},responsive:!0,maintainAspectRatio:!1,tooltips:u,plugins:{datalabels:{display:!1}},scales:{yAxes:[{gridLines:{display:!0,lineWidth:1,color:"rgba(0,0,0,0.1)",drawBorder:!1},ticks:{beginAtZero:!0,stepSize:10,suggestedMin:0,suggestedMax:20,padding:20}}],xAxes:[{gridLines:{display:!1}}]}},O={legend:{position:"bottom",labels:{padding:30,usePointStyle:!0,fontSize:12}},responsive:!0,maintainAspectRatio:!1,title:{display:!1},layout:{padding:{bottom:20}},tooltips:u},p=r(14),x=function(e){var t=e.data,r=e.shadow,a=void 0!==r&&r,n=Object(c.useRef)(null),s=Object(c.useState)(null),i=Object(o.a)(s,2)[1];return Object(c.useEffect)((function(){if(n&&n.current){a&&(b.Chart.controllers.lineWithShadow=b.Chart.controllers.line,b.Chart.controllers.lineWithShadow=b.Chart.controllers.line.extend({draw:function(e){b.Chart.controllers.line.prototype.draw.call(this,e);var t=this.chart.ctx;t.save(),t.shadowColor="rgba(0,0,0,0.15)",t.shadowBlur=10,t.shadowOffsetX=0,t.shadowOffsetY=10,t.responsive=!0,t.stroke(),b.Chart.controllers.line.prototype.draw.apply(this,arguments),t.restore()}}));var e=n.current.getContext("2d"),r=new b.Chart(e,{type:a?"lineWithShadow":"line",options:m,data:t});i(r)}}),[n,t,a]),Object(p.jsx)("canvas",{ref:n})},f=function(e){var t=e.data,r=e.shadow,a=void 0!==r&&r,n=Object(c.useRef)(null),s=Object(c.useState)(null),i=Object(o.a)(s,2)[1];return Object(c.useEffect)((function(){if(n&&n.current){a&&(b.Chart.defaults.pieWithShadow=b.Chart.defaults.pie,b.Chart.controllers.pieWithShadow=b.Chart.controllers.pie.extend({draw:function(e){b.Chart.controllers.pie.prototype.draw.call(this,e);var t=this.chart.ctx;t.save(),t.shadowColor="rgba(0,0,0,0.15)",t.shadowBlur=10,t.shadowOffsetX=0,t.shadowOffsetY=10,t.responsive=!0,b.Chart.controllers.pie.prototype.draw.apply(this,arguments),t.restore()}}));var e=n.current.getContext("2d"),r=new b.Chart(e,{type:a?"pieWithShadow":"pie",options:O,data:t});i(r)}}),[n,t,a]),Object(p.jsx)("canvas",{ref:n})},g=r(113),v=r(120),w=r(114),C=function(e){var t=e.className,r=void 0===t?"mb-4":t,a=e.icon,o=e.title,c=e.value;return Object(p.jsx)("div",{className:"icon-row-item ".concat(r),children:Object(p.jsx)(i.a,{children:Object(p.jsxs)(l.a,{className:"text-center",children:[Object(p.jsx)("i",{className:a}),Object(p.jsx)("p",{className:"card-text font-weight-semibold mb-0",children:Object(p.jsx)(w.a,{id:o})}),Object(p.jsx)("p",{className:"lead text-center",children:c})]})})})},y=n.a.memo(C),N=r(277),_=r(10),V=(r(278),-1),k=-1;function S(e){var t,r,o=function(){clearTimeout(V),V=setTimeout((function(){r.update(),V=-1}),500)};Object(c.useEffect)((function(){return(r=new N.a(t,Object(a.a)(Object(a.a)({},e.settings),{},{direction:Object(_.i)().direction}))).mount(),r.on("resize",o),k=setTimeout((function(){var e=document.createEvent("HTMLEvents");e.initEvent("resize",!1,!1),window.dispatchEvent(e)}),500),function(){clearTimeout(V),clearTimeout(k),r&&r.destroy()}}),[]);return Object(p.jsx)("div",{children:Object(p.jsxs)("div",{className:"glide",ref:function(e){return t=e},children:[Object(p.jsx)("div",{"data-glide-el":"track",className:"glide__track",children:Object(p.jsx)("div",{className:"glide__slides",children:e.children})}),!e.settings.hideNav&&Object(p.jsxs)("div",{className:"glide__arrows slider-nav","data-glide-el":"controls",children:[Object(p.jsx)("button",{type:"button",className:"glide__arrow glide__arrow--left left-arrow btn btn-link","data-glide-dir":"<",children:Object(p.jsx)("i",{className:"simple-icon-arrow-left"})}),Object(p.jsx)("div",{className:"glide__bullets slider-dot-container","data-glide-el":"controls[nav]",children:function(){for(var t=n.a.Children.count(e.children),r=[],a=0;a<t;a++)r.push(Object(p.jsx)("button",{type:"button",className:"glide__bullet slider-dot","data-glide-dir":"=".concat(a)},a));return r}()}),Object(p.jsx)("button",{type:"button",className:"glide__arrow glide__arrow--right right-arrow btn btn-link","data-glide-dir":">",children:Object(p.jsx)("i",{className:"simple-icon-arrow-right"})})]})]})})}S.defaultProps={settings:{}};var P=S,E=function(e){var t=e.data;return Object(p.jsx)("div",{className:"icon-cards-row",children:Object(p.jsx)(P,{settings:{gap:5,perView:4,type:"carousel",breakpoints:{320:{perView:1},576:{perView:2},1600:{perView:4}},hideNav:!0},children:t.map((function(e,t){return Object(p.jsx)("div",{children:Object(p.jsx)(y,Object(a.a)(Object(a.a)({},e),{},{className:"mb-4"}))},"icon_card_".concat(t))}))})})},T=r(116),W=(r(208),r(45)),z=r(164),A=r.n(z),B=r(279),R=r(209),F=r(323),H=r(6),L=function(){var e=Object(c.useState)({from:Object(_.h)(),to:Object(_.h)()}),t=Object(o.a)(e,2),r=t[0],n=t[1],s=function(e,t){Object(_.j)(e),n(Object(a.a)(Object(a.a)({},r),{},Object(W.a)({},t,Object(_.h)(e))))};return Object(p.jsx)(i.a,{children:Object(p.jsxs)(l.a,{children:[Object(p.jsx)(d.a,{children:Object(p.jsx)(w.a,{id:"dashboard.download-report"})}),Object(p.jsxs)(B.a,{children:[Object(p.jsx)(R.a,{children:Object(p.jsx)(w.a,{id:"dashboard.download-report-from"})}),Object(p.jsx)(A.a,{value:r.from,onChange:function(e){return s(e,"from")}})]}),Object(p.jsxs)(B.a,{children:[Object(p.jsx)(R.a,{children:Object(p.jsx)(w.a,{id:"dashboard.download-report-to"})}),Object(p.jsx)(A.a,{value:r.to,onChange:function(e){return s(e,"to")}})]}),Object(p.jsx)(B.a,{className:"d-flex justify-content-end",children:Object(p.jsx)(F.a,{size:"sm",className:"btn-shadow btn btn-primary",download:!0,href:"".concat(H.a,"/dashboard/download-client-service-report-datewise?from=").concat(r.from,"&to=").concat(r.to),target:"_blank",children:Object(p.jsx)(w.a,{id:"dashboard.download-reports-button"})})})]})})},M=h(),U={labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],datasets:[{label:"",data:[54,63,60,65,50,68,60],borderColor:M.themeColor1,pointBackgroundColor:M.foregroundColor,pointBorderColor:M.themeColor1,pointHoverBackgroundColor:M.themeColor1,pointHoverBorderColor:M.foregroundColor,pointRadius:6,pointBorderWidth:2,pointHoverRadius:8,fill:!1}]};t.default=Object(j.b)((function(e){var t=e.authUser;return{accessToken:t.accessToken,currentUser:t.currentUser}}),{})((function(e){var t=e.match,r=e.accessToken,n=e.currentUser.is_superadmin,j=Object(T.a)({url:"/dashboard/get-card-info",headers:{Authorization:r},initialValue:[{title:"dashboards.no-of-clients",icon:"iconsminds-clock",value:0},{title:"dashboards.no-of-services",icon:"iconsminds-basket-coins",value:0},{title:"dashboards.no-of-visits",icon:"iconsminds-arrow-refresh",value:0}]}),b=Object(o.a)(j,4),h=b[0],u=b[1],m=b[2],O=b[3],C=Object(T.a)({url:"/dashboard/get-client-visits",headers:{Authorization:r},initialValue:U,nextSuccess:function(e,t){t(Object(a.a)(Object(a.a)({},U),{},{labels:e.labels,datasets:[Object(a.a)(Object(a.a)({},U.datasets[0]),{},{data:e.data})]}))}}),y=Object(o.a)(C,4),N=y[0],V=y[1],k=y[2],S=y[3],P=Object(T.a)({url:"/dashboard/get-referral-pie-chart",headers:{Authorization:r},initialValue:U,nextSuccess:function(e,t){t(Object(a.a)(Object(a.a)({},U),{},{labels:e.labels,datasets:[Object(a.a)(Object(a.a)({},U.datasets[0]),{},{data:e.data})]}))}}),W=Object(o.a)(P,4),z=W[0],A=W[1],B=W[2],R=W[3];return Object(c.useEffect)((function(){h(),N(),z()}),[]),u||V||A?Object(p.jsx)("div",{className:"loading"}):((k||B||m)&&Object(_.j)({chartLineError:k,chartPieError:B,cardError:m}),Object(p.jsxs)(p.Fragment,{children:[Object(p.jsx)(s.a,{children:Object(p.jsxs)(g.a,{xxs:"12",children:[Object(p.jsx)(v.a,{heading:"menu.dashboard",match:t}),Object(p.jsx)(g.b,{className:"mb-5"})]})}),Object(p.jsxs)(s.a,{children:[Object(p.jsx)(g.a,{xxs:"12",md:"8",className:"mb-4",children:Object(p.jsx)(i.a,{className:"h-100",children:Object(p.jsxs)(l.a,{children:[Object(p.jsx)(d.a,{children:Object(p.jsx)(w.a,{id:"dashboard.client-activity-data"})}),Object(p.jsx)("div",{className:"dashboard-line-chart my-4",children:Object(p.jsx)(x,{data:S})})]})})}),Object(p.jsx)(g.a,{xxs:"12",md:"4",className:"mb-4",children:n&&Object(p.jsx)(L,{})})]}),Object(p.jsx)(s.a,{children:Object(p.jsx)(g.a,{xxs:"12",md:"8",className:"mb-4",children:Object(p.jsx)(i.a,{className:"h-100",children:Object(p.jsxs)(l.a,{children:[Object(p.jsx)(d.a,{children:Object(p.jsx)(w.a,{id:"dashboard.client-referral-data"})}),Object(p.jsx)("div",{className:"dashboard-line-chart my-4",children:Object(p.jsx)(f,{data:R})})]})})})}),Object(p.jsx)(s.a,{children:Object(p.jsx)(g.a,{lg:"12",xl:"8",children:Object(p.jsx)(E,{data:O})})})]}))}))}}]);
//# sourceMappingURL=views-home.b7fc6f94.chunk.js.map