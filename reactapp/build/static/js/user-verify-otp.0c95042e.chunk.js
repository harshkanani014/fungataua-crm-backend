(this["webpackJsonpfungataua-crm-frontend"]=this["webpackJsonpfungataua-crm-frontend"]||[]).push([[8],{113:function(t,e,n){"use strict";n.d(e,"a",(function(){return s})),n.d(e,"b",(function(){return i}));var r=n(0),a=(n(5),n(205)),o=n(14),s=function(t){return Object(o.jsx)(a.a,Object(r.a)(Object(r.a)({},t),{},{widths:["xxs","xs","sm","md","lg","xl","xxl"]}))},i=function(t){var e=t.className;return Object(o.jsx)("div",{className:"separator ".concat(e)})}},114:function(t,e,n){"use strict";var r=n(0),a=(n(5),n(204)),o=n(147),s=n(14);e.a=Object(o.c)((function(t){return Object(s.jsx)(a.a,Object(r.a)({},t))}),{withRef:!1})},116:function(t,e,n){"use strict";var r=n(2),a=n.n(r),o=n(8),s=n(43),i=n(5),c=n(12),u=n(10);e.a=function(t){var e=t.url,n=t.method,r=t.data,l=t.headers,f=t.nextSuccess,m=t.nextError,p=t.initialValue,d=void 0===p?"":p,h=Object(i.useState)(d),b=Object(s.a)(h,2),v=b[0],j=b[1],O=Object(i.useState)(!1),y=Object(s.a)(O,2),T=y[0],S=y[1],g=Object(i.useState)(""),x=Object(s.a)(g,2),P=x[0],D=x[1];return[function(){var t=Object(o.a)(a.a.mark((function t(){var o;return a.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,D(null),S(!0),t.next=5,Object(c.a)({url:e,method:n,headers:l,data:r});case 5:(o=t.sent).data.success?(j(o.data.data),f&&f(o.data.data,j),S(!1)):(m&&m(o.data.error),S(!1),D(o.data.error)),t.next=14;break;case 9:t.prev=9,t.t0=t.catch(0),Object(u.j)(t.t0),S(!1),D(t.t0);case 14:case"end":return t.stop()}}),t,null,[[0,9]])})));return function(){return t.apply(this,arguments)}}(),T,P,v]}},377:function(t,e,n){"use strict";n.r(e);var r=n(0),a=n(43),o=n(5),s=n(203),i=n(206),c=n(162),u=n(163),l=n(279),f=n(209),m=n(105),p=n(173),d=n(44),h=n(30);function b(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function v(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function j(t,e,n){return e&&v(t.prototype,e),n&&v(t,n),t}function O(t,e){if("function"!==typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&T(t,e)}function y(t){return(y=Object.setPrototypeOf?Object.getPrototypeOf:function(t){return t.__proto__||Object.getPrototypeOf(t)})(t)}function T(t,e){return(T=Object.setPrototypeOf||function(t,e){return t.__proto__=e,t})(t,e)}function S(t,e){return!e||"object"!==typeof e&&"function"!==typeof e?function(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}(t):e}function g(t){var e=function(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(t){return!1}}();return function(){var n,r=y(t);if(e){var a=y(this).constructor;n=Reflect.construct(r,arguments,a)}else n=r.apply(this,arguments);return S(this,n)}}function x(t){return function(t){if(Array.isArray(t))return P(t)}(t)||function(t){if("undefined"!==typeof Symbol&&Symbol.iterator in Object(t))return Array.from(t)}(t)||function(t,e){if(!t)return;if("string"===typeof t)return P(t,e);var n=Object.prototype.toString.call(t).slice(8,-1);"Object"===n&&t.constructor&&(n=t.constructor.name);if("Map"===n||"Set"===n)return Array.from(t);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return P(t,e)}(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function P(t,e){(null==e||e>t.length)&&(e=t.length);for(var n=0,r=new Array(e);n<e;n++)r[n]=t[n];return r}function D(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:2,n=String(t);if(0===e)return n;var r=n.match(/(.*?)([0-9]+)(.*)/),a=r?r[1]:"",o=r?r[3]:"",s=r?r[2]:n,i=s.length>=e?s:(x(Array(e)).map((function(){return"0"})).join("")+s).slice(-1*e);return"".concat(a).concat(i).concat(o)}var w={daysInHours:!1,zeroPadTime:2};function C(t,e){var n=t.days,r=t.hours,a=t.minutes,o=t.seconds,s=Object.assign(Object.assign({},w),e),i=s.daysInHours,c=s.zeroPadTime,u=s.zeroPadDays,l=void 0===u?c:u,f=Math.min(2,c),m=i?D(r+24*n,c):D(r,f);return{days:i?"":D(n,l),hours:m,minutes:D(a,f),seconds:D(o,f)}}var k=function(t){O(n,t);var e=g(n);function n(){var t;return b(this,n),(t=e.apply(this,arguments)).state={count:t.props.count||3},t.startCountdown=function(){t.interval=window.setInterval((function(){0===t.state.count-1?(t.stopCountdown(),t.props.onComplete&&t.props.onComplete()):t.setState((function(t){return{count:t.count-1}}))}),1e3)},t.stopCountdown=function(){clearInterval(t.interval)},t.addTime=function(e){t.stopCountdown(),t.setState((function(t){return{count:t.count+e}}),t.startCountdown)},t}return j(n,[{key:"componentDidMount",value:function(){this.startCountdown()}},{key:"componentWillUnmount",value:function(){clearInterval(this.interval)}},{key:"render",value:function(){return this.props.children?Object(o.cloneElement)(this.props.children,{count:this.state.count}):null}}]),n}(o.Component);k.propTypes={count:h.number,children:h.element,onComplete:h.func};var E=function(t){O(n,t);var e=g(n);function n(t){var r;if(b(this,n),(r=e.call(this,t)).mounted=!1,r.initialTimestamp=r.calcOffsetStartTimestamp(),r.offsetStartTimestamp=r.props.autoStart?0:r.initialTimestamp,r.offsetTime=0,r.legacyMode=!1,r.legacyCountdownRef=Object(o.createRef)(),r.tick=function(){var t=r.calcTimeDelta(),e=t.completed&&!r.props.overtime?void 0:r.props.onTick;r.setTimeDeltaState(t,void 0,e)},r.start=function(){if(!r.isStarted()){var t=r.offsetStartTimestamp;r.offsetStartTimestamp=0,r.offsetTime+=t?r.calcOffsetStartTimestamp()-t:0;var e=r.calcTimeDelta();r.setTimeDeltaState(e,"STARTED",r.props.onStart),r.props.controlled||e.completed&&!r.props.overtime||(r.clearTimer(),r.interval=window.setInterval(r.tick,r.props.intervalDelay))}},r.pause=function(){r.isPaused()||(r.clearTimer(),r.offsetStartTimestamp=r.calcOffsetStartTimestamp(),r.setTimeDeltaState(r.state.timeDelta,"PAUSED",r.props.onPause))},r.stop=function(){r.isStopped()||(r.clearTimer(),r.offsetStartTimestamp=r.calcOffsetStartTimestamp(),r.offsetTime=r.offsetStartTimestamp-r.initialTimestamp,r.setTimeDeltaState(r.calcTimeDelta(),"STOPPED",r.props.onStop))},r.isStarted=function(){return r.isStatus("STARTED")},r.isPaused=function(){return r.isStatus("PAUSED")},r.isStopped=function(){return r.isStatus("STOPPED")},r.isCompleted=function(){return r.isStatus("COMPLETED")},r.handleOnComplete=function(t){r.props.onComplete&&r.props.onComplete(t)},t.date){var a=r.calcTimeDelta();r.state={timeDelta:a,status:a.completed?"COMPLETED":"STOPPED"}}else r.legacyMode=!0;return r}return j(n,[{key:"componentDidMount",value:function(){this.legacyMode||(this.mounted=!0,this.props.onMount&&this.props.onMount(this.calcTimeDelta()),this.props.autoStart&&this.start())}},{key:"componentDidUpdate",value:function(t){this.legacyMode||this.props.date!==t.date&&(this.initialTimestamp=this.calcOffsetStartTimestamp(),this.offsetStartTimestamp=this.initialTimestamp,this.offsetTime=0,this.setTimeDeltaState(this.calcTimeDelta()))}},{key:"componentWillUnmount",value:function(){this.legacyMode||(this.mounted=!1,this.clearTimer())}},{key:"calcTimeDelta",value:function(){var t=this.props,e=t.date,n=t.now,r=t.precision,a=t.controlled,o=t.overtime;return function(t){var e,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=n.now,a=void 0===r?Date.now:r,o=n.precision,s=void 0===o?0:o,i=n.controlled,c=n.offsetTime,u=void 0===c?0:c,l=n.overtime;e="string"===typeof t?new Date(t).getTime():t instanceof Date?t.getTime():t,i||(e+=u);var f=i?e:e-a(),m=Math.min(20,Math.max(0,s)),p=Math.round(1e3*parseFloat(((l?f:Math.max(0,f))/1e3).toFixed(m))),d=Math.abs(p)/1e3;return{total:p,days:Math.floor(d/86400),hours:Math.floor(d/3600%24),minutes:Math.floor(d/60%60),seconds:Math.floor(d%60),milliseconds:Number((d%1*1e3).toFixed()),completed:p<=0}}(e,{now:n,precision:r,controlled:a,offsetTime:this.offsetTime,overtime:o})}},{key:"calcOffsetStartTimestamp",value:function(){return Date.now()}},{key:"addTime",value:function(t){this.legacyCountdownRef.current.addTime(t)}},{key:"clearTimer",value:function(){window.clearInterval(this.interval)}},{key:"isStatus",value:function(t){return this.state.status===t}},{key:"setTimeDeltaState",value:function(t,e,n){var r=this;if(this.mounted){var a;!this.state.timeDelta.completed&&t.completed&&(this.props.overtime||this.clearTimer(),a=this.handleOnComplete);return this.setState((function(n){var a=e||n.status;return t.completed&&!r.props.overtime?a="COMPLETED":e||"COMPLETED"!==a||(a="STOPPED"),{timeDelta:t,status:a}}),(function(){n&&n(r.state.timeDelta),a&&a(r.state.timeDelta)}))}}},{key:"getApi",value:function(){return this.api=this.api||{start:this.start,pause:this.pause,stop:this.stop,isStarted:this.isStarted,isPaused:this.isPaused,isStopped:this.isStopped,isCompleted:this.isCompleted}}},{key:"getRenderProps",value:function(){var t=this.props,e=t.daysInHours,n=t.zeroPadTime,r=t.zeroPadDays,a=this.state.timeDelta;return Object.assign(Object.assign({},a),{api:this.getApi(),props:this.props,formatted:C(a,{daysInHours:e,zeroPadTime:n,zeroPadDays:r})})}},{key:"render",value:function(){if(this.legacyMode){var t=this.props,e=t.count,n=t.children,r=t.onComplete;return Object(o.createElement)(k,{ref:this.legacyCountdownRef,count:e,onComplete:r},n)}var a=this.props,s=a.className,i=a.overtime,c=a.children,u=a.renderer,l=this.getRenderProps();if(u)return u(l);if(c&&this.state.timeDelta.completed&&!i)return Object(o.cloneElement)(c,{countdown:l});var f=l.formatted,m=f.days,p=f.hours,d=f.minutes,h=f.seconds;return Object(o.createElement)("span",{className:s},l.total<0?"-":"",m,m?":":"",p,":",d,":",h)}}]),n}(o.Component);E.defaultProps=Object.assign(Object.assign({},w),{controlled:!1,intervalDelay:1e3,precision:0,autoStart:!0}),E.propTypes={date:Object(h.oneOfType)([Object(h.instanceOf)(Date),h.string,h.number]),daysInHours:h.bool,zeroPadTime:h.number,zeroPadDays:h.number,controlled:h.bool,intervalDelay:h.number,precision:h.number,autoStart:h.bool,overtime:h.bool,className:h.string,children:h.element,renderer:h.func,now:h.func,onMount:h.func,onStart:h.func,onPause:h.func,onStop:h.func,onTick:h.func,onComplete:h.func};var M=E,N=n(113),A=n(114),R=n(1),I=n(117),z=n(10),U=n(116),_=n(14),L=function(t){var e;return t?4!==t.length&&(e="Please enter a valid OTP!"):e="Please enter an OTP",e},V=function(){var t=Object(z.c)().email,e=Object(U.a)({url:"/auth/resend-otp",method:"POST",data:{email:t},nextSuccess:function(){I.b.success("OTP reset Successful!","Verify OTP Success",3e3,null,null,"")}}),n=Object(a.a)(e,1)[0],r=function(){return n()};return Object(_.jsx)(M,{date:Date.now()+3e5,renderer:function(t){var e=t.hours,n=t.minutes,a=t.seconds,o=t.completed;return Object(_.jsx)(s.a,{className:"btn-shadow btn btn-primary btn-lg",onClick:o?r:function(){},disabled:!o,children:o?"Resend OTP":"".concat(D(e),":").concat(D(n),":").concat(D(a))})}})},F=Object(o.memo)(V);e.default=Object(d.b)((function(t){var e=t.authUser;return{loading:e.loading,message:e.message,error:e.error}}),{verifyOTPAction:R.bc})((function(t){var e=t.history,n=t.loading,d=t.error,h=t.message,b=t.verifyOTPAction,v=Object(o.useState)(""),j=Object(a.a)(v,1)[0],O=Object(z.c)(),y=O.active,T=O.email;Object(o.useEffect)((function(){d?I.b.error(d,"Verify OTP Error",3e3,null,null,""):n||"logged_in"!==h||I.b.success("Login Successful!","Verify OTP Success",3e3,null,null,"")}),[d,h,n]);var S={otp:j};return y||e.push("/"),Object(_.jsx)(i.a,{className:"h-100",children:Object(_.jsx)(N.a,{xxs:"12",md:"10",className:"mx-auto my-auto",children:Object(_.jsxs)(c.a,{className:"auth-card",children:[Object(_.jsx)("div",{className:"position-relative image-side "}),Object(_.jsxs)("div",{className:"form-side",children:[Object(_.jsx)(m.b,{to:"/",className:"white"}),Object(_.jsxs)(u.a,{className:"mb-4",children:[Object(_.jsx)("h1",{className:"mb-4",children:" FUGATAUA CRM PORTAL "})," ",Object(_.jsx)("br",{}),Object(_.jsx)(A.a,{id:"user.verify-otp"})]}),Object(_.jsx)(p.c,{initialValues:S,onSubmit:function(t){if(!n)return void 0===T?(I.b.error("Invalid Request!","Verify OTP Error",3e3,null,null,""),void e.push("/")):void(""!==T&&""!==t.otp&&b(Object(r.a)(Object(r.a)({},t),{},{email:T}),e))},children:function(t){var e=t.errors,r=t.touched;return Object(_.jsxs)(p.b,{className:"av-tooltip tooltip-label-bottom",children:[Object(_.jsxs)(l.a,{className:"form-group has-float-label",children:[Object(_.jsx)(f.a,{children:Object(_.jsx)(A.a,{id:"user.enter-otp"})}),Object(_.jsx)(p.a,{className:"form-control",autoFocus:!0,name:"otp",validate:L}),e.otp&&r.otp&&Object(_.jsx)("div",{className:"invalid-feedback d-block",children:e.otp})]}),Object(_.jsxs)("div",{className:"d-flex justify-content-end align-items-center",children:[Object(_.jsx)(F,{}),Object(_.jsxs)(s.a,{color:"primary",className:"btn-shadow btn-multiple-state ml-2 ".concat(n?"show-spinner":""),size:"lg",type:"submit",children:[Object(_.jsxs)("span",{className:"spinner d-inline-block",children:[Object(_.jsx)("span",{className:"bounce1"}),Object(_.jsx)("span",{className:"bounce2"}),Object(_.jsx)("span",{className:"bounce3"})]}),Object(_.jsx)("span",{className:"label",children:Object(_.jsx)(A.a,{id:"user.verify-otp-button"})})]})]})]})}})]})]})})})}))}}]);
//# sourceMappingURL=user-verify-otp.0c95042e.chunk.js.map